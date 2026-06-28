"""
components/evaluation/dataset_panel.py

ARRAI Dataset Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title

from utils.evaluation_service import get_dataset_information


# ==========================================================
# PUBLIC
# ==========================================================

def render_dataset_panel() -> None:

    section_title(

        "Dataset Information",

        "Dataset and evaluation configuration.",

    )

    html = """

<div class="model-card">

"""

    for key, value in get_dataset_information():

        html += f"""

<div class="model-item">

<div class="model-label">

{key}

</div>

<div class="model-value">

{value}

</div>

</div>

"""

    html += """

</div>

"""

    st.markdown(

        html,

        unsafe_allow_html=True,

    )