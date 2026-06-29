"""
components/sections/about.py

ARRAI About Section
"""

from __future__ import annotations

import streamlit as st


_TITLE = "Research-Driven AI Platform"

_DESCRIPTION = (
    "ARRAI is a multilingual image captioning platform developed "
    "for research, education and real-world AI applications. "
    "The platform combines CLIP Vision Encoder, "
    "Transformer Mapper, GPT-2 Language Model, "
    "and automatic translation into a unified "
    "end-to-end workflow."
)
def _about_card():
    
    st.markdown(
        f"""<div class="glass">
<h2 class="section-title">{_TITLE}</h2>
<p class="section-description">{_DESCRIPTION}</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric("AI Models", "4")

    with c2:

        st.metric("Languages", "5")

    with c3:

        st.metric("Inference", "≈2 sec")
def render_about():
    
    _about_card()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )