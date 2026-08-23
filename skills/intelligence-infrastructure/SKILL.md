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
