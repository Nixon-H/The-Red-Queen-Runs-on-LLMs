# Task Plan: Extreme Forensic Audit of Research Paper

## Goal
Audit the current repository state, verify citations, sources, claims, numbers, dates, taxonomy, tables, figures, and final PDF, then produce the requested audit artifacts and apply only evidence-backed corrections.

## Phases
- [x] Phase 1: Establish target state and inventory repository artifacts
- [x] Phase 2: Build citation, reference, claim, numeric, and artifact inventories
- [x] Phase 3: Verify evidence, metadata, internal logic, tables, figures, and rendered PDF
- [x] Phase 4: Record complete issue inventory and apply justified fixes
- [x] Phase 5: Rebuild from a clean LaTeX state and run targeted re-audit
- [x] Phase 6: Finalize deliverables and report unresolved items

## Key Questions
1. What exact commit and working-tree state are being audited?
2. Do all used citations resolve to correct, locally reproducible primary or authoritative sources?
3. Which manuscript claims, numbers, dates, classifications, tables, figures, and references are unsupported, overstated, contradictory, stale, or malformed?
4. Does the rebuilt final PDF match the audited source and pass the build checks?

## Decisions Made
- The canonical empirical corpus remains `corpus/included/` plus `references/record-id-map.csv`, per repository instructions; source-map role counts are not treated as record counts.
- Findings will be recorded before edits so the original audit state remains traceable.
- No web download will be attempted unless a missing source is identified and network access is needed; local primary artifacts are preferred.

## Errors Encountered
- None yet.

## Status
**All phases complete** - inventories, evidence classifications, fixes, clean rebuild, rendered-PDF inspection, final report, and fix summary are complete.
