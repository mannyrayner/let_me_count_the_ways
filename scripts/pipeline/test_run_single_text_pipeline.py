import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.pipeline.run_single_text_pipeline import (
    chapter_at,
    chapter_locations,
    enrich_occurrence,
    resolve_annotation_contract,
    resolve_source,
    run_pipeline,
)
from scripts.pipeline.audit_pipeline_run import audit_run


FIXED_TIME = datetime(2026, 9, 1, 12, 0, tzinfo=timezone.utc)


def valid_v0_1_result(occurrence_id):
    return {
        "occurrence_id": occurrence_id,
        "label_support": {
            "truth_conditional": 4,
            "performative": 1,
            "exclamatory_reflexive": 0,
        },
        "construals": [{"perspective": "speaker", "analysis": "An avowal."}],
        "features": ["none_of_these"],
        "evidence": [{"text": "I love you", "supports": "Direct evidence."}],
        "needs_more_context": False,
        "context_request": None,
        "typology_adequate": True,
        "typology_diagnosis": "The truth-conditional label is natural.",
        "proposed_missing_dimensions": [],
        "confidence": 0.95,
    }


def api_response(result):
    return {
        "output": [{"content": [{"type": "output_text", "text": json.dumps(result)}]}],
        "usage": {
            "input_tokens": 100,
            "input_tokens_details": {"cached_tokens": 10},
            "output_tokens": 50,
        },
    }


def supplied_input(request):
    text = request["input"].split("## Input\n\n", 1)[1].split("\n\n## JSON Schema", 1)[0]
    return json.loads(text)


class RecordingAnnotator:
    def __init__(self, response_factory):
        self.response_factory = response_factory
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        return self.response_factory(request)


class SingleTextPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.repo = Path(self.temporary.name)
        project = Path(__file__).resolve().parents[2]
        for relative in [
            "prompts/annotation/classify_passage_v0_1.md",
            "prompts/annotation/classification_schema_v0_1.json",
            "prompts/annotation/classify_passage_v0_2.md",
            "prompts/annotation/classification_schema_v0_2.json",
            "prompts/annotation/classify_passage_v0_3.md",
            "prompts/annotation/classification_schema_v0_3.json",
            "prompts/annotation/classify_passage_v0_3_1.md",
        ]:
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((project / relative).read_bytes())
        for relative in [
            "scripts/extraction/extract_passages.py",
            "scripts/annotation/validate_classification.py",
        ]:
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("fixture version\n", encoding="utf-8")

        self.source_text = "Preface\n\nCHAPTER I\n\nBefore I love you after.\n"
        self.source = self.repo / "data/raw/work/source.txt"
        self.source.parent.mkdir(parents=True)
        self.source.write_text(self.source_text, encoding="utf-8")
        source_hash = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.provenance = self.repo / "provenance/sources/source.json"
        self.provenance.parent.mkdir(parents=True)
        self.provenance.write_text(json.dumps({
            "source_id": "source",
            "work_id": "work",
            "author": "Author",
            "title": "Title",
            "language": "en",
            "repository": "Fixture repository",
            "repository_ebook_id": "1",
            "source_url": "https://example.invalid/1",
            "retrieved_at": "2026-01-01T00:00:00Z",
            "sha256": source_hash,
            "local_path": "data/raw/work/source.txt",
            "rights_note": "Test fixture.",
            "review_status": "approved_for_development_processing",
        }), encoding="utf-8")
        self.patterns = self.repo / "patterns.json"
        self.patterns.write_text(json.dumps({
            "schema_version": "test-patterns",
            "languages": {"en": {"patterns": [
                {"id": "en_i_love_you", "regex": r"\bI\s+love\s+you\b"}
            ]}},
        }), encoding="utf-8")
        catalog = self.repo / "config/api_models.json"
        catalog.parent.mkdir(parents=True)
        catalog.write_text(json.dumps({
            "stale_after_days": 9999,
            "pricing_source": "https://example.invalid/pricing",
            "models": {"test": {
                "api_model": "test-model",
                "pricing_verified_on": "2026-09-01",
                "usd_per_million_tokens": {"input": 1, "cached_input": 0.1, "output": 2},
            }},
        }), encoding="utf-8")

    def tearDown(self):
        self.temporary.cleanup()

    def test_resolve_source_explains_how_to_handle_a_draft(self):
        record = json.loads(self.provenance.read_text(encoding="utf-8"))
        record["review_status"] = "draft"
        self.provenance.write_text(json.dumps(record), encoding="utf-8")

        with self.assertRaisesRegex(
            ValueError,
            r"source is not approved: 'draft'.*complete the source and rights review.*"
            r"approved_for_development_processing.*do not approve it merely to bypass",
        ):
            resolve_source(self.provenance, self.repo)

    def execute_pipeline(self, **overrides):
        arguments = {
            "repo_root": self.repo,
            "provenance_path": self.provenance,
            "patterns_path": self.patterns,
            "annotation_version": "0.2",
            "model_alias": "test",
            "output_root": Path("results/pipeline_runs"),
            "now": lambda: FIXED_TIME,
        }
        arguments.update(overrides)
        return run_pipeline(**arguments)

    def occurrence_id(self, run_dir):
        return json.loads((run_dir / "extraction/passages.jsonl").read_text())["occurrence_id"]

    def test_dry_run_extracts_enriches_and_summarizes_without_api(self):
        trace = []
        run_dir = self.execute_pipeline(dry_run=True, trace=trace.append)
        records = (run_dir / "extraction/passages.jsonl").read_text().splitlines()
        self.assertEqual(len(records), 1)
        occurrence_id = json.loads(records[0])["occurrence_id"]
        prepared = json.loads((run_dir / "inputs" / f"{occurrence_id}.json").read_text())
        self.assertEqual(prepared["annotation_version"], "0.2")
        self.assertEqual(prepared["metadata"]["title"], "Title")
        self.assertEqual(prepared["metadata"]["location"]["chapter_or_section"], "CHAPTER I")
        expected_position = round(prepared["occurrence"]["start"] / len(self.source_text), 6)
        self.assertEqual(prepared["metadata"]["location"]["relative_position"], expected_position)
        self.assertEqual(prepared["metadata"]["supplied_context"]["characters"],
                         len(prepared["occurrence"]["context"]))
        summary = json.loads((run_dir / "summary.json").read_text())
        self.assertEqual(summary["model_calls_needed"], 1)
        self.assertEqual(summary["status"], "prepared")
        self.assertFalse((run_dir / "annotations").exists())
        report = (run_dir / "report.md").read_text()
        self.assertIn("Single-text pipeline report: Title", report)
        self.assertIn("Before I love you after.", report)
        self.assertIn("No annotation attempt has been recorded.", report)
        self.assertTrue(any("Extracted 1 occurrence" in message for message in trace))
        self.assertTrue(any("Dry run" in message for message in trace))

    def test_annotation_version_selection_is_explicit(self):
        contract = resolve_annotation_contract("0.1", self.repo)
        self.assertEqual(contract.version, "0.1")
        self.assertIn("v0_1", str(contract.prompt_path))
        compact = resolve_annotation_contract("0.3", self.repo)
        self.assertEqual(compact.version, "0.3")
        self.assertEqual(compact.schema_path.name, "classification_schema_v0_3.json")
        calibrated = resolve_annotation_contract("0.3.1", self.repo)
        self.assertEqual(calibrated.prompt_path.name, "classify_passage_v0_3_1.md")
        self.assertEqual(calibrated.schema_path, compact.schema_path)
        with self.assertRaisesRegex(ValueError, "unsupported annotation version"):
            resolve_annotation_contract("9.9", self.repo)

    def test_french_chapter_location_is_recovered(self):
        text = "Préface\n\nCHAPITRE PREMIER\n\nJe t’aime.\n"
        locations = chapter_locations(text)
        self.assertEqual(chapter_at(locations, text.index("Je t’aime")), "CHAPITRE PREMIER")

    def test_enrichment_contains_no_interpretive_metadata(self):
        record = {
            "start": 30, "end": 40, "context_start": 20, "context_end": 45,
            "context": "context", "match": "I love you",
        }
        provenance = json.loads(self.provenance.read_text())
        prepared = enrich_occurrence(record, provenance, self.source_text)
        serialized = json.dumps(prepared["metadata"])
        for prohibited in ["speaker", "addressee", "romantic", "deceptive", "revoicing"]:
            self.assertNotIn(prohibited, serialized)

    def test_enrichment_preserves_multi_volume_source_provenance(self):
        record = {"start": 1, "end": 2, "context_start": 0, "context_end": 3}
        provenance = json.loads(self.provenance.read_text())
        provenance.update({
            "repository_ebook_ids": ["2407", "2408"],
            "source_urls": ["https://example.test/2407", "https://example.test/2408"],
        })
        edition = enrich_occurrence(record, provenance, self.source_text)["metadata"][
            "edition_source"]
        self.assertEqual(edition["repository_ebook_ids"], ["2407", "2408"])
        self.assertEqual(len(edition["source_urls"]), 2)

    def test_valid_annotation_is_preserved_and_manifested(self):
        trace = []
        annotator = RecordingAnnotator(
            lambda request: api_response(valid_v0_1_result(
                supplied_input(request)["occurrence"]["occurrence_id"]
            ))
        )
        run_dir = self.execute_pipeline(
            annotation_version="0.1", annotator=annotator, trace=trace.append,
        )
        occurrence_id = self.occurrence_id(run_dir)
        attempt = run_dir / "annotations" / occurrence_id / "attempt-001"
        self.assertEqual(json.loads((attempt / "status.json").read_text())["state"], "valid")
        self.assertTrue(json.loads((attempt / "validation.json").read_text())["valid"])
        manifest = json.loads((run_dir / "manifest.json").read_text())
        self.assertEqual(manifest["valid_occurrences"], 1)
        self.assertEqual(manifest["status"], "complete")
        self.assertEqual(manifest["usage_and_cost"]["input_tokens"], 100)
        self.assertGreater(manifest["usage_and_cost"]["estimated_total_cost_usd"], 0)
        report = (run_dir / "report.md").read_text()
        self.assertIn("**T/P/E support:** 4 / 1 / 0", report)
        self.assertIn("Complete structured annotation", report)
        self.assertTrue(any("starting annotation attempt 1" in message for message in trace))
        self.assertTrue(any("annotation valid" in message for message in trace))
        audit = audit_run(run_dir, self.repo, expected_occurrences=1)
        self.assertEqual(audit["status"], "complete")
        self.assertEqual(audit["occurrences"], 1)

    def test_audit_rejects_prepared_dry_run(self):
        run_dir = self.execute_pipeline(dry_run=True)
        with self.assertRaisesRegex(ValueError, "not 'complete'"):
            audit_run(run_dir, self.repo, expected_occurrences=1)

    def test_resume_skips_valid_result_and_force_creates_new_attempt(self):
        def response(request):
            supplied = supplied_input(request)
            return api_response(valid_v0_1_result(supplied["occurrence"]["occurrence_id"]))

        annotator = RecordingAnnotator(response)
        run_dir = self.execute_pipeline(annotation_version="0.1", annotator=annotator)
        (run_dir / "report.md").unlink()
        self.execute_pipeline(annotation_version="0.1", annotator=annotator, run_dir=run_dir)
        self.assertEqual(len(annotator.requests), 1)
        self.assertTrue((run_dir / "report.md").exists())
        manifest = json.loads((run_dir / "manifest.json").read_text())
        self.assertTrue(manifest["extraction_reused"])
        self.assertEqual(manifest["skipped_valid_this_invocation"], 1)
        self.execute_pipeline(annotation_version="0.1", annotator=annotator, run_dir=run_dir, force=True)
        self.assertEqual(len(annotator.requests), 2)
        occurrence_id = self.occurrence_id(run_dir)
        self.assertTrue((run_dir / "annotations" / occurrence_id / "attempt-002").exists())

    def test_successful_retry_clears_unresolved_but_preserves_failure_history(self):
        calls = 0

        def response(request):
            nonlocal calls
            calls += 1
            if calls == 1:
                return {"output": [{"content": [{"type": "output_text", "text": "not json"}]}]}
            supplied = supplied_input(request)
            return api_response(valid_v0_1_result(supplied["occurrence"]["occurrence_id"]))

        annotator = RecordingAnnotator(response)
        run_dir = self.execute_pipeline(annotation_version="0.1", annotator=annotator)
        first = json.loads((run_dir / "summary.json").read_text())
        self.assertEqual(first["failed_attempts"], 1)
        self.execute_pipeline(
            annotation_version="0.1", annotator=annotator, run_dir=run_dir)
        summary = json.loads((run_dir / "summary.json").read_text())
        self.assertEqual(summary["failed_attempts"], 0)
        self.assertEqual(summary["historical_failed_attempts"], 1)
        report = (run_dir / "report.md").read_text()
        self.assertIn("Unresolved failed occurrences:** 0", report)
        self.assertIn("Historical failed/invalid attempts:** 1", report)

    def test_v0_3_request_uses_structured_outputs(self):
        def response(request):
            occurrence_id = supplied_input(request)["occurrence"]["occurrence_id"]
            result = {
                "occurrence_id": occurrence_id,
                "core_classification": {
                    "label_support": {"truth_conditional": 4, "performative": 0,
                                      "exclamatory_reflexive": 0, "other": 0},
                    "confidence": 0.9, "analysis": "An avowal.", "ambiguity": None,
                },
                "other_diagnosis": {"tpe_failure": None, "core_not_context": None},
                "utterance_status": {"status": "direct", "description": "Direct speech."},
                "contextual_interpretation": "The passage presents an avowal.",
                "evidence": [{"evidence_id": "e1", "source": "local_text",
                              "quotation_or_description": "I love you", "supports": "Avowal.",
                              "confidence": 1.0}],
                "background_knowledge": {"used": False, "familiarity": "none",
                                         "confidence": None, "contribution": None},
                "ontology_assessment": {"fit": "natural", "diagnosis": "T fits.",
                                        "candidate_recurrent_dimension": None},
                "notes": None,
            }
            return api_response(result)

        annotator = RecordingAnnotator(response)
        self.execute_pipeline(annotation_version="0.3", annotator=annotator)
        response_format = annotator.requests[0]["text"]["format"]
        self.assertEqual(response_format["type"], "json_schema")
        self.assertTrue(response_format["strict"])
        self.assertNotIn("allOf", response_format["schema"])

    def test_invalid_annotation_is_excluded_and_preserved_as_failure(self):
        def invalid(request):
            supplied = supplied_input(request)
            result = valid_v0_1_result(supplied["occurrence"]["occurrence_id"])
            result["label_support"]["performative"] = 9
            return api_response(result)

        run_dir = self.execute_pipeline(annotation_version="0.1", annotator=RecordingAnnotator(invalid))
        occurrence_id = self.occurrence_id(run_dir)
        attempt = run_dir / "annotations" / occurrence_id / "attempt-001"
        self.assertEqual(json.loads((attempt / "status.json").read_text())["state"], "invalid")
        self.assertTrue((attempt / "output.json").exists())
        self.assertTrue((attempt / "failure.json").exists())
        self.assertEqual(json.loads((run_dir / "manifest.json").read_text())["valid_occurrences"], 0)

    def test_api_failure_is_preserved_without_aborting_manifest(self):
        def fail(_request):
            raise RuntimeError("mock transport failure")

        run_dir = self.execute_pipeline(annotation_version="0.1", annotator=RecordingAnnotator(fail))
        occurrence_id = self.occurrence_id(run_dir)
        attempt = run_dir / "annotations" / occurrence_id / "attempt-001"
        failure = json.loads((attempt / "failure.json").read_text())
        self.assertEqual(failure["state"], "api_failure")
        self.assertIn("mock transport failure", failure["error_message"])
        self.assertEqual(json.loads((run_dir / "summary.json").read_text())["failed_attempts"], 1)


if __name__ == "__main__":
    unittest.main()
