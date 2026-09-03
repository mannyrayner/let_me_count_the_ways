#!/usr/bin/env python3
"""Validate a v0.1, v0.2, or v0.3 passage-classification JSON result."""

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
    """Validate a v0.1 result; retained as the backwards-compatible API."""
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


V0_2_TOP_LEVEL = {
    "occurrence_id", "core_love_content", "realisation", "current_discourse_act",
    "contextual_modification", "participant_construals", "disagreements",
    "assessments", "evidence", "background_knowledge", "context_needs",
    "ontology_assessment", "notes",
}
V0_2_LABELS = {"truth_conditional", "performative", "exclamatory_reflexive"}
REALISATION_TYPES = {
    "direct_represented_speech", "quotation_revoicing", "reported_speech",
    "narratively_attributed_speech", "imagined_speech",
    "verbalisation_of_nonverbal_behaviour", "hypothetical_counterfactual",
    "hedged", "negated", "metalinguistic_mention", "other",
}
ACT_TYPES = {
    "direct_avowal", "reassurance", "explanation", "quotation",
    "elicitation_of_reaffirmation", "pressure", "use_as_evidence",
    "distancing", "hedging", "rejection", "reinterpretation", "manipulation",
    "irony", "other",
}
MODIFICATION_EFFECTS = {
    "preserves", "weakens", "strengthens", "redirects", "quotes", "distances",
    "challenges", "manipulates", "other",
}
ANALYTICAL_LAYERS = {
    "core_love_content", "realisation", "current_discourse_act",
    "contextual_modification", "participant_construals", "disagreements",
    "assessments", "background_knowledge", "ontology_assessment",
}
ASSESSMENT_NAMES = {
    "deception_misrepresentation", "manipulation_pressure", "strategic_ambiguity",
}


def require_exact_keys(value: object, keys: set[str], name: str) -> dict:
    require(isinstance(value, dict), f"{name} must be an object")
    actual = set(value)
    require(actual == keys,
            f"{name} must contain exactly {sorted(keys)}; got {sorted(actual)}")
    return value


def require_string(value: object, name: str, nullable: bool = False) -> None:
    if nullable and value is None:
        return
    require(isinstance(value, str) and bool(value.strip()), f"{name} must be a non-empty string")


def require_confidence(value: object, name: str, nullable: bool = False) -> None:
    if nullable and value is None:
        return
    require(type(value) in {int, float} and 0 <= value <= 1,
            f"{name} must be a number from 0 to 1")


def require_enum(value: object, allowed: set[str], name: str) -> None:
    require(isinstance(value, str) and value in allowed, f"invalid {name}: {value!r}")


def require_unique_enum_array(value: object, allowed: set[str], name: str,
                              min_items: int = 0) -> list:
    require(isinstance(value, list), f"{name} must be an array")
    require(len(value) >= min_items, f"{name} must contain at least {min_items} item(s)")
    require(all(isinstance(item, str) for item in value), f"{name} values must be strings")
    require(len(value) == len(set(value)), f"{name} values must be unique")
    require(set(value) <= allowed, f"{name} contains an invalid value")
    return value


def require_unique_string_array(value: object, name: str, min_items: int = 0) -> list[str]:
    require(isinstance(value, list), f"{name} must be an array")
    require(len(value) >= min_items, f"{name} must contain at least {min_items} item(s)")
    require(all(isinstance(item, str) and bool(item.strip()) for item in value),
            f"{name} values must be non-empty strings")
    require(len(value) == len(set(value)), f"{name} values must be unique")
    return value


def validate_open_multi_value_layer(value: object, *, name: str,
                                    values_key: str, allowed: set[str],
                                    include_actuality: bool = False) -> None:
    keys = {values_key, "other_description", "analysis", "confidence"}
    if include_actuality:
        keys.add("actuality")
    item = require_exact_keys(value, keys, name)
    selected = require_unique_enum_array(item[values_key], allowed,
                                         f"{name}.{values_key}", min_items=1)
    if "other" in selected:
        require_string(item["other_description"], f"{name}.other_description")
    else:
        require(item["other_description"] is None,
                f"{name}.other_description must be null unless other is selected")
    if include_actuality:
        require_enum(item["actuality"],
                     {"spoken", "written", "not_spoken", "uncertain", "not_applicable"},
                     f"{name}.actuality")
    require_string(item["analysis"], f"{name}.analysis")
    require_confidence(item["confidence"], f"{name}.confidence")


