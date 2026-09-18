import hashlib
import json
from pathlib import Path

import pytest

from scripts.annotation.annotate_canonical_candidates import (
    compatible,
    fingerprint,
    prepare_annotation_input,
    request_body,
    selected_rows,
)
from scripts.annotation.enrich_canonical_candidates import (
    enrich,
    validate_generated_enrichment,
    wide_bounds,
)


def fixture(tmp_path: Path, language="en", policy="PUBLIC_DOMAIN_FULL_CONTEXT_OK",
            occurrence_id="oid", work_id="work"):
    text = "Opening paragraph.\n\nBefore I love you after.\n\nClosing paragraph."
    start = text.index("I love you"); end = start + len("I love you")
    work = tmp_path / "works" / work_id; work.mkdir(parents=True, exist_ok=True)
    canonical_bytes = text.encode("utf-8")
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    (work / "canonical.txt").write_bytes(canonical_bytes)
    (work / "work.json").write_text(json.dumps({"work_id":work_id,"title":"Title","author":"Author",
        "language":language,"source_type":"fixture","canonical_sha256":digest,
        "rights":{"public_render_policy":policy}}), encoding="utf-8")
    candidate={"occurrence_id":occurrence_id,"work_id":work_id,"canonical_sha256":digest,"start":start,"end":end,
        "context_start":start-7,"context_end":end+6,"match":"I love you","context":text[start-7:end+6],
        "pattern_id":"x","pattern_version":"0.11"}
    return {"candidate":candidate,"review":{"decision":"KEEP","confidence":.9,"reason_code":"VALID_EXPLICIT_LOVE_I_YOU"}}


def test_enrichment_validates_offsets_preserves_local_and_is_deterministic(tmp_path):
    source=fixture(tmp_path); first=enrich(source,tmp_path); second=enrich(source,tmp_path)
    assert first["context"] == second["context"]
    assert first["context"]["local"]["text"] == source["candidate"]["context"]
    assert first["translation"] is None
    assert wide_bounds("abc",1,2)==(0,3)


def test_wide_context_expands_nominal_window_outward_across_paragraphs():
    paragraphs = [character * 120 for character in "abcdefg"]
    text = "\n\n".join(paragraphs)
    start = text.index(paragraphs[3]) + 50
    end = start + 10

    ws, we = wide_bounds(text, start, end, radius=150)

    assert ws <= start - 150
    assert we >= end + 150
    assert we - ws > len(paragraphs[3]) * 3
    assert text[start:end] in text[ws:we]


def test_enrichment_translation_placeholder_hash_and_rights(tmp_path):
    source=fixture(tmp_path,"it"); result=enrich(source,tmp_path)
    assert result["translation"]["status"] == "required"
    assert len(result["translation"]["source_language_text_sha256"]) == 64


def test_generated_enrichment_rejects_uncurated_translation_template():
    generated = {
        "example-id": {"translation": {"status": "required", "text": None}}
    }
    with pytest.raises(ValueError, match="incomplete translations: example-id"):
        validate_generated_enrichment(generated)

    generated["example-id"]["translation"] = {
        "status": "provided", "text": "A complete translation."
    }
    validate_generated_enrichment(generated)


def test_enrichment_rejects_translation_for_different_source(tmp_path):
    source = fixture(tmp_path, "it")
    supplied = {"oid": {"translation": {
        "status": "provided", "text": "Translation", "source_occurrence_id": "oid",
        "source_language": "it", "source_language_text_sha256": "0" * 64,
        "scope": "wide_context", "notice": "Analytical aid; not source text.",
    }}}
    with pytest.raises(ValueError, match="incompatible translation provenance"):
        enrich(source, tmp_path, supplied)


def test_enrichment_allows_permissioned_context_but_restricts_private_context(tmp_path):
    permissioned=fixture(tmp_path / "permissioned","en","PERMISSIONED_CONTEXT_OK")
    assert enrich(permissioned,tmp_path / "permissioned")

    private=fixture(tmp_path / "private","en","LOCAL_PRIVATE_NO_PUBLIC_CONTEXT")
    with pytest.raises(ValueError,match="rights policy"): enrich(private,tmp_path / "private")
    assert enrich(private,tmp_path / "private",allow_private_output=True)


def test_enrichment_rejects_hash_and_offset_drift(tmp_path):
    source=fixture(tmp_path); source["candidate"]["canonical_sha256"]="0"*64
    with pytest.raises(ValueError,match="hash mismatch"): enrich(source,tmp_path)
    source=fixture(tmp_path / "offset"); source["candidate"]["match"]="wrong"
    with pytest.raises(ValueError,match="offsets"): enrich(source,tmp_path / "offset")


def test_annotation_input_and_structured_request_are_layered(tmp_path):
    row=enrich(fixture(tmp_path),tmp_path)
    prepared=prepare_annotation_input(row)
    assert prepared["SOURCE_TEXT"]["exact_match"] == "I love you"
    assert prepared["TRANSLATION_ANALYTICAL_AID"] is None
    body=request_body("PROMPT",{"type":"object"},prepared,"model")
    assert body["model"]=="model" and body["text"]["format"]["type"]=="json_schema"
    assert "SOURCE_TEXT" in body["input"]


def test_annotation_rejects_incomplete_required_translation(tmp_path):
    row=enrich(fixture(tmp_path,"it"),tmp_path)
    with pytest.raises(ValueError,match="required translation is incomplete"):
        prepare_annotation_input(row)


def test_annotation_allows_optional_narrative_context_to_be_absent(tmp_path):
    row=enrich(fixture(tmp_path),tmp_path)
    assert prepare_annotation_input(row)["MODEL_GENERATED_SOURCE_GROUNDED_SUMMARY"] is None


def test_all_mode_is_explicit_and_selects_every_keep_record(tmp_path):
    enriched = tmp_path / "enriched.jsonl"
    rows = [enrich(fixture(tmp_path / "corpus", occurrence_id=f"oid-{i}"),
                   tmp_path / "corpus") for i in range(2)]
    enriched.write_text("".join(json.dumps(row) + "\n" for row in rows))
    assert len(selected_rows(enriched, None, True)) == 2
    with pytest.raises(ValueError, match="choose"):
        selected_rows(enriched, None, False)


def test_annotation_fingerprint_controls_resumption(tmp_path):
    directory = tmp_path / "annotation"; directory.mkdir()
    key = fingerprint("oid", "model", "prompt", "schema", "input-one")
    (directory / "provenance.json").write_text(json.dumps(key))
    (directory / "output.json").write_text(json.dumps({"occurrence_id": "oid"}))

    def validator(value, oid):
        if value.get("occurrence_id") != oid:
            raise ValueError("wrong id")

    assert compatible(directory, validator, key)
    changed = fingerprint("oid", "model", "prompt", "schema", "input-two")
    assert not compatible(directory, validator, changed)
