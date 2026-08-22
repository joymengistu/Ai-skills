#!/usr/bin/env python3
"""Validate the repository's small, model-agnostic evaluation case set."""
import json
from pathlib import Path

path = Path(__file__).with_name("cases.jsonl")
required = {"id", "category", "prompt", "verifier"}
seen = set()
for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
    if not line.strip():
        continue
    item = json.loads(line)
    missing = required - item.keys()
    if missing:
        raise SystemExit(f"line {line_no}: missing {sorted(missing)}")
    if item["id"] in seen:
        raise SystemExit(f"line {line_no}: duplicate id {item['id']}")
    seen.add(item["id"])
    if not item["prompt"].strip() or not item["verifier"].strip():
        raise SystemExit(f"line {line_no}: prompt and verifier must be non-empty")
print(f"validated {len(seen)} evaluation cases")
