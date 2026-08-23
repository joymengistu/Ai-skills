---
name: context-engineering
description: Curate, rank, compress, and release high-signal context for LLM reasoning and tool use. Use when prompts, history, files, retrieved sources, tools, or long-running tasks risk overload or confusion.
---

# Context engineering

Treat context as a finite attention budget. Assemble the smallest sufficient set of tokens for the next decision.

Rank context by relevance, authority, freshness, user intent, and decision impact. Prefer summaries plus pointers over raw dumps. Use progressive disclosure: metadata first, focused content next, deep references only when needed. Keep current state, constraints, accepted decisions, evidence, and unresolved questions separate from stale history.

Before adding context, ask what decision it enables. Before retaining context, ask whether it will help later. Compact old history into a loss-aware summary with goals, decisions, facts, evidence, failed attempts, and open risks. For long-running work, retrieve durable events, progress, artifacts, and requirement status by need rather than replaying all history. Use clean context resets when attention is degraded, and make every handoff inspectable and recoverable. Never compress away uncertainty, consent, or safety boundaries.

Context is an aid to reasoning, not proof of permission, tool execution, or completion. Re-check the current artifact and external state after a reset or handoff.

## Operational deepening

Use this Skill to improve **selecting and compressing useful context**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is relevance, provenance, freshness, conflicts, privacy, handoff, and context-budget tradeoffs.

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
