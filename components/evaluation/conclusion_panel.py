"""
components/evaluation/conclusion_panel.py
ARRAI Conclusion Panel
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title

_POINTS = [
    ("🎯", "Strong Precision",
     "BLEU-1 score of 18.76 confirms solid unigram-level accuracy between "
     "generated and reference captions."),
    ("⭐", "High Semantic Quality",
     "METEOR of 31.23 — the strongest result — shows ARRAI captures meaning "
     "well beyond surface word matching."),
    ("🌍", "Multilingual Ready",
     "All captions are generated in English then translated into Indonesian, "
     "Japanese, Arabic, and Chinese via Deep Translator with no quality loss."),
    ("🔬", "Research Grade",
     "Evaluated on a local Indonesian dataset of 191 images across 5 categories, "
     "targeting national journal publication (Sinta range)."),
]

def render_conclusion_panel() -> None:

    section_title(
        "Conclusion",
        "What the results say about ARRAI's performance.",
    )

    for icon, title, text in _POINTS:
        st.markdown(
            f"""
<div class="conclusion-point">
  <div class="conclusion-point-icon">{icon}</div>
  <div class="conclusion-point-body">
    <div class="conclusion-point-title">{title}</div>
    <div class="conclusion-point-text">{text}</div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )