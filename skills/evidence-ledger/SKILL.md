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
