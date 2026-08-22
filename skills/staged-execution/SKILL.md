---
name: staged-execution
description: Execute complex builds in fast, observable stages with a vertical slice, bounded parallel work, integration checkpoints, budgets, and explicit release gates. Use for long-horizon coding, game creation, product development, or multi-agent implementation.
---

# Staged execution

Run the work as waves: brief compilation, architecture, vertical slice, independent feature increments, integration, dynamic verification, repair, and release. Each stage has an entry condition, output, verifier, budget, and stop condition.

Build one thin end-to-end path first. Parallelize only independent, side-effect-free work such as research, asset preparation, test authoring, or isolated modules. Assign one integration owner for shared state and fragile files. Every handoff includes assumptions, artifacts, evidence, failures, and unresolved decisions.

At each checkpoint compare the running artifact to the requirement ledger and capability map. If the vertical slice fails, repair it before adding breadth. If a stage exceeds its budget or reveals an architecture mismatch, pause, re-plan, and preserve the current working state.

Make progress visible without flooding the user. Report what is usable now, what is being built, what is unverified, and what decision or approval is required.
