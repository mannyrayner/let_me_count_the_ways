import copy
import tempfile
import unittest
from pathlib import Path

from scripts.reporting.compare_corpus_reports import (
    build_comparison, render_markdown, summarize, work_summaries,
)
from scripts.reporting.audit_indie_comparison import audit, review_inventory


def occurrence(work_id="work", title="Work", scores=None, status="direct",
               fit="natural", confidence=0.9):
    return {
        "occurrence_id": f"{work_id}-occurrence", "work_id": work_id, "title": title,
        "annotation": {"scores": scores or {"P": 0, "T": 4, "E": 0, "O": 0},
                       "confidence": confidence, "ontology_fit": fit,
                       "utterance_status": {"status": status}},
    }


class ComparisonTests(unittest.TestCase):
    def test_zero_denominators_and_missing_inventory(self):
        summary = summarize([])
        self.assertIsNone(summary["P_at_least_2"]["proportion"])
        broken = summarize([{"work_id": "x", "annotation": {}}])
        self.assertEqual(1, broken["missing_data"]["scores"])
        self.assertIsNone(broken["P_at_least_2"]["proportion"])

    def test_score_boundaries_and_mixed_definition(self):
        records = [occurrence(scores={"P": 2, "T": 2, "E": 1, "O": 0}),
                   occurrence(scores={"P": 1, "T": 4, "E": 2, "O": 1})]
        summary = summarize(records)
        self.assertEqual(1, summary["P_at_least_2"]["count"])
        self.assertEqual(1, summary["E_at_least_2"]["count"])
        self.assertEqual(2, summary["mixed_PTE"]["count"])
        self.assertEqual(1, summary["score_distributions"]["P"]["2"])

    def test_statuses_surface_unknown_and_do_not_infer_negation(self):
        records = [occurrence(status="reported"), occurrence(status="quoted_or_revoiced"),
                   {"work_id": "x", "annotation": {"scores": {"P": 0, "T": 4,
                                                                  "E": 0, "O": 0},
                                                     "ontology_fit": "natural"}}]
        summary = summarize(records)
        self.assertEqual(1, summary["missing_data"]["utterance_status"])
        self.assertEqual(1, summary["utterance_status"]["categories"]
                         ["embedded_or_reported"]["count"])
        self.assertIsNone(summary["utterance_status"]["categories"]["negated"]["count"])
        self.assertIsNone(summary["utterance_status"]["categories"]
                          ["direct_affirmative"]["count"])

    def test_deterministic_work_order_and_reconciliation(self):
        records = [occurrence("z", "Zulu"), occurrence("a", "Alpha")]
        summary = summarize(records)
        self.assertEqual(2, sum(summary["score_distributions"]["T"].values()))
        self.assertEqual(["Alpha", "Zulu"],
                         [work["title"] for work in work_summaries(records)])

    def test_builder_enforces_eight_vs_nikki_and_renders_deterministically(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); canonical_path = root / "canonical.json"; pilot_path = root / "pilot.json"
            canonical_records = [occurrence(str(i), f"Work {i}") for i in range(8)]
            pilot_records = [occurrence("nikki", "Nikki's Touch")]
            canonical = {"complete": True, "summary": {"occurrences": 8},
                         "occurrences": canonical_records}
            pilot = {"complete": True, "summary": {"occurrences": 1},
                     "occurrences": pilot_records}
            canonical_path.write_text("canonical", encoding="utf-8")
            pilot_path.write_text("pilot", encoding="utf-8")
            comparison = build_comparison(canonical, pilot, canonical_path, pilot_path)
            first = render_markdown(comparison)
            self.assertEqual(first, render_markdown(copy.deepcopy(comparison)))
            self.assertIn("not two scene-level confirmations", first)
            errors = audit(pilot, comparison, canonical_path, pilot_path)
            self.assertIn("pilot report must be complete with 10 occurrences", errors)

    def test_audit_reconciles_expected_live_shape_and_lists_interesting_cases(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); canonical_path = root / "canonical.json"; pilot_path = root / "pilot.json"
            canonical_records = [occurrence(str(i % 8), f"Work {i % 8}") for i in range(41)]
            pilot_records = [occurrence("nikki", "Nikki's Touch") for _ in range(10)]
            pilot_records[0]["annotation"]["scores"] = {"P": 3, "T": 4, "E": 0, "O": 0}
            for index, record in enumerate(canonical_records + pilot_records):
                record["occurrence_id"] = f"occurrence-{index}"
                record["annotation_provenance"] = {"annotation_version": "0.3.1"}
            canonical = {"complete": True, "summary": {"occurrences": 41},
                         "occurrences": canonical_records}
            pilot = {"complete": True, "summary": {"occurrences": 10},
                     "occurrences": pilot_records}
            canonical_path.write_text("canonical", encoding="utf-8")
            pilot_path.write_text("pilot", encoding="utf-8")
            comparison = build_comparison(canonical, pilot, canonical_path, pilot_path)
            self.assertEqual([], audit(pilot, comparison, canonical_path, pilot_path))
            inventory = review_inventory(pilot, comparison)
            self.assertEqual("occurrence-41",
                             inventory["pilot_cases_requiring_review"][0]["occurrence_id"])


if __name__ == "__main__":
    unittest.main()
