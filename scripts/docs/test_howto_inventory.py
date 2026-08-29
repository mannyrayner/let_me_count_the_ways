"""Guard against retaining superseded how-to runbooks."""

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
OBSOLETE = {
    "00_setup_and_verify.md",
    "01_generate_targets.md",
    "02_review_targets.md",
    "03_acquire_one_text.md",
    "04_extract_passages.md",
    "05_classify_one_passage.md",
}


class HowtoInventoryTests(unittest.TestCase):
    def test_only_canonical_runbooks_are_present(self):
        actual = {path.name for path in HOWTO.glob("*.md")}
        self.assertEqual(actual, CANONICAL)

    def test_obsolete_runbooks_are_absent(self):
        actual = {path.name for path in HOWTO.glob("*.md")}
        self.assertTrue(actual.isdisjoint(OBSOLETE))


if __name__ == "__main__":
    unittest.main()
