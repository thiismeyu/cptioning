"""
components/about/overview.py
ARRAI About Overview — premium redesign
"""
from __future__ import annotations
from pathlib import Path
import streamlit as st
from components.ui.badge import badge

_LOGO_PATH = Path(__file__).resolve().parents[2] / "assets" / "logo" / "arrai_logo.png"

_HIGHLIGHTS = [
    ("🧠", "ClipCap Architecture",
     "Fine-tuned on a local Indonesian dataset (191 images, 5 categories) "
     "using CLIP ViT-B/32 + Transformer Mapper + GPT-2."),
    ("🌍", "5 Languages",
     "Generates English captions, then auto-translates to Indonesian, "
     "Japanese, Arabic, and Simplified Chinese."),
    ("⚡", "~2s Inference",
     "Optimized pipeline runs end-to-end caption generation and translation "
     "in approximately 2 seconds on GPU."),
    ("🔬", "Research Grade",
     "Designed for Sinta-range national journal publication, targeting "
     "rigorous evaluation with BLEU, ROUGE-L, METEOR, and CIDEr metrics."),
]

def render_overview() -> None:

    left, right = st.columns([1.1, 0.9], gap="large")

    with left:

        badge("Advanced Research for AI Image Captioning")

        st.markdown(
            """
<h1 class="about-hero-title">
  ARRAI
  <span class="about-hero-subtitle-inline">AI Platform</span>
</h1>
<p class="about-hero-desc">
  A multilingual image captioning platform built on ClipCap —
  combining CLIP Vision Encoder, Transformer Mapper, GPT-2,
  and Deep Translator into one unified AI pipeline.
</p>
""",
            unsafe_allow_html=True,
        )

        for icon, title, text in _HIGHLIGHTS:
            st.markdown(
                f"""
<div class="about-highlight-row">
  <div class="about-highlight-icon">{icon}</div>
  <div class="about-highlight-body">
    <div class="about-highlight-title">{title}</div>
    <div class="about-highlight-text">{text}</div>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )

    with right:

        # Logo slot
        if _LOGO_PATH.exists():
            st.markdown('<div class="about-logo-wrapper">', unsafe_allow_html=True)
            st.image(str(_LOGO_PATH), width=180)
            st.markdown('</div>', unsafe_allow_html=True)

        # Stats
        st.markdown(
            """
<div class="about-stats-grid">

  <div class="about-stat-card">
    <div class="about-stat-value">191</div>
    <div class="about-stat-label">Training Images</div>
  </div>

  <div class="about-stat-card">
    <div class="about-stat-value">5</div>
    <div class="about-stat-label">Local Categories</div>
  </div>

  <div class="about-stat-card">
    <div class="about-stat-value">31.23</div>
    <div class="about-stat-label">METEOR Score</div>
  </div>

  <div class="about-stat-card">
    <div class="about-stat-value">5</div>
    <div class="about-stat-label">Output Languages</div>
  </div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)