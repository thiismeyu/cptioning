"""
components/evaluation/metric_panel.py
ARRAI Metric Detail Panel
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title
from utils.evaluation_service import get_metric_details

_ICONS = {
    "BLEU-1":  "🎯",
    "BLEU-4":  "📐",
    "ROUGE-L": "🔗",
    "METEOR":  "⭐",
    "CIDEr":   "🏆",
}

def render_metric_panel() -> None:

    section_title(
        "Metric Breakdown",
        "What each score means and how ARRAI performed.",
    )

    for metric, score, description in get_metric_details():
        icon = _ICONS.get(metric, "📊")
        st.markdown(
            f"""
<div class="metric-detail-row">
  <div class="metric-detail-icon">{icon}</div>
  <div class="metric-detail-body">
    <div class="metric-detail-top">
      <span class="metric-detail-name">{metric}</span>
      <span class="metric-detail-score">{score}</span>
    </div>
    <div class="metric-detail-desc">{description}</div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )