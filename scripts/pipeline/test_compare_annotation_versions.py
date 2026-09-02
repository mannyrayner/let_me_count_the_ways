import unittest

from scripts.pipeline.compare_annotation_versions import old_context_summary, scores


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
        summary = old_context_summary(output)
        self.assertIn("Calculated reassurance", summary)
        self.assertIn("deception_misrepresentation", summary)


if __name__ == "__main__":
    unittest.main()
