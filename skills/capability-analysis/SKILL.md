---
name: capability-analysis
description: Analyze an agent capability by separating model contribution, harness contribution, tool contribution, state and memory contribution, and unknown or unsupported claims. Use for vendor comparisons, research synthesis, and architecture decisions.
---

# Capability analysis

For each claimed behavior identify the observable result, the model capabilities it may require, the host controls and workflow that may enable it, the tools and data it depends on, the state or memory it needs, and plausible alternative explanations. Label evidence as `confirmed`, `supported`, `inferred`, `speculative`, `unsupported`, or `unknown`.

Do not turn a vendor claim into a universal fact. Distinguish a public product description, a controlled benchmark, an anecdotal demonstration, and a reproducible result. Record source, date, task distribution, missing variables, and confidence. Do not seek or reproduce leaked, private, or hidden prompts or reasoning.

Translate findings into portable contracts: what any capable hosted model can attempt, what the runtime must enforce, what tools must provide, what evaluators must measure, and what remains dependent on model quality. Recommend experiments that isolate one factor at a time and report cost, latency, safety, user effort, and verified outcome quality.
