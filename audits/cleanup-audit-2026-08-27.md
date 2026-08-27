# Repository Cleanup Audit — 2026-08-27

Date: 2026-08-27  
Git baseline: `master` at `4fe7498f68ef17f70a1b5af6b16267322b005470`
Scope: build dependencies, submission materials, evidence/reproducibility artifacts, historical files, generated files, and unrelated nested repositories.

## Executive result

The active manuscript is `main.tex` and the active compiled paper is `main.pdf`. A minimal copy containing only `main.tex`, `refs.bib`, `IEEEtran.cls`, `IEEEtran.bst`, and the three active figure `.tex` files rebuilt successfully as an 18-page PDF with no fatal errors. The repository verification scripts also pass:

- `python3 scripts/verify_final.py`: all checks pass
- `python3 scripts/scripts_audit_final.py`: all gates pass

The cleanup is complete. A separate `submission/` folder now contains the rebuildable PDF package, while the parent retains the active research evidence and current audit record.

## Cleanup executed

Removed:

- generated LaTeX intermediates: `main.aux`, `main.bbl`, `main.blg`, `main.log`
- superseded output: `sok-coevolution.pdf`
- duplicate/invalid/unreferenced reference artifacts listed in the high-confidence section
- stale bundle: `sok-coevolution-release-bundle.tar.gz`
- obsolete checksum manifests: `docs/MANIFEST.sha256` and `docs/SHA256SUMS.manifest`
- empty placeholder directories: `build/`, `review/`, and `references/quarantine/`
- superseded top-level audits: `AUDIT_PLAN.md`, `CITATION_AUDIT_REPORT.md`,
  `CLAIM_LEDGER.md`, `FORENSIC_AUDIT_REPORT.md`, `CORRECTED_AUDIT_REPORT.md`, and `notes.md`
- superseded/legacy `docs/` records: `CP1-report.md`, `CVE-REDACTION-MAP.md`,
  `reference-audit.md`, `audit-final-transcript.txt`, `autonomy-loop-assignments.csv`,
  `claim-verification.csv`, `corpus-summary.csv`, `corpus.csv`, and `prisma-counts.csv`

The active `main.tex`, `refs.bib`, local LaTeX style files, figure sources, `main.pdf`, evidence, corpus, reference maps, current audit files, and unrelated `CLEANROOM_AUDIT_*`/`CURRENT_HEAD_*` files were preserved.

Post-clean verification passed before final packaging: `python3 scripts/scripts_audit_final.py` reported all gates pass; the isolated `submission/` package rebuilt to an 18-page PDF with no fatal or undefined-reference diagnostics. `RELEASE_MANIFEST.md` records the package and current reference-directory counts.

## Files required to build the PDF

Keep these files in the project if the PDF must remain rebuildable:

- `main.tex`
- `refs.bib`
- `IEEEtran.cls`
- `IEEEtran.bst`
- `figures/prisma-flow.tex`
- `figures/autonomy-loop-map.tex`
- `figures/timeline-f3.tex`

`main.tex` directly inputs only the three figure files and the `refs.bib` bibliography. The local PDF/TXT sources, YAML corpus, CSV evidence, Markdown audits, and Python scripts are not read by LaTeX during compilation.

## CSV and Markdown disposition

No CSV or Markdown file is required to compile `main.pdf`. The current files kept in the parent repository are retained for one of three reasons:

- **Authoritative evidence/provenance:** `evidence/autonomy-loop-assignments.csv`,
  `references/manifest.csv`, `references/source-map.csv`,
  `references/record-id-map.csv`, `corpus/included/`, and the evidence notes.
- **Current audit/release record:** `CLAIM_EVIDENCE_MATRIX.csv`,
  `REFERENCE_INVENTORY.csv`, `NUMERIC_FACT_AUDIT.csv`, all four `CURRENT_HEAD_*.csv`
  files, `FORENSIC_AUDIT_FINAL.md`, `FINAL_FIX_SUMMARY.md`,
  `CONTRADICTION_MATRIX.md`, the dated `audits/` reports, and the clean-room notes.
- **Submission or research provenance:** `ai-use-disclosure.md`,
  `venue-fit-cover-letter.md`, `docs/CP1-final.md`, `docs/research-protocol.md`,
  `docs/search-log.md`, `docs/CHANGES.md`, `docs/framework-changelog.md`,
  `docs/outline.md`, `docs/skill-routing.md`, `docs/venue-compliance.md`,
  `corpus/saturation-rationale.md`, and the reference-access notes.

The deleted CSVs were legacy aggregates or a 26-record snapshot; they were replaced by the 36-record canonical corpus and current audit matrices. The deleted Markdown was superseded, explicitly reversed, or stale. Git retains the deleted tracked files in repository history.

## Clean submission folder

`submission/` contains `main.tex`, `refs.bib`, `IEEEtran.cls`, `IEEEtran.bst`, the three active figure sources, the current compiled `main.pdf`, `README.md`, and the two submission-support Markdown files. It is independent of the parent CSV/evidence tree and can be copied as a PDF-only/rebuildable submission package.

Keep `main.pdf` as the current submission PDF. `ai-use-disclosure.md` and `venue-fit-cover-letter.md` are submission-support documents and should be retained if they are still needed for the venue workflow.

## High-confidence cleanup candidates (executed)

These were not required by the active build and had clear evidence of being generated, duplicated, invalid, stale, or unrelated. They were deleted after the normal version-control check:

### Generated LaTeX intermediates

