"""
components/evaluation/comparison_panel.py
ARRAI Comparison Table Panel
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title
from utils.evaluation_service import get_metric_details

def render_comparison_panel() -> None:

    section_title(
        "Score Summary",
        "All metrics at a glance — model evaluation on local test set.",
    )

    rows_html = ""
    for metric, score, description in get_metric_details():
        rows_html += f"""
<tr>
  <td class="cmp-td cmp-td-metric">{metric}</td>
  <td class="cmp-td"><strong class="cmp-score">{score}</strong></td>
  <td class="cmp-td cmp-td-desc">{description}</td>
</tr>
"""

    st.markdown(
        f"""
<div class="cmp-card">
  <table class="cmp-table">
    <thead>
      <tr>
        <th class="cmp-th">Metric</th>
        <th class="cmp-th">Score</th>
        <th class="cmp-th">Interpretation</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
</div>
""",
        unsafe_allow_html=True,
    )