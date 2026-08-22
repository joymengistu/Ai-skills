---
name: planning
description: Create practical plans with decomposition, checkpoints, stopping conditions, dependencies, risk classes, and verification. Use for complex, multi-step, or tool-using work.
---

# Planning

Plan for progress, not ceremony. Start with the final artifact and verifier, then work backward to the smallest sequence of steps that can produce them.

Each step should state its purpose, input, output, owner, dependency, risk, expected evidence, and rollback. Put inspection before mutation, reversible actions before irreversible ones, and cheap validation before expensive execution. Add a human checkpoint when a reasonable user could be surprised, harmed, charged, exposed, or committed by the next step.

Stop when the definition of done is satisfied or when further work has lower expected value than asking the user for clarification. Update the plan when facts change; do not silently continue on stale assumptions.
