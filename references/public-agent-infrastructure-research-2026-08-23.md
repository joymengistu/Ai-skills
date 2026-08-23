# Public agent-infrastructure research checkpoint

**Research date:** 2026-08-23

## Evidence boundary

These notes summarize publicly observable guidance. They do not reveal or reproduce proprietary prompts, hidden reasoning, or private implementations. Claims below are marked by evidence status.

## Findings

| Status | Finding | Source |
|---|---|---|
| FACT | Public guidance distinguishes predefined workflows from agents whose model dynamically directs process and tool use. | Anthropic, “Building Effective AI Agents,” https://www.anthropic.com/engineering/building-effective-agents |
| FACT | Public guidance recommends the simplest solution first and warns that agentic complexity trades latency and cost for task performance. | Anthropic, “Building Effective AI Agents,” https://www.anthropic.com/engineering/building-effective-agents |
| FACT | Publicly described workflow patterns include prompt chaining with gates, routing, parallelization, orchestrator-workers, and evaluator-optimizer loops. | Anthropic, “Building Effective AI Agents,” https://www.anthropic.com/engineering/building-effective-agents |
| FACT | Public evaluation guidance defines tasks, trials, graders, transcripts/trajectories, outcomes, evaluation harnesses, agent harnesses, and evaluation suites as distinct components. | Anthropic, “Demystifying evals for AI agents,” https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| FACT | Public evaluation guidance recommends combining code-based, model-based, and human graders, using multi-turn trials for agents, and testing outcomes as well as trajectories. | Anthropic, “Demystifying evals for AI agents,” https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| INFERENCE | Ai-skills should represent evaluator, harness, trial, grader, outcome, and trajectory as separate records so improvements can be attributed without confusing model, prompt, host, tools, or evaluator effects. | Derived from the two public sources and the repository’s existing capability-analysis/evidence-ledger rules. |
| HYPOTHESIS | A small deterministic reference implementation for record validation and paired comparison will create more durable improvement value than adding many new prose Skills. | Repository design hypothesis; requires real matched-model experiments. |
| UNKNOWN | Public articles do not establish that any particular Fable-like workflow universally outperforms other architectures or models. | No public evidence in the reviewed sources establishes universal superiority. |

## Design consequences

1. Keep workflows and dynamic agents as separate architectural choices.
2. Require gates, bounded budgets, and environment-grounded verification for agent loops.
3. Make paired baseline-versus-candidate trials, held-out cases, regression checks, and cost/safety/user-effort measures first-class.
4. Preserve alternative valid paths and outcome truth; do not reward unsupported confidence or copied rationale.
5. Treat Fable-inspired observations as public behavioral hypotheses, not as evidence of hidden implementation details.

## References

1. [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
2. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
