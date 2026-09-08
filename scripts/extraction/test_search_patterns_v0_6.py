import json
import re
import unittest
from pathlib import Path


V05 = Path("data/development/search_patterns_v0_5.json")
V06 = Path("data/development/search_patterns_v0_6.json")


@unittest.skipUnless(V06.is_file(), "v0.6 is created only when corpus evidence requires it")
class PatternV06Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v05 = json.loads(V05.read_text(encoding="utf-8"))
        cls.v06 = json.loads(V06.read_text(encoding="utf-8"))
        cls.formal = next(
            pattern for pattern in cls.v06["languages"]["no"]["patterns"]
            if pattern["id"] == "no_jeg_elsker_dem_formal"
        )

    def formal_matches(self, text):
        flags = 0 if self.formal.get("case_sensitive") else re.IGNORECASE
        return bool(re.search(self.formal["regex"], text, flags))

    def test_minimally_extends_v0_5(self):
        self.assertEqual(self.v06["schema_version"], "0.6")
        for language in ("en", "fr", "sv", "de"):
            self.assertEqual(self.v06["languages"][language],
                             self.v05["languages"][language])
        self.assertEqual(self.v06["languages"]["no"]["patterns"][:-1],
                         self.v05["languages"]["no"]["patterns"])
        self.assertTrue(self.formal["case_sensitive"])

    def test_formal_dem_case_behavior(self):
        self.assertTrue(self.formal_matches("Jeg elsker Dem"))
        self.assertTrue(self.formal_matches("jeg elsker Dem"))
        self.assertFalse(self.formal_matches("jeg elsker dem"))

    def test_ordinary_norwegian_forms_remain_covered(self):
        ordinary = self.v06["languages"]["no"]["patterns"][0]
        for text in ("Jeg elsker deg", "Jeg elsker dig", "Jeg elsker dere"):
            with self.subTest(text=text):
                self.assertRegex(text, re.compile(ordinary["regex"], re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
