#!/usr/bin/env python3
"""Static structural checks for the Ai skills repository."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
required = [ROOT / "README.md", ROOT / "manifest.yaml", ROOT / "core" / "self-directing-prompt.md"]
for path in required:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 10:
    raise SystemExit(f"expected at least 10 skills, found {len(skills)}")
for path in skills:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"invalid frontmatter: {path}")
    if len(text.splitlines()) > 500:
        raise SystemExit(f"skill exceeds 500 lines: {path}")

for path in [ROOT / "core" / "operating-contract.md", ROOT / "skills" / "safety-governance" / "SKILL.md", ROOT / "skills" / "evaluation" / "SKILL.md"]:
    if not path.exists():
        raise SystemExit(f"missing governance file: {path}")

prompt = (ROOT / "core" / "self-directing-prompt.md").read_text(encoding="utf-8")
for phrase in ["Never claim success", "Ask for approval", "smallest sufficient context", "Verify"]:
    if phrase.lower() not in prompt.lower():
        raise SystemExit(f"self-prompt missing principle: {phrase}")

subprocess.run(["python3", str(ROOT / "evals" / "validate_cases.py")], check=True)
print(f"validated repository with {len(skills)} skills")
