"""
components/sections/features.py

ARRAI Features Section
"""

from __future__ import annotations

import streamlit as st


# ==========================================================
# FEATURE DATA
# ==========================================================

_FEATURES = [

    {
        "icon": "🧠",
        "title": "Vision Understanding",
        "description":
            "Powered by CLIP Vision Encoder for rich semantic image representation.",
    },

    {
        "icon": "⚙",
        "title": "Transformer Mapper",
        "description":
            "Bridges visual embeddings into GPT-2 language space with fine-tuned mapping.",
    },

    {
        "icon": "💬",
        "title": "Natural Caption",
        "description":
            "Generate fluent and context-aware captions using GPT-2 language generation.",
    },

    {
        "icon": "🌍",
        "title": "Multilingual",
        "description":
            "Automatically translate captions into multiple languages with Deep Translator.",
    },

    {
        "icon": "⚡",
        "title": "Fast Inference",
        "description":
            "Optimized inference pipeline designed for real-time demonstrations.",
    },

    {
        "icon": "🔬",
        "title": "Research Ready",
        "description":
            "Designed for researchers, lecturers, students and AI practitioners.",
    },

]
# ==========================================================
# FEATURE CARD
# ==========================================================

def _feature_card(
    icon: str,
    title: str,
    description: str,
) -> None:

    st.markdown(
        f"""<div class="feature-card">
<div class="feature-icon">{icon}</div>
<div class="feature-title">{title}</div>
<div class="feature-description">{description}</div>
</div>""",
        unsafe_allow_html=True,
    )
# ==========================================================
# GRID
# ==========================================================

def _render_grid() -> None:

    rows = [
        _FEATURES[0:3],
        _FEATURES[3:6],
    ]

    for row in rows:

        cols = st.columns(3)

        for col, feature in zip(cols, row):

            with col:

                _feature_card(
                    feature["icon"],
                    feature["title"],
                    feature["description"],
                )
# ==========================================================
# PUBLIC
# ==========================================================

def render_features() -> None:

    st.markdown(
        """<h2 class="section-title">Why ARRAI?</h2>
<p class="section-description">Modern AI Captioning Platform built for research, education and production-ready demonstrations.</p>""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    _render_grid()

    st.markdown(
        '<div class="hero-spacing"></div>',
        unsafe_allow_html=True,
    )