def validate_v0_2(result: dict, expected_occurrence_id: str | None = None) -> None:
    """Validate the layered v0.2 annotation contract without third-party packages."""
    root = require_exact_keys(result, V0_2_TOP_LEVEL, "result")
    require_string(root["occurrence_id"], "occurrence_id")
    if expected_occurrence_id is not None:
        require(root["occurrence_id"] == expected_occurrence_id,
                "occurrence_id does not match the requested passage")

    core = require_exact_keys(
        root["core_love_content"],
        {"label_support", "mixed_reading", "relationship_modifier", "analysis", "confidence"},
        "core_love_content",
    )
    labels = require_exact_keys(core["label_support"], V0_2_LABELS,
                                "core_love_content.label_support")
    for label, score in labels.items():
        require(type(score) is int and 0 <= score <= 4,
                f"core_love_content.label_support.{label} must be an integer from 0 to 4")
    mixed = require_exact_keys(core["mixed_reading"],
                               {"is_mixed", "basis", "justification"},
                               "core_love_content.mixed_reading")
    require(type(mixed["is_mixed"]) is bool, "mixed_reading.is_mixed must be boolean")
    if mixed["is_mixed"]:
        require_enum(mixed["basis"],
                     {"substantial_multiple_support", "qualitative_interaction"},
                     "mixed_reading.basis")
        require_string(mixed["justification"], "mixed_reading.justification")
        if mixed["basis"] == "substantial_multiple_support":
            require(sum(score >= 2 for score in labels.values()) >= 2,
                    "substantial_multiple_support requires at least two core scores of 2 or more")
    else:
        require(mixed["basis"] == "none", "non-mixed reading must use basis none")
        require(mixed["justification"] is None,
                "non-mixed reading must use a null justification")
    require_string(core["relationship_modifier"], "core_love_content.relationship_modifier",
                   nullable=True)
    require_string(core["analysis"], "core_love_content.analysis")
    require_confidence(core["confidence"], "core_love_content.confidence")

    validate_open_multi_value_layer(
        root["realisation"], name="realisation", values_key="types",
        allowed=REALISATION_TYPES, include_actuality=True,
    )
    validate_open_multi_value_layer(
        root["current_discourse_act"], name="current_discourse_act",
        values_key="types", allowed=ACT_TYPES,
    )
    validate_open_multi_value_layer(
        root["contextual_modification"], name="contextual_modification",
        values_key="effects", allowed=MODIFICATION_EFFECTS,
    )

    require(isinstance(root["participant_construals"], list),
            "participant_construals must be an array")
    for index, value in enumerate(root["participant_construals"]):
        name = f"participant_construals[{index}]"
        item = require_exact_keys(
            value, {"role", "discourse_level", "status", "analysis", "confidence"}, name)
        require_string(item["role"], f"{name}.role")
        require_enum(item["discourse_level"],
                     {"core_love_content", "current_discourse_act", "both"},
                     f"{name}.discourse_level")
        require_enum(item["status"], {"supported", "uncertain", "unavailable"},
                     f"{name}.status")
        if item["status"] == "unavailable":
            require_string(item["analysis"], f"{name}.analysis")
            require(item["confidence"] is None,
                    f"{name} unavailable construal must have null confidence")
        else:
            require_string(item["analysis"], f"{name}.analysis")
            require_confidence(item["confidence"], f"{name}.confidence")

    require(isinstance(root["disagreements"], list), "disagreements must be an array")
    evidence_references: list[tuple[str, list]] = []
    for index, value in enumerate(root["disagreements"]):
        name = f"disagreements[{index}]"
        item = require_exact_keys(
            value, {"parties", "subject", "description", "evidence_ids", "confidence"}, name)
        require_unique_string_array(item["parties"], f"{name}.parties", 2)
        require_string(item["subject"], f"{name}.subject")
        require_string(item["description"], f"{name}.description")
        require_unique_string_array(item["evidence_ids"], f"{name}.evidence_ids")
        require_confidence(item["confidence"], f"{name}.confidence")
        evidence_references.append((name, item["evidence_ids"]))

    assessments = require_exact_keys(root["assessments"], ASSESSMENT_NAMES, "assessments")
    for assessment_name, value in assessments.items():
        name = f"assessments.{assessment_name}"
        item = require_exact_keys(value, {"status", "analysis", "confidence"}, name)
        require_enum(item["status"], {"supported", "unsupported", "uncertain_not_assessable"},
                     f"{name}.status")
        require_string(item["analysis"], f"{name}.analysis")
        require_confidence(item["confidence"], f"{name}.confidence")

    require(isinstance(root["evidence"], list), "evidence must be an array")
    evidence_ids = []
    for index, value in enumerate(root["evidence"]):
        name = f"evidence[{index}]"
        item = require_exact_keys(
            value,
            {"evidence_id", "source", "quotation_or_description", "supports", "confidence"},
            name,
        )
        require_string(item["evidence_id"], f"{name}.evidence_id")
        evidence_ids.append(item["evidence_id"])
        require_enum(item["source"], {"local_text", "supplied_metadata", "background_knowledge"},
                     f"{name}.source")
        require_string(item["quotation_or_description"], f"{name}.quotation_or_description")
        require_string(item["supports"], f"{name}.supports")
        require_confidence(item["confidence"], f"{name}.confidence")
    require(len(evidence_ids) == len(set(evidence_ids)), "evidence IDs must be unique")
    for name, references in evidence_references:
        require(set(references) <= set(evidence_ids), f"{name} refers to an unknown evidence ID")

    background = require_exact_keys(
        root["background_knowledge"],
        {"used", "familiarity", "confidence", "contribution", "notes"},
        "background_knowledge",
    )
    require(type(background["used"]) is bool, "background_knowledge.used must be boolean")
    require_enum(background["familiarity"], {"none", "limited", "moderate", "extensive"},
                 "background_knowledge.familiarity")
    require_string(background["notes"], "background_knowledge.notes", nullable=True)
    background_evidence = any(
        item["source"] == "background_knowledge" for item in root["evidence"])
    if background["used"]:
        require_confidence(background["confidence"], "background_knowledge.confidence")
        require_string(background["contribution"], "background_knowledge.contribution")
        require(background_evidence,
                "used background knowledge requires at least one background_knowledge evidence item")
    else:
        require(background["confidence"] is None and background["contribution"] is None,
                "unused background knowledge must have null confidence and contribution")
        require(not background_evidence,
                "background_knowledge evidence requires background_knowledge.used to be true")

    require(isinstance(root["context_needs"], list), "context_needs must be an array")
    for index, value in enumerate(root["context_needs"]):
        name = f"context_needs[{index}]"
        item = require_exact_keys(value, {"need", "layers", "claim", "request"}, name)
        require_enum(item["need"],
                     {"required_for_core_classification", "useful_for_richer_interpretation"},
                     f"{name}.need")
        require_unique_enum_array(item["layers"], ANALYTICAL_LAYERS, f"{name}.layers", 1)
        require_string(item["claim"], f"{name}.claim")
        require_string(item["request"], f"{name}.request")

    ontology = require_exact_keys(
        root["ontology_assessment"],
        {"adequate", "diagnosis", "proposed_missing_dimensions"},
        "ontology_assessment",
    )
    require(type(ontology["adequate"]) is bool, "ontology_assessment.adequate must be boolean")
    require_string(ontology["diagnosis"], "ontology_assessment.diagnosis")
    require(isinstance(ontology["proposed_missing_dimensions"], list),
            "ontology_assessment.proposed_missing_dimensions must be an array")
    for value in ontology["proposed_missing_dimensions"]:
        require_string(value, "ontology_assessment.proposed_missing_dimensions item")
    require_string(root["notes"], "notes", nullable=True)


