# Master mission implementation map

This map keeps the large mission bounded. It distinguishes existing coverage from genuinely new work and avoids creating skills merely to increase the catalog count.

| Mission block | Existing coverage | New or strengthened asset | Status |
|---|---|---|---|
| Repository audit | Manifest, validator, capability analysis, repository comparison | `references/intelligence-infrastructure-audit.md` and preserved source missions | Complete at reference scope |
| Formal skill specification | Skill contract schema and example | Enriched examples, limitations, uncertainty, lessons, version history | Complete |
| Example-driven intelligence | Skill contracts, evaluation cases, UI and Lovability examples | Contract-level example taxonomy | Complete |
| Contextual reasoning | Intent preservation, context engineering, contextual-user-intelligence | Typed predictions and ambiguity policy | Complete |
| Knowledge boundaries | Evidence ledger, capability analysis, research notes | `runtime/intelligence/research-memory.schema.json` with FACT/EVIDENCE/INFERENCE/HYPOTHESIS/UNKNOWN plus outdated/conflicting states | Complete at reference scope |
| Research memory | Evidence ledger and cited research references | `research-memory.schema.json` and representative JSONL record | Complete at reference scope |
| Self-improvement memory | Capability-gap response, skill forging, human feedback | `lesson-memory.schema.json` and representative failure lesson | Complete at reference scope |
| Learning loop | Evaluation, repair loop, dynamic verification | `runtime/intelligence/kernel.py` paired decision plus lesson/improvement records | Complete at reference scope |
| Skill improvement engine | Skill forging, capability-gap response | `improvement-record.schema.json`, smallest-change rule, paired comparison, hard gates, and one focused meta-capability Skill | Complete at reference scope |
| Example generation | Skill contract examples and eval cases | `example-record.schema.json`, five-kind coverage checker, and representative records | Complete at reference scope |
| Capability gap detection | Capability discovery and gap response | Minimal-bundle and non-self-authorizing promotion | Covered |
| Composition | Skill composition and typed contract | Compatibility, order, permissions, evidence flow | Covered |
| Critic system | Evaluator-critic and dynamic verification | Independent critique and repair | Covered |
| Benchmarking | Evaluation suite and comparative plan | `intelligence-benchmark.json`, `benchmark-run.schema.json`, and deterministic runner | Complete at reference scope |
| Professional UI Taste | UI Vision and professional-taste | Contextual taste model and screenshot limits | Complete |
| UI Screenshot Critic | Evaluator-critic, UI Vision, professional-taste | Separate screenshot-visible and live-only checks | Covered |
| Pixel Perfect UI | UI Vision and design-reference library | Not treated as universal target; use measured intent and accessibility | Deliberately bounded |
| Brainstorm Mode | Brainstorm Mode and Lovability | Preserve branches, label speculation, crystallize by invitation | Covered |
| Lovability | Lovability and benchmark plan | Communication learning and multidimensional evaluation | Complete |
| Human satisfaction | Human satisfaction and Lovability benchmark | Outcome, effort, clarity, trust, control, frustration | Covered |
| Meta-learning | Skill forging, capability analysis | Cross-skill lessons require evidence and authorization | Covered |
| Frontier comparison | Fable report, repository comparison, benchmark plan | Model/harness/tools/memory distinction | Complete at public-evidence boundary |
| Self-critique | Evaluator-critic, evidence ledger, quality gates | Audit, architecture, and public research records with explicit unknowns and stopping rules | Complete at reference scope |
| Quality gate | Capability-risk matrix, validator, runtime host | Hard safety/privacy/control/recovery gates | Covered |
| Final architecture | Core prompt, runtime host, references | Layered capability engine | Covered |
| Implementation roadmap | Existing roadmap references | This staged map and completed block checkpoints | Complete |

## Guiding decision

The architectural leap is **not a larger prompt collection**. It is a governed capability engine that can represent skill contracts, compose the smallest sufficient bundle, reason with separated context, verify outputs independently, record evidence and lessons, and propose—but not self-authorize—future changes.

## Remaining high-value gaps

The largest unimplemented capabilities remain production-grade provider adapters, OS-level sandbox and network enforcement, real identity and secret lifecycle, durable memory quarantine services, live monitoring, human blind studies, and benchmark execution against real matched models. The reference kernel now validates records and comparison rules, but it does not produce model-quality measurements by itself. These require infrastructure and real usage; they should not be faked as Markdown completion.
