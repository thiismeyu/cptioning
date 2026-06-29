"""
components/about/roadmap.py
ARRAI Development Status
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title

_ITEMS = [
    ("done",    "✅", "ClipCap Fine-tuning",
     "Fine-tuned on local Indonesian dataset (191 images, 5 categories)."),
    ("done",    "✅", "Multilingual Translation",
     "Deep Translator supports EN → ID, JA, AR, ZH-CN."),
    ("done",    "✅", "Streamlit Web App",
     "Multi-page app with Caption Studio, Evaluation, and About pages."),
    ("done",    "✅", "Evaluation Pipeline",
     "BLEU, ROUGE-L, METEOR, CIDEr computed on local test set."),
    ("planned", "📋", "Dataset Expansion",
     "Collecting more local images for improved generalization."),
]

def render_roadmap() -> None:

    section_title("Development Status", "Project progress and upcoming milestones.")

    for status, icon, title, desc in _ITEMS:
        st.markdown(
            f"""
<div class="roadmap-row roadmap-{status}">
  <div class="roadmap-icon">{icon}</div>
  <div class="roadmap-body">
    <div class="roadmap-title">{title}</div>
    <div class="roadmap-desc">{desc}</div>
  </div>
  <div class="roadmap-badge roadmap-badge-{status}">
    {"Done" if status == "done" else "Active" if status == "active" else "Planned"}
  </div>
</div>
""",
            unsafe_allow_html=True,
        )