V0_3_TOP_LEVEL = {
    "occurrence_id", "core_classification", "other_diagnosis", "utterance_status",
    "contextual_interpretation", "evidence", "background_knowledge",
    "ontology_assessment", "notes",
}
V0_3_LABELS = {
    "truth_conditional", "performative", "exclamatory_reflexive", "other",
}
UTTERANCE_STATUSES = {
    "direct", "quoted_or_revoiced", "reported", "imagined", "written",
    "nonverbal_verbalised", "hypothetical", "other",
}


def validate_v0_3(result: dict, expected_occurrence_id: str | None = None) -> None:
    """Validate the compact v0.3 T/P/E/O annotation contract."""
    root = require_exact_keys(result, V0_3_TOP_LEVEL, "result")
    require_string(root["occurrence_id"], "occurrence_id")
    if expected_occurrence_id is not None:
        require(root["occurrence_id"] == expected_occurrence_id,
                "occurrence_id does not match the requested passage")

    core = require_exact_keys(
        root["core_classification"],
        {"label_support", "confidence", "analysis", "ambiguity"},
        "core_classification",
    )
    labels = require_exact_keys(core["label_support"], V0_3_LABELS,
                                "core_classification.label_support")
    for label, score in labels.items():
        require(type(score) is int and 0 <= score <= 4,
                f"core_classification.label_support.{label} must be an integer from 0 to 4")
    require_confidence(core["confidence"], "core_classification.confidence")
    require_string(core["analysis"], "core_classification.analysis")
    require_string(core["ambiguity"], "core_classification.ambiguity", nullable=True)

    diagnosis = require_exact_keys(
        root["other_diagnosis"], {"tpe_failure", "core_not_context"}, "other_diagnosis")
    if labels["other"] > 0:
        require_string(diagnosis["tpe_failure"], "other_diagnosis.tpe_failure")
        require_string(diagnosis["core_not_context"], "other_diagnosis.core_not_context")
    else:
        require(diagnosis["tpe_failure"] is None and diagnosis["core_not_context"] is None,
                "other_diagnosis fields must be null when the O score is 0")

    status = require_exact_keys(
        root["utterance_status"], {"status", "description"}, "utterance_status")
    require_enum(status["status"], UTTERANCE_STATUSES, "utterance_status.status")
    require_string(status["description"], "utterance_status.description")
    require_string(root["contextual_interpretation"], "contextual_interpretation")

    require(isinstance(root["evidence"], list) and bool(root["evidence"]),
            "evidence must be a non-empty array")
    evidence_ids = []
    for index, value in enumerate(root["evidence"]):
        name = f"evidence[{index}]"
        item = require_exact_keys(
            value,
            {"evidence_id", "source", "quotation_or_description", "supports", "confidence"},
            name,
        )
        require_string(item["evidence_id"], f"{name}.evidence_id")
        evidence_ids.append(item["evidence_id"])
        require_enum(item["source"],
                     {"local_text", "supplied_metadata", "background_knowledge"},
                     f"{name}.source")
        require_string(item["quotation_or_description"], f"{name}.quotation_or_description")
        require_string(item["supports"], f"{name}.supports")
        require_confidence(item["confidence"], f"{name}.confidence")
    require(len(evidence_ids) == len(set(evidence_ids)), "evidence IDs must be unique")

    background = require_exact_keys(
        root["background_knowledge"],
        {"used", "familiarity", "confidence", "contribution"},
        "background_knowledge",
    )
    require(type(background["used"]) is bool, "background_knowledge.used must be boolean")
    require_enum(background["familiarity"], {"none", "limited", "moderate", "extensive"},
                 "background_knowledge.familiarity")
    background_evidence = any(
        item["source"] == "background_knowledge" for item in root["evidence"])
    if background["used"]:
        require_confidence(background["confidence"], "background_knowledge.confidence")
        require_string(background["contribution"], "background_knowledge.contribution")
        require(background_evidence,
                "used background knowledge requires at least one background_knowledge evidence item")
    else:
        require(background["confidence"] is None and background["contribution"] is None,
                "unused background knowledge must have null confidence and contribution")
        require(not background_evidence,
                "background_knowledge evidence requires background_knowledge.used to be true")

    ontology = require_exact_keys(
        root["ontology_assessment"],
        {"fit", "diagnosis", "candidate_recurrent_dimension"},
        "ontology_assessment",
    )
    require_enum(ontology["fit"], {"natural", "strained", "inadequate"},
                 "ontology_assessment.fit")
    require_string(ontology["diagnosis"], "ontology_assessment.diagnosis")
    require_string(ontology["candidate_recurrent_dimension"],
                   "ontology_assessment.candidate_recurrent_dimension", nullable=True)
    require_string(root["notes"], "notes", nullable=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--expected-occurrence-id")
    parser.add_argument("--schema-version", choices=["0.1", "0.2", "0.3", "0.3.1"], default="0.1")
    args = parser.parse_args()
    result = json.loads(args.input.read_text(encoding="utf-8"))
    validators = {
        "0.1": validate, "0.2": validate_v0_2,
        "0.3": validate_v0_3, "0.3.1": validate_v0_3,
    }
    validator = validators[args.schema_version]
    validator(result, args.expected_occurrence_id)
    print(f"Classification v{args.schema_version} validation passed: {result['occurrence_id']}")


if __name__ == "__main__":
    main()
