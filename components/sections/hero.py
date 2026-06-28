"""
components/sections/hero.py

ARRAI Hero Section — Premium redesign dengan slot logo.

LOGO INSTRUCTIONS:
------------------
Siapkan 1 file logo untuk navigasi & hero:

  assets/logo/arrai_logo.png
    → Ukuran: 400 x 400 px (square, transparan background)
    → Digunakan di: nav logo box + hero logo display
    → Style: bold icon/symbol, bisa hexagon atau abstract AI shape
    → Warna: putih atau gradient ungu-cyan di atas transparan

Kalau logo belum ada, komponen ini otomatis fallback ke
teks "ARRAI" + emoji ⬡ — jadi app tetap jalan tanpa logo.
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from components.ui.badge import badge
from components.ui.button import primary_button, secondary_button
from components.ui.metric import metric_row
from components.ui.tag import tags


# ==========================================================
# LOGO PATH
# ==========================================================

_LOGO_PATH = Path(__file__).resolve().parents[2] / "assets" / "logo" / "arrai_logo.png"


# ==========================================================
# CONTENT CONFIG
# ==========================================================

_EYEBROW = "Research Grade AI Platform"

_TITLE_LINE1 = "Understanding Images."
_TITLE_LINE2 = "Beyond Pixels."

_DESCRIPTION = (
    "ARRAI generates natural, multilingual image captions using "
    "a fine-tuned ClipCap architecture — CLIP Vision Encoder, "
    "Transformer Mapper, GPT-2 Language Model, and Deep Translator "
    "— in one unified pipeline."
)

_METRICS = [
    ("Models",     "4"),
    ("Languages",  "5"),
    ("BLEU-1",     "18.76"),
    ("METEOR",     "31.23"),
]

_TAGS = [
    "CLIP ViT-B/32",
    "Transformer",
    "GPT-2",
    "Deep Translator",
    "Fine-tuned",
    "Research Grade",
]

_PIPELINE = [
    ("🖼",  "Image",     "Input"),
    ("🧠",  "CLIP",      "Vision Encoder"),
    ("⚙",   "Mapper",    "Transformer"),
    ("💬",  "GPT-2",     "Language Model"),
    ("🌍",  "Translate", "5 Languages"),
    ("✅",  "Caption",   "Output"),
]


# ==========================================================
# LOGO HELPER
# ==========================================================

def _logo_exists() -> bool:
    return _LOGO_PATH.exists()


# ==========================================================
# LEFT PANEL
# ==========================================================

def _render_left() -> None:

    # ── Logo (jika ada) ───────────────────────────────────
    if _logo_exists():
        st.markdown('<div class="hero-logo-wrapper">', unsafe_allow_html=True)
        st.image(str(_LOGO_PATH), width=64)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Eyebrow badge ─────────────────────────────────────
    badge(_EYEBROW)

    # ── Headline ──────────────────────────────────────────
    st.markdown(
        f"""
<h1 class="hero-title">
  <span class="hero-title-line1">{_TITLE_LINE1}</span>
  <span class="hero-title-line2 hero-gradient-text">{_TITLE_LINE2}</span>
</h1>
""",
        unsafe_allow_html=True,
    )

    # ── Description ───────────────────────────────────────
    st.markdown(
        f'<p class="hero-description">{_DESCRIPTION}</p>',
        unsafe_allow_html=True,
    )

    # ── CTA buttons ───────────────────────────────────────
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        primary_button(
            label="🚀 Launch Studio",
            page="pages/2_Caption_Generator.py",
            key="hero_launch",
        )

    with col2:
        secondary_button(
            label="Research →",
            page="pages/4_About.py",
            key="hero_about",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Metrics row ───────────────────────────────────────
    metric_row(_METRICS)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tech tags ─────────────────────────────────────────
    tags(_TAGS)


# ==========================================================
# RIGHT PANEL — Pipeline card
# ==========================================================

def _pipeline_html() -> str:

    nodes_html = ""
    last = len(_PIPELINE) - 1

    for i, (icon, name, subtitle) in enumerate(_PIPELINE):

        is_last = i == last
        node_class = "pipeline-node pipeline-node-success" if is_last else "pipeline-node"

        nodes_html += f"""
<div class="{node_class}">
  <div class="pipeline-icon">{icon}</div>
  <div>
    <div class="pipeline-name">{name}</div>
    <div class="pipeline-subtitle">{subtitle}</div>
  </div>
</div>
"""
        if not is_last:
            nodes_html += '<div class="pipeline-arrow">↓</div>'

    return f"""
<div class="pipeline-card">

  <div class="pipeline-header">
    <div class="pipeline-label">AI Pipeline</div>
    <h3>Multilingual Caption Generation</h3>
    <p>From image understanding to natural language output.</p>
  </div>

  <div class="pipeline-flow">
    {nodes_html}
  </div>

</div>
"""


def _render_right() -> None:
    st.markdown(_pipeline_html(), unsafe_allow_html=True)


# ==========================================================
# BACKGROUND BLOBS
# ==========================================================

def _render_background() -> None:
    st.markdown(
        """
<div class="hero-background" aria-hidden="true">
  <div class="hero-blur hero-blur-left"></div>
  <div class="hero-blur hero-blur-right"></div>
</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# PUBLIC
# ==========================================================

def render_hero() -> None:
    """Render ARRAI Hero Section."""

    _render_background()

    left, right = st.columns([1.3, 0.7], gap="large")

    with left:
        _render_left()

    with right:
        _render_right()

    st.markdown('<div class="hero-spacing"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)