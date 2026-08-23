# Maximum-capability gap audit

**Baseline release:** `14969c3`  
**Current baseline:** 61 Skills, 76 evaluation cases, reference host with 15 tests, intelligence kernel, benchmark runner, and normalized redacted trace adapter.

## Ranked gaps

| Rank | Gap | Value | Evidence | Safe bounded increment |
|---:|---|---|---|---|
| 1 | Real hosted provider adapter and authenticated execution | Enables actual model comparisons and user value | Research roadmap and current adapter seam; no provider calls in repository | Define a provider-neutral request/response contract and a local deterministic experiment runner first; do not add credentials or claim hosted results |
| 2 | Environment-grounded outcome verification | Prevents “done” claims without artifact evidence | Existing completion gate and benchmark guidance; host currently accepts evidence refs supplied by caller | Add verifier protocol and deterministic file/artifact verifier with tamper-evident evidence records |
| 3 | Paired experiment analysis | Turns runs into measurable improvement | Current kernel decides from supplied metrics but does not aggregate per-case trial results | Add per-case result aggregation, hard-gate accounting, deltas, and abstention on missing data |
| 4 | Durable privacy/identity/memory services | Required for real hosted deployment | Explicitly documented as future infrastructure | Research and design only until service boundaries and consent lifecycle are available |
| 5 | Human-value study | Tests Lovability and communication claims | Current benchmark has cases but no real participants | Define blinded protocol; do not simulate human results |

## Selection

Implement **Rank 2 plus the minimum needed for Rank 3**: an environment-grounded verifier seam and per-case paired result aggregation. This improves the quality of evidence produced by the existing host without pretending to be a real hosted provider, adding credentials, or creating redundant Skills.

## Non-goals

This increment will not call external model APIs, handle secrets, create a production sandbox, infer sensitive traits, or report a model-quality win. It will produce deterministic local evidence and conservative abstention behavior that a future hosted adapter can reuse.

## Public research checkpoint

| Status | Finding | Source |
|---|---|---|
| FACT | The Reward Hacking Benchmark describes multi-step tool tasks with shortcut opportunities such as skipping verification, using task-adjacent metadata, or tampering with evaluation-relevant functions; its abstract reports that simple environmental hardening reduced exploit rates in the studied setup without reducing task success. | [Thaman — Reward Hacking Benchmark](https://arxiv.org/abs/2605.02964) |
| FACT | The Regression Tax paper reports that Skills can cause regressions and identifies skill-description osmosis, grounding displacement, and verification displacement as mechanisms; it argues that net improvement should account for regressions rather than average success alone. | [Tank and Nama — The Regression Tax](https://arxiv.org/abs/2607.22520) |
| EVIDENCE | These are public paper abstracts and should be treated as bounded evidence about the studied tasks and setups, not universal model rankings. | The linked arXiv records. |
| INFERENCE | The highest-leverage next improvement for Ai-skills is a verifier and per-case regression accounting layer, because a larger Skill can reduce performance by displacing grounding or verification. | Derived from the two public studies and the repository’s own evaluation contract. |
| HYPOTHESIS | Environment-grounded checks plus explicit gain/regression/residual-failure accounting will prevent more false promotions than adding more procedural Skill prose. | Requires controlled implementation and benchmark testing. |
| UNKNOWN | Whether these observed effects transfer to Ai-skills’ existing cases, providers, and hosted environments. | Requires matched experiments. |
