"""
components/sections/pipeline.py

ARRAI AI Pipeline Section
"""

from __future__ import annotations

import streamlit as st


_PIPELINE = [

    {
        "step": "01",
        "icon": "🖼",
        "title": "Input Image",
        "description":
            "Upload an image for caption generation.",
    },

    {
        "step": "02",
        "icon": "🧠",
        "title": "CLIP Vision Encoder",
        "description":
            "Extract high-level semantic visual embeddings.",
    },

    {
        "step": "03",
        "icon": "⚙",
        "title": "Transformer Mapper",
        "description":
            "Project visual embeddings into GPT-2 latent space.",
    },

    {
        "step": "04",
        "icon": "💬",
        "title": "GPT-2",
        "description":
            "Generate natural English captions.",
    },

    {
        "step": "05",
        "icon": "🌍",
        "title": "Deep Translator",
        "description":
            "Translate captions into multiple languages.",
    },

    {
        "step": "06",
        "icon": "✅",
        "title": "Final Caption",
        "description":
            "Ready for copy, export and evaluation.",
    },

]
# ==========================================================
# CARD
# ==========================================================

def _pipeline_card(
    item: dict,
) -> None:

    st.markdown(
        f"""<div class="pipeline-stage">
<div class="pipeline-step">{item["step"]}</div>
<div class="pipeline-stage-icon">{item["icon"]}</div>
<div class="pipeline-stage-title">{item["title"]}</div>
<div class="pipeline-stage-description">{item["description"]}</div>
</div>""",
        unsafe_allow_html=True,
    )
# ==========================================================
# GRID
# ==========================================================

def _render_pipeline() -> None:

    row1 = st.columns(3)

    for col, item in zip(row1, _PIPELINE[:3]):

        with col:

            _pipeline_card(item)

    st.markdown(
        '<div class="pipeline-connector">↓</div>',
        unsafe_allow_html=True,
    )

    row2 = st.columns(3)

    for col, item in zip(row2, _PIPELINE[3:]):

        with col:

            _pipeline_card(item)
# ==========================================================
# PUBLIC
# ==========================================================

def render_pipeline() -> None:

    st.markdown(
        """<h2 class="section-title">ARRAI AI Pipeline</h2>
<p class="section-description">From computer vision to multilingual language generation through an end-to-end AI workflow.</p>""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    _render_pipeline()

    st.markdown(
        '<div class="hero-spacing"></div>',
        unsafe_allow_html=True,
    )