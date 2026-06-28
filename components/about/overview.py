"""
components/about/overview.py
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


def render_overview():

    section_title(
        "About ARRAI",
        "Advanced Research for AI Image Captioning",
    )

    st.markdown(
        """
<div class="glass">

<p class="result-text">

ARRAI (Advanced Research for AI Image Captioning)
is a multilingual image captioning platform based on
ClipCap.

The system generates image captions in English and
automatically translates them into multiple languages.

ARRAI was developed as a research project focusing on
Deep Learning, Computer Vision, and Natural Language
Processing.

</p>

</div>
""",
        unsafe_allow_html=True,
    )