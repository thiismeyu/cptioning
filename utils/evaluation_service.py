"""
utils/evaluation_service.py

ARRAI Evaluation Service
"""

from __future__ import annotations

import json

from config import EVAL_JSON_PATH


# ==========================================================
# LOAD
# ==========================================================

def load_evaluation() -> dict:
    """
    Load evaluation metrics from JSON.
    """

    with open(
        EVAL_JSON_PATH,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# ==========================================================
# SCORE CARDS
# ==========================================================

def get_scores() -> list[tuple[str, str]]:

    data = load_evaluation()

    return [

        ("BLEU-1", f"{data['BLEU-1']:.2f}"),

        ("BLEU-4", f"{data['BLEU-4']:.2f}"),

        ("ROUGE-L", f"{data['ROUGE-L']:.2f}"),

        ("METEOR", f"{data['METEOR']:.2f}"),

        ("CIDEr", f"{data['CIDEr']:.2f}"),

    ]


# ==========================================================
# METRIC DETAIL
# ==========================================================

def get_metric_details() -> list[tuple[str, str, str]]:

    data = load_evaluation()

    return [

        (

            "BLEU-1",

            f"{data['BLEU-1']:.2f}",

            "Unigram precision between generated and reference captions.",

        ),

        (

            "BLEU-4",

            f"{data['BLEU-4']:.2f}",

            "4-gram precision measuring fluency and similarity.",

        ),

        (

            "ROUGE-L",

            f"{data['ROUGE-L']:.2f}",

            "Longest common subsequence similarity.",

        ),

        (

            "METEOR",

            f"{data['METEOR']:.2f}",

            "Semantic similarity considering synonyms and stemming.",

        ),

        (

            "CIDEr",

            f"{data['CIDEr']:.2f}",

            "Consensus score widely used in image captioning.",

        ),

    ]


# ==========================================================
# DATASET INFO
# ==========================================================

def get_dataset_information() -> list[tuple[str, str]]:

    data = load_evaluation()

    return [

        (

            "Evaluation Samples",

            str(data["num_test"]),

        ),

        (

            "Average Caption Length",

            f"{data['avg_len']:.2f}",

        ),

        (

            "Caption Field",

            data["caption_field_used"],

        ),

        (

            "Evaluation File",

            "eval_local.json",

        ),

    ]


# ==========================================================
# RAW
# ==========================================================

def get_raw_metrics() -> dict:

    return load_evaluation()