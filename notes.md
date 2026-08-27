# Notes: Forensic Audit of Research Paper

## Scope

Audit target: `/home/nixon/RESEARCH CYBER`.

The user-provided master prompt requires an exhaustive source-level audit and these deliverables:

- `FORENSIC_AUDIT_FINAL.md`
- `CLAIM_EVIDENCE_MATRIX.csv`
- `REFERENCE_INVENTORY.csv`
- `NUMERIC_FACT_AUDIT.csv`
- `CONTRADICTION_MATRIX.md`
- final fix summary

## Baseline findings

- Working tree was clean before the audit; only the audit planning files are new.
- `main.tex` cites 50 unique keys across 131 citation commands; all 50 keys are present in `refs.bib`, and every BibTeX entry is cited.
- `references/source-map.csv` has 49 rows and disagrees with the active citation registry: `cybergym2026` and `darpa2023aixcc` are missing, while stale key `cybergym2025` remains.
- `references/manifest.csv` has the same key-layer drift and also points one NVD record at a stale `NOTFETCHED` text filename.
- Canonical corpus counts agree at 36 across `corpus/included/`, `references/record-id-map.csv`, the autonomy assignment CSV, and active Tables II/IV; this does not make the 49-entry source layer equivalent to the 36-record corpus.
- `r3survey2026` is dated 1 July 2026 but is marked `in-window` in the canonical YAML and assignment CSV, while the manuscript marks it `OUT`; protocol metadata must be normalized to `out-of-window`.
- `refs.bib` has a high-confidence author error for `r2slr2024` (source: Enna Basic and Alberto Giaretta) and a missing Jing Liu in `rissebohme-wrongexam2024`.
- Active manuscript issues requiring correction include the GTG-1002 “unresolved ... resolved” contradiction, the 23-versus-24 repository discrepancy in AIxCC accounts, the mathematically incorrect Team Atlanta 44.44% complement calculation if presented as an independent calculation, and ambiguous sensitivity-table relaxation logic.
- Active figure sources contain a stale context-count comment and timeline labels that use continuous-looking `..` ranges for discrete events.
- `scripts/verify_final.py` and `scripts/scripts_audit_final.py` contain stale/hard-coded release assumptions (17 pages; an archived PDF target); these will be audited and updated after the manuscript changes.
- `RELEASE_MANIFEST.md` is historical and does not describe the current 50-entry, 18-page build at the baseline commit.

## Evidence-handling notes

- The current CyberGym PDF is `cybergym-2025.pdf` but identifies itself as arXiv v3/ICLR 2026; the filename and source-map key are stale, not the BibTeX key.
- `references/txt/artemis-vs-professionals-2025.txt` contains NUL extraction artifacts and must be searched after NUL removal.
- `references/txt/anthropic-gtg1002-report-full.txt` is a stale 22-byte “Not Found” artifact and is not the mapped evidence file.
- Clean rebuild completed 2026-08-27 with `pdflatex → bibtex → pdflatex → pdflatex`; final PDF is 18 pages, BibTeX parsing errors are 0, citation/record-set checks pass, and the strengthened audit script passes.
- Rendered representative pages 1, 4, 12, 15, 16, 17, and 18. No visible clipping, overlap, or figure overflow was observed. The LaTeX log retains two overfull-vbox warnings and several underfull-hbox warnings, which are reported as nonfatal layout warnings.
- Final source-layer reconciliation is 50 BibTeX keys = 50 source-map rows = 50 manifest rows; canonical record layer remains 36 YAML/CSV/Table II/Table IV records. R4 and R6 remain explicitly metadata-only/paywalled limitations.

## Audit Evidence Log

Findings will be added here during inventory and verification. This file is working memory and is not itself the final audit report.
- Local primary PDFs/extracted text remain the evidence source for claims where the repository has them; web verification was used for current arXiv/DARPA/participant metadata where appropriate.
