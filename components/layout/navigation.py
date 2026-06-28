"""
components/layout/navigation.py

ARRAI Premium Navigation — full HTML render, zero Streamlit buttons.
Nav links pakai st.button tapi di-override CSS jadi terlihat seperti
anchor link biasa, bukan tombol gradien.
"""

from __future__ import annotations

import streamlit as st


_MENU = [
    ("Home",            "pages/1_Home.py"),
    ("Caption Studio",  "pages/2_Caption_Generator.py"),
    ("Evaluation",      "pages/3_Evaluation.py"),
    ("About",           "pages/4_About.py"),
]


# ==========================================================
# PRIVATE
# ==========================================================

def _logo() -> None:

    st.markdown(
        """
<div class="nav-brand">

  <div class="nav-logo-box">
    <span class="nav-logo-icon">⬡</span>
  </div>

  <div class="nav-info">
    <div class="nav-title">ARRAI</div>
    <div class="nav-subtitle">AI Captioning Platform</div>
  </div>

</div>
""",
        unsafe_allow_html=True,
    )


def _status() -> None:

    st.markdown(
        """
<div class="nav-status">
  <span class="status-dot"></span>
  <span class="status-text">LIVE</span>
</div>
""",
        unsafe_allow_html=True,
    )


def _nav_links() -> None:
    """
    Render nav links sebagai st.button dengan CSS class khusus
    supaya terlihat seperti text link, bukan gradient button.
    """

    cols = st.columns(len(_MENU), gap="small")

    for col, (title, page) in zip(cols, _MENU):

        with col:

            if st.button(
                title,
                key=f"nav_{title}",
                use_container_width=True,
            ):
                st.switch_page(page)


# ==========================================================
# PUBLIC
# ==========================================================

def render_navigation() -> None:

    # Wrapper nav bar
    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    left, center, right = st.columns(
        [1.4, 3.6, 0.8],
        vertical_alignment="center",
        gap="small",
    )

    with left:
        _logo()

    with center:
        _nav_links()

    with right:
        _status()

    st.markdown('</div>', unsafe_allow_html=True)

    # Divider bawah navbar
    st.markdown(
        '<div class="nav-divider"></div>',
        unsafe_allow_html=True,
    )