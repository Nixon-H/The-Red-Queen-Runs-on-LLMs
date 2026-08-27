# Clean-Room Audit Plan — Current Repository State

## Goal

Independently re-audit the exact current repository state at HEAD 80f6ce263b2ef78e14437752d0f54305c41ae9da plus its working-tree changes, without treating the prior forensic report as proof.

## Phases

- [x] Phase 1: Capture exact commit, worktree, and artifact inventory
- [x] Phase 2: Rebuild citation/reference and bibliographic semantic inventories
- [x] Phase 3: Recheck every AIxCC and GTG-1002 occurrence and all numeric facts
- [ ] Phase 4: Reconcile all 36 record-level fields and source-access limitations
- [ ] Phase 5: Clean rebuild, map warnings, render all pages, and inspect PDF text
- [ ] Phase 6: Record findings, apply only necessary fixes, and finalize report

## Rules

- The exact current HEAD and working-tree state are the audit target.
- Earlier audit artifacts are inputs to compare, not authoritative results.
- The canonical record layer is corpus/included plus references/record-id-map.csv.
- Primary PDFs outrank extracted text; official web pages support non-PDF sources.
- Preserve DIRECT, QUALIFIED, INFERRED, PARTIAL, and UNSUPPORTED distinctions.
- Do not silently merge AIxCC denominators or resolve access limitations by inference.

## Status

Phase 4 in progress. The fresh 50-row reference sweep and 80-row AIxCC/GTG occurrence audit are recorded in current-head CSV artifacts. Manifest schema and sparse metadata defects were repaired; the unrelated task_plan.md change remains preserved.
