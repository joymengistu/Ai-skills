---
name: evidence-ledger
description: Track claims, sources, observations, freshness, confidence, counterevidence, and dependent decisions so an AI agent can produce defensible conclusions. Use for research, recommendations, high-impact analysis, and any claim that must be verified later.
---

# Evidence ledger

Separate claims from conclusions. A fluent answer is not evidence.

## Claim record

For each material claim record: `claim_id`, claim text, source or observation, source authority, publication/access date, freshness requirement, confidence, supporting passage or artifact, counterevidence, dependent decisions, review status, and redactions. Prefer primary sources and direct observations; label secondary reports and model-generated suggestions.

## Reasoning discipline

Mark each item as **FACT**, **INFERENCE**, **HYPOTHESIS**, or **OPINION**. Link conclusions to the claims that support them. When sources conflict, preserve both records, compare authority and freshness, explain the conflict, and avoid false precision. Search for counterexamples before selecting an apparent winner.

## Context and privacy

Pass only the claims needed for the next decision. Redact secrets and sensitive personal data. Keep source identifiers separate from protected content and respect retention and deletion requirements.

## Delivery

Cite claims near the text they support. Include date boundaries, limitations, uncertainty, and what evidence would change the conclusion. Update or expire stale claims rather than silently treating them as current.

## Operational deepening

Use this Skill to improve **traceable claims and source-backed decisions**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is claim status, provenance, authority, freshness, counterevidence, confidence, and expiry.

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
