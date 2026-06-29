"""
components/evaluation/score_panel.py
ARRAI Evaluation Score Panel — premium metric cards
"""
from __future__ import annotations
import streamlit as st
from components.ui.section import section_title
from utils.evaluation_service import get_scores, get_raw_metrics

_SCORE_META = {
    "BLEU-1":  {"icon": "🎯", "label": "Unigram Precision",   "color": "primary"},
    "BLEU-4":  {"icon": "📐", "label": "4-gram Fluency",      "color": "accent"},
    "ROUGE-L": {"icon": "🔗", "label": "Longest Subseq.",     "color": "primary"},
    "METEOR":  {"icon": "⭐", "label": "Semantic Similarity", "color": "success"},
    "CIDEr":   {"icon": "🏆", "label": "Consensus Score",     "color": "accent"},
}

def render_score_panel() -> None:

    st.markdown(
        """
<div class="eval-header">
  <div class="eval-eyebrow">
    <span class="eval-dot"></span>
    MODEL PERFORMANCE
  </div>
  <h1 class="eval-title">Evaluation Results</h1>
  <p class="eval-description">
    Fine-tuned ClipCap model evaluated on local Indonesian dataset
    (191 images, 5 categories, 20 test samples).
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

    scores = get_scores()
    cols   = st.columns(len(scores))

    for col, (metric, value) in zip(cols, scores):
        meta = _SCORE_META.get(metric, {"icon": "📊", "label": metric, "color": "primary"})

        with col:
            st.markdown(
                f"""
<div class="score-card score-card-{meta['color']}">
  <div class="score-icon">{meta['icon']}</div>
  <div class="score-value">{value}</div>
  <div class="score-metric">{metric}</div>
  <div class="score-label">{meta['label']}</div>
</div>
""",
                unsafe_allow_html=True,
            )