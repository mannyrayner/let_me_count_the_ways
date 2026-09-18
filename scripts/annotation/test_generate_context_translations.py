import hashlib
import json
from pathlib import Path

import pytest

from scripts.annotation.generate_context_translations import generate
from scripts.annotation.test_canonical_annotation import fixture


def write_inputs(tmp_path: Path) -> tuple[Path, Path]:
    rows = [fixture(tmp_path / "corpus", "en", occurrence_id="english", work_id="english-work"),
            fixture(tmp_path / "corpus", "it", occurrence_id="italian", work_id="italian-work")]
    reviewed = tmp_path / "reviewed.jsonl"
    reviewed.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    calibration = tmp_path / "calibration.json"
    calibration.write_text(json.dumps({"cases": [
        {"occurrence_id": "english"}, {"occurrence_id": "italian"}]}), encoding="utf-8")
    return reviewed, calibration


def run(tmp_path: Path, caller):
    reviewed, calibration = write_inputs(tmp_path)
    return generate(reviewed=reviewed, calibration=calibration,
        output=tmp_path / "output", corpus=tmp_path / "corpus", model_alias="5.6",
        model_catalog=Path("config/api_models.json"), endpoint="mock", api_key="test",
        caller=caller)


def test_english_skipped_non_english_generated_validated_and_resumed(tmp_path):
    calls = []

    def caller(prompt, schema, payload, model, endpoint, api_key):
        calls.append(payload)
        return {"text": "Before, I love you, after."}, {
            "input_tokens": 20, "output_tokens": 10,
            "input_tokens_details": {"cached_tokens": 2}}

    first = run(tmp_path, caller)
    assert first["translations"] == 1 and first["api_calls_this_run"] == 1
    assert calls[0]["source_language"] == "it"
    generated = json.loads((tmp_path / "output/generated_enrichment.json").read_text())
    assert set(generated) == {"italian"}
    translation = generated["italian"]["translation"]
    assert translation["status"] == "provided"
    assert translation["source_language"] == "it"
    assert translation["model_usage"]["input_tokens"] == 20
    assert translation["estimated_cost_usd"] > 0
    assert len(translation["prompt_sha256"]) == len(translation["schema_sha256"]) == 64

    second = run(tmp_path, caller)
    assert second["api_calls_this_run"] == 0 and second["resumed"] == 1
    assert len(calls) == 1


def test_changed_source_hash_is_not_reused(tmp_path):
    calls = []

    def caller(*args):
        calls.append(args[2]["text"])
        return {"text": "Translation"}, {"input_tokens": 1, "output_tokens": 1}

    run(tmp_path, caller)
    canonical = tmp_path / "corpus/works/italian-work/canonical.txt"
    canonical.write_text(canonical.read_text(encoding="utf-8") + " Changed.", encoding="utf-8")
    reviewed = tmp_path / "reviewed.jsonl"
    rows = [json.loads(line) for line in reviewed.read_text().splitlines()]
    digest = hashlib.sha256(canonical.read_bytes()).hexdigest()
    rows[1]["candidate"]["canonical_sha256"] = digest
    work = tmp_path / "corpus/works/italian-work/work.json"
    metadata = json.loads(work.read_text()); metadata["canonical_sha256"] = digest
    work.write_text(json.dumps(metadata))
    reviewed.write_text("".join(json.dumps(row) + "\n" for row in rows))

    generate(reviewed=reviewed, calibration=tmp_path / "calibration.json",
        output=tmp_path / "output", corpus=tmp_path / "corpus", model_alias="5.6",
        model_catalog=Path("config/api_models.json"), endpoint="mock", api_key="test",
        caller=caller)
    assert len(calls) == 2


def test_invalid_structured_translation_is_rejected(tmp_path):
    def caller(*args):
        return {"text": "", "explanation": "not allowed"}, {}

    with pytest.raises(ValueError, match="only the text field"):
        run(tmp_path, caller)
