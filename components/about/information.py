"""
components/about/information.py
ARRAI Project Information + Pipeline + Tech Stack
"""
from __future__ import annotations
import streamlit as st
from config import APP_VERSION, APP_AUTHOR, INSTITUTION, RESEARCHER
from components.ui.section import section_title

_PIPELINE_STEPS = [
    ("🖼", "Image Input",        "Upload PNG/JPG/JPEG image (max 10 MB)"),
    ("🧠", "CLIP ViT-B/32",     "Extracts high-level visual embeddings (512-dim)"),
    ("⚙",  "Transformer Mapper","Projects CLIP features into GPT-2 latent space"),
    ("💬", "GPT-2",             "Generates natural English caption (beam search, 5 beams)"),
    ("🌍", "Deep Translator",   "Translates caption into selected target language"),
    ("✅", "Caption Output",    "Ready to copy, export as TXT or JSON"),
]

_TECH_STACK = [
    ("🐍", "Python 3.10",       "Core language"),
    ("🎈", "Streamlit",         "Web framework"),
    ("🔥", "PyTorch",           "Deep learning backend"),
    ("👁",  "CLIP ViT-B/32",    "OpenAI vision encoder"),
    ("💬", "GPT-2",             "OpenAI language model"),
    ("🌍", "Deep Translator",   "Multilingual translation"),
    ("🖼", "Pillow",            "Image processing"),
]

def render_information() -> None:

    # ── AI Pipeline ───────────────────────────────────────
    section_title("AI Pipeline", "End-to-end caption generation workflow.")

    for icon, name, desc in _PIPELINE_STEPS:
        st.markdown(
            f"""
<div class="info-pipeline-row">
  <div class="info-pipeline-icon">{icon}</div>
  <div class="info-pipeline-body">
    <div class="info-pipeline-name">{name}</div>
    <div class="info-pipeline-desc">{desc}</div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ── Tech Stack + Project Info (side by side) ──────────
    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        section_title("Technology Stack", "Libraries and frameworks powering ARRAI.")
        for icon, name, role in _TECH_STACK:
            st.markdown(
                f"""
<div class="tech-row">
  <div class="tech-icon">{icon}</div>
  <div class="tech-body">
    <span class="tech-name">{name}</span>
    <span class="tech-role">{role}</span>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )

    with right:
        section_title("Project Info", "Research metadata and version.")
        for label, value in [
            ("Researcher",  RESEARCHER),
            ("Institution", INSTITUTION),
            ("Author",      APP_AUTHOR),
            ("Version",     APP_VERSION),
            ("Target",      "Sinta 2–3 Journal"),
            ("Status",      "Active Development"),
        ]:
            st.markdown(
                f"""
<div class="info-kv-row">
  <span class="info-kv-label">{label}</span>
  <span class="info-kv-value">{value}</span>
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)