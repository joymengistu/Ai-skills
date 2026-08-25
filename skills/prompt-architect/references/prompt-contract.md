# Prompt Contract

## Minimum useful structure

| Field | Include when | Guidance |
|---|---|---|
| Operating stance | A specialized behavior changes the task. | State a useful role, not a fictional identity. |
| Outcome | Always. | Describe an observable artifact, decision, or state. |
| Inputs | Source material or context matters. | Separate authoritative user input from assumptions and examples. |
| Requirements | Explicit needs exist. | Preserve them as checkable statements; state non-goals when scope needs protection. |
| Constraints | Cost, time, safety, privacy, tools, format, or quality are material. | Do not imply permissions or capabilities that do not exist. |
| Process | A critical order, evidence rule, or failure path matters. | Specify checkpoints, not private reasoning. |
| Output contract | Always. | Request a precise response, file, table, schema, or action plan. |
| Verification | Claims need evidence. | Match evidence to the claim; label unverified work honestly. |

## Compact pattern

```text
Goal: [observable outcome]
Context: [only relevant facts/source material]
Requirements: [non-negotiable items]
Constraints: [scope, authority, format, budget]
Return: [deliverable structure]
If blocked: [state what is missing, preserve work, propose the next safe action]
```

## Reusable pattern

```text
You are helping with [narrow operating stance].

Outcome
Produce [artifact/decision/state] for [audience/context].

Inputs
- Authoritative inputs: [sources/user facts]
- Assumptions: [labeled defaults]
- Unknowns: [only material gaps]

Requirements and boundaries
- Must: [checkable needs]
- Must not: [non-goals/prohibited behavior]
- Authority and tools: [what may and may not be assumed]

Method
1. [critical step or evidence checkpoint]
2. [critical step or failure handling]

Return
[exact format/schema]

Quality and honesty
Link claims to evidence where available. Label verified, partial, blocked, deferred, and unknown items. Do not claim actions, access, or outcomes that were not observed.
```

## Anti-patterns

Avoid prompts that restate the same goal as role, objective, instruction, and reminder; demand unavailable tools; require “perfect” without a definition; hide material ambiguity; mix incompatible output formats; or give a checklist that has no success condition.
