"""Tests for deterministic, immutable corpus reporting."""

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.reporting.build_corpus_report import (
    anchors, bounded_context, cache_identity, collect_occurrences, enrich_one, existing_cache,
    render_markdown, report_document, validate_enrichment,
)
from scripts.reporting.validate_corpus_report import validate_report


def record(language="en", occurrence_id="work-id-123", key="abc123def456"):
    return {
        "report_occurrence_key": key, "occurrence_id": occurrence_id,
        "batch_id": "batch", "batch_run": "run", "batch_index": 0,
        "work_index": 0, "occurrence_index": 1, "work_id": "work",
        "source_id": "source", "title": "A & B", "author": "Author",
        "language": language,
        "source_location": {"relative_position": 0.5, "source_start": 10},
        "target": {"text": "I love you", "start": 10, "end": 20},
        "original_passage": "Before <tag> & **text** I love you after.",
        "annotation": {
            "scores": {"P": 0, "T": 4, "E": 0, "O": 0}, "confidence": 0.9,
            "ontology_fit": "natural",
            "utterance_status": {"status": "direct", "description": "direct speech"},
            "analysis": "An avowal.", "ambiguity_note": None,
            "contextual_interpretation": "Context.", "evidence": [],
            "background_knowledge": {"used": False},
        },
        "annotation_provenance": {"path": "annotation.json", "annotation_version": "0.3.1",
                                  "model": "model", "prompt_sha256": "p", "schema_sha256": "s"},
        "source_provenance": "source.json",
    }


def enrichment(language="en"):
    return {"translation_en": None if language == "en" else "Before **I love you**.",
            "larger_context_summary": "Useful context.",
            "interpretive_commentary": "Useful commentary."}


