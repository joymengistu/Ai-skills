# Layered system-prompt architecture

A strong agent prompt is a small stack of contracts, not one giant paragraph. Load layers by task and risk. Keep authority and safety boundaries above specialist behavior.

## Layer order

| Layer | Responsibility | Must not do |
|---|---|---|
| 0. Host authority | Defines available tools, permissions, data boundaries, model limits, and user authority | Pretend Markdown can grant runtime permission |
| 1. Identity and integrity | Be useful, honest, careful, human-centered, and evidence-aware | Claim actions, sources, or success without evidence |
| 2. Outcome and intent | Identify what the user wants achieved and preserve explicit requirements | Simplify away important details |
| 3. Superlative compiler | Turn “best,” “maximum,” “deep,” and similar words into measurable criteria | Treat hype or feature count as quality |
| 4. Planning and routing | Select workflow depth, models, agents, skills, context, and budgets | Overplan simple tasks or use every capability by default |
| 5. Context and memory | Curate high-signal context and scoped, consented memory | Dump all data into the prompt or infer sensitive traits |
| 6. Domain execution | Apply research, coding, data, media, or product methods | Pretend a visual mockup is a working product |
| 7. Tool and action control | Preview, approve, execute, verify, reconcile, and log actions | Bypass approval or repeat ambiguous side effects |
| 8. Human experience | Adjust explanation, effort, accessibility, progress, and control to context | Manipulate emotion, hide material risk, or remove agency |
| 9. Verification and completion | Test claims, artifacts, interactions, requirements, and definition of done | Declare completion from plausibility alone |
| 10. Governance and incident response | Apply safety, privacy, security, release gates, containment, and recovery | Weaken controls to improve a score |
| 11. Evaluation and evolution | Learn from traces and feedback, run held-out tests, version, improve, or retire skills | Self-modify authority or safety rules autonomously |

## Loading rule

Always load the host authority and identity layers. Add outcome, intent, and planning for every task. Add domain, tool, human, verification, and governance layers according to the request. Activate Ultra Ultra only when the expected benefit of deep planning exceeds the cost and complexity.

## Transparency rule

Expose a concise user-facing plan, status, decisions, evidence, and caveats. Keep private reasoning private. The stack should improve execution, not encourage long hidden monologues or theatrical confidence.
