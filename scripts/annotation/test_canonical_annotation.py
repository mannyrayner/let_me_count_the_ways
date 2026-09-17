import hashlib
import json
from pathlib import Path

import pytest

from scripts.annotation.annotate_canonical_candidates import prepare_annotation_input, request_body
from scripts.annotation.enrich_canonical_candidates import enrich, wide_bounds


def fixture(tmp_path: Path, language="en", policy="PUBLIC_DOMAIN_FULL_CONTEXT_OK"):
    text = "Opening paragraph.\n\nBefore I love you after.\n\nClosing paragraph."
    start = text.index("I love you"); end = start + len("I love you")
    work = tmp_path / "works" / "work"; work.mkdir(parents=True)
    digest = hashlib.sha256(text.encode()).hexdigest()
    (work / "canonical.txt").write_text(text, encoding="utf-8")
    (work / "work.json").write_text(json.dumps({"work_id":"work","title":"Title","author":"Author",
        "language":language,"source_type":"fixture","canonical_sha256":digest,
        "rights":{"public_render_policy":policy}}), encoding="utf-8")
    candidate={"occurrence_id":"oid","work_id":"work","canonical_sha256":digest,"start":start,"end":end,
        "context_start":start-7,"context_end":end+6,"match":"I love you","context":text[start-7:end+6],
        "pattern_id":"x","pattern_version":"0.11"}
    return {"candidate":candidate,"review":{"decision":"KEEP","confidence":.9,"reason_code":"VALID_EXPLICIT_LOVE_I_YOU"}}


def test_enrichment_validates_offsets_preserves_local_and_is_deterministic(tmp_path):
    source=fixture(tmp_path); first=enrich(source,tmp_path); second=enrich(source,tmp_path)
    assert first["context"] == second["context"]
    assert first["context"]["local"]["text"] == source["candidate"]["context"]
    assert first["translation"] is None
    assert wide_bounds("abc",1,2)==(0,3)


def test_enrichment_translation_placeholder_hash_and_rights(tmp_path):
    source=fixture(tmp_path,"it"); result=enrich(source,tmp_path)
    assert result["translation"]["status"] == "required"
    assert len(result["translation"]["source_language_text_sha256"]) == 64
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