- `main.aux`
- `main.bbl`
- `main.blg`
- `main.log`

They are regenerated by the documented `pdflatex → bibtex → pdflatex → pdflatex` sequence. `scripts/verify_final.py` also rebuilds when `main.aux` is absent. The `.gitignore` already excludes them.

### Superseded or duplicate paper outputs

- `sok-coevolution.pdf` — older 18-page PDF; the current deliverable is `main.pdf`.
- `references/pdf/fang-one-day-2024.pdf` — byte-identical to `references/pdf/fang-agents-exploit-one-day-2024.pdf`.
- `references/txt/fang-one-day-2024.txt` — byte-identical to `references/txt/fang-agents-exploit-one-day-2024.txt`.
- `references/txt/anthropic-gtg1002-report-full.txt` — a 22-byte `Not Found \\ Anthropic` artifact and not the mapped evidence extract.

### Unreferenced source leftovers

These files are not in the active bibliography, source map, manifest paths, or canonical corpus:

- `references/pdf/bugdar-2025.pdf`
- `references/txt/bugdar-2025.txt`
- `references/pdf/zhu-zero-day-2025.pdf`
- `references/txt/zhu-zero-day-2025.txt`

Delete them for a submission-only tree. Move them to a separate research archive instead if the literature search history matters.

### Stale release material

- `sok-coevolution-release-bundle.tar.gz` — 44.8 MB, created before the active final build. Its embedded `main.tex`, `refs.bib`, `main.pdf`, figure files, and evidence CSV have hashes different from the current files; it also contains the unrelated nested repositories and an older `sections_archive/` layout. It is not a current submission bundle.
- `docs/MANIFEST.sha256`
- `docs/SHA256SUMS.manifest`

The two `docs/` checksum manifests describe the old bundle, not the current `RELEASE_MANIFEST.md` state. Delete or move all three together only after confirming that no historical release snapshot is needed.

### Unrelated nested repositories

- `academic-research-skills/` — 28 MB, separate Git repository, explicitly marked in `.gitignore` as not part of the paper.
- `claude-code/` — 42 MB, separate Git repository, explicitly marked in `.gitignore` as not part of the paper.

These should preferably be moved outside this project rather than destroyed, because each has its own Git history and working-tree state.

## Historical Markdown removed from the active tree

The following files were useful only for audit/history and were removed from the active tree:

- `AUDIT_PLAN.md`
- `FORENSIC_AUDIT_REPORT.md` — superseded by the corrected/final reports
- `CORRECTED_AUDIT_REPORT.md` — superseded by `FORENSIC_AUDIT_FINAL.md`
- `CITATION_AUDIT_REPORT.md` — older 49-entry report; the current registry has 50 entries
- `CLAIM_LEDGER.md` — earlier incomplete ledger; the current claim matrix is `CLAIM_EVIDENCE_MATRIX.csv`
- `docs/CP1-report.md` — explicitly superseded by `docs/CP1-final.md`
- `docs/reference-audit.md` — older 38-entry audit
- `docs/CVE-REDACTION-MAP.md` — explicitly marked superseded/reversed
- `docs/audit-final-transcript.txt` — old build transcript
- `notes.md` — working notes, not a build or submission dependency

Keep one compact current audit set if you want an auditable project record:
`FORENSIC_AUDIT_FINAL.md`, `FINAL_FIX_SUMMARY.md`, `CONTRADICTION_MATRIX.md`, `RELEASE_MANIFEST.md`, and `audits/2026-08-27-forensic-audit.md`.

## Keep or archive, depending on the submission target

These files are not needed to compile `main.pdf`, but they preserve the evidence and provenance behind the paper. They should remain if the submission includes an artifact/reproducibility package:

- `evidence/`
- `corpus/included/`
- `corpus/excluded/` — selection-history only, optional for the final artifact
- `corpus/saturation-rationale.md`
- `references/record-id-map.csv`
- `references/source-map.csv`
- `references/manifest.csv`
- `references/pdf/`
- `references/txt/`
- `CLAIM_EVIDENCE_MATRIX.csv`
- `REFERENCE_INVENTORY.csv`
- `NUMERIC_FACT_AUDIT.csv`
- `A3_SENSITIVITY_ANALYSIS.md`
- `CITATION_VERIFICATION_S1_S3.md`
- `CLAIM_VERIFICATION_S4_S9.md`
- `E1_E2_JUSTIFICATION.md`
- `I3_CALIBRATION.md`
- `TABLE_FIGURE_RECONCILIATION.md`
- `docs/research-protocol.md`, `docs/search-log.md`, `docs/outline.md`, `docs/framework-changelog.md`, and `docs/CHANGES.md`
- `references/convert-failures.md` and `references/paywalled.md`
- `scripts/verify_final.py` and `scripts/scripts_audit_final.py`

If only the conference PDF is being uploaded, these can be stored outside the paper folder rather than deleted.

## Empty directories

These directories currently contain no files and can be removed if they are not placeholders for future work:

- `build/`
- `review/`
- `references/quarantine/misidentified/`

## Recommended cleanup order

1. Preserve or commit the current state.
2. Move the two nested repositories out of this project.
3. Remove the stale bundle and old checksum manifests.
4. Remove generated LaTeX intermediates and the duplicate/invalid reference files.
5. Archive historical audit Markdown separately; retain the compact current audit set if provenance matters.
6. Rebuild with the documented four-command sequence and rerun both verification scripts.

The current `RELEASE_MANIFEST.md` has been updated so it no longer claims the deleted historical files are part of the release.
