# Intelligence infrastructure self-critique

## Review result

The implementation now provides a **reference intelligence kernel**, not a continuously self-improving production agent. The kernel validates structured records, preserves append-only memory examples, checks high-information example coverage, validates benchmark case separation, and makes conservative paired decisions. It does not run model trials, collect real users, enforce OS isolation, or provide identity and network security.

## What is strong

| Area | Evidence | Confidence |
|---|---|---:|
| Contract completeness | Nine intelligence schemas and representative records validate in deterministic tests. | High for structural validity |
| Anti-self-deception gates | Kernel tests reject hard-gate failures, regressions, no-improvement results, incomplete metrics, unmeasured fixtures, and mismatched model/budget controls. | High for implemented branches |
| Evidence discipline | Audit, architecture, behavior-observation, and research records preserve FACT/EVIDENCE/INFERENCE/HYPOTHESIS/UNKNOWN distinctions and counterevidence. | High for documented behavior |
| Minimality | One meta-capability Skill was added; requested systems are represented primarily as schemas, records, tests, and benchmark infrastructure. | High for repository diff |
| Human-centered behavior | Intent and communication records require scope, correction, agency, trust calibration, and anti-manipulation checks. | Medium until blinded human review |

## Weaknesses and unknowns

| Status | Weakness or question | Why it matters | Next evidence |
|---|---|---|---|
| UNKNOWN | Whether the kernel improves real model behavior on user tasks | Structural validity is not task performance | Run matched baseline/candidate trials with fixed model, tools, budgets, and held-out cases |
| UNKNOWN | Effect size and statistical reliability of contextual-intelligence changes | Eight cases are coverage, not a powered study | Multiple trials per case plus confidence intervals and failure analysis |
| UNKNOWN | Whether Lovability records predict voluntary continued collaboration without encouraging dependency | Human value cannot be inferred from warmth scores alone | Blinded human review with agency and usefulness criteria |
| UNKNOWN | Whether public Fable-like workflow observations transfer across models | A public pattern may be task- or model-specific | Reproduce bounded patterns using lawful public tools and compare ablations |
| FACT | The benchmark runner currently validates the suite without measured metrics when no metric files are supplied | No false performance claim is made | Connect it to a hosted evaluation harness later |
| FACT | The reference host is not an OS-level sandbox, identity service, network firewall, or production memory quarantine | Prompt rules and schemas cannot enforce these controls alone | Implement and red-team a hosted runtime before consequential deployment |
| HYPOTHESIS | Typed memory and conditional lessons will reduce repeated failure without causing excessive clarification or stale personalization | The design is plausible but untested at scale | Measure correction rate, task success, user effort, stale-memory errors, and privacy incidents |
| HYPOTHESIS | High-information examples will improve generalization more efficiently than longer Skill prose | This is a design hypothesis, not a result | Run length-matched ablations with and without example kinds |

## Stopping rule

Stop expanding the Skill catalog when a requested capability can be represented by an existing Skill plus a typed record, verifier, benchmark case, or runtime control. Create a new Skill only when repeated evidence shows a reusable procedural capability is missing and the candidate has a clear trigger, scope, permissions, verification, evaluation, rollback, and authorized promotion path.

Stop promoting an improvement when any hard safety, privacy, authority, or recoverability gate fails; paired controls differ; held-out cases were used for tuning; a material regression appears; the result is based only on a model judge without artifact evidence; or the improvement cannot be attributed with reasonable confidence.

## Next research priorities

1. Build a hosted adapter that emits the same trace and intelligence records for at least two providers while keeping tool policy and budgets matched.
2. Execute the benchmark suite across baseline, candidate, and ablation arms with repeated trials, code graders, model graders, and blinded human review.
3. Add durable memory quarantine, user-visible inspection, deletion, retention expiry, and incident handling.
4. Add OS-level sandboxing, explicit network egress policy, identity/secret lifecycle, and live monitoring around the reference host.
5. Study whether contextual predictions reduce clarification cost without increasing privacy, stale-memory, or overconfidence failures.
6. Conduct a small, consent-aware human study of communication quality that measures usefulness, effort, agency, trust calibration, and unwanted pressure separately.

## Final judgment

The release is justified as a **measurable foundation for future intelligence**, not as proof of a better model, universal Fable equivalence, or autonomous self-improvement. The most important remaining work is empirical and operational rather than additional prose.
