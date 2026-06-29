"""
components/evaluation/dataset_panel.py
ARRAI Dataset Info Panel
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title
from utils.evaluation_service import get_dataset_information

_ICONS = {
    "Evaluation Samples":    "🗂",
    "Average Caption Length": "📏",
    "Caption Field":          "🏷",
    "Evaluation File":        "📄",
}

def render_dataset_panel() -> None:

    section_title(
        "Dataset & Configuration",
        "Training and evaluation dataset details.",
    )

    items = get_dataset_information()
    cols  = st.columns(len(items))

    for col, (key, value) in zip(cols, items):
        icon = _ICONS.get(key, "📌")
        with col:
            st.markdown(
                f"""
<div class="dataset-stat-card">
  <div class="dataset-stat-icon">{icon}</div>
  <div class="dataset-stat-value">{value}</div>
  <div class="dataset-stat-label">{key}</div>
</div>
""",
                unsafe_allow_html=True,
            )