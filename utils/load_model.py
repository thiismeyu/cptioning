"""
utils/load_model.py

Load model ClipCap dari checkpoint.
Mekanisme loading PERSIS seperti notebook — tidak ada redesign.

Checkpoint keys yang digunakan:
  ckpt["config"]       → dict konfigurasi model
  ckpt["mapping_net"]  → state_dict TransformerMapper / MLPMapper
  ckpt["gpt2"]         → state_dict GPT-2

Catatan: notebook Cell 5 menggunakan key "mapping_net_state_dict" dan
"gpt2_state_dict" saat load base model (COCO), tetapi Cell 11 menyimpan
checkpoint fine-tuned dengan key "mapping_net" dan "gpt2".
File ini meload checkpoint fine-tuned, jadi menggunakan key tanpa suffix.
"""

import sys
import warnings
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

import torch
import streamlit as st

# Pastikan architecture/ bisa diimport
ROOT_DIR = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT_DIR))

from config import (
    CHECKPOINT_PATH,
    CLIP_BACKBONE,
    CLIP_DIM,
    GPT2_DIM,
    PREFIX_LEN,
    CLIP_PROJECT_LEN,
    TRANSFORMER_LAYERS,
    TRANSFORMER_HEADS,
    setup_logging,
)
from architecture.model_architecture import TransformerMapper, MLPMapper

logger = setup_logging(__name__)


@dataclass
class ModelBundle:
    """
    Satu objek yang membawa semua komponen yang dibutuhkan untuk inference.
    Dikirim ke inference.py — tidak perlu unpack satu per satu.
    """
    clip_model: object
    preprocess: object
    mapping_net: torch.nn.Module
    gpt2: object
    tokenizer: object
    config: dict
    device: str


@st.cache_resource(show_spinner=False)
def load_model(checkpoint_path: Optional[str] = None) -> ModelBundle:
    """
    Load semua komponen model. Di-cache oleh Streamlit —
    hanya dieksekusi sekali per session server, tidak per user request.

    Args:
        checkpoint_path: Override path checkpoint. Jika None, pakai CHECKPOINT_PATH dari config.

    Returns:
        ModelBundle dengan semua komponen siap untuk inference.

    Raises:
        FileNotFoundError: jika .pth tidak ditemukan.
        RuntimeError: jika checkpoint corrupt atau keys tidak sesuai.
    """
    import clip
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

    ckpt_path = Path(checkpoint_path) if checkpoint_path else CHECKPOINT_PATH

    # ── 1. Validasi file checkpoint ──────────────────────────────────────
    logger.info(f"Mencari checkpoint di: {ckpt_path}")
    if not ckpt_path.exists():
        msg = (
            f"Checkpoint tidak ditemukan: {ckpt_path}\n"
            f"Pastikan file 'clipcap_finetuned_local.pth' ada di folder 'models/'.\n"
            f"File ini tidak disertakan di repository karena ukurannya ~600MB."
        )
        logger.error(msg)
        raise FileNotFoundError(msg)

    # ── 2. Device ─────────────────────────────────────────────────────────
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Device: {device}")

    # ── 3. Load checkpoint ────────────────────────────────────────────────
    logger.info("Memuat checkpoint...")
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)

    # Validasi keys wajib
    required_keys = {"config", "mapping_net", "gpt2"}
    missing = required_keys - set(ckpt.keys())
    if missing:
        raise RuntimeError(
            f"Checkpoint tidak memiliki keys: {missing}. "
            f"Keys yang tersedia: {list(ckpt.keys())}"
        )

    cfg = ckpt["config"]
    logger.info(f"Config dari checkpoint: {cfg}")

    # ── 4. Rebuild TransformerMapper / MLPMapper ──────────────────────────
    # Selalu baca dari cfg agar konsisten dengan checkpoint,
    # bukan dari konstanta di config.py
    mapping_type = cfg.get("mapping_type", "transformer")
    prefix_len = cfg.get("prefix_len", PREFIX_LEN)
    clip_project_len = cfg.get("clip_project_len", CLIP_PROJECT_LEN)
    gpt2_dim = cfg.get("gpt2_dim", GPT2_DIM)
    trans_layers = cfg.get("transformer_layers", TRANSFORMER_LAYERS)
    trans_heads = cfg.get("transformer_heads", TRANSFORMER_HEADS)
    clip_dim = cfg.get("clip_dim", CLIP_DIM)
    clip_backbone = cfg.get("clip_backbone", CLIP_BACKBONE)

    logger.info(f"Membangun {mapping_type} mapper...")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # suppress norm_first warning dari PyTorch
        if mapping_type == "transformer":
            mapping_net = TransformerMapper(
                clip_dim=clip_dim,
                gpt2_dim=gpt2_dim,
                prefix_len=prefix_len,
                clip_project_len=clip_project_len,
                num_layers=trans_layers,
                num_heads=trans_heads,
            ).to(device)
        else:
            mapping_net = MLPMapper(
                clip_dim=clip_dim,
                gpt2_dim=gpt2_dim,
                prefix_len=prefix_len,
            ).to(device)

    mapping_net.load_state_dict(ckpt["mapping_net"])
    mapping_net.eval()
    logger.info(f"Mapping network ({mapping_type}) loaded ✅")

    # ── 5. Load GPT-2 ─────────────────────────────────────────────────────
    logger.info("Memuat GPT-2 tokenizer...")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

    logger.info("Memuat GPT-2 model...")
    gpt2 = GPT2LMHeadModel.from_pretrained("gpt2").to(device)
    gpt2.load_state_dict(ckpt["gpt2"])
    gpt2.eval()

    # Freeze GPT-2 (tidak perlu grad saat inference)
    for p in gpt2.parameters():
        p.requires_grad = False

    logger.info("GPT-2 loaded ✅")

    # ── 6. Load CLIP ──────────────────────────────────────────────────────
    logger.info(f"Memuat CLIP {clip_backbone}...")
    clip_model, preprocess = clip.load(clip_backbone, device=device)
    clip_model.eval()
    for p in clip_model.parameters():
        p.requires_grad = False

    logger.info(f"CLIP {clip_backbone} loaded ✅")

    # ── 7. Log ringkasan ──────────────────────────────────────────────────
    total_params = sum(p.numel() for p in mapping_net.parameters())
    logger.info(f"Mapping network parameters: {total_params:,}")
    logger.info("Model bundle siap digunakan.")

    return ModelBundle(
        clip_model=clip_model,
        preprocess=preprocess,
        mapping_net=mapping_net,
        gpt2=gpt2,
        tokenizer=tokenizer,
        config=cfg,
        device=device,
    )


def get_model_info(bundle: ModelBundle) -> dict:
    """
    Kembalikan informasi ringkasan model untuk ditampilkan di UI.
    """
    cfg = bundle.config
    return {
        "mapping_type": cfg.get("mapping_type", "transformer"),
        "clip_backbone": cfg.get("clip_backbone", CLIP_BACKBONE),
        "prefix_len": cfg.get("prefix_len", PREFIX_LEN),
        "transformer_layers": cfg.get("transformer_layers", TRANSFORMER_LAYERS),
        "transformer_heads": cfg.get("transformer_heads", TRANSFORMER_HEADS),
        "gpt2_dim": cfg.get("gpt2_dim", GPT2_DIM),
        "device": bundle.device,
        "freeze_gpt2": cfg.get("freeze_gpt2", True),
        "finetune_info": bundle.config.get("finetune_info", {}),
    }
