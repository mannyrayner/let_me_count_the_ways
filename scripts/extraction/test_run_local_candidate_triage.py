import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.extraction.run_local_candidate_triage import load_local_source, require_ignored


class LocalCandidateTriageTests(unittest.TestCase):
    def test_loads_only_hash_verified_local_triage_text(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            text_path = root / "book.txt"
            text_path.write_text("I love you.\n", encoding="utf-8")
            digest = hashlib.sha256(text_path.read_bytes()).hexdigest()
            provenance_path = root / "source.json"
            provenance_path.write_text(json.dumps({
                "review_status": "local_triage_only", "source_id": "source",
                "work_id": "work", "title": "Title", "author": "Author",
                "language": "en", "local_path": str(text_path), "sha256": digest,
                "original_source_path": "/private/book.epub",
                "original_source_sha256": "0" * 64,
            }), encoding="utf-8")
            with patch("scripts.extraction.run_local_candidate_triage.require_ignored"):
                provenance, source, text = load_local_source(provenance_path, root)
            self.assertEqual(provenance["review_status"], "local_triage_only")
            self.assertEqual(source, text_path)
            self.assertEqual(text, "I love you.\n")

    def test_rejects_rights_approved_status_instead_of_bypassing_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "source.json"
            path.write_text('{"review_status":"approved_for_development_processing"}',
                            encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "local_triage_only"):
                load_local_source(path, Path(temporary))

    def test_rejects_repo_path_not_ignored_by_git(self):
        failure = subprocess.CompletedProcess([], 1)
        with patch("subprocess.run", return_value=failure):
            with self.assertRaisesRegex(ValueError, "not ignored"):
                require_ignored(Path("tracked.txt"), Path.cwd())


if __name__ == "__main__":
    unittest.main()
