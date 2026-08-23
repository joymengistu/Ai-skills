---
name: memory
description: Design and use scoped, consent-aware, inspectable, deletable memory for AI agents. Use when an agent needs continuity across turns or sessions.
---

# Memory

Store only information that is useful, stable enough to retain, and appropriate for the scope. Use `references/memory-lifecycle-contract.md` to distinguish conversation, project, research, lesson, user-preference, and checkpoint memory; record purpose, provenance, scope, sensitivity, consent, confidence, status, expiry, correction, deletion, and promotion evidence. Prefer explicit user preferences and project facts over speculative personality inferences. Separate general facts from structured keys, as in CLAI's `facts` and `special` memory pattern.

Every memory item should have provenance, scope, confidence, sensitivity, created/updated time, expiry or review rule, and deletion path. Do not store secrets, credentials, sensitive personal data, or high-impact inferences by default. Show users what is remembered when it matters and support correction and forget operations.

Inject memory as a compact, clearly labeled context block. Never let memory override the current user request, safety policy, or fresh evidence. Review memory on correction, contradiction, source change, expiry, or repeated failure; supersede or delete it rather than silently rewriting it.

## Operational deepening

Use this Skill to improve **relevant, scoped, controllable memory**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is purpose, consent, sensitivity, scope, expiry, correction, deletion, provenance, and retrieval.

### Execute

1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.
2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.
3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.
4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.

### Evidence and boundaries

Treat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |
| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |
| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |
| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |
| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |

### Composition and stopping rule

Declare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.
