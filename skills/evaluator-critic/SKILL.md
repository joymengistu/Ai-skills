---
name: evaluator-critic
description: Evaluate an agent-generated artifact independently and skeptically using explicit criteria, live inspection, evidence, and actionable repair priorities. Use when quality is subjective, when the generator may praise its own work, or before a high-stakes release.
---

# Evaluator critic

Separate generator and evaluator roles whenever practical. Give the evaluator the requirement ledger, quality criteria, artifact access, relevant tools, and an output schema. Do not ask only whether the work is good; require evidence, failures, severity, likely cause, and a minimal repair proposal.

For software inspect the running artifact, not only source files. For interfaces evaluate design quality, originality, craft, functionality, accessibility, intent alignment, and restraint independently. For research inspect source authority, freshness, contradictions, reasoning, and citation coverage.

Return a score breakdown with confidence and concrete observations. Prioritize the highest-impact defect rather than enumerating every possible preference. Feed critique to the generator, then rerun the affected checks. Stop or pivot when scores plateau, the current direction is structurally wrong, or additional iteration harms clarity, accessibility, safety, or user intent.

Do not let a favorable score override a failed hard gate. Never fabricate inspection, testing, or evidence.
