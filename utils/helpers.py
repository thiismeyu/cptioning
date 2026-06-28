"""
utils/helpers.py

Fungsi utilitas umum yang digunakan di banyak tempat.
Tidak ada logika model atau inference di sini.
"""

import json
import logging
from pathlib import Path
from typing import Any, Optional

import streamlit as st
from PIL import Image

logger = logging.getLogger(__name__)


def load_css(filepath: str | Path) -> None:
    """Inject satu file CSS ke dalam Streamlit via st.markdown."""
    path = Path(filepath)
    if not path.exists():
        logger.warning(f"CSS file tidak ditemukan: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def load_css_files(*paths: str | Path) -> None:
    """Inject beberapa file CSS sekaligus."""
    for p in paths:
        load_css(p)


def load_json(filepath: str | Path) -> Optional[Any]:
    """Load JSON file dengan error handling. Return None jika gagal."""
    path = Path(filepath)
    if not path.exists():
        logger.warning(f"JSON file tidak ditemukan: {path}")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error di {path}: {e}")
        return None


def format_inference_time(seconds: float) -> str:
    """Format waktu inference ke string yang readable."""
    if seconds < 1.0:
        return f"{seconds * 1000:.0f} ms"
    return f"{seconds:.2f} s"


def get_image_info(image: Image.Image) -> dict:
    """Kembalikan metadata gambar untuk ditampilkan di UI."""
    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "format": getattr(image, "format", "Unknown") or "Unknown",
        "size_str": f"{image.width} × {image.height} px",
    }


def get_checkpoint_status(checkpoint_path: Path) -> dict:
    """
    Cek status file checkpoint.
    Return dict untuk ditampilkan di sidebar atau halaman About.
    """
    if not checkpoint_path.exists():
        return {
            "exists": False,
            "size_mb": None,
            "status": "❌ Tidak ditemukan",
            "color": "red",
        }
    size_bytes = checkpoint_path.stat().st_size
    size_mb = size_bytes / (1024 * 1024)
    return {
        "exists": True,
        "size_mb": round(size_mb, 1),
        "status": f"✅ Tersedia ({size_mb:.0f} MB)",
        "color": "green",
    }
