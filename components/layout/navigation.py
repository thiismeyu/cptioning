"""
components/layout/navigation.py
ARRAI Premium Navigation
"""
from __future__ import annotations
import streamlit as st

_MENU = [
    ("Home",           "pages/1_Home.py"),
    ("Caption Studio", "pages/2_Caption_Generator.py"),
    ("Evaluation",     "pages/3_Evaluation.py"),
    ("About",          "pages/4_About.py"),
]

def render_navigation() -> None:

    st.markdown("""
<div class="navbar">
    <div style="display:flex;align-items:center;gap:14px;">
        <div style="
            width:42px; height:42px;
            border-radius:12px;
            background:linear-gradient(135deg,#6D5DF6,#27C5FF);
            box-shadow:0 4px 20px rgba(109,93,246,.35);
            display:flex; align-items:center; justify-content:center;
            font-size:20px; color:white; flex-shrink:0;
        ">⬡</div>
        <div>
            <div style="font-size:1.15rem;font-weight:800;letter-spacing:-.03em;color:#F5F7FA;line-height:1;">ARRAI</div>
            <div style="font-size:.68rem;color:#8E98A8;letter-spacing:.02em;">AI Captioning Platform</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5, nav_col6 = st.columns(
        [2, 1, 1, 1, 1, 0.8], gap="small"
    )

    # brand placeholder sudah di HTML atas, nav links di columns
    with nav_col2:
        if st.button("Home", key="nav_home", use_container_width=True):
            st.switch_page("pages/1_Home.py")
    with nav_col3:
        if st.button("Caption Studio", key="nav_caption", use_container_width=True):
            st.switch_page("pages/2_Caption_Generator.py")
    with nav_col4:
        if st.button("Evaluation", key="nav_eval", use_container_width=True):
            st.switch_page("pages/3_Evaluation.py")
    with nav_col5:
        if st.button("About", key="nav_about", use_container_width=True):
            st.switch_page("pages/4_About.py")
    with nav_col6:
        st.markdown("""
<div style="
    display:inline-flex; align-items:center; gap:7px;
    padding:6px 13px;
    border-radius:999px;
    background:rgba(46,204,113,.08);
    border:1px solid rgba(46,204,113,.20);
    margin-top:4px;
">
    <div style="
        width:7px;height:7px;border-radius:50%;
        background:#2ECC71;
        box-shadow:0 0 8px #2ECC71;
        animation:pulse-dot 2s ease-in-out infinite;
    "></div>
    <span style="font-size:.65rem;font-weight:800;letter-spacing:.12em;color:#2ECC71;">LIVE</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="
    height:1px;
    background:linear-gradient(90deg,transparent,rgba(109,93,246,.25),rgba(39,197,255,.15),transparent);
    margin: 8px 0 2rem;
"></div>
""", unsafe_allow_html=True)