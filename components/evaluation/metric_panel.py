"""
components/evaluation/metric_panel.py

ARRAI Metric Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title

from utils.evaluation_service import get_metric_details


# ==========================================================
# PUBLIC
# ==========================================================

def render_metric_panel() -> None:

    section_title(

        "Metric Details",

        "Description of each evaluation metric used in ARRAI.",

    )

    html = """

<div class="model-card">

"""

    for metric, score, description in get_metric_details():

        html += f"""

<div class="model-item">

<div>

<div class="model-title">

{metric}

</div>

<div class="result-text">

{description}

</div>

</div>

<div class="model-value">

{score}

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