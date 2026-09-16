import json
from pathlib import Path

import pytest

from scripts.review.scholarly_candidate_review import PROMPT_VERSION, call_model, render, validate


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def candidate(oid: str, work: str, context: str = "I love you") -> dict:
    return {"occurrence_id": oid, "work_id": work, "language": "en", "match": "I love you",
            "context": context, "pattern_id": "en_present", "pattern_version": "0.7"}


def review(oid: str, work: str, decision: str = "KEEP",
           reason: str = "VALID_EXPLICIT_LOVE_I_YOU") -> dict:
    return {"occurrence_id": oid, "work_id": work, "decision": decision,
            "reason_code": reason, "confidence": 0.9, "review_note": "Local syntax is in scope.",
            "review_model": "test-model", "review_prompt_version": PROMPT_VERSION,
            "reviewed_at": "2026-09-15T00:00:00+00:00"}


def test_validate_requires_exact_coverage_and_compatible_reason(tmp_path):
    source, output = tmp_path / "source", tmp_path / "output"
    write_jsonl(source / "works/public/candidates.jsonl", [candidate("one", "public")])
    write_jsonl(output / "works/public/review.jsonl", [review("one", "public")])
    candidates, reviews = validate([source], [output], expected_total=1)
    assert len(candidates) == len(reviews) == 1

    bad = review("one", "public", "EXCLUDE", "VALID_EXPLICIT_LOVE_I_YOU")
    write_jsonl(output / "works/public/review.jsonl", [bad])
    with pytest.raises(ValueError, match="incompatible"):
        validate([source], [output], expected_total=1)


def test_validate_rejects_missing_duplicate_and_unknown_ids(tmp_path):
    source, output = tmp_path / "source", tmp_path / "output"
    write_jsonl(source / "works/public/candidates.jsonl", [candidate("one", "public"), candidate("two", "public")])
    write_jsonl(output / "works/public/review.jsonl", [review("one", "public"), review("one", "public"), review("three", "public")])
    with pytest.raises(ValueError) as exc:
        validate([source], [output])
    message = str(exc.value)
    assert "duplicate review IDs" in message and "unknown review IDs" in message and "missing review IDs" in message


def test_render_omits_private_text_and_orders_attention_cases(tmp_path):
    public_source, private_source = tmp_path / "public-source", tmp_path / "private-source"
    public_review, private_review, rendered = tmp_path / "public-review", tmp_path / "private-review", tmp_path / "rendered"
    write_jsonl(public_source / "works/public/candidates.jsonl", [candidate("keep", "public"), candidate("exclude", "public")])
    write_jsonl(private_source / "works/mcmillan-error-of-understanding/candidates.jsonl",
                [candidate("private", "mcmillan-error-of-understanding", "SECRET QUOTATION")])
    write_jsonl(public_review / "works/public/review.jsonl", [review("keep", "public"),
        review("exclude", "public", "EXCLUDE", "EXCLUDE_NOT_LOVE_SENSE")])
    write_jsonl(private_review / "works/mcmillan-error-of-understanding/review.jsonl",
                [review("private", "mcmillan-error-of-understanding")])
    summary = render([public_source, private_source], [public_review, private_review], rendered)
    sheet = (rendered / "human_inspection.tsv").read_text(encoding="utf-8")
    assert summary["candidate_count"] == 3
    assert "SECRET QUOTATION" not in sheet and "private" not in sheet
    assert sheet.index("exclude") < sheet.index("keep")


def test_call_model_omits_unsupported_temperature(monkeypatch):
    captured = {}

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def read(self):
            output = {"decision": "KEEP", "reason_code": "VALID_EXPLICIT_LOVE_I_YOU",
                      "confidence": 0.9, "review_note": "Explicit target construction."}
            response = {"output": [{"content": [{"type": "output_text", "text": json.dumps(output)}]}],
                        "usage": {"input_tokens": 10, "output_tokens": 5}}
            return json.dumps(response).encode()

    def fake_urlopen(request, timeout):
        captured.update(json.loads(request.data))
        assert timeout == 300
        return Response()

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    answer, usage = call_model(prompt="prompt", schema={"type": "object"},
                               payload_input={"occurrence_id": "one"}, model="gpt-5.6-sol",
                               endpoint="https://example.invalid", api_key="secret")
    assert "temperature" not in captured
    assert answer["decision"] == "KEEP"
    assert usage == {"input_tokens": 10, "output_tokens": 5}
