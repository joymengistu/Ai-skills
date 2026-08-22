# User contribution adapter: CLAI

Source repository: [joymengistu/CLAI](https://github.com/joymengistu/CLAI)

This adapter preserves the strongest ideas from the user's CLAI project while translating them into model-agnostic skills:

| CLAI pattern | Ai skills interpretation |
|---|---|
| Persistent `facts` and structured `special` keys | Scoped, inspectable memory with provenance and deletion. |
| Project architect scan with exclusions and text allowlist | Curated context acquisition that inspects structure before reading content. |
| `[READ:filename]` | Explicit context request; must respect path boundaries and data-as-untrusted rules. |
| `[WRITE:filename]...[/WRITE]` | Proposal state followed by approval, execution, verification, and rollback. |
| Shell command approval | Consequential-tool confirmation and least privilege. |
| Menus and file selection | Human checkpoints and guided choice that preserve user control. |
| History export and auto-compaction | Context lifecycle management and loss-aware summaries. |
| Creative “singularity” mode | Optional creative-work route, bounded by coherence, user intent, and safety. |

Legacy tags are transport syntax, not authorization. A host implementation should wrap them in the action protocol defined in `core/action-protocol.md`.
