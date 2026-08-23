# One-shot execution improvement report

## Purpose

The new one-shot capability is a **transparent execution contract**, not a hidden reasoning prompt and not a guarantee of perfect one-pass work. It is designed to maximize the chance of a coherent first execution arc by preserving requirements, choosing proportional planning depth, building a thin complete slice, verifying the real result, repairing the smallest cause, and reporting limits honestly.

## Repository changes

| Area | Change |
|---|---|
| Prompt resource | Added `references/one-shot-execution-prompt.md`, a copyable self-directing prompt with six execution stages and a stop rule. |
| Ultra Plan | Added a one-shot path that reuses requirement compilation, product completeness, dynamic verification, repair, and completion reporting. |
| Core router | Added `ONE-SHOT EXECUTION ROUTE` to `core/self-directing-prompt.md`. |
| Benchmarks | Added five cases for detailed builds, simple-task proportionality, requirement conservation, honest completion, and private-reasoning boundaries. |
| Release checks | Added the prompt reference to required repository validation. |

## What the prompt forces

The agent must preserve explicit requirements, distinguish necessary inferences from optional ideas and unknowns, ask only when ambiguity materially changes architecture or risk, and choose the smallest sufficient capability bundle. It must map the relevant interface, interaction, state, data, persistence, security, accessibility, deployment, observability, and acceptance dimensions; build a thin end-to-end slice; test risky states; and separate verified work from partial, unverified, deferred, or blocked work.

For simple reversible tasks, the prompt explicitly chooses a focused exception. This prevents “maximum” from turning into wasteful overplanning. For complex builds, it reuses the existing Ultra Ultra protocol rather than creating another parallel planning system.

## Evidence boundary

| Label | Conclusion |
|---|---|
| **FACT** | The prompt resource, router integration, and five benchmark records are present and pass repository validation. |
| **EVIDENCE** | The benchmark cases encode failure modes already represented in the repository: shallow demos, requirement loss, overplanning, unsupported completion claims, and requests for private reasoning. |
| **INFERENCE** | A transparent self-directing contract can reduce requirement loss and improve first-pass coherence when the model and host have sufficient context and tools. |
| **HYPOTHESIS** | Baseline-versus-candidate trials will show better requirement coverage, edge-state coverage, and honest completion reporting on suitable build tasks. |
| **UNKNOWN** | Whether the prompt improves real hosted model outcomes, by how much, for which providers, and whether its added instructions ever displace useful context. |

## Validation

The repository passes with **61 Skills**, **85 evaluation cases**, all Skill quick validators, the full repository validator, **17 reference-host tests**, **10 intelligence-kernel tests**, and **5 benchmark-runner tests**. The benchmark runner remains `not_run` when real baseline and candidate measurements are absent; no model-quality gain is claimed.

## Limits and safety

The prompt cannot enforce permissions, approvals, budgets, isolation, secrets handling, network policy, or external side-effect safety by itself. The host runtime must enforce those boundaries. One-shot execution also does not mean that the agent should silently execute destructive or consequential actions, reveal private chain-of-thought, or claim universal superiority. The correct stopping rule is verified acceptance, a clear blocker, exhausted budget, rising risk, or diminishing returns.
