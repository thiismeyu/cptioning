"""
components/caption/generate_panel.py

ARRAI Generate Panel
"""

from __future__ import annotations

import streamlit as st


# ==========================================================
# PUBLIC
# ==========================================================

def render_generate_panel() -> bool:

    st.markdown(
        '<h3 class="section-title">Generate Caption</h3>',
        unsafe_allow_html=True,
    )

    return st.button(
        "🚀 Generate Caption",
        type="primary",
        use_container_width=True,
    )