"""
controllers/caption_controller.py

ARRAI Caption Controller
"""

from __future__ import annotations

from PIL import Image

import streamlit as st

from components.layout.layout import (
    start_layout,
    end_layout,
)

from components.caption.workspace import (
    render_workspace,
)

from components.caption.loading_panel import (
    render_loading_panel,
)

from components.caption.result_panel import (
    render_result_panel,
)

from components.caption.stats_panel import (
    render_stats_panel,
)

from components.caption.action_panel import (
    render_action_panel,
)

from components.caption.export_panel import (
    render_export_panel,
)

from components.caption.model_panel import (
    render_model_panel,
)

from utils.session_manager import (
    initialize_session,
    save_generation,
    reset_generation,
    has_result,
)

from utils.model_manager import (
    load_bundle,
    load_model_info,
)

from utils.caption_service import (
    generate,
)

from utils.translator import (
    get_language_flag,
)
# ==========================================================
# INITIALIZATION
# ==========================================================

def _initialize():

    initialize_session()

    bundle = load_bundle()

    model_info = load_model_info(
        bundle,
    )

    return (
        bundle,
        model_info,
    )
# ==========================================================
# GENERATION
# ==========================================================

def _generate_caption(
    image,
    bundle,
    language_name,
    language_code,
):

    with st.spinner(
        "Generating caption..."
    ):

        result = generate(

            image=image,

            bundle=bundle,

            language_code=language_code,

        )

    save_generation(

        caption=result["caption"],

        translation=result["translation"],

        elapsed=result["elapsed"],

        language_name=language_name,

        language_code=language_code,

    )
# ==========================================================
# RESULT
# ==========================================================

def _render_result(bundle):

    if not has_result():

        return

    render_result_panel(

        english_caption=st.session_state.caption,

        translated_caption=st.session_state.translation,

        language_name=st.session_state.language_name,

        language_flag=get_language_flag(

            st.session_state.language_code,

        ),

    )

    st.divider()

    render_stats_panel(

        inference_time=st.session_state.elapsed,

        language=st.session_state.language_name,

        caption=st.session_state.caption,

        device=bundle.device,

    )

    st.divider()

    regenerate = render_action_panel()

    if regenerate:

        reset_generation()

        st.rerun()

    st.divider()

    render_export_panel(

        english_caption=st.session_state.caption,

        translated_caption=st.session_state.translation,

        language_name=st.session_state.language_name,

    )
# ==========================================================
# PUBLIC
# ==========================================================

def render_caption_page() -> None:
    """
    Render Caption Studio Page.
    """

    bundle, model_info = _initialize()

    start_layout()

    uploaded, language_name, language_code, generate_clicked = (
        render_workspace()
    )

    if uploaded is not None and generate_clicked:

        image = Image.open(
            uploaded,
        ).convert(
            "RGB",
        )

        try:

            render_loading_panel()

            _generate_caption(

                image=image,

                bundle=bundle,

                language_name=language_name,

                language_code=language_code,

            )

            st.rerun()

        except Exception as e:

            st.error(
                "Caption generation failed."
            )

            st.exception(e)

    _render_result(
        bundle,
    )

    st.divider()

    render_model_panel(
        model_info,
    )

    end_layout()