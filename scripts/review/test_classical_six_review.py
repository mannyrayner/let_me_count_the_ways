import json
from pathlib import Path

import pytest

from scripts.review.classical_six_review import filter_runs, render, validate


def fixtures(tmp_path):
    inventory = tmp_path / "inventory.tsv"
    inventory.write_text("source_id\toccurrence_id\tpattern_id\tstart\tend\tmatch_json\ns\to1\tp\t1\t2\t\"x\"\n")
    item = {"occurrence_id": "o1", "source_id": "s", "pattern_id": "p", "start": 1,
            "end": 2, "decision": "KEEP", "structural_status": "direct",
            "scene_cluster": "S1", "adjudication": "AI v1 accepted by human audit"}
    review = tmp_path / "review.json"
    review.write_text(json.dumps({"schema_version": "1.0", "occurrences": [item]}))
    return inventory, review


def test_validate_and_render(tmp_path):
    inventory, review = fixtures(tmp_path)
    rows, _ = validate(inventory, review)
    assert len(rows) == 1
    output = tmp_path / "review.md"
    render(inventory, review, output)
    assert "final decision: KEEP" in output.read_text()


def test_pending_is_rejected(tmp_path):
    inventory, review = fixtures(tmp_path)
    value = json.loads(review.read_text())
    value["occurrences"][0]["scene_cluster"] = "PENDING"
    review.write_text(json.dumps(value))
    with pytest.raises(ValueError, match="PENDING"):
        validate(inventory, review)


def test_filter_materializes_only_keep_records(tmp_path):
    inventory, review = fixtures(tmp_path)
    with inventory.open("a") as stream:
        stream.write("s\texcluded\tp\t3\t4\t\"y\"\n")
    value = json.loads(review.read_text())
    value["occurrences"].append({"occurrence_id": "excluded", "source_id": "s",
        "pattern_id": "p", "start": 3, "end": 4, "decision": "EXCLUDE",
        "structural_status": "lexical false positive", "scene_cluster": "NA",
        "adjudication": "AI v1 accepted by human audit"})
    review.write_text(json.dumps(value))
    run = tmp_path / "original"
    extraction = run / "extraction"
    extraction.mkdir(parents=True)
    (extraction / "passages.jsonl").write_text(
        json.dumps({"occurrence_id": "o1"}) + "\n" +
        json.dumps({"occurrence_id": "excluded"}) + "\n")
    (extraction / "metadata.json").write_text(json.dumps({"fingerprint": {"x": 1}}))
    selected = tmp_path / "selected.json"
    selected.write_text(json.dumps([{"source_id": "s", "run_directory": str(run)}]))
    output = tmp_path / "filtered"
    filter_runs(inventory, review, selected, output)
    destination = output / "s" / "adjudicated" / "extraction"
    assert [json.loads(line)["occurrence_id"] for line in
            (destination / "passages.jsonl").read_text().splitlines()] == ["o1"]
    metadata = json.loads((destination / "metadata.json").read_text())
    assert metadata["retained_occurrences"] == 1
    assert metadata["adjudicated_from_occurrences"] == 2
