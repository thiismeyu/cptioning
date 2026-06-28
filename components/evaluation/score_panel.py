"""
components/evaluation/score_panel.py

ARRAI Evaluation Score Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title

from utils.evaluation_service import get_scores


# ==========================================================
# PUBLIC
# ==========================================================

def render_score_panel() -> None:

    section_title(

        "Evaluation Metrics",

        "Performance obtained from the fine-tuned ClipCap model.",

    )

    scores = get_scores()

    cols = st.columns(len(scores))

    for col, (metric, value) in zip(cols, scores):

        with col:

            st.markdown(

                f"""
<div class="glass">

<div class="metric-name">

{metric}

</div>

<div class="metric-score">

{value}

</div>

</div>
""",

                unsafe_allow_html=True,

            )