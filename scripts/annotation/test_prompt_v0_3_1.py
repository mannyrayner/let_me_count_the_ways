import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class CalibratedEPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = (ROOT / "prompts/annotation/classify_passage_v0_3.md").read_text(
            encoding="utf-8")
        cls.calibrated = (ROOT / "prompts/annotation/classify_passage_v0_3_1.md").read_text(
            encoding="utf-8")

    def test_requires_e_force_independent_of_emotional_delivery(self):
        self.assertIn("Passion is not E", self.calibrated)
        self.assertIn("positive evidence", self.calibrated)
        self.assertIn("emotionally intense realisation of T and/or P", self.calibrated)
        self.assertIn("not, assign E=0", self.calibrated)

    def test_retains_independent_mixed_scores_and_o_distinction(self):
        self.assertIn("E may coexist with T or P", self.calibrated)
        self.assertIn("belongs under E rather than O", self.calibrated)
        self.assertIn("O has a deliberately high burden of proof", self.calibrated)

    def test_includes_contrasting_calibration_cases(self):
        self.assertIn("screamed through tears", self.calibrated)
        self.assertIn("after months of reflection", self.calibrated)
        self.assertIn("heard himself blurt", self.calibrated)

    def test_original_prompt_remains_uncalibrated_artifact(self):
        self.assertNotIn("Passion is not E", self.original)
        self.assertIn("# Passage classification prompt v0.3", self.original)


if __name__ == "__main__":
    unittest.main()
