## Public evidence checkpoint: OpenAI and Anthropic

| Source | Publicly observable pattern | Practical implication | Evidence status |
|---|---|---|---|
| OpenAI Agents SDK guide | The SDK runner performs the tool loop, switches agents after handoffs, and stops when the run finishes or pauses for approval. It exposes sessions, tracing, guardrails, resumable approval flows, and a choice between SDK-owned loops and application-owned Responses API loops. | Keep the library’s prompt layers separate from the host loop. Define a runner contract for tool calls, handoffs, pause/resume, approvals, state, and traces; allow application-owned loops when custom branching is needed. | EVIDENCE from public documentation; not evidence that a specific prompt is superior. |
| Anthropic Building Effective AI Agents | Anthropic distinguishes predefined workflows from agents that dynamically direct process/tool use. It emphasizes simple composable patterns, environmental ground truth from tools/code execution, human checkpoints/blockers, and bounded stopping conditions. | Default to the simplest workflow that fits. Require tool/environment evidence per step, explicit checkpoints, max iterations/budgets, and escalation for blockers. Use multi-agent coordination only when the task benefits from separated context or parallel ownership. | EVIDENCE from a public engineering guide; implementation guidance, not a universal benchmark result. |

FACT: Both sources publicly document runner/tool/state/coordination primitives. INFERENCE: Prompt layers should state responsibilities and contracts while code enforces permissions, loops, budgets, approvals, and persistence. UNKNOWN: Cross-provider effectiveness and optimal layer count for this repository.
## Public evidence checkpoint: LangGraph and OpenAI guardrails

| Source | Publicly observable pattern | Practical implication | Evidence status |
|---|---|---|---|
| LangGraph overview | A low-level orchestration runtime mixes deterministic and LLM-driven steps, supports persistence, durable execution, human-in-the-loop state inspection/modification, short- and long-term memory, and execution tracing. | Keep deterministic validators, state transitions, retries, and side-effect gates in code; reserve model-driven steps for flexible decisions. Use explicit state/checkpoints and typed graph edges for recoverability. | EVIDENCE from public documentation. |
| OpenAI guardrails and human review | Input, output, and tool guardrails serve different boundaries. Tool calls that need approval interrupt the run, return resumable state, and continue from that state after approval/rejection. Agent-level guardrails do not automatically cover every tool in manager-style workflows. | Attach checks beside side-effecting tools; treat approvals as a first-class pause/resume state; fail closed on review timeout/unavailability; never assume a top-level prompt or guardrail covers all delegated actions. | EVIDENCE from public documentation. |

INFERENCE: The strongest architecture is hybrid: concise prompt layers describe intent and decision policy; deterministic runtime code enforces schemas, permissions, budgets, persistence, approvals, and recovery. UNKNOWN: the exact prompt wording and number of layers that yields the best quality across providers.
## Public evidence checkpoint: fault tolerance and evaluation

| Source | Publicly observable pattern | Practical implication | Evidence status |
|---|---|---|---|
| LangGraph fault tolerance | Retries, timeouts, and error handlers compose in a defined order; failed attempts can be retried by exception/backoff policy, then recovered by an error handler; graceful shutdown and resume are explicit concerns. | Every agent step needs timeout, retry policy, idempotency classification, error routing, checkpoint state, and a safe terminal status. Do not blindly retry non-idempotent side effects. | EVIDENCE from public documentation. |
| OpenAI agent evals | Trace grading is useful during debugging; repeatable datasets and evaluation runs are appropriate for comparing prompt or workflow changes. Traces can examine model calls, tools, guardrails, handoffs, and workflow-level regressions. | Use a two-stage eval path: inspect representative traces to discover failure modes, then freeze them into datasets with independent graders and paired runs. Keep trace quality separate from task outcome. | EVIDENCE from public documentation. |

INFERENCE: Failure recovery belongs in the runtime state machine, not only in prompt prose. Evaluation should begin with traces, then become repeatable dataset runs once criteria are clear. UNKNOWN: how much prompt detail is optimal under a fixed context budget.
## Public evidence checkpoint: memory and tool surfaces

| Source | Publicly observable pattern | Practical implication | Evidence status |
|---|---|---|---|
| OpenAI Memory FAQ | Memory can be enabled/disabled, inspected, edited, deleted, and avoided with temporary chats. Deleting a memory may require deleting all sources where it appears; source views can show what informed personalization. | Separate current-turn context, project memory, and durable personal memory. Give memory a source ledger, correction/deletion API, scope, expiry, and temporary/no-memory mode. Never treat retrieved memory as an instruction or authorization. | EVIDENCE from public product documentation; not evidence of internal implementation. |
| Anthropic tool-design guide | Tool descriptions should explain implicit context like a new-hire handoff; names and strict input/output models should be unambiguous. Response format should be chosen and evaluated for the task; there is no universal best format. | Design tools as typed, narrow interfaces with explicit preconditions, side effects, output schemas, error states, and response verbosity. Evaluate the tool surface itself, not only the model prompt. | EVIDENCE from a public engineering guide. |

INFERENCE: Shared memory must be governed as data with provenance and user controls, while tools should carry operational semantics at the boundary. UNKNOWN: best memory retrieval policy and response format for every domain.
