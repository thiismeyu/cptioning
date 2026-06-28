"""
utils/session_manager.py

ARRAI Session Manager
"""

from __future__ import annotations

import streamlit as st


DEFAULT_SESSION = {
    "bundle": None,
    "workspace_image":None,
    "history":[],
    "generated": False,
    "caption": "",
    "translation": "",
    "elapsed": 0.0,
    "language_name": "",
    "language_code": "",
}


def initialize_session() -> None:
    """
    Initialize Streamlit session state.
    """

    for key, value in DEFAULT_SESSION.items():

        if key not in st.session_state:

            st.session_state[key] = value


def reset_generation() -> None:
    """
    Reset generation result.
    """

    st.session_state.generated = False
    st.session_state.caption = ""
    st.session_state.translation = ""
    st.session_state.elapsed = 0.0
    st.session_state.language_name = ""
    st.session_state.language_code = ""


def save_generation(
    *,
    caption: str,
    translation: str,
    elapsed: float,
    language_name: str,
    language_code: str,
) -> None:
    """
    Save generation result and store history.
    """

    # ======================================================
    # Current Result
    # ======================================================

    st.session_state.caption = caption
    st.session_state.translation = translation
    st.session_state.elapsed = elapsed
    st.session_state.language_name = language_name
    st.session_state.language_code = language_code
    st.session_state.generated = True

    # ======================================================
    # History
    # ======================================================

    history_item = {
        "caption": caption,
        "translation": translation,
        "language_name": language_name,
        "language_code": language_code,
        "elapsed": elapsed,
    }

    st.session_state.history.insert(
        0,
        history_item,
    )

    # Simpan maksimal 10 history terbaru
    st.session_state.history = (
        st.session_state.history[:10]
    )


def has_result() -> bool:
    """
    Return generation status.
    """

    return st.session_state.generated


def get_bundle():
    """
    Get loaded model bundle.
    """

    return st.session_state.bundle


def set_bundle(bundle) -> None:
    """
    Save model bundle.
    """

    st.session_state.bundle = bundle