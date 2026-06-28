"""
components/caption/stats_panel.py
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


def render_stats_panel(
    inference_time: float,
    language: str,
    caption: str,
    device: str,
) -> None:

    section_title(
        "Generation Statistics",
        "Performance information for the latest inference.",
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Inference",
            f"{inference_time:.2f}s",
        )

    with c2:

        st.metric(
            "Language",
            language,
        )

    with c3:

        st.metric(
            "Words",
            len(caption.split()),
        )

    with c4:

        st.metric(
            "Device",
            device,
        )