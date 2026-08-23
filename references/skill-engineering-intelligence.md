# Skill engineering intelligence

## Purpose

Learn how to create and improve skills without treating every observed success as truth. This is a governed meta-capability: it proposes narrow changes, measures them against a baseline, and keeps only changes with evidence and no critical regression.

## Skill intelligence record

For each important principle, keep:

| Field | Meaning |
|---|---|
| Principle | The behavior or decision the skill is meant to improve. |
| General rule | The useful default, stated without pretending it is universal. |
| Context | Product, task, user, platform, risk, and conditions where it applies. |
| Positive example | A response or artifact that demonstrates the principle. |
| Negative example | A failure that violates it and the user cost. |
| Borderline example | A case where the default could be right or wrong. |
| Exception | A context where the default changes and why. |
| Transformation | The smallest change from failure to better behavior. |
| Evidence | Observations, tests, human feedback, and source provenance. |
| Uncertainty | What remains unknown, disputed, stale, or not assessable. |

Examples must explain **why** they represent the principle. Do not use them as decoration or memorize superficial phrase-to-action associations.

## Learning loop

`observe → record → analyze cause → form conditional lesson → generate smallest candidate → test representative/ambiguous/adversarial/held-out cases → compare baseline → check regressions → approve or reject → preserve provenance`.

A lesson is trusted only after sufficient, relevant evidence. The candidate must remain reversible and experimental until an authorized owner promotes it. A model or skill may recommend an improvement but cannot grant itself permissions, trust, production status, or authority to weaken a hard safety, privacy, control, recovery, or accessibility gate.

## High-information example set

For each principle, prefer one example of each kind:

| Kind | Example question |
|---|---|
| Positive | What does good behavior look like in the target context? |
| Negative | What common failure does the principle prevent? |
| Borderline | Which contextual facts could reverse the default? |
| Exception | When is the default intentionally not appropriate? |
| Transformation | What is the smallest repair and what evidence would show improvement? |
| Edge | What happens under ambiguity, missing context, adversarial input, or partial failure? |

Do not generate thousands of near-duplicates. Choose cases that distinguish competing hypotheses or expose regressions.

## Promotion evidence

Report baseline and candidate separately. Include task success, requirement coverage, evidence quality, error and recovery rates, unnecessary actions, latency, cost, human effort, accessibility, privacy, safety, and user control. A smaller candidate that produces equal or better outcomes with fewer tokens, instructions, or failure modes should win. If results are mixed, keep the candidate experimental and state the tradeoff.

## Self-critique questions

Before promotion, ask: what might this conclusion get wrong; which assumptions are unsupported; what part is unnecessarily complicated; what would an expert disagree with; which users or contexts are missing; could the improvement increase manipulation, privacy risk, or approval fatigue; and what evidence would falsify the lesson?

## Boundaries

This reference does not create autonomous self-modification, hidden profiling, or universal taste rules. It does not prove that any skill system is better than a frontier model or competitor. It defines a repeatable way to learn from failures while preserving human authority and rollback.
