import json

import pytest

from scripts.review.classical_six_review import filter_runs, validate


def fixtures(tmp_path):
    inventory = tmp_path / "inventory.tsv"
    inventory.write_text(
        "source_id\toccurrence_id\tpattern_id\tstart\tend\tmatch_json\n"
        "s\to1\tp\t1\t2\t\"x\"\n", encoding="utf-8")
    item = {"occurrence_id": "o1", "source_id": "s", "pattern_id": "p", "start": 1,
            "end": 2, "decision": "KEEP", "structural_note": "direct",
            "scene_cluster": "S1", "reviewer": "AI", "review_version": "ai_v2"}
    review = tmp_path / "review.json"
    review.write_text(json.dumps({"schema_version": "1.0", "occurrences": [item]}))
    return inventory, review


def test_validate_accepts_complete_review_and_explicit_null_cluster(tmp_path):
    inventory, review = fixtures(tmp_path)
    value = json.loads(review.read_text())
    value["occurrences"][0]["scene_cluster"] = None
    review.write_text(json.dumps(value))
    rows, _, effective = validate(inventory, review)
    assert len(rows) == 1
    assert effective[0]["decision"] == "KEEP"


@pytest.mark.parametrize("mutation", [
    lambda value: value["occurrences"][0].update(decision="PENDING"),
    lambda value: value["occurrences"].append(dict(value["occurrences"][0])),
    lambda value: value["occurrences"][0].update(occurrence_id="unknown"),
    lambda value: value["occurrences"][0].update(start=99),
])
def test_invalid_review_is_rejected(tmp_path, mutation):
    inventory, review = fixtures(tmp_path)
    value = json.loads(review.read_text())
    mutation(value)
    review.write_text(json.dumps(value))
    with pytest.raises(ValueError):
        validate(inventory, review)


def test_optional_human_override_changes_effective_decision(tmp_path):
    inventory, review = fixtures(tmp_path)
    overrides = tmp_path / "overrides.json"
    overrides.write_text(json.dumps({"schema_version": "1.0", "overrides": [{
        "occurrence_id": "o1", "ai_decision": "KEEP", "override_decision": "EXCLUDE",
        "reason": "human correction", "reviewer": "Manny", "date": "2026-09-10",
    }]}))
    _, original, effective = validate(inventory, review, overrides)
    assert original["occurrences"][0]["decision"] == "KEEP"
    assert effective[0]["decision"] == "EXCLUDE"


def test_duplicate_override_is_rejected(tmp_path):
    inventory, review = fixtures(tmp_path)
    item = {"occurrence_id": "o1", "ai_decision": "KEEP", "override_decision": "EXCLUDE",
            "reason": "correction", "reviewer": "Manny", "date": "2026-09-10"}
    overrides = tmp_path / "overrides.json"
    overrides.write_text(json.dumps({"schema_version": "1.0", "overrides": [item, item]}))
    with pytest.raises(ValueError, match="duplicate override"):
        validate(inventory, review, overrides)


def test_filter_materializes_only_keep_and_checks_inventory_fields(tmp_path, capsys):
    inventory, review = fixtures(tmp_path)
    with inventory.open("a") as stream:
        stream.write("s\texcluded\tp\t3\t4\t\"y\"\n")
    value = json.loads(review.read_text())
    value["occurrences"].append({"occurrence_id": "excluded", "source_id": "s",
        "pattern_id": "p", "start": 3, "end": 4, "decision": "EXCLUDE",
        "structural_note": "lexical false positive", "scene_cluster": None,
        "reviewer": "AI", "review_version": "ai_v2"})
    review.write_text(json.dumps(value))
    run = tmp_path / "original"
    extraction = run / "extraction"
    extraction.mkdir(parents=True)
    records = [
        {"occurrence_id": "o1", "source_id": "s", "pattern_id": "p", "start": 1, "end": 2},
        {"occurrence_id": "excluded", "source_id": "s", "pattern_id": "p", "start": 3, "end": 4},
    ]
    (extraction / "passages.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in records))
    (extraction / "metadata.json").write_text(json.dumps({"fingerprint": {"x": 1}}))
    selected = tmp_path / "selected.json"
    selected.write_text(json.dumps([{"source_id": "s", "run_directory": str(run)}]))
    output = tmp_path / "filtered"
    filter_runs(inventory, review, selected, output)
    destination = output / "s" / "reviewed" / "extraction"
    assert [json.loads(line)["occurrence_id"] for line in
            (destination / "passages.jsonl").read_text().splitlines()] == ["o1"]
    assert "filtered 1 EXCLUDE occurrence(s): excluded" in capsys.readouterr().out

    records[0]["start"] = 999
    (extraction / "passages.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in records))
    with pytest.raises(ValueError, match="selected start does not match inventory"):
        filter_runs(inventory, review, selected, output)
