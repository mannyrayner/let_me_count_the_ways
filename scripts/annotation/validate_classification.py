#!/usr/bin/env python3
"""Validate a v0.1 passage-classification JSON result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TOP_LEVEL_REQUIRED = {
    "occurrence_id", "label_support", "construals", "features", "evidence",
    "needs_more_context", "typology_adequate", "typology_diagnosis", "confidence",
}
TOP_LEVEL_OPTIONAL = {"context_request", "proposed_missing_dimensions"}
PERSPECTIVES = {"speaker", "hearer", "narrator_or_text", "reader"}
FEATURES = {
    "quoted", "negated", "metalinguistic", "conventionally_scripted",
    "strategically_ambiguous", "deceptive_or_manipulative",
    "participant_disagreement", "mixed_reading", "none_of_these",
}
LABELS = {"truth_conditional", "performative", "exclamatory_reflexive"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(result: dict, expected_occurrence_id: str | None = None) -> None:
    require(isinstance(result, dict), "result must be an object")
    keys = set(result)
    require(TOP_LEVEL_REQUIRED <= keys, f"missing keys: {sorted(TOP_LEVEL_REQUIRED - keys)}")
    require(keys <= TOP_LEVEL_REQUIRED | TOP_LEVEL_OPTIONAL,
            f"unexpected keys: {sorted(keys - TOP_LEVEL_REQUIRED - TOP_LEVEL_OPTIONAL)}")
    require(isinstance(result["occurrence_id"], str), "occurrence_id must be a string")
    if expected_occurrence_id is not None:
        require(result["occurrence_id"] == expected_occurrence_id,
                "occurrence_id does not match the requested passage")

    labels = result["label_support"]
    require(isinstance(labels, dict) and set(labels) == LABELS,
            "label_support must contain exactly the three v0.1 labels")
    for label, score in labels.items():
        require(type(score) is int and 0 <= score <= 4,
                f"{label} must be an integer from 0 to 4")

    require(isinstance(result["construals"], list), "construals must be an array")
    for item in result["construals"]:
        require(isinstance(item, dict) and set(item) == {"perspective", "analysis"},
                "each construal must contain perspective and analysis")
        require(item["perspective"] in PERSPECTIVES, "invalid construal perspective")
        require(isinstance(item["analysis"], str), "construal analysis must be a string")

    features = result["features"]
    require(isinstance(features, list), "features must be an array")
    require(len(features) == len(set(features)), "features must be unique")
    require(set(features) <= FEATURES, "features contains an invalid value")

    require(isinstance(result["evidence"], list), "evidence must be an array")
    for item in result["evidence"]:
        require(isinstance(item, dict) and set(item) == {"text", "supports"},
                "each evidence item must contain text and supports")
        require(all(isinstance(item[key], str) for key in item),
                "evidence values must be strings")

    require(type(result["needs_more_context"]) is bool,
            "needs_more_context must be boolean")
    require(type(result["typology_adequate"]) is bool,
            "typology_adequate must be boolean")
    require(isinstance(result["typology_diagnosis"], str),
            "typology_diagnosis must be a string")
    confidence = result["confidence"]
    require(type(confidence) in {int, float} and 0 <= confidence <= 1,
            "confidence must be a number from 0 to 1")

    if "context_request" in result:
        require(result["context_request"] is None or isinstance(result["context_request"], str),
                "context_request must be a string or null")
    if "proposed_missing_dimensions" in result:
        values = result["proposed_missing_dimensions"]
        require(isinstance(values, list) and all(isinstance(value, str) for value in values),
                "proposed_missing_dimensions must be an array of strings")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--expected-occurrence-id")
    args = parser.parse_args()
    result = json.loads(args.input.read_text(encoding="utf-8"))
    validate(result, args.expected_occurrence_id)
    print(f"Classification validation passed: {result['occurrence_id']}")


if __name__ == "__main__":
    main()
