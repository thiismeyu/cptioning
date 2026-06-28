"""
components/ui/button.py

ARRAI Button Components
"""

from __future__ import annotations

import streamlit as st


# ==========================================================
# PRIMARY BUTTON
# ==========================================================

def primary_button(
    label: str,
    page: str,
    key: str,
    *,
    disabled: bool = False,
) -> None:
    """
    Render primary navigation button.
    """

    if st.button(
        label,
        key=key,
        type="primary",
        use_container_width=True,
        disabled=disabled,
    ):
        st.switch_page(page)


# ==========================================================
# SECONDARY BUTTON
# ==========================================================

def secondary_button(
    label: str,
    page: str,
    key: str,
    *,
    disabled: bool = False,
) -> None:
    """
    Render secondary navigation button.
    """

    if st.button(
        label,
        key=key,
        use_container_width=True,
        disabled=disabled,
    ):
        st.switch_page(page)


# ==========================================================
# NORMAL BUTTON
# ==========================================================

def button(
    label: str,
    *,
    key: str,
    button_type: str = "secondary",
    disabled: bool = False,
) -> bool:
    """
    Render reusable Streamlit button.

    Returns
    -------
    bool
        True if clicked.
    """

    return st.button(
        label,
        key=key,
        type=button_type,
        use_container_width=True,
        disabled=disabled,
    )