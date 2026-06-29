"""
components/ui/tag.py
"""

from __future__ import annotations

import streamlit as st


def tags(
    values: list[str],
) -> None:

    html = "".join(f'<span class="tag">{item}</span>' for item in values)

    st.markdown(
        f'<div class="tags">{html}</div>',
        unsafe_allow_html=True,
    )