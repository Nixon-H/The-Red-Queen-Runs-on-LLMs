# Final Fix Summary

Audit date: 2026-08-27  
Baseline commit: 2eacec16192b1d2f33238180c11d805526367a5c  
Working-tree status: changes are uncommitted; no unrelated files were intentionally changed.

## Outcome

The paper now has a clean evidence boundary and a reproducible audit trail. The bounded A3 conclusion is:

> No included evidence met our operational definition of A3.

The final build is 18 pages and passes both repository verification scripts.

## Fixes by area

### Bibliography and source mapping

- Reconciled all 50 cited BibTeX keys with 50 source-map rows and 50 manifest rows.
- Repaired R2 authors, Risse/Böhme authors, R7’s exact author list, R3’s arXiv subject, and R4’s 2026 ACM metadata.
- Protected group authors and separated personal author names from affiliations.
- Repaired the DARPA 2023 URL.
- Replaced stale cybergym2025 mapping with the normalized cybergym2026 key while preserving the legacy local filename.
- Added darpa2023aixcc as a source-layer background anchor.
- Repaired the NVD path/provenance fields and malformed manifest rows.
- Removed locally evidenced placeholder verification labels from the manifest; paywalled limitations remain explicitly documented for R4/R6.

### Canonical corpus and protocol

- Preserved corpus/included plus references/record-id-map.csv as the authoritative 36-record empirical layer.
- Normalized non-schema unit-type values to system where the record is a system, leaving experiment, source, and scope semantics in their dedicated fields.
- Marked R3 as out-of-window consistently in YAML, the assignment CSV, and protocol documentation.
- Corrected R4 to 2026 throughout the canonical record, assignment, manuscript tables, and manifest.
- Quoted YAML values containing colons and repaired the MCP ecosystem metadata label.
- Retained legitimate factual uses of “pending” in source results; only unresolved audit placeholders were removed.

### Claim and numerical evidence

- Added CLAIM_EVIDENCE_MATRIX.csv with 76 claim-level rows: 39 DIRECT, 33 QUALIFIED, 3 INFERRED, 1 PARTIAL, and 0 UNSUPPORTED.
- Added NUMERIC_FACT_AUDIT.csv with 52 numerical rows: 30 DIRECT, 21 QUALIFIED, 1 PARTIAL, and 0 UNSUPPORTED.
- Corrected the AIxCC wording to distinguish 54 unique synthetic vulnerabilities from 63 final challenges.
- Preserved the 23-repository Trail of Bits account and the 24-repository R7 account as separate source-level denominators.
- Preserved Team Atlanta’s 0.9044 value as source-reported and recorded the independently computed 0.9047 value.
- Separated DARPA’s $29.5M commitment, $8.5M final pool, and $30.5M retrospective distribution scopes.
- Preserved vendor, foundation, competition, and participant qualifiers.

### Autonomy framework and sensitivity analysis

- Clarified that 36 records receive metadata coding while 14 in-window records receive autonomy-axis assessment.
- Replaced contradictory GTG-1002 wording with explicit uncertainty.
- Defined A3 using independent planning/target selection P, execution X, validation V, reporting R, and E2 environment predicates.
- Rewrote the sensitivity appendix with explicit counterfactual scenarios rather than forced zero counts.
- Kept the finding corpus- and definition-bounded rather than universalizing it.

### Figures and build tooling

- Corrected the autonomy-map context comment to distinguish loop-transition and off-axis records.
- Replaced continuous-looking timeline ranges with discrete month labels.
- Updated scripts/verify_final.py for the 18-page build, manifest row validation, and current release state.
- Updated scripts/scripts_audit_final.py to target main.pdf, parse citation variants, verify source-layer parity, validate canonical fields, and enforce the A3 sentinel.
- Updated RELEASE_MANIFEST.md with current counts, hashes, build warnings, baseline commit, and visual-QA status.

## Residual items requiring author attention

- R4 full text remains paywalled; only DOI/index metadata is verified.
- R6 full text remains paywalled; the open author repository supports bibliometric metadata, but full-text nuances remain unverified.
- The 23-versus-24 AIxCC repository denominator difference remains open and should be resolved only if an authoritative reconciliation becomes available.
- The final LaTeX log retains two overfull-vbox and several underfull-hbox warnings. Representative rendered pages show no visible clipping or overlap, but camera-ready authors may choose to improve the layout.
- The manuscript remains an anonymous review copy and still needs final author review.

## Final verification

- python3 scripts/verify_final.py: ALL CHECKS PASS.
- python3 scripts/scripts_audit_final.py: ALL GATES PASS.
- BibTeX: 50 entries, 50 cited, 0 uncited, 0 missing, 0 parse errors.
- Records: 36 YAML = 36 assignment rows = 36 Table II records = 36 Table IV records.
- PDF: 18 pages, 276,166 bytes.
- Visual inspection: representative pages 1, 4, 12, 15, 16, 17, and 18 checked.
- Release hashes: synchronized for main.tex, refs.bib, main.pdf, evidence/autonomy-loop-assignments.csv, and references/manifest.csv.

Related artifacts:

- [FORENSIC_AUDIT_FINAL.md](</home/nixon/RESEARCH CYBER/FORENSIC_AUDIT_FINAL.md>)
- [CLAIM_EVIDENCE_MATRIX.csv](</home/nixon/RESEARCH CYBER/CLAIM_EVIDENCE_MATRIX.csv>)
- [REFERENCE_INVENTORY.csv](</home/nixon/RESEARCH CYBER/REFERENCE_INVENTORY.csv>)
- [NUMERIC_FACT_AUDIT.csv](</home/nixon/RESEARCH CYBER/NUMERIC_FACT_AUDIT.csv>)
- [CONTRADICTION_MATRIX.md](</home/nixon/RESEARCH CYBER/CONTRADICTION_MATRIX.md>)
- [main.pdf](</home/nixon/RESEARCH CYBER/main.pdf>)
