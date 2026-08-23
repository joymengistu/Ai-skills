# Maximum-capability improvement report

**Baseline:** `14969c3`  
**Target:** Maximize credible capability without maximizing Skill count or workflow complexity.

## Selected improvement

The audit ranked environment-grounded outcome verification and per-case regression accounting above additional Skills. Public research on reward hacking and Skill regressions supports this priority: benchmark shortcuts can exploit weak verifiers, and Skills can cause regressions by displacing grounding or verification [1] [2]. These findings are bounded evidence about their studied setups, not universal model claims.

## Implemented

| Component | Change |
|---|---|
| Grounded verifier seam | Added `runtime/reference_host/verifiers.py` with a read-only `OutcomeVerifier` protocol, confined `FileStateVerifier`, evidence SHA-256 digests, missing/hash-mismatch failure states, and path-escape rejection. |
| Host completion gate | `ReferenceHost` can now require verifier success and blocks completion when artifact state is missing or mismatched. Verifier evidence is placed in the trace and result. |
| Paired case analysis | Added `aggregate_paired_results()` to distinguish gains, regressions, residual failures, unchanged successes, hard-gate failures, success rates, and net deltas. |
| Benchmark runner | Added `--case-results` support so measured per-case outcomes can be aggregated without collapsing them into one score. |
| Documentation | Added a ranked gap audit and updated the README to explain why this is higher leverage than adding Skills. |

## Validation

The full repository validator passes with **61 Skills**, **76 evaluation cases**, **17 reference-host tests**, **10 intelligence-kernel tests**, and **5 benchmark-runner tests**. All Skill quick validators pass, and the working tree is clean after publication.

The tests prove structural and deterministic behavior: correct artifact hashes produce verifier evidence; missing or mismatched artifacts block completion; unsafe paths are rejected; paired analysis preserves regressions and residual failures; malformed or duplicate pairs fail closed. They do not prove that a hosted model improves on real tasks.

## Evidence boundary

| Label | Conclusion |
|---|---|
| **FACT** | The new verifier and aggregation branches pass deterministic tests. |
| **EVIDENCE** | Public RHB and Regression Tax abstracts discuss reward-hacking shortcuts and regression modes; the repository’s own test outputs verify implementation behavior [1] [2]. |
| **INFERENCE** | Environment-grounded verification is a higher-leverage infrastructure improvement than additional procedural Skill prose for this repository’s current gaps. |
| **HYPOTHESIS** | The verifier and regression accounting will reduce false promotions and expose Skill-induced regressions in real hosted experiments. |
| **UNKNOWN** | Cross-provider performance, effect size, statistical reliability, human-value outcomes, production privacy, and sandbox security. |

## Remaining limits

The verifier is intentionally read-only and local. It is not a general filesystem sandbox, a network policy, a hosted provider adapter, a multi-tenant identity layer, or a production evidence store. SHA-256 evidence proves the observed file bytes at verification time; it does not prove that the artifact is semantically correct unless the task supplies a valid expected digest or a stronger domain verifier.

## Next experiment

Connect one authorized read-only hosted provider adapter to a small development and held-out subset. Run baseline, candidate, and optional ablation arms under fixed model, tool, budget, and environment controls. Emit normalized redacted traces, use environment-grounded verifiers, aggregate per-case gains and regressions, and stop if safety, privacy, authority, recoverability, or attribution gates fail.

## References

1. [Thaman — Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964)
2. [Tank and Nama — The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520)
