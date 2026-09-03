import json
import tempfile
import unittest
from pathlib import Path

from scripts.pipeline.compare_annotation_versions import (
    context_summary, latest_reference_run, scores,
)


class AnnotationComparisonTests(unittest.TestCase):
    def test_reads_scores_from_each_contract(self):
        labels = {"truth_conditional": 4, "performative": 1, "exclamatory_reflexive": 0}
        self.assertEqual(scores({"core_love_content": {"label_support": labels}}, "0.2"), labels)
        new_labels = dict(labels, other=0)
        self.assertEqual(
            scores({"core_classification": {"label_support": new_labels}}, "0.3"), new_labels)

    def test_context_summary_preserves_supported_assessment_signal(self):
        output = {
            "core_love_content": {"analysis": "An avowal."},
            "realisation": {"analysis": "Direct speech."},
            "current_discourse_act": {"analysis": "Calculated reassurance."},
            "contextual_modification": {"analysis": "The context casts doubt."},
            "assessments": {
                "deception_misrepresentation": {"status": "supported"},
                "manipulation_pressure": {"status": "unsupported"},
            },
        }
        summary = context_summary(output, "0.2")
        self.assertIn("Calculated reassurance", summary)
        self.assertIn("deception_misrepresentation", summary)

    def test_new_context_summary_uses_open_interpretation(self):
        output = {"contextual_interpretation": "Passion accompanies a T avowal."}
        self.assertEqual(context_summary(output, "0.3"), output["contextual_interpretation"])

    def test_finds_stable_batch_text_as_reference_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "manifest.json").write_text(json.dumps({
                "annotation_version": "0.3", "status": "complete",
            }), encoding="utf-8")
            self.assertEqual(latest_reference_run(root, "source", "0.3"), source)


if __name__ == "__main__":
    unittest.main()
