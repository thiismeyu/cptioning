"""
components/evaluation/comparison_panel.py

ARRAI Comparison Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title

from utils.evaluation_service import get_metric_details


def render_comparison_panel() -> None:

    section_title(

        "Evaluation Comparison",

        "Overall evaluation results of the trained ARRAI model.",

    )

    html = """

<div class="comparison-card">

<table class="comparison-table">

<thead>

<tr>

<th>Metric</th>

<th>Score</th>

<th>Interpretation</th>

</tr>

</thead>

<tbody>

"""

    for metric, score, description in get_metric_details():

        html += f"""

<tr>

<td>{metric}</td>

<td><strong>{score}</strong></td>

<td>{description}</td>

</tr>

"""

    html += """

</tbody>

</table>

</div>

"""

    st.markdown(

        html,

        unsafe_allow_html=True,

    )