"""
components/caption/action_panel.py

ARRAI Action Panel
"""

from __future__ import annotations

import streamlit as st


# ==========================================================
# PUBLIC
# ==========================================================

def render_action_panel() -> bool:
    """
    Render action buttons.

    Returns
    -------
    bool
        True if regenerate button is clicked.
    """

    st.markdown(
        '<h2 class="section-title">Actions</h2>',
        unsafe_allow_html=True,
    )

    regenerate = st.button(
        "🔄 Generate Again",
        use_container_width=True,
    )

    return regenerate