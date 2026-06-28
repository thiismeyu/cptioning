"""
controllers/evaluation_controller.py

ARRAI Evaluation Controller
"""

from __future__ import annotations

import streamlit as st

from components.layout.layout import (
    start_layout,
    end_layout,
)

from components.evaluation.score_panel import (
    render_score_panel,
)

from components.evaluation.metric_panel import (
    render_metric_panel,
)

from components.evaluation.comparison_panel import (
    render_comparison_panel,
)

from components.evaluation.dataset_panel import (
    render_dataset_panel,
)

from components.evaluation.conclusion_panel import (
    render_conclusion_panel,
)


# ==========================================================
# PUBLIC
# ==========================================================

def render_evaluation_page() -> None:
    """
    Render Evaluation Page.
    """

    start_layout()

    render_score_panel()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    render_metric_panel()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    render_comparison_panel()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    render_dataset_panel()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    render_conclusion_panel()

    end_layout()