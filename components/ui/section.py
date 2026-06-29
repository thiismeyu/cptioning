"""
components/ui/section.py
"""

from __future__ import annotations

import streamlit as st


def section_title(
    title: str,
    description: str | None = None,
) -> None:

    st.markdown(
        f'<h2 class="section-title">{title}</h2>',
        unsafe_allow_html=True,
    )

    if description:

        st.markdown(
            f'<p class="section-description">{description}</p>',
            unsafe_allow_html=True,
        )