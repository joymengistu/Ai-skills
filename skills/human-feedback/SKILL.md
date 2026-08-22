---
name: human-feedback
description: Collect, interpret, and apply user corrections, preferences, and satisfaction feedback without overfitting, manipulation, or unwanted profiling. Use when improving an AI agent from real interactions or when a user reports that an outcome was wrong or hard to use.
---

# Human feedback

Treat feedback as evidence about a specific interaction, not automatic permission to rewrite the agent. First classify whether the issue was outcome quality, factuality, clarity, effort, trust, control, progress, personalization, completion, or safety.

Ask what the user wants changed now and whether the preference should persist. Separate one-off correction, project-scoped preference, and durable preference. Store only what is useful, consented, scoped, inspectable, and deletable. Do not infer sensitive traits or emotional profiles from a single interaction.

Record the feedback, affected behavior, hypothesis, proposed change, expected benefit, possible regressions, evaluation cases, and rollback. Test the change on representative and held-out cases. Never optimize for positive ratings by hiding uncertainty, reducing user control, or making the agent emotionally dependent.

At delivery, confirm what changed and how the user can correct or forget it. Treat explicit dissatisfaction as a valuable signal, not a failure to conceal.
