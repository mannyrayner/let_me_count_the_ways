import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.corpus.build_canonical_work import build_work
from scripts.corpus.validate_canonical_corpus import rights_review_lines, validate_corpus, validate_work


class CanonicalCorpusTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.works = self.root / "corpus" / "works"
        source = self.root / "approved.txt"
        source.write_text("Source-faithful café.\n", encoding="utf-8")
        reference = self.root / "provenance" / "source.json"
        reference.parent.mkdir()
        reference.write_text("{}\n", encoding="utf-8")
        self.metadata = {
            "work_id": "author-example", "title": "Example", "author": "Author",
            "language": "en", "source_type": "local_permissioned",
            "source_references": ["provenance/source.json"], "analysis_allowed": True,
            "public_render_policy": "PERMISSIONED_CONTEXT_OK", "notes": "Test.",
        }
        self.manifest_path = build_work(source, self.works, self.metadata)

    def tearDown(self):
        self.temporary.cleanup()

    def manifest(self):
        return json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def write_manifest(self, manifest):
        self.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def errors(self):
        return validate_work(self.manifest_path.parent, self.root)[0]

    def test_valid_manifest_and_corpus(self):
        errors, manifests = validate_corpus(self.works, self.root)
        self.assertEqual(errors, [])
        self.assertEqual([item["work_id"] for item in manifests], ["author-example"])
        canonical = self.manifest_path.parent / "canonical.txt"
        self.assertEqual(self.manifest()["canonical_sha256"], hashlib.sha256(canonical.read_bytes()).hexdigest())

    def test_detects_sha_mismatch(self):
        (self.manifest_path.parent / "canonical.txt").write_text("changed", encoding="utf-8")
        self.assertTrue(any("SHA-256 mismatch" in error for error in self.errors()))

    def test_detects_missing_canonical_text(self):
        (self.manifest_path.parent / "canonical.txt").unlink()
        self.assertTrue(any("missing canonical.txt" in error for error in self.errors()))

    def test_detects_invalid_or_missing_work_id(self):
        for value in (None, "Not A Slug"):
            manifest = self.manifest()
            if value is None:
                manifest.pop("work_id")
            else:
                manifest["work_id"] = value
            self.write_manifest(manifest)
            self.assertTrue(any("work_id" in error for error in self.errors()))

    def test_detects_invalid_rights_metadata(self):
        manifest = self.manifest()
        manifest["rights"]["public_render_policy"] = "UNREVIEWED"
        self.write_manifest(manifest)
        self.assertTrue(any("invalid rights metadata" in error for error in self.errors()))

    def make_private(self, content="Private café.\n"):
        local = self.root / "private" / "text.txt"
        local.parent.mkdir()
        local.write_text(content, encoding="utf-8")
        manifest = self.manifest()
        manifest.update({
            "canonical_storage": "local_private", "canonical_text": None,
            "canonical_local_path": "private/text.txt",
            "canonical_sha256": hashlib.sha256(local.read_bytes()).hexdigest(),
        })
        (self.manifest_path.parent / "canonical.txt").unlink()
        self.write_manifest(manifest)
        return local

    def test_local_private_validates_when_present(self):
        self.make_private()
        warnings = []
        self.assertEqual(validate_work(self.manifest_path.parent, self.root, warnings)[0], [])
        self.assertEqual(warnings, [])

    def test_local_private_missing_is_a_warning(self):
        self.make_private().unlink()
        warnings = []
        self.assertEqual(validate_work(self.manifest_path.parent, self.root, warnings)[0], [])
        self.assertTrue(any("private canonical source unavailable locally" in item for item in warnings))

    def test_local_private_hash_mismatch_is_an_error(self):
        local = self.make_private()
        local.write_text("changed", encoding="utf-8")
        self.assertTrue(any("SHA-256 mismatch" in error for error in self.errors()))

    def test_limited_quotation_and_review_required_are_valid(self):
        manifest = self.manifest()
        manifest["rights"] = {
            "analysis_allowed": True,
            "public_render_policy": "LIMITED_QUOTATION_ONLY",
            "rights_review": {
                "status": "REVIEW_REQUIRED",
                "issue": "AUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS",
                "note": "Approval is outstanding.",
            },
        }
        self.write_manifest(manifest)
        self.assertEqual(self.errors(), [])
        line = rights_review_lines([manifest])[0]
        self.assertEqual(
            line,
            "REVIEW_REQUIRED\tauthor-example\tAUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS",
        )


if __name__ == "__main__":
    unittest.main()
