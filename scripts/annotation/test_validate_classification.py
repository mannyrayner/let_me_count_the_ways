import unittest

from validate_classification import validate, validate_v0_2


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


def valid_v0_2_result():
    assessment = {"status": "unsupported", "analysis": "No support here.", "confidence": 0.8}
    return {
        "occurrence_id": "occurrence-2",
        "core_love_content": {
            "label_support": {
                "truth_conditional": 4,
                "performative": 1,
                "exclamatory_reflexive": 0,
            },
            "mixed_reading": {"is_mixed": False, "basis": "none", "justification": None},
            "relationship_modifier": None,
            "analysis": "A direct avowal of an existing state.",
            "confidence": 0.95,
        },
        "realisation": {
            "types": ["direct_represented_speech"],
            "other_description": None,
            "actuality": "spoken",
            "analysis": "The character currently speaks the words.",
            "confidence": 0.95,
        },
        "current_discourse_act": {
            "types": ["direct_avowal", "reassurance"],
            "other_description": None,
            "analysis": "The avowal also reassures the addressee.",
            "confidence": 0.85,
        },
        "contextual_modification": {
            "effects": ["preserves"],
            "other_description": None,
            "analysis": "The context preserves the asserted content.",
            "confidence": 0.9,
        },
        "participant_construals": [
            {
                "role": "original_avower",
                "discourse_level": "core_love_content",
                "status": "supported",
                "analysis": "The avower presents love as existing.",
                "confidence": 0.9,
            },
            {
                "role": "current_addressee",
                "discourse_level": "current_discourse_act",
                "status": "unavailable",
                "analysis": "The supplied material contains no addressee response.",
                "confidence": None,
            },
        ],
        "disagreements": [],
        "assessments": {
            "deception_misrepresentation": dict(assessment),
            "manipulation_pressure": dict(assessment),
            "strategic_ambiguity": dict(assessment),
        },
        "evidence": [
            {
                "evidence_id": "e1",
                "source": "local_text",
                "quotation_or_description": "I love you",
                "supports": "Directly supports the core avowal.",
                "confidence": 1.0,
            }
        ],
        "background_knowledge": {
            "used": False,
            "familiarity": "moderate",
            "confidence": None,
            "contribution": None,
            "notes": "Familiarity was unnecessary for this classification.",
        },
        "context_needs": [],
        "ontology_assessment": {
            "adequate": True,
            "diagnosis": "The layered scheme represents the case.",
            "proposed_missing_dimensions": [],
        },
        "notes": None,
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


class ClassificationV02ValidationTests(unittest.TestCase):
    def test_accepts_valid_result(self):
        validate_v0_2(valid_v0_2_result(), "occurrence-2")

    def test_rejects_wrong_occurrence(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            validate_v0_2(valid_v0_2_result(), "other")

    def test_rejects_weak_scores_as_substantial_mixture(self):
        result = valid_v0_2_result()
        result["core_love_content"]["mixed_reading"] = {
            "is_mixed": True,
            "basis": "substantial_multiple_support",
            "justification": "Two readings matter.",
        }
        with self.assertRaisesRegex(ValueError, "at least two core scores"):
            validate_v0_2(result)

    def test_accepts_qualitative_mixture_without_score_threshold(self):
        result = valid_v0_2_result()
        result["core_love_content"]["mixed_reading"] = {
            "is_mixed": True,
            "basis": "qualitative_interaction",
            "justification": "The interaction is central despite the lower secondary score.",
        }
        validate_v0_2(result)

    def test_requires_other_description(self):
        result = valid_v0_2_result()
        result["realisation"]["types"] = ["other"]
        with self.assertRaisesRegex(ValueError, "other_description"):
            validate_v0_2(result)

    def test_rejects_confidence_for_unavailable_construal(self):
        result = valid_v0_2_result()
        result["participant_construals"][1]["confidence"] = 0.5
        with self.assertRaisesRegex(ValueError, "null confidence"):
            validate_v0_2(result)

    def test_requires_independent_assessment_fields(self):
        result = valid_v0_2_result()
        del result["assessments"]["strategic_ambiguity"]
        with self.assertRaisesRegex(ValueError, "assessments must contain exactly"):
            validate_v0_2(result)

    def test_requires_background_evidence_when_background_is_used(self):
        result = valid_v0_2_result()
        result["background_knowledge"].update(
            used=True, confidence=0.7, contribution="Wider plot context clarifies the act."
        )
        with self.assertRaisesRegex(ValueError, "requires at least one"):
            validate_v0_2(result)

    def test_accepts_auditable_background_knowledge(self):
        result = valid_v0_2_result()
        result["background_knowledge"].update(
            used=True, confidence=0.7, contribution="Wider plot context clarifies the act."
        )
        result["evidence"].append({
            "evidence_id": "e2",
            "source": "background_knowledge",
            "quotation_or_description": "A later plot revelation changes the interpretation.",
            "supports": "The avowal may be deceptive.",
            "confidence": 0.7,
        })
        validate_v0_2(result)

    def test_rejects_unknown_disagreement_evidence_id(self):
        result = valid_v0_2_result()
        result["disagreements"] = [{
            "parties": ["speaker", "hearer"],
            "subject": "commitment",
            "description": "They construe the commitment differently.",
            "evidence_ids": ["missing"],
            "confidence": 0.6,
        }]
        with self.assertRaisesRegex(ValueError, "unknown evidence ID"):
            validate_v0_2(result)

    def test_rejects_unscoped_context_request(self):
        result = valid_v0_2_result()
        result["context_needs"] = [{
            "need": "useful_for_richer_interpretation",
            "layers": [],
            "claim": "Hearer uptake is unclear.",
            "request": "Supply the response.",
        }]
        with self.assertRaisesRegex(ValueError, "at least 1"):
            validate_v0_2(result)

if __name__ == "__main__":
    unittest.main()
