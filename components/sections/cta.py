"""
components/sections/cta.py

ARRAI Call To Action Section
"""

from __future__ import annotations

import streamlit as st

from components.ui.button import (
    primary_button,
    secondary_button,
)

_TITLE = "Ready to Experience ARRAI?"

_DESCRIPTION = (
    "Generate multilingual captions using our "
    "fine-tuned ClipCap architecture and "
    "experience research-grade AI in seconds."
)


# ==========================================================
# CTA
# ==========================================================

def _render_cta() -> None:

    st.markdown(
        f"""<div class="cta-card">
<div class="cta-badge">AI PLATFORM</div>
<h2 class="cta-title">{_TITLE}</h2>
<p class="cta-description">{_DESCRIPTION}</p>
</div>""",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:

        primary_button(
            label="Launch Studio",
            page="pages/2_Caption_Generator.py",
            key="cta_launch_button",
        )

    with col2:

        secondary_button(
            label="About ARRAI",
            page="pages/4_About.py",
            key="cta_about_button",
        )

    with col3:
        st.empty()


# ==========================================================
# PUBLIC
# ==========================================================

def render_cta() -> None:

    _render_cta()

    st.markdown(
        '<div class="hero-spacing"></div>',
        unsafe_allow_html=True,
    )