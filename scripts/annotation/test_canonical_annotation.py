import hashlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

import scripts.annotation.annotate_canonical_candidates as annotation
from scripts.annotation.annotate_canonical_candidates import (
    attempt_directory,
    compatible,
    fingerprint,
    prepare_annotation_input,
    render_reports,
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


def test_annotation_timeout_defaults_to_300(monkeypatch, tmp_path):
    captured = {}
    monkeypatch.setattr(annotation, "run", lambda args: captured.update(vars(args)))
    monkeypatch.setattr(sys, "argv", ["annotate", "--enriched", str(tmp_path / "in.jsonl"),
                                      "--all", "--output", str(tmp_path / "out")])

    annotation.main()

    assert captured["timeout"] == 300


def _run_args(tmp_path, enriched, output, timeout):
    return SimpleNamespace(
        enriched=enriched, calibration=None, all=True, output=output, model="model",
        model_catalog=tmp_path / "models.json", endpoint="https://example.test", timeout=timeout,
        estimate_only=False,
    )


def _stub_annotation_dependencies(monkeypatch):
    contract = SimpleNamespace(
        prompt="PROMPT", schema=json.dumps({"type": "object"}),
        validator=lambda value, oid: None if value.get("occurrence_id") == oid else (_ for _ in ()).throw(ValueError("wrong id")),
    )
    monkeypatch.setattr(annotation, "resolve_annotation_contract", lambda *_: contract)
    monkeypatch.setattr(annotation, "resolve_model", lambda *_: ("model", {}))
    monkeypatch.setattr(annotation, "calculate_cost", lambda *_: {
        "input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0,
        "estimated_total_cost": 0,
    })
    return contract


def test_custom_timeout_reaches_injected_caller(tmp_path, monkeypatch):
    row = enrich(fixture(tmp_path / "corpus"), tmp_path / "corpus")
    enriched = tmp_path / "enriched.jsonl"
    enriched.write_text(json.dumps(row) + "\n", encoding="utf-8")
    _stub_annotation_dependencies(monkeypatch)
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    received = []

    annotation.run(_run_args(tmp_path, enriched, tmp_path / "output", 600),
                   caller=lambda body, endpoint, key, timeout: received.append(timeout) or {})

    assert received == [600]


def test_changing_timeout_does_not_alter_fingerprint():
    first = fingerprint("oid", "model", "prompt", "schema", "input")
    timeout = 1200
    second = fingerprint("oid", "model", "prompt", "schema", "input")

    assert timeout == 1200
    assert first == second
    assert "timeout" not in first


def test_compatible_annotation_resumes_under_different_timeout(tmp_path, monkeypatch):
    row = enrich(fixture(tmp_path / "corpus"), tmp_path / "corpus")
    enriched = tmp_path / "enriched.jsonl"
    enriched.write_text(json.dumps(row) + "\n", encoding="utf-8")
    contract = _stub_annotation_dependencies(monkeypatch)
    prepared = prepare_annotation_input(row)
    key = fingerprint("oid", "model", annotation.sha(contract.prompt), annotation.sha(contract.schema),
                      annotation.sha(json.dumps(prepared, sort_keys=True, ensure_ascii=False, separators=(",", ":"))))
    directory = attempt_directory(tmp_path / "output", key)
    directory.mkdir(parents=True)
    (directory / "provenance.json").write_text(json.dumps(key), encoding="utf-8")
    (directory / "output.json").write_text(json.dumps({"occurrence_id": "oid"}), encoding="utf-8")
    calls = []

    summary = annotation.run(_run_args(tmp_path, enriched, tmp_path / "output", 600),
                             caller=lambda *args: calls.append(args))

    assert calls == []
    assert summary["resumed"] == 1


def test_report_renderer_reads_unicode_model_output_as_utf8(tmp_path, monkeypatch):
    key = fingerprint("oid", "model", "prompt", "schema", "input")
    directory = attempt_directory(tmp_path, key)
    directory.mkdir(parents=True)
    result = {
        "core_classification": {
            "label_support": {
                "truth_conditional": 4,
                "performative": 0,
                "exclamatory_reflexive": 0,
                "other": 0,
            },
            "confidence": 0.9,
        },
        "utterance_status": {"status": "utterance"},
        "ontology_assessment": {"fit": "natural"},
        "background_knowledge": {"used": False},
        "model_explanation": "Love letter 💝",
    }
    (directory / "output.json").write_text(
        json.dumps(result, ensure_ascii=False), encoding="utf-8"
    )
    source = {
        "occurrence": {"occurrence_id": "oid", "work_id": "work"},
        "work_metadata": {"language": "en"},
    }

    original_read_text = Path.read_text

    def windows_read_text(path, encoding=None, errors=None):
        # Simulate a Windows legacy locale, where the UTF-8 bytes for the
        # non-ASCII model output above cannot be decoded as cp1252.
        return original_read_text(path, encoding=encoding or "cp1252", errors=errors)

    monkeypatch.setattr(Path, "read_text", windows_read_text)

    summary = render_reports(tmp_path, [source], [key], {"status": "complete"})

    assert summary["cases"][0]["occurrence_id"] == "oid"


def test_local_private_canonical_path_keeps_rights_guard(tmp_path):
    corpus=tmp_path/'corpus'
    source=fixture(corpus,'fr',policy='LIMITED_QUOTATION_ONLY')
    work=corpus/'works/work';manifest=json.loads((work/'work.json').read_text())
    local=tmp_path/'data/local_candidate_derived/example.txt';local.parent.mkdir(parents=True)
    (work/'canonical.txt').rename(local)
    manifest.update(canonical_storage='local_private',canonical_text=None,
                    canonical_local_path='data/local_candidate_derived/example.txt')
    (work/'work.json').write_text(json.dumps(manifest))
    with pytest.raises(ValueError,match='rights policy'):
        enrich(source,corpus)
    result=enrich(source,corpus,allow_private_output=True)
    assert result['context']['local']['text']==source['candidate']['context']
    assert result['translation']['status']=='required'
