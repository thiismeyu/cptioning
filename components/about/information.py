"""
components/about/information.py
"""

from __future__ import annotations

import streamlit as st

from config import (
    APP_VERSION,
    APP_AUTHOR,
    INSTITUTION,
    RESEARCHER,
)

from components.ui.section import section_title


def render_information():

    section_title(
        "Project Information",
        "Basic information about this project.",
    )

    html = f"""
<div class="model-card">

<div class="model-item">
<div class="model-label">Version</div>
<div class="model-value">{APP_VERSION}</div>
</div>

<div class="model-item">
<div class="model-label">Researcher</div>
<div class="model-value">{RESEARCHER}</div>
</div>

<div class="model-item">
<div class="model-label">Institution</div>
<div class="model-value">{INSTITUTION}</div>
</div>

<div class="model-item">
<div class="model-label">Author</div>
<div class="model-value">{APP_AUTHOR}</div>
</div>

</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )