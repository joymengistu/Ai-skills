---
name: intelligence-infrastructure
description: Govern the evaluation, memory, example, intent, communication, research, composition, and improvement records that let an AI capability system learn without fooling itself. Use when auditing Skills, recording research or lessons, comparing baseline and candidate versions, designing benchmarks, or proposing capability changes.
---

# Intelligence infrastructure

Use this as the **meta-capability route** when the task is to improve the capability system itself. It is an evidence and experiment layer, not a replacement for domain Skills.

## Operating contract

1. **Audit first.** Identify the current Skill, runtime, model, tools, memory, evaluator, and environment. Do not infer that a prose instruction is an enforced control.
2. **Label claims.** Mark every material statement as `FACT`, `EVIDENCE`, `INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`. Preserve source, counterevidence, freshness, confidence, scope, and deletion path.
3. **Represent quality.** For each important principle, keep positive, negative, borderline, exception, and transformation examples. Explain why each response is good or bad and name the observable consequence.
4. **Record failure.** Convert each material failure or correction into a lesson with observation, likely cause, conditional applicability, non-applicability, expected benefit, regression risk, test cases, confidence, and rollback.
5. **Change the smallest thing.** Prefer better context, tool contracts, routing, verifiers, or examples before expanding a Skill or changing the core prompt. Never equate length, complexity, or Skill count with quality.
6. **Compare fairly.** Run baseline and candidate under the same model, tools, cases, budgets, and environment where possible. Include held-out cases, ablations, failure examples, cost, user effort, and hard safety/privacy/authority/recoverability gates.
7. **Promote conservatively.** Promote only when there is measurable improvement, no material regression, all hard gates pass, evidence is sufficient, and the authorized release process approves the change. Otherwise hold, reject, or request human review.
8. **Preserve agency.** Intent predictions are scoped and correctable; memories are inspectable and deletable; predictions never authorize side effects; communication optimizes useful collaboration rather than engagement or dependency.
9. **Research behavior, not secrets.** For Fable-inspired research, record only publicly observable artifacts. Separate model, prompt/Skill, harness, tools, memory, environment, and unknown mechanism. Do not seek or reproduce proprietary prompts or hidden reasoning.
10. **Report limits.** State what was tested, what was not tested, what is inferred, what remains unknown, and the next experiment.

## Skill deepening route

When an existing Skill is unusually short or repeatedly fails to guide execution, read `references/skill-expansion-self-prompt.md`. Audit first, preserve the contract, find a real gap, add only high-information workflow detail, examples, failure handling, composition rules, evidence boundaries, or stopping rules, and compare the prior and expanded versions when a real experiment is available. Keep the Skill compact when extra prose would duplicate references or displace task context. Length, Skill count, and apparent complexity are not quality metrics.

## Resource map

| Need | Read or use |
|---|---|
| Claim and research memory | `runtime/intelligence/research-memory.schema.json`, `skills/evidence-ledger/SKILL.md` |
| Failure and lesson memory | `runtime/intelligence/lesson-memory.schema.json`, `skills/human-feedback/SKILL.md`, `skills/self-improvement/SKILL.md` |
| Examples and counterexamples | `runtime/intelligence/example-record.schema.json`, `runtime/skill-contract.schema.json` |
| User intent prediction | `runtime/intelligence/intent-prediction.schema.json`, `skills/contextual-user-intelligence/SKILL.md` |
| Lovability trials | `runtime/intelligence/communication-trial.schema.json`, `skills/lovability/SKILL.md` |
| Skill evaluation | `runtime/intelligence/evaluation-record.schema.json`, `skills/evaluation/SKILL.md`, `skills/evaluator-critic/SKILL.md` |
| Candidate improvement | `runtime/intelligence/improvement-record.schema.json`, `skills/skill-forging/SKILL.md` |
| Benchmarks | `runtime/intelligence/benchmark-run.schema.json`, `evals/comparative-benchmark-plan.md` |
| Fable behavioral research | `runtime/intelligence/behavior-observation.schema.json`, `references/fable-capability-evidence-ledger.yaml`, `references/public-agent-infrastructure-research-2026-08-23.md` |
| Deterministic reference kernel | `runtime/intelligence/kernel.py` and its tests |

## Reference implementation

Use `runtime/intelligence/kernel.py` for offline validation, append-only JSONL records, example coverage, and conservative paired decisions. It is intentionally dependency-light and provider-agnostic. It does not call a model, access credentials, infer sensitive traits, run production isolation, or authorize external actions.

## Required record sequence

`observe → preserve evidence → classify claim → record failure or lesson → propose smallest candidate → run paired and held-out tests → inspect hard gates and regressions → obtain authorized decision → preserve provenance → schedule review or expiry`.

A candidate that improves an average score but fails a hard gate is rejected. A candidate with no measurable improvement is held. A candidate with incomplete paired metrics is not comparable. A favorable model judge is evidence, not authority.

## Operational deepening

Use this Skill to improve **governed evaluation, memory, and improvement of capabilities**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is audit, records, paired tests, hard gates, promotion, provenance, and stopping rules.

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
