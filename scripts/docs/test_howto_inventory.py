"""Test the mechanically authoritative runbook index."""

import tempfile
import unittest
from pathlib import Path

from scripts.docs.validate_runbook_index import parse_entries, validate_index


def write_fixture(root: Path, rows: list[tuple[int, str]], files: list[str]) -> Path:
    howto = root / "howto"
    howto.mkdir()
    table = ["# Runbooks", "", "| Step | Runbook | Result |", "| --- | --- | --- |"]
    table.extend(f"| {step} | [Runbook]({link}) | Result |" for step, link in rows)
    (howto / "README.md").write_text("\n".join(table) + "\n", encoding="utf-8")
    for name in files:
        (howto / name).write_text(f"# {name}\n", encoding="utf-8")
    return howto


class RunbookIndexTests(unittest.TestCase):
    def inventory(self, rows, files):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        return validate_index(write_fixture(Path(temporary.name), rows, files))

    def test_repository_index_is_valid(self):
        inventory = validate_index(Path("docs/howto"))
        self.assertEqual((), inventory.errors)
        self.assertEqual(21, len(inventory.canonical))
        self.assertEqual((), inventory.unlinked)

    def test_valid_canonical_directory(self):
        inventory = self.inventory([(0, "00_start.md"), (1, "01_next.md")],
                                   ["00_start.md", "01_next.md"])
        self.assertEqual((), inventory.errors)

    def test_missing_linked_file(self):
        inventory = self.inventory([(0, "00_start.md")], [])
        self.assertTrue(any("does not exist" in error for error in inventory.errors))

    def test_extra_unlinked_numbered_runbook(self):
        rows = [(step, f"{step:02d}_current.md") for step in range(15)]
        rows.append((15, "15_current_version.md"))
        files = [link for _, link in rows]
        files.append("15_old_version.md")
        inventory = self.inventory(
            rows,
            files,
        )
        self.assertIn("15_old_version.md", inventory.unlinked)
        self.assertTrue(any("unlinked numbered" in error for error in inventory.errors))
        self.assertTrue(any("duplicate numbered runbook prefix 15" in error
                            for error in inventory.errors))

    def test_obsolete_indie_runbook_names_are_unlinked_numbered_files(self):
        inventory = self.inventory(
            [(15, "15_ingest_indie_romance_pilot.md"),
             (16, "16_annotate_indie_romance_pilot.md"),
             (17, "17_report_and_compare_indie_romance_pilot.md")],
            ["15_ingest_indie_romance_pilot.md",
             "16_annotate_indie_romance_pilot.md",
             "17_report_and_compare_indie_romance_pilot.md",
             "15_ingest_indie_romance_three.md",
             "17_report_and_compare_indie_romance.md"],
        )
        self.assertEqual(
            ("15_ingest_indie_romance_three.md",
             "17_report_and_compare_indie_romance.md"),
            inventory.unlinked,
        )
        self.assertTrue(any("duplicate numbered runbook prefix 15" in error
                            for error in inventory.errors))
        self.assertTrue(any("duplicate numbered runbook prefix 17" in error
                            for error in inventory.errors))

    def test_duplicate_step(self):
        inventory = self.inventory([(0, "00_start.md"), (0, "00_other.md")],
                                   ["00_start.md", "00_other.md"])
        self.assertTrue(any("claims step 0" in error for error in inventory.errors))

    def test_wrong_numeric_prefix(self):
        inventory = self.inventory([(0, "01_start.md")], ["01_start.md"])
        self.assertTrue(any("numeric prefix" in error for error in inventory.errors))

    def test_duplicate_readme_link(self):
        inventory = self.inventory([(0, "00_start.md"), (1, "00_start.md")], ["00_start.md"])
        self.assertTrue(any("links to '00_start.md' 2 times" in error for error in inventory.errors))

    def test_parser_reads_actual_table_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            howto = write_fixture(Path(temporary), [(0, "00_start.md")], ["00_start.md"])
            self.assertEqual("00_start.md", parse_entries(howto / "README.md")[0].link)

    def test_indie_pilot_preserves_unspecified_cc_by_version(self):
        step = Path("docs/howto/15_ingest_indie_romance_pilot.md").read_text(encoding="utf-8")
        self.assertIn("Some Rights Reserved - Creative Commons (CC BY)", step)
        self.assertIn('"license_version": None', step)
        self.assertIn("Not specified on the Lulu product page", step)
        self.assertNotIn("creativecommons.org/licenses/by/4.0", step)

if __name__ == "__main__":
    unittest.main()