class CorpusReportTests(unittest.TestCase):
    def test_translation_language_contract(self):
        self.assertEqual([], validate_enrichment(enrichment("en"), "en"))
        self.assertEqual([], validate_enrichment(enrichment("fr"), "fr"))
        for language in ("fr", "de", "no", "sv"):
            self.assertTrue(validate_enrichment(enrichment("en"), language))
        self.assertTrue(validate_enrichment(enrichment("fr"), "en"))

    def test_cache_identity_invalidates_all_material_inputs(self):
        original = record()
        base = cache_identity(original, "model-a", "prompt-a", "schema-a")
        variants = []
        variants.append(cache_identity(original, "model-b", "prompt-a", "schema-a"))
        variants.append(cache_identity(original, "model-a", "prompt-b", "schema-a"))
        passage = copy.deepcopy(original); passage["original_passage"] += " changed"
        variants.append(cache_identity(passage, "model-a", "prompt-a", "schema-a"))
        annotation = copy.deepcopy(original); annotation["annotation"]["scores"]["P"] = 2
        variants.append(cache_identity(annotation, "model-a", "prompt-a", "schema-a"))
        self.assertTrue(all(item != base for item in variants))

    def test_cache_hit_requires_no_call(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            item = record(); identity = cache_identity(item, "model", "p", "s")
            directory = root / item["report_occurrence_key"] / __import__(
                "scripts.reporting.build_corpus_report", fromlist=["canonical_hash"]
            ).canonical_hash(identity)
            directory.mkdir(parents=True)
            (directory / "result.json").write_text(json.dumps(
                {"identity": identity, "enrichment": enrichment()}), encoding="utf-8")
            cached, _ = existing_cache(root, identity, "en")
            self.assertEqual(enrichment(), cached)

    def test_failed_enrichment_is_preserved_and_retry_succeeds(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            item, identity = record(), {"identity": "x"}
            failed, _ = enrich_one(record=item, identity=identity, directory=directory,
                                   payload={"model": "m"}, api_key="x", endpoint="x",
                                   pricing={"usd_per_million_tokens": {
                                       "input": 1, "cached_input": 1, "output": 1}},
                                   caller=lambda *_: (_ for _ in ()).throw(RuntimeError("boom")))
            self.assertIsNone(failed)
            self.assertTrue((directory / "attempt-001/error.txt").is_file())
            response = {"output": [{"content": [{"type": "output_text",
                         "text": json.dumps(enrichment())}]}], "usage": {}}
            valid, _ = enrich_one(record=item, identity=identity, directory=directory,
                                  payload={"model": "m"}, api_key="x", endpoint="x",
                                  pricing={"usd_per_million_tokens": {
                                      "input": 1, "cached_input": 1, "output": 1}},
                                  caller=lambda *_: response)
            self.assertEqual(enrichment(), valid)
            self.assertTrue((directory / "attempt-002/status.json").is_file())

    def test_bounded_context_keeps_target_and_marks_clipping(self):
        occurrence = {"occurrence_id": "x", "context": "a" * 50 + "TARGET" + "b" * 50,
                      "context_start": 0, "start": 50, "match": "TARGET"}
        clipped = bounded_context(occurrence, 30)
        self.assertIn("TARGET", clipped)
        self.assertTrue(clipped.startswith("…") and clipped.endswith("…"))

    def test_deterministic_unique_anchors_with_duplicate_occurrence_ids(self):
        first, second = record(key="aaa111"), record(key="bbb222")
        self.assertEqual(anchors([first, second]), anchors([first, second]))
        self.assertEqual(2, len(set(anchors([first, second]))))

    def test_deterministic_render_handles_markdown_sensitive_source(self):
        item = record(); item["enrichment"] = enrichment()
        report = report_document(name="test", records=[item],
                                 batches=[{"batch_id": "batch", "path": "run", "works": 1,
                                           "occurrences": 1}], model="m", prompt_hash="p",
                                 schema_hash="s", reused=1, generated=0, failures=0,
                                 invocation_cost=0, total_cost=0, complete=True)
        first = render_markdown(report)
        self.assertEqual(first, render_markdown(json.loads(json.dumps(report))))
        self.assertIn("Before <tag> & **text**", first)

    def test_validator_detects_annotation_mutation_and_missing_occurrence(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "annotation.json").write_text("{}", encoding="utf-8")
            (root / "source.json").write_text("{}", encoding="utf-8")
            original = record(); original["annotation_provenance"]["path"] = "annotation.json"
            original["source_provenance"] = "source.json"
            shown = copy.deepcopy(original); shown["anchor"] = "one"; shown["enrichment"] = enrichment()
            report = {"complete": True, "batches": [{"occurrences": 1}],
                      "summary": {"occurrences": 1}, "occurrences": [shown]}
            self.assertEqual([], validate_report(report, [original], root))
            shown["annotation"]["scores"]["T"] = 3
            self.assertTrue(any("immutable" in error for error in validate_report(report, [original], root)))
            report["occurrences"] = []
            self.assertTrue(validate_report(report, [original], root))

    def test_source_order_is_retained_by_document_builder(self):
        first, second = record(key="1"), record(occurrence_id="other", key="2")
        first["enrichment"] = second["enrichment"] = enrichment()
        report = report_document(name="x", records=[second, first], batches=[], model="m",
                                 prompt_hash="p", schema_hash="s", reused=2, generated=0,
                                 failures=0, invocation_cost=0, total_cost=0, complete=True)
        self.assertEqual(["other", "work-id-123"],
                         [item["occurrence_id"] for item in report["occurrences"]])

    def test_incomplete_batch_is_rejected_before_collection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run = root / "run"; run.mkdir()
            (run / "summary.json").write_text(json.dumps({
                "status": "partial", "dry_run": False, "texts_completed": 0,
                "texts_requested": 1, "failures": 1, "valid_annotations": 0,
                "occurrences": 1,
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not a completed real run"):
                collect_occurrences([run], root)


if __name__ == "__main__":
    unittest.main()
