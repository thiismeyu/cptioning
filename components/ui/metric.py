"""
components/ui/metric.py
"""

from __future__ import annotations

import streamlit as st


def metric_row(
    metrics: list[tuple[str, str]],
) -> None:

    cols = st.columns(len(metrics))

    for col, item in zip(cols, metrics):

        label, value = item

        with col:

            st.metric(
                label,
                value,
            )