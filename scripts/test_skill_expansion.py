"""Regression tests for the controlled Skill-deepening migration."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillExpansionTests(unittest.TestCase):
    def test_every_deepened_skill_has_exactly_one_operational_section(self):
        paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertGreaterEqual(len(paths), 1)
        exempt = {"screenshot-reconstruction"}
        for path in paths:
            if path.parent.name in exempt:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertEqual(text.count("## Operational deepening"), 1, path.parent.name)
            self.assertIn("### Execute", text)
            self.assertIn("### Evidence and boundaries", text)
            self.assertIn("### Decision examples", text)
            self.assertIn("### Composition and stopping rule", text)

    def test_expansion_is_meaningful_but_stays_within_skill_limit(self):
        for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertGreaterEqual(len(lines), 40, path.parent.name)
            self.assertLess(len(lines), 500, path.parent.name)
            self.assertTrue(lines[0] == "---", path.parent.name)
            self.assertIn("name:", "\n".join(lines[:8]), path.parent.name)
            self.assertIn("description:", "\n".join(lines[:8]), path.parent.name)

    def test_expansion_prompt_and_audit_are_present(self):
        self.assertTrue((ROOT / "references" / "skill-expansion-self-prompt.md").is_file())
        self.assertTrue((ROOT / "references" / "skill-expansion-audit-2026-08-23.md").is_file())
        prompt = (ROOT / "references" / "skill-expansion-self-prompt.md").read_text(encoding="utf-8")
        self.assertIn("Do not pad it", prompt)
        self.assertIn("before-versus-after", prompt)
        self.assertIn("CLOSING QUESTION", prompt)


if __name__ == "__main__":
    unittest.main()
