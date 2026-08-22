---
name: context-engineering
description: Curate, rank, compress, and release high-signal context for LLM reasoning and tool use. Use when prompts, history, files, retrieved sources, tools, or long-running tasks risk overload or confusion.
---

# Context engineering

Treat context as a finite attention budget. Assemble the smallest sufficient set of tokens for the next decision.

Rank context by relevance, authority, freshness, user intent, and decision impact. Prefer summaries plus pointers over raw dumps. Use progressive disclosure: metadata first, focused content next, deep references only when needed. Keep current state, constraints, accepted decisions, evidence, and unresolved questions separate from stale history.

Before adding context, ask what decision it enables. Before retaining context, ask whether it will help later. Compact old history into a loss-aware summary with goals, decisions, facts, evidence, failed attempts, and open risks. Never compress away uncertainty, consent, or safety boundaries.
