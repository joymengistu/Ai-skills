# Cross-Modal Consistency Contract

When a task includes more than one modality, treat each modality as evidence with its own coverage, fidelity, and limits. Cross-modal agreement is a claim that must be checked; it is not a default assumption.

## Evidence record

For every material claim, record:

| Field | Meaning |
|---|---|
| Claim | The exact statement or decision supported |
| Modalities | Image, screenshot, text, OCR, audio, transcript, video frame, runtime, or metadata used |
| Locator | Page, frame, timestamp, crop, region, transcript span, DOM state, or source URL |
| Observation | What was directly seen, heard, extracted, or measured |
| Transformation | OCR, transcription, resize, crop, compression, translation, summarization, or other processing |
| Confidence | Confidence after accounting for quality and ambiguity |
| Scope | What the evidence covers and what it does not |
| Cross-check | Independent modality or source that agrees, conflicts, or was unavailable |
| Status | `verified`, `partial`, `unverified`, `deferred`, `blocked`, or `needs_review` |

## Consistency workflow

1. Identify the user decision, modalities, resolution, time range, capture conditions, and privacy constraints.
2. Inspect each modality independently before comparing interpretations. Preserve original locators and do not let an early transcription or vision guess anchor later review.
3. Normalize only documented transformations. Mark unreadable text, missing frames, muted audio, cropped regions, compression artifacts, translation loss, and stale metadata.
4. Compare claims across modalities for identity, content, order, timing, state, quantity, geometry, and provenance. Classify disagreement as true conflict, scope difference, temporal difference, definition difference, transformation artifact, source/version difference, or unresolved.
5. Prefer direct evidence over derived summaries. If modalities conflict, preserve the conflict, lower confidence, and seek the smallest resolving check; never silently choose the most convenient interpretation.
6. For generated or reconstructed artifacts, compare the brief, source media, extracted text, rendered output, and runtime behavior separately. A visual match does not prove semantics or interaction; transcript agreement does not prove visual identity.
7. Report the verified claim, supporting locators, transformations, disagreements, unknowns, and the next resolving check. Feed material failures into the shared repair and completion protocol.

## Modality boundaries

| Evidence | Can support | Cannot prove alone |
|---|---|---|
| Image or screenshot | Visible geometry, color, text if readable, asset presence | Hidden behavior, semantics, unseen states, performance, complete accessibility |
| OCR or transcript | Extracted words within readable, covered regions | Visual hierarchy, speaker intent, exact wording where confidence is low |
| Audio | Audible words, timing, sound events | Visual scene, identity, off-mic content |
| Video frames | Visible state at sampled times | Continuous behavior between frames, full audio meaning |
| Runtime or DOM | Observed behavior and state under tested conditions | Unseen viewport/device paths, universal accessibility, future stability |
| Metadata | Capture conditions, timestamps, dimensions, version clues | Content truth or semantic correctness |

## Conflict and reporting rules

State `observed`, `extracted`, `inferred`, `approximated`, `verified`, and `unknown` separately. If a high-consequence decision depends on an unresolved cross-modal conflict, stop or escalate to `needs_review` or `blocked`. Do not fabricate missing pixels, audio, text, timestamps, or semantic intent. Do not claim cross-modal fidelity, production readiness, or universal correctness from one modality or one successful comparison.
