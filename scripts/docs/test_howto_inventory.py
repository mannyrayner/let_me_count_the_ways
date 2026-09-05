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
    "07_classify_diagnostic_passages.md",
    "08_complete_jane_eyre_v0_1.md",
    "09_run_single_text_pipeline.md",
    "10_acquire_and_dry_run_next_texts.md",
    "11_annotate_next_texts_v0_2.md",
    "12_run_annotation_batches.md",
    "13_annotate_multilingual_five_v0_3_1.md",
    "14_build_canonical_corpus_report.md",
    "15_ingest_indie_romance_three.md",
    "16_annotate_indie_romance_three.md",
    "17_report_and_compare_indie_romance.md",
}


class HowtoInventoryTests(unittest.TestCase):
    def test_all_canonical_runbooks_are_present(self):
        actual = {path.name for path in HOWTO.glob("*.md")}
        self.assertTrue(CANONICAL.issubset(actual))


if __name__ == "__main__":
    unittest.main()
