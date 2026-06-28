"""
components/ui/glass.py

ARRAI Glass Component
"""

from __future__ import annotations

import streamlit as st


def open_glass(
    class_name: str = "",
) -> None:
    """
    Open glass container.
    """

    classes = "glass"

    if class_name:
        classes += f" {class_name}"

    st.markdown(
        f'<div class="{classes}">',
        unsafe_allow_html=True,
    )


def close_glass() -> None:
    """
    Close glass container.
    """

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


class Glass:

    """
    Context Manager

    Example

    with Glass():

        st.write(...)
    """

    def __init__(
        self,
        class_name: str = "",
    ):

        self.class_name = class_name

    def __enter__(self):

        open_glass(self.class_name)

    def __exit__(
        self,
        exc_type,
        exc,
        traceback,
    ):

        close_glass()