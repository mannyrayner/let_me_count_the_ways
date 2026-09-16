import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.corpus.canonicalize_expansion_15 import (
    BALZAC_END,
    BALZAC_PARTS,
    BALZAC_START,
    EXPECTED_METADATA,
    UNDSET_REGRESSIONS,
    derive_balzac,
    execute,
)


class ExpansionCanonicalizationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "data/acquisition/expansion_15_v1").mkdir(parents=True)
        self.items = []
        for work_id in EXPECTED_METADATA:
            if work_id == "undset-kristin-lavransdatter":
                parts = []
                bodies = [
                    "KRANSEN\n" + "\n".join(UNDSET_REGRESSIONS) + "\n",
                    "HUSFRUE\n",
                    "KORSET\n",
                ]
                for title, body in zip(("Kransen", "Husfrue", "Korset"), bodies):
                    path = f"data/raw/undset/{title.lower()}.txt"
                    parts.append(self._source(path, body, title=title))
                self.items.append({"work_id": work_id, "constituent_parts": parts})
            else:
                path = f"data/raw/{work_id}/source.txt"
                body = f"ordinary text for {work_id}\n"
                if work_id == "balzac-illusions-perdues":
                    body = "UNRELATED BEFORE\n" + BALZAC_START + "\n" + "\n".join(BALZAC_PARTS) + "\n1835-1843." + BALZAC_END + "\nUNRELATED AFTER\n"
                self.items.append({"work_id": work_id, **self._source(path, body)})
        self._write_inventory()

    def tearDown(self):
        self.temporary.cleanup()

    def _source(self, relative, text, title=None):
        data = text.encode()
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        result = {"derived_text_path": relative, "derived_sha256": hashlib.sha256(data).hexdigest()}
        if title:
            result["title"] = title
        return result

    def _write_inventory(self):
        path = self.root / "data/acquisition/expansion_15_v1/manifest.json"
        path.write_text(json.dumps({"works": self.items}), encoding="utf-8")

    def test_inventory_must_have_exact_expected_ids(self):
        self.items.pop()
        self._write_inventory()
        with self.assertRaisesRegex(ValueError, "exactly the expected 15"):
            execute(self.root, check=True)

    def test_hash_mismatch_stops_before_writes(self):
        self.items[0]["derived_sha256"] = "0" * 64
        self._write_inventory()
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            execute(self.root)
        self.assertFalse((self.root / "corpus").exists())

    def test_balzac_boundaries_include_parts_and_exclude_surroundings(self):
        source = ("BEFORE\n" + BALZAC_START + "\n" + "\n".join(BALZAC_PARTS) + "\nEND" + BALZAC_END + "\nAFTER").encode()
        output = derive_balzac(source).decode()
        self.assertTrue(all(part in output for part in BALZAC_PARTS))
        self.assertNotIn("BEFORE", output)
        self.assertNotIn("AFTER", output)
        self.assertNotIn("FIN DU HUITIÈME VOLUME", output)

    def test_missing_undset_repair_regression_stops(self):
        kransen = self.items[-1]["constituent_parts"][0]
        replacement = "KRANSEN without repaired passages\n"
        updated = self._source(kransen["derived_text_path"], replacement, title="Kransen")
        self.items[-1]["constituent_parts"][0] = updated
        self._write_inventory()
        with self.assertRaisesRegex(ValueError, "Undset repaired regression text missing"):
            execute(self.root)

    def test_generation_is_byte_identical_ordered_and_writes_checkpoint(self):
        execute(self.root)
        ordinary = self.items[0]
        work_id = ordinary["work_id"]
        self.assertEqual((self.root / ordinary["derived_text_path"]).read_bytes(), (self.root / "corpus/works" / work_id / "canonical.txt").read_bytes())
        trilogy = (self.root / "corpus/works/undset-kristin-lavransdatter/canonical.txt").read_text()
        self.assertLess(trilogy.index("KRANSEN"), trilogy.index("HUSFRUE"))
        self.assertLess(trilogy.index("HUSFRUE"), trilogy.index("KORSET"))
        self.assertTrue(all(text in trilogy for text in UNDSET_REGRESSIONS))
        checkpoint = json.loads((self.root / "data/canonicalization/expansion_15_v1/manifest.json").read_text())
        self.assertEqual(checkpoint["status"], "15/15 canonicalized")
        self.assertEqual(len(checkpoint["works"]), 15)

    def test_identical_rerun_is_unchanged(self):
        execute(self.root)
        statuses = execute(self.root)
        self.assertEqual(len(statuses), 15)
        self.assertTrue(all(status.endswith("VALID/UNCHANGED") for status in statuses))

    def test_divergent_existing_target_stops_without_touching_old_work(self):
        old = self.root / "corpus/works/existing-old-work/canonical.txt"
        old.parent.mkdir(parents=True)
        old.write_text("do not touch\n")
        target = self.root / f"corpus/works/{self.items[0]['work_id']}"
        target.mkdir(parents=True)
        (target / "canonical.txt").write_text("divergent\n")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            execute(self.root)
        self.assertEqual(old.read_text(), "do not touch\n")


if __name__ == "__main__":
    unittest.main()
