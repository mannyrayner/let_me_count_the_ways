import csv
import json
from pathlib import Path

from scripts.pipeline.run_batch import markdown_summary
from scripts.reporting.validate_classical_six_batch import (
    EXCLUDED_ID, EXPECTED_STATISTICS, EXPECTED_SUMMARY, EXPECTED_TEXT_COUNTS,
    EXPECTED_UNUSUAL_CRITERIA,
    expected_reasons, validate,
)


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def fixture(tmp_path):
    batch = tmp_path / "batch"
    recon = tmp_path / "recon"
    recon.mkdir()
    notable = ["lawrence-women-in-love-5ab672887915", "hamsun-victoria-be00bbdbf853"]
    ids = notable + [f"occurrence-{number:02d}" for number in range(35)]
    source_ids = []
    for source_id, count in EXPECTED_TEXT_COUNTS.items():
        source_ids.extend([source_id] * count)
    reviewed = []
    with (recon / "occurrence_inventory.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(["source_id", "occurrence_id", "pattern_id", "start", "end"])
        for number, (oid, source_id) in enumerate(zip(ids, source_ids)):
            writer.writerow([source_id, oid, "pattern", number, number + 1])
            reviewed.append({"occurrence_id": oid, "source_id": source_id, "decision": "KEEP"})
        writer.writerow(["gutenberg-2419", EXCLUDED_ID, "pattern", 100, 101])
    reviewed.append({"occurrence_id": EXCLUDED_ID, "source_id": "gutenberg-2419",
                     "decision": "EXCLUDE"})
    write_json(recon / "reviewed_occurrences.json", {"occurrences": reviewed})

    unusual_cases = []
    for index, (oid, source_id) in enumerate(zip(ids, source_ids)):
        scores = {"P": 0, "T": 4, "E": 0, "O": 0}
        if oid == notable[0]:
            scores.update(T=0, O=4)
        elif oid == notable[1]:
            scores["E"] = 3
        elif 2 <= index < 7:
            scores["P"] = 2
        elif 7 <= index < 12:
            scores["P"] = 1
        output = {
            "core_love_content": {"label_support": {
                "performative": scores["P"], "truth_conditional": scores["T"],
                "exclamatory_reflexive": scores["E"], "other": scores["O"],
            }, "confidence": 0.9},
            "ontology_assessment": {"fit": "natural"},
        }
        attempt = batch / "texts" / source_id / "annotations" / oid / "attempt-001"
        write_json(attempt / "output.json", output)
        write_json(attempt / "status.json", {"state": "valid"})
        for name in ("cost.json", "metadata.json", "parsing.json", "request.json",
                     "response.json", "validation.json"):
            write_json(attempt / name, {})
        (attempt / "output.txt").write_text("stored response", encoding="utf-8")
        write_json(batch / "texts" / source_id / "inputs" / f"{oid}.json", {})
        reasons = expected_reasons(scores, "natural", 0.9)
        if reasons:
            unusual_cases.append({"source_id": source_id, "occurrence_id": oid,
                "scores": scores, "ontology_fit": "natural", "confidence": 0.9,
                "reasons": sorted(reasons), "result": str(attempt / "output.json")})

    texts = [{"source_id": source_id, "title": source_id, "status": "complete",
              "extracted_occurrences": count, "valid_occurrences": count, "failures": 0,
              "attempted_this_invocation": count, "historical_failed_attempts": 0,
              "estimated_total_cost_usd": 0.0, "cost_per_valid_annotation_usd": 0.0,
              "result_location": f"texts/{source_id}"}
             for source_id, count in EXPECTED_TEXT_COUNTS.items()]
    summary = dict(EXPECTED_SUMMARY)
    summary.update(estimated_total_cost_usd=1.4321, texts_resumed_or_skipped=0,
                   occurrences_attempted_this_invocation=37,
                   ontology_statistics=EXPECTED_STATISTICS, texts=texts)
    write_json(batch / "summary.json", summary)
    (batch / "report.md").write_text(markdown_summary(summary), encoding="utf-8")
    write_json(batch / "unusual_cases.json",
               {"criteria": EXPECTED_UNUSUAL_CRITERIA, "cases": unusual_cases})
    return batch, recon


def test_completed_batch_is_valid(tmp_path):
    batch, recon = fixture(tmp_path)
    assert validate(batch, recon) == []


def test_reports_labelled_summary_and_exclusion_errors(tmp_path):
    batch, recon = fixture(tmp_path)
    summary = json.loads((batch / "summary.json").read_text())
    summary["valid_annotations"] = 36
    write_json(batch / "summary.json", summary)
    excluded = batch / "texts/gutenberg-2419/annotations" / EXCLUDED_ID
    excluded.mkdir(parents=True)
    errors = validate(batch, recon)
    assert any("summary.valid_annotations: expected 37, found 36" in error for error in errors)
    assert any("excluded occurrence has annotation artifacts" in error for error in errors)


def test_unusual_case_must_match_valid_output(tmp_path):
    batch, recon = fixture(tmp_path)
    unusual = json.loads((batch / "unusual_cases.json").read_text())
    unusual["cases"][0]["scores"]["O"] = 3
    write_json(batch / "unusual_cases.json", unusual)
    assert any(".scores" in error for error in validate(batch, recon))
