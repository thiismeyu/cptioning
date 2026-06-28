"""
components/layout/navigation.py

ARRAI Premium Navigation
"""

from __future__ import annotations

import streamlit as st


_MENU = [

    ("Home", "pages/1_Home.py"),

    ("Caption Studio", "pages/2_Caption_Generator.py"),

    ("Evaluation", "pages/3_Evaluation.py"),

    ("About", "pages/4_About.py"),

]


def _logo():

    st.markdown(
        """
<div class="nav-brand">

<div class="nav-logo">

🧠

</div>

<div class="nav-info">

<div class="nav-title">

ARRAI

</div>

<div class="nav-subtitle">

Research Grade AI Platform

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def _status():

    st.markdown(
        """
<div class="nav-status">

<div class="status-dot"></div>

<div class="status-text">

SYSTEM READY

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_navigation():

    left, center, right = st.columns(
        [1.5, 3.5, 1],
        vertical_alignment="center",
    )

    with left:

        _logo()

    with center:

        cols = st.columns(len(_MENU))

        for col, (title, page) in zip(cols, _MENU):

            with col:

                if st.button(
                    title,
                    key=f"nav_{title}",
                    use_container_width=True,
                ):

                    st.switch_page(page)

    with right:

        _status()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )