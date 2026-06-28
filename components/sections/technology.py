"""
components/sections/technology.py

ARRAI Technology Stack
"""

from __future__ import annotations

import streamlit as st


_TECHNOLOGIES = [

    {
        "icon": "🧠",
        "name": "CLIP",
        "subtitle": "Vision Encoder",
        "description":
            "Extracts semantic visual embeddings from uploaded images.",
    },

    {
        "icon": "⚙",
        "name": "Transformer",
        "subtitle": "Mapper",
        "description":
            "Projects visual features into GPT-2 embedding space.",
    },

    {
        "icon": "💬",
        "name": "GPT-2",
        "subtitle": "Language Model",
        "description":
            "Generates natural language captions from mapped embeddings.",
    },

    {
        "icon": "🌍",
        "name": "Deep Translator",
        "subtitle": "Translation",
        "description":
            "Converts English captions into multiple supported languages.",
    },

]
# ==========================================================
# CARD
# ==========================================================

def _technology_card(item: dict) -> None:

    st.markdown(
        f"""
<div class="technology-card">

<div class="technology-icon">

{item["icon"]}

</div>

<div class="technology-name">

{item["name"]}

</div>

<div class="technology-subtitle">

{item["subtitle"]}

</div>

<div class="technology-description">

{item["description"]}

</div>

</div>
""",
        unsafe_allow_html=True,
    )
# ==========================================================
# GRID
# ==========================================================

def _render_grid() -> None:

    cols = st.columns(4)

    for col, item in zip(cols, _TECHNOLOGIES):

        with col:

            _technology_card(item)
# ==========================================================
# PUBLIC
# ==========================================================

def render_technology() -> None:

    st.markdown(
        """
<h2 class="section-title">

Technology Stack

</h2>

<p class="section-description">

ARRAI integrates state-of-the-art computer vision,
natural language processing and multilingual translation
into a unified AI workflow.

</p>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    _render_grid()

    st.markdown(
        '<div class="hero-spacing"></div>',
        unsafe_allow_html=True,
    )