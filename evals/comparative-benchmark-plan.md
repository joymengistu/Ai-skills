# Comparative benchmark plan

This plan compares an agent host with and without the Ai-skills control layer. It is designed to test the repository's claims rather than assume them.

## First runnable slice

The reference host can now run a credential-free deterministic arm with the same policy, trace, checkpoint, approval, and completion-evidence behavior used by future hosted-provider adapters. Use `python3 -m runtime.reference_host` for a smoke test and `python3 -m unittest discover -s runtime/reference_host -p 'test_*.py'` for deterministic regression checks. This validates host behavior, not model quality.

## Experimental arms

| Arm | Description |
|---|---|
| Baseline | Same hosted model, tools, budgets, and runtime without Ai-skills routing and quality layers. |
| Ai-skills | Same model, tools, budgets, and runtime with the smallest sufficient Ai-skills bundle selected by the umbrella router. |
| Framework + Ai-skills | Optional third arm using a public runtime such as LangGraph, CrewAI, or OpenAI Agents SDK plus Ai-skills. This tests complementarity, not framework superiority. |

Keep the model, tool permissions, task prompt, time budget, and external conditions matched wherever possible. Randomize task order and use held-out cases that were not used to author or tune the skills. The reference host should remain the common control surface so provider differences are not confused with missing approvals, traces, checkpoints, or completion gates.

## Task families

Use at least five families: short-brief application or game builds; research with citations and uncertainty; multi-step file or data workflows; long-running work with context reset and recovery; and human-facing brainstorming or design conversations. Include normal, ambiguous, adversarial, partial-failure, and consequential-action cases.

## Measures

| Dimension | Example measure |
|---|---|
| Requirement coverage | Fraction of must-have requirements satisfied with evidence. |
| Completion truthfulness | Unsupported completion claims, fabricated tests, or missing verification. |
| Dynamic quality | Real execution, build health, interaction behavior, visual usability, intent alignment, and operational readiness. |
| Safety and control | Permission violations, missing approvals, privacy failures, irreversible actions, and recoverability. |
| Repair | Defects found, repaired, regressions introduced, and convergence steps. |
| Human effort | Corrections, clarifying turns, review time, rework, frustration, and perceived agency. |
| Efficiency | Model calls, tool calls, tokens, latency, retries, and estimated cost. |
| Conversation quality | Specific understanding, honest appreciation, useful initiative, memory relevance, interruption cost, and constructive disagreement. |

Use deterministic graders for files, tests, schemas, traces, and requirement ledgers. Use independent model judges only for structured qualitative criteria and require evidence snippets. Use human review for taste, perceived understanding, emotional appropriateness, trust calibration, and delight. Never score away a critical safety or control failure.

## Analysis

Report paired outcomes, confidence intervals where sample size supports them, failure examples, and cost-quality tradeoffs. Attribute gains carefully: a difference can come from the model, prompt, skill content, tool host, evaluator, or runtime. Run ablations for requirement compilation, completion intelligence, skeptical evaluation, context handoff, and Lovability/Brainstorm Mode rather than claiming the full bundle caused every improvement.

## Release rule

Publish a comparative result only when the task set, model versions, prompts, tools, budgets, grader definitions, and failure handling are documented. A positive result on one task family is a scoped result, not evidence that Ai-skills universally beats another repository or framework.
