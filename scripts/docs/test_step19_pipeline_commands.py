import unittest
from pathlib import Path


RUNBOOK = Path("docs/howto/19_acquire_and_reconnoitre_classical_six.md")


class Step19PipelineCommandTests(unittest.TestCase):
    def test_single_text_pipeline_uses_positional_provenance(self):
        text = RUNBOOK.read_text(encoding="utf-8")
        invocations = text.split("python scripts/pipeline/run_single_text_pipeline.py \\\n")[1:]
        self.assertEqual(len(invocations), 2)
        for invocation in invocations:
            first_argument_line = invocation.splitlines()[0].strip()
            self.assertEqual(first_argument_line, '"$PROVENANCE" --patterns "$PATTERNS" \\')
        self.assertNotIn('--provenance "$PROVENANCE"', text)

    def test_cygwin_paths_strip_windows_carriage_returns(self):
        text = RUNBOOK.read_text(encoding="utf-8")
        strip = "PROVENANCE=${PROVENANCE%$'\\r'}"
        self.assertEqual(text.count(strip), 2)
        command = "python scripts/pipeline/run_single_text_pipeline.py \\\n"
        parts = text.split(command)
        self.assertEqual(len(parts), 3)
        self.assertIn(strip, parts[0])
        self.assertIn(strip, parts[1])

    def test_step7_records_and_step8_consumes_exact_runs(self):
        text = RUNBOOK.read_text(encoding="utf-8")
        self.assertIn('RUN_LIST="$RECON/selected-run-directories.txt"', text)
        self.assertIn('printf \'%s\\n\' "$RUN_DIR" >> "$RUN_LIST_PART"', text)
        self.assertIn('mv "$RUN_LIST_PART" "$RUN_LIST"', text)
        self.assertNotIn("PASTE_SIX_EXACT_RUN_DIRECTORIES", text)
        self.assertIn("Expected 6 selected run directories", text)
        self.assertIn("Run selection order/source mismatch", text)


if __name__ == "__main__":
    unittest.main()
