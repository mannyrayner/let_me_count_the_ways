"""Verify that every canonical how-to runbook is available."""

import unittest
from pathlib import Path


HOWTO = Path("docs/howto")
CANONICAL = {
    "README.md",
    "00_configure_cygwin.md",
    "01_checkout_and_verify.md",
    "02_configure_model_and_generate_targets.md",
    "03_review_targets.md",
    "04_acquire_one_text.md",
    "05_extract_passages.md",
    "06_classify_one_passage.md",
}


class HowtoInventoryTests(unittest.TestCase):
    def test_all_canonical_runbooks_are_present(self):
        actual = {path.name for path in HOWTO.glob("*.md")}
        self.assertTrue(CANONICAL.issubset(actual))


if __name__ == "__main__":
    unittest.main()
