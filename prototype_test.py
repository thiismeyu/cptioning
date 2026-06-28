"""
prototype_test.py

PROTOTYPE MINIMAL — validasi pipeline sebelum UI penuh dibangun.

Jalankan dengan:
    streamlit run prototype_test.py

Halaman ini HANYA berisi:
  1. Load model (dengan status indicator)
  2. Upload gambar
  3. Generate caption
  4. Translate caption
  5. Tampilkan hasil

Tidak ada CSS kustom, tidak ada multi-page, tidak ada animasi.
Jika ini bekerja dengan benar, lanjut ke Step 3 (UI penuh).
"""

import sys
from pathlib import Path

# Pastikan root project ada di sys.path
ROOT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from PIL import Image

from config import CHECKPOINT_PATH, SUPPORTED_LANGUAGES, setup_logging
from utils.load_model import load_model
from utils.inference import generate_caption, run_inference_test
from utils.translator import translate, get_language_flag
from utils.helpers import format_inference_time, get_image_info, get_checkpoint_status

logger = setup_logging("prototype")

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="ClipCap Prototype",
    page_icon="🖼️",
    layout="centered",
)

st.title("🖼️ ClipCap — Prototype Pipeline Test")
st.caption("Validasi pipeline sebelum UI penuh dibangun.")
st.divider()

# ─────────────────────────────────────────────
# CHECKPOINT STATUS
# ─────────────────────────────────────────────
ckpt_info = get_checkpoint_status(CHECKPOINT_PATH)
if ckpt_info["exists"]:
    st.success(f"Checkpoint: {ckpt_info['status']}")
else:
    st.error(
        f"**Checkpoint tidak ditemukan** di `{CHECKPOINT_PATH}`\n\n"
        "Letakkan file `clipcap_finetuned_local.pth` di folder `models/` "
        "lalu refresh halaman ini."
    )
    st.stop()

# ─────────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────────
with st.spinner("Memuat model... (hanya sekali, cache aktif)"):
    try:
        bundle = load_model()
        st.success(
            f"Model loaded ✅  |  Device: `{bundle.device}`  |  "
            f"Backbone: `{bundle.config.get('clip_backbone', 'ViT-B/32')}`  |  "
            f"Mapper: `{bundle.config.get('mapping_type', 'transformer')}`"
        )
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()
    except RuntimeError as e:
        st.error(f"Error saat load model: {e}")
        st.stop()

st.divider()

# ─────────────────────────────────────────────
# INFERENCE TEST (synthetic image)
# ─────────────────────────────────────────────
with st.expander("🧪 Inference Test (gambar sintetis)", expanded=False):
    st.caption(
        "Test ini menggunakan gambar noise acak untuk memverifikasi bahwa "
        "pipeline tidak crash. Kualitas caption tidak relevan di sini."
    )
    if st.button("Jalankan Inference Test"):
        with st.spinner("Testing..."):
            result = run_inference_test(bundle)
        if result["success"]:
            st.success(f"✅ PASSED — Elapsed: {format_inference_time(result['elapsed'])}")
            st.code(f'Caption: "{result["caption"]}"', language=None)
        else:
            st.error(f"❌ FAILED — Error: {result['error']}")

st.divider()

# ─────────────────────────────────────────────
# MAIN: UPLOAD → CAPTION → TRANSLATE
# ─────────────────────────────────────────────
st.subheader("Upload Gambar")

uploaded = st.file_uploader(
    "Pilih gambar (JPG, PNG, WEBP)",
    type=["jpg", "jpeg", "png", "webp"],
    help="Ukuran maksimum 10MB",
)

lang_name = st.selectbox(
    "Bahasa output",
    options=list(SUPPORTED_LANGUAGES.keys()),
    index=0,
)
lang_code = SUPPORTED_LANGUAGES[lang_name]
flag = get_language_flag(lang_code)

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    info = get_image_info(image)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(image, caption="Gambar yang diupload", use_container_width=True)
    with col2:
        st.markdown("**Info Gambar**")
        st.text(f"Ukuran : {info['size_str']}")
        st.text(f"Mode   : {info['mode']}")
        st.text(f"Format : {info['format']}")

    st.divider()

    if st.button("⚡ Generate Caption", type="primary"):

        # ── Generate ──────────────────────────────────────────────────────
        with st.spinner("Generating caption..."):
            try:
                caption_en, elapsed = generate_caption(image, bundle)
            except Exception as e:
                st.error(f"Error saat generate: {e}")
                logger.error(f"Generate error: {e}", exc_info=True)
                st.stop()

        st.markdown(f"**⏱ Inference time:** `{format_inference_time(elapsed)}`")

        # ── Caption EN ────────────────────────────────────────────────────
        st.markdown("**Caption (English):**")
        st.info(caption_en)

        # ── Translate ─────────────────────────────────────────────────────
        if lang_code != "en":
            with st.spinner(f"Menerjemahkan ke {lang_name}..."):
                try:
                    caption_translated = translate(caption_en, lang_code)
                except Exception as e:
                    st.warning(f"Translate gagal: {e}. Menampilkan caption EN.")
                    caption_translated = caption_en

            st.markdown(f"**Caption ({flag} {lang_name}):**")
            st.success(caption_translated)
        else:
            caption_translated = caption_en

        # ── Download ──────────────────────────────────────────────────────
        output_text = (
            f"=== ClipCap Image Caption ===\n\n"
            f"[English]\n{caption_en}\n\n"
            f"[{lang_name}]\n{caption_translated}\n"
        )
        st.download_button(
            label="⬇ Download caption (.txt)",
            data=output_text,
            file_name="caption.txt",
            mime="text/plain",
        )

        # ── Debug info ────────────────────────────────────────────────────
        with st.expander("🔍 Debug Info", expanded=False):
            st.json({
                "device": bundle.device,
                "clip_backbone": bundle.config.get("clip_backbone"),
                "mapping_type": bundle.config.get("mapping_type"),
                "prefix_len": bundle.config.get("prefix_len"),
                "target_lang": lang_code,
                "caption_en_len_tokens": len(caption_en.split()),
                "elapsed_s": round(elapsed, 3),
            })

st.divider()
st.caption(
    "Prototype ini hanya untuk validasi pipeline. "
    "UI profesional akan dibangun setelah prototype ini dikonfirmasi berjalan."
)
