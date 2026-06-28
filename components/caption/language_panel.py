"""
components/caption/language_panel.py

ARRAI Language Panel
"""

from __future__ import annotations

import streamlit as st

from config import (
    DEFAULT_LANGUAGE,
    SUPPORTED_LANGUAGES,
)


# ==========================================================
# PUBLIC
# ==========================================================

def render_language_panel() -> tuple[str, str]:
    """
    Render language selector.

    Returns
    -------
    language_name
    language_code
    """

    st.markdown(
        """
<h3 class="section-title">

Output Language

</h3>
""",
        unsafe_allow_html=True,
    )

    languages = list(SUPPORTED_LANGUAGES.keys())

    default_index = languages.index(DEFAULT_LANGUAGE)

    language_name = st.selectbox(
        "Select Language",
        languages,
        index=default_index,
        
    )

    language_code = SUPPORTED_LANGUAGES[language_name]

    return (
        language_name,
        language_code,
    )