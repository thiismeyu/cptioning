"""
utils/inference.py

Fungsi generate_caption() — implementasi PERSIS dari Cell 35 notebook.

Pipeline:
  PIL.Image → CLIP preprocess → CLIP encode → feat [1, 512]
            → TransformerMapper → prefix [1, prefix_len, 768]
            → concat dengan EOS token embedding [1, 1, 768]
            → GPT-2 generate (inputs_embeds, beam search)
            → decode → caption string

TIDAK ADA modifikasi dari versi notebook.
"""

import time
import warnings
from typing import Optional

import torch
from PIL import Image

from config import (
    GENERATE_NUM_BEAMS,
    GENERATE_MAX_NEW_TOKENS,
    GENERATE_MIN_NEW_TOKENS,
    GENERATE_NO_REPEAT_NGRAM,
    GENERATE_REPETITION_PENALTY,
    setup_logging,
)
from utils.load_model import ModelBundle

logger = setup_logging(__name__)


@torch.no_grad()
def generate_caption(
    image: Image.Image,
    bundle: ModelBundle,
    num_beams: int = GENERATE_NUM_BEAMS,
    max_new_tokens: int = GENERATE_MAX_NEW_TOKENS,
    min_new_tokens: int = GENERATE_MIN_NEW_TOKENS,
    no_repeat_ngram_size: int = GENERATE_NO_REPEAT_NGRAM,
    repetition_penalty: float = GENERATE_REPETITION_PENALTY,
) -> tuple[str, float]:
    """
    Generate caption untuk satu gambar.

    Args:
        image: PIL Image (mode RGB)
        bundle: ModelBundle dari load_model()
        num_beams: jumlah beam untuk beam search
        max_new_tokens: panjang maksimum caption (dalam token)
        min_new_tokens: panjang minimum caption
        no_repeat_ngram_size: cegah pengulangan n-gram
        repetition_penalty: penalti untuk token berulang

    Returns:
        (caption, elapsed_seconds)
        caption: string bahasa Inggris
        elapsed_seconds: float waktu inference dalam detik
    """
    t_start = time.perf_counter()

    device = bundle.device
    clip_model = bundle.clip_model
    preprocess = bundle.preprocess
    mapping_net = bundle.mapping_net
    gpt2 = bundle.gpt2
    tokenizer = bundle.tokenizer

    # ── 1. Pastikan gambar RGB ─────────────────────────────────────────────
    if image.mode != "RGB":
        image = image.convert("RGB")

    # ── 2. CLIP encode ─────────────────────────────────────────────────────
    # preprocess: resize, center crop, normalize sesuai CLIP ViT-B/32
    clip_input = preprocess(image).unsqueeze(0).to(device)
    feat = clip_model.encode_image(clip_input)       # [1, 512]
    feat = feat.float()                              # pastikan float32

    # ── 3. TransformerMapper → prefix tokens ───────────────────────────────
    # mapping_net sudah di .eval(), tidak ada dropout
    prefix = mapping_net(feat)                       # [1, prefix_len, gpt2_dim]

    # ── 4. EOS token embedding (start token) ───────────────────────────────
    # Persis dari notebook: input_ids = [[eos_token_id]]
    eos_id = torch.tensor([[tokenizer.eos_token_id]], device=device)
    tok_emb = gpt2.transformer.wte(eos_id)           # [1, 1, gpt2_dim]

    # ── 5. Concat prefix + EOS embedding ──────────────────────────────────
    embeds = torch.cat([prefix, tok_emb], dim=1)     # [1, prefix_len+1, gpt2_dim]

    # ── 6. GPT-2 generate ─────────────────────────────────────────────────
    # Suppress warning tentang repetition_penalty dengan inputs_embeds
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        output = gpt2.generate(
            inputs_embeds=embeds,
            max_new_tokens=max_new_tokens,
            min_new_tokens=min_new_tokens,
            num_beams=num_beams,
            no_repeat_ngram_size=no_repeat_ngram_size,
            early_stopping=False,
            repetition_penalty=repetition_penalty,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    # ── 7. Decode ─────────────────────────────────────────────────────────
    caption = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    elapsed = time.perf_counter() - t_start
    logger.info(f"Caption generated in {elapsed:.2f}s: {caption[:80]}...")

    return caption, elapsed


def run_inference_test(bundle: ModelBundle) -> dict:
    """
    Test inference dengan gambar sintetis (noise).
    Digunakan untuk memverifikasi model berjalan benar
    TANPA memerlukan gambar nyata.

    Tidak menjamin kualitas caption — hanya memverifikasi bahwa
    pipeline tidak crash dan menghasilkan string non-empty.

    Returns:
        dict dengan keys: success, caption, elapsed, error
    """
    import numpy as np

    logger.info("Menjalankan inference test dengan gambar sintetis...")

    try:
        # Buat gambar dummy: 224x224 noise RGB
        dummy_array = (torch.rand(224, 224, 3).numpy() * 255).astype("uint8")
        dummy_image = Image.fromarray(dummy_array, mode="RGB")

        caption, elapsed = generate_caption(dummy_image, bundle)

        success = isinstance(caption, str) and len(caption.strip()) > 0
        logger.info(f"Inference test {'PASSED ✅' if success else 'FAILED ❌'}")
        logger.info(f"Caption: {caption}")
        logger.info(f"Elapsed: {elapsed:.3f}s")

        return {
            "success": success,
            "caption": caption,
            "elapsed": elapsed,
            "error": None,
        }

    except Exception as e:
        logger.error(f"Inference test FAILED: {e}", exc_info=True)
        return {
            "success": False,
            "caption": "",
            "elapsed": 0.0,
            "error": str(e),
        }
