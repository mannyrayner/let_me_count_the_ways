import json
import tempfile
import unittest
from pathlib import Path

from scripts.pipeline.run_batch import (
    find_reusable_extraction, load_batch_manifest, ontology_records, pattern_for_extraction,
)


class BatchRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_manifest_contains_membership_only(self):
        path = self.root / "batch.json"
        self.write_json(path, {
            "schema_version": "0.1", "batch_id": "pilot", "description": "Pilot.",
            "sources": [{"provenance": "provenance/sources/a.json"}],
        })
        manifest = load_batch_manifest(path)
        self.assertEqual(manifest["batch_id"], "pilot")
        self.assertNotIn("annotation_version", manifest)

    def test_manifest_rejects_duplicate_sources(self):
        path = self.root / "batch.json"
        self.write_json(path, {
            "schema_version": "0.1", "batch_id": "pilot", "description": "Pilot.",
            "sources": [
                {"provenance": "provenance/sources/a.json"},
                {"provenance": "provenance/sources/a.json"},
            ],
        })
        with self.assertRaisesRegex(ValueError, "unique"):
            load_batch_manifest(path)

    def test_finds_latest_complete_compatible_extraction(self):
        root = self.root / "runs"
        for run_id, status in (("001", "prepared"), ("002", "complete")):
            run = root / "source" / run_id
            self.write_json(run / "manifest.json", {"status": status})
            self.write_json(run / "extraction/metadata.json", {"fingerprint": {
                "source_sha256": "source-hash", "context_characters": 1000,
                "extractor_sha256": "extractor-hash", "patterns_sha256": "patterns-hash",
            }})
            (run / "extraction/passages.jsonl").write_text("{}\n", encoding="utf-8")
        selected = find_reusable_extraction(
            source_id="source", source_sha256="source-hash", context_chars=1000,
            extractor_sha256="extractor-hash", extraction_root=root,
        )
        self.assertEqual(selected, root / "source/002/extraction")

    def test_matches_reused_extraction_to_its_pattern_version(self):
        extraction = self.root / "extraction"
        old, new = self.root / "patterns-old.json", self.root / "patterns-new.json"
        old.write_text("old", encoding="utf-8")
        new.write_text("new", encoding="utf-8")
        import hashlib
        self.write_json(extraction / "metadata.json", {"fingerprint": {
            "patterns_sha256": hashlib.sha256(b"old").hexdigest(),
        }})
        self.assertEqual(pattern_for_extraction(extraction, [new, old]), old)

    def test_ontology_statistics_and_review_flags(self):
        attempt = self.root / "texts/source/annotations/occurrence/attempt-001"
        self.write_json(attempt / "status.json", {"state": "valid"})
        self.write_json(attempt / "output.json", {
            "core_classification": {"label_support": {
                "truth_conditional": 3, "performative": 2,
                "exclamatory_reflexive": 0, "other": 0,
            }, "confidence": 0.7},
            "ontology_assessment": {"fit": "natural"},
        })
        stats, review = ontology_records(self.root, [{"source_id": "source"}])
        self.assertEqual(stats["score_distributions"]["T"]["3"], 1)
        self.assertEqual(stats["p_at_least_two"], 1)
        self.assertEqual(stats["balanced_core"], 1)
        self.assertEqual(review[0]["reasons"], [
            "P >= 2", "confidence < 0.75", "two or more of P/T/E >= 2",
        ])


if __name__ == "__main__":
    unittest.main()
