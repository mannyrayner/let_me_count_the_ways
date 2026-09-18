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


def run(tmp_path: Path, caller, *, timeout=300):
    reviewed, calibration = write_inputs(tmp_path)
    return generate(reviewed=reviewed, calibration=calibration,
        output=tmp_path / "output", corpus=tmp_path / "corpus", model_alias="5.6",
        model_catalog=Path("config/api_models.json"), endpoint="mock", api_key="test",
        caller=caller, timeout=timeout)


def test_english_skipped_non_english_generated_validated_and_resumed(tmp_path):
    calls = []

    def caller(prompt, schema, payload, model, endpoint, api_key, timeout):
        calls.append(payload)
        assert timeout == 300
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

    summary = run(tmp_path, caller)
    assert summary["status"] == "partial"
    assert summary["failed"] == 1
    failure = json.loads((tmp_path / "output/failures/italian.json").read_text())
    assert failure["retry_appropriate"] is True


def test_all_reviewed_failure_isolated_and_progress_reported(tmp_path, capsys):
    reviewed, _ = write_inputs(tmp_path)
    rows = [json.loads(line) for line in reviewed.read_text().splitlines()]
    rows.append(fixture(tmp_path / "corpus", "no", occurrence_id="norwegian",
                        work_id="norwegian-work"))
    reviewed.write_text("".join(json.dumps(row) + "\n" for row in rows))
    calls = []

    def caller(*args):
        calls.append(args[2]["occurrence_id"])
        if len(calls) == 1:
            raise RuntimeError("temporary")
        return {"text": "Translation"}, {"input_tokens": 4, "output_tokens": 2}

    summary = generate(reviewed=reviewed, calibration=None, all_reviewed=True,
        output=tmp_path / "output", corpus=tmp_path / "corpus", model_alias="5.6",
        model_catalog=Path("config/api_models.json"), endpoint="mock", api_key="test",
        caller=caller)
    assert calls == ["italian", "norwegian"]
    assert summary["failed"] == 1 and summary["api_calls_this_run"] == 1
    assert "API call started" in capsys.readouterr().err


def test_custom_timeout_retries_failure_clears_stale_state_and_then_resumes(tmp_path):
    timeouts = []

    def timeout_caller(*args):
        timeouts.append(args[6])
        raise TimeoutError("temporary")

    first = run(tmp_path, timeout_caller)
    failure_path = tmp_path / "output/failures/italian.json"
    assert first["status"] == "partial" and failure_path.exists()

    def successful_caller(*args):
        timeouts.append(args[6])
        return {"text": "Translation"}, {"input_tokens": 1, "output_tokens": 1}

    second = run(tmp_path, successful_caller, timeout=600)
    assert timeouts == [300, 600]
    assert second["status"] == "complete"
    assert second["translations"] == 1 and second["failed"] == 0
    assert second["unresolved_occurrences"] == []
    assert not failure_path.exists()

    # Timeout is transport configuration, not part of the semantic resumption key.
    third = run(tmp_path, successful_caller, timeout=123)
    assert timeouts == [300, 600]
    assert third["api_calls_this_run"] == 0 and third["resumed"] == 1
