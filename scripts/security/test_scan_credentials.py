import tempfile
import unittest
from pathlib import Path

from scripts.security.scan_credentials import files_under, findings


class CredentialScanTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self):
        self.temporary.cleanup()

    def test_clean_tree_has_no_findings(self):
        (self.root / "clean.json").write_text('{"model": "gpt-test"}\n', encoding="utf-8")
        self.assertEqual(findings([self.root]), [])

    def test_detects_names_bearer_headers_and_key_shapes_without_decoding(self):
        samples = {
            "name.txt": b"OPENAI_API_KEY=something\n",
            "header.txt": b"authorization: Bearer secret\n",
            "binary.dat": b"\x00sk-abcdefghijklmnop\xff\n",
        }
        for name, content in samples.items():
            (self.root / name).write_bytes(content)
        self.assertEqual(len(findings([self.root])), 3)

    def test_missing_path_fails_instead_of_appearing_clean(self):
        with self.assertRaises(FileNotFoundError):
            files_under([self.root / "missing"])


if __name__ == "__main__":
    unittest.main()
