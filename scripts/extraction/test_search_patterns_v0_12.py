import json
import re
import unittest
from pathlib import Path


class NorwegianAlsoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = json.loads(Path("data/development/search_patterns_v0_11.json").read_text(encoding="utf-8"))
        cls.current = json.loads(Path("data/development/search_patterns_v0_12.json").read_text(encoding="utf-8"))
        cls.regex = next(p["regex"] for p in cls.current["languages"]["no"]["patterns"]
                         if p["id"] == "no_also_main")

    def test_only_additive_norwegian_change(self):
        self.assertEqual(self.current["schema_version"], "0.12")
        for lang in self.previous["languages"]:
            if lang == "no":
                self.assertEqual(self.current["languages"][lang]["patterns"][:-2],
                                 self.previous["languages"][lang]["patterns"])
            else:
                self.assertEqual(self.current["languages"][lang], self.previous["languages"][lang])

    def test_current_and_historical_also_with_second_person(self):
        for text in ["jeg elsker også Dig", "Jeg elsker ogsaa dig", "Jeg elsket også deg",
                     "Jeg elsker\nogså Dem", "jeg elsker også dere"]:
            with self.subTest(text=text):
                self.assertIsNotNone(re.fullmatch(self.regex, text, re.I))

    def test_does_not_relax_person_or_target(self):
        for text in ["han elsker også Dig", "jeg elsker også hende", "vi elsker også dere",
                     "jeg elsker også digteren", "jeg elsker Dig"]:
            with self.subTest(text=text):
                self.assertIsNone(re.search(self.regex, text, re.I))

    def test_historical_dano_norwegian_past_form(self):
        regex = next(p["regex"] for p in self.current["languages"]["no"]["patterns"]
                     if p["id"] == "no_historical_past")
        for text in ["Jeg elskede dig", "jeg elskede Dem", "jeg elskede\ndere"]:
            self.assertIsNotNone(re.fullmatch(regex, text, re.I))
        for text in ["Du elskede mig", "jeg elskede hende", "jeg elskede digteren"]:
            self.assertIsNone(re.search(regex, text, re.I))


if __name__ == "__main__":
    unittest.main()
