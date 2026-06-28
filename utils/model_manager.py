"""
utils/model_manager.py

ARRAI Model Manager
"""

from __future__ import annotations

import streamlit as st

from utils.load_model import (
    load_model,
    get_model_info,
)

from utils.session_manager import (
    get_bundle,
    set_bundle,
)


@st.cache_resource(show_spinner=False)
def _cached_bundle():
    """
    Cache AI model.
    """

    return load_model()


def load_bundle():
    """
    Load AI bundle once.
    """

    bundle = get_bundle()

    if bundle is None:

        with st.spinner("Loading AI Model..."):

            bundle = _cached_bundle()

        set_bundle(bundle)

    return bundle


def load_model_info(bundle):
    """
    Wrapper for model info.
    """

    return get_model_info(bundle)