"""
components/ui/card.py

ARRAI Card Component
"""

from __future__ import annotations

import streamlit as st


def open_card() -> None:

    st.markdown(
        """
<div class="glass">
""",
        unsafe_allow_html=True,
    )


def close_card() -> None:

    st.markdown(
        """
</div>
""",
        unsafe_allow_html=True,
    )