"""
config.py

Satu-satunya tempat untuk semua path, konstanta, dan konfigurasi aplikasi.
Tidak ada path atau magic value yang boleh di-hardcode di file lain.
Semua file lain mengimport dari sini.
"""


import logging
from pathlib import Path

# ─────────────────────────────────────────────
# ROOT PROJECT
# ─────────────────────────────────────────────
# Selalu relatif terhadap lokasi config.py ini.
# Bekerja di lokal, VPS, Streamlit Cloud, maupun HF Spaces
# tanpa perlu modifikasi.
ROOT_DIR = Path(__file__).parent.resolve()

# ─────────────────────────────────────────────
# MODEL PATHS
# ─────────────────────────────────────────────
MODEL_DIR = ROOT_DIR / "models"
CHECKPOINT_PATH = MODEL_DIR / "clipcap_finetuned_local.pth"
ARCHITECTURE_DIR = ROOT_DIR / "architecture"

# ─────────────────────────────────────────────
# DATA PATHS
# ─────────────────────────────────────────────
DATA_DIR = ROOT_DIR / "data"
EVAL_JSON_PATH = DATA_DIR / "eval_local.json"
SAMPLE_CAPTIONS_PATH = DATA_DIR / "sample_captions.json"

# ─────────────────────────────────────────────
# ASSETS
# ─────────────────────────────────────────────
ASSETS_DIR = ROOT_DIR / "assets"
SAMPLE_IMAGES_DIR = ASSETS_DIR / "sample_images"
ICONS_DIR = ASSETS_DIR / "icons"

# ==========================================================
# STYLES
# ==========================================================

STYLES_DIR = ROOT_DIR / "styles"

CSS_VARIABLES = STYLES_DIR / "variables.css"
CSS_THEME = STYLES_DIR / "theme.css"
CSS_NAVIGATION = STYLES_DIR / "navigation.css"
CSS_HERO = STYLES_DIR / "hero.css"
CSS_CARDS = STYLES_DIR / "cards.css"
CSS_CAPTION = STYLES_DIR / "caption.css"
CSS_ABOUT = STYLES_DIR / "about.css"
CSS_FOOTER = STYLES_DIR / "footer.css"
CSS_ANIMATIONS = STYLES_DIR / "animations.css"
CSS_RESPONSIVE = STYLES_DIR / "responsive.css"
# ─────────────────────────────────────────────
# MODEL CONSTANTS
# Nilai-nilai ini harus konsisten dengan checkpoint.
# Jika checkpoint menggunakan config berbeda,
# nilai di config["..."] yang dipakai (lihat load_model.py).
# ─────────────────────────────────────────────
CLIP_BACKBONE = "ViT-B/32"
CLIP_DIM = 512
GPT2_DIM = 768
PREFIX_LEN = 10
CLIP_PROJECT_LEN = 10
TRANSFORMER_LAYERS = 8
TRANSFORMER_HEADS = 8

# ─────────────────────────────────────────────
# INFERENCE CONSTANTS
# Persis sesuai Cell 35 notebook
# ─────────────────────────────────────────────
GENERATE_NUM_BEAMS = 5
GENERATE_MAX_NEW_TOKENS = 60
GENERATE_MIN_NEW_TOKENS = 8
GENERATE_NO_REPEAT_NGRAM = 3
GENERATE_REPETITION_PENALTY = 1.2

# ─────────────────────────────────────────────
# TRANSLATOR
# ─────────────────────────────────────────────
SUPPORTED_LANGUAGES: dict[str, str] = {
    "English": "en",
    "Indonesian": "id",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
}

# Bahasa default output
DEFAULT_LANGUAGE = "English"

# Caption selalu di-generate dalam bahasa Inggris, lalu ditranslate.
# Tidak ada translate jika target == "en".
GENERATION_LANGUAGE = "en"

# ─────────────────────────────────────────────
# STREAMLIT APP
# ─────────────────────────────────────────────
APP_NAME="ARRAI"
APP_TITLE = "ARRAI"

APP_SHORT_TITLE = "ARRAI"

APP_DESCRIPTION = (
    "ARRAI is a multilingual AI image captioning platform "
    "powered by ClipCap, CLIP Vision Encoder, GPT-2, "
    "and Deep Translator."
)
APP_AUTHOR = "ARRAI Research Lab"
APP_VERSION = "1.0.0"

RESEARCHER = "Ayu"

INSTITUTION = "Universitas Halu Oleo"

MAX_UPLOAD_SIZE_MB = 10
ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp"]

# ==========================================================
# UI
# ==========================================================

DEFAULT_PAGE_ICON = "🧠"

DEFAULT_LAYOUT = "wide"

DEFAULT_SIDEBAR = "collapsed"

MAX_PREVIEW_WIDTH = 720

ENABLE_ANIMATION = True

# ─────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────
LOG_LEVEL = logging.DEBUG  # Ganti ke logging.INFO di production
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
    name: str = "ARRAI",
) -> logging.Logger:
    """
    Buat logger dengan format yang konsisten.
    Panggil di awal setiap modul:
        from config import setup_logging
        logger = setup_logging(__name__)
    """
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )
    return logging.getLogger(name)


# ─────────────────────────────────────────────
# VALIDATION
# ─────────────────────────────────────────────
def check_environment() -> dict[str, bool]:
    """
    Cek status environment saat startup.
    Return dict yang bisa ditampilkan di sidebar atau log.
    """
    return {
        "checkpoint_exists": CHECKPOINT_PATH.exists(),
        "eval_json_exists": EVAL_JSON_PATH.exists(),
        "sample_captions_exists": SAMPLE_CAPTIONS_PATH.exists(),
        "sample_images_dir_exists": SAMPLE_IMAGES_DIR.exists(),
        "models_dir_exists": MODEL_DIR.exists(),
    }
