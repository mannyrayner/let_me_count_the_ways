import unittest

from validate_classification import validate


def valid_result():
    return {
        "occurrence_id": "occurrence-1",
        "label_support": {
            "truth_conditional": 4,
            "performative": 1,
            "exclamatory_reflexive": 0,
        },
        "construals": [{"perspective": "speaker", "analysis": "An avowal."}],
        "features": ["mixed_reading"],
        "evidence": [{"text": "I love you", "supports": "Direct evidence."}],
        "needs_more_context": False,
        "context_request": None,
        "typology_adequate": True,
        "typology_diagnosis": "The first label is natural.",
        "proposed_missing_dimensions": [],
        "confidence": 0.95,
    }


class ClassificationValidationTests(unittest.TestCase):
    def test_accepts_valid_result(self):
        validate(valid_result(), "occurrence-1")

    def test_rejects_wrong_occurrence(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            validate(valid_result(), "other")

    def test_rejects_out_of_range_score(self):
        result = valid_result()
        result["label_support"]["performative"] = 5
        with self.assertRaisesRegex(ValueError, "0 to 4"):
            validate(result)

    def test_rejects_unexpected_key(self):
        result = valid_result()
        result["extra"] = True
        with self.assertRaisesRegex(ValueError, "unexpected keys"):
            validate(result)


if __name__ == "__main__":
    unittest.main()
