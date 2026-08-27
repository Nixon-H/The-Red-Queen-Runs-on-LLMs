# Final Forensic Audit Report

Audit date: 2026-08-27  
Repository: /home/nixon/RESEARCH CYBER  
Baseline: master at 2eacec16192b1d2f33238180c11d805526367a5c  
Final state: audit changes are present in the working tree; no commit was created by this audit.

## Executive verdict

The manuscript is structurally reconciled and reproducibly rebuildable after the audit corrections. The final evidence-backed conclusion is bounded:

> No included evidence met our operational definition of A3.

That statement is limited to the canonical 36-record corpus, the stated temporal scope, the A0–A3 operational rule, and the evidence available in this repository. It is not a universal claim that no A3 system exists.

The principal remaining limitations are explicit rather than hidden:

1. R4 and R6 remain metadata-only/paywalled records for full-text purposes.
2. AIxCC sources report different final denominators: Trail of Bits reports 48 challenges across 23 repositories, while the R7 systematization reports 48 scored projects from 24 OSS-Fuzz repositories. The manuscript preserves both accounts.
3. GTG-1002 remains uncertain under the weakest-missing-condition rule because the incident reporting does not document every autonomy predicate.
4. Team Atlanta’s 44.4% → 0.9044 value is retained as source-reported; the displayed complement formula independently evaluates to approximately 0.9047.

## Scope and method

The audit covered:

- main.tex, refs.bib, active figure TeX, and the compiled main.pdf;
- the 36 canonical YAML records and references/record-id-map.csv;
- evidence/autonomy-loop-assignments.csv;
- references/source-map.csv and references/manifest.csv;
- local PDFs and extracted texts, with the original PDFs preferred when extraction artifacts could affect classification;
- build scripts and RELEASE_MANIFEST.md;
- citation support, numerical precision, qualifiers, dates, environments, autonomy levels, loop positions, tables, figures, and contradictions.

The source hierarchy was original PDF/source document, official web page or report, extracted text, then BibTeX metadata. Claims were decomposed and classified as DIRECT, QUALIFIED, INFERRED, PARTIAL, or UNSUPPORTED. No claim was upgraded to DIRECT solely because its wording appeared plausible.

Current metadata and primary-source checks included the current arXiv records for R2 ([2412.15004](https://arxiv.org/abs/2412.15004)), R3 ([2607.02605](https://arxiv.org/abs/2607.02605)), and R7 ([2602.07666](https://arxiv.org/abs/2602.07666)); official DARPA close-out and scoring pages ([results](https://www.darpa.mil/news/2025/aixcc-results), [scoring](https://www.darpa.mil/news/2025/ai-cyber-challenge-scoring), and [program announcement](https://www.darpa.mil/news/2023/ai-cyber-challenge-opens)); and Team Atlanta’s [AFC retrospective](https://team-atlanta.github.io/blog/post-afc/). R3 was correctly identified as submitted 2026-07-01 and is therefore out of the 2026-06-30 inclusion window.

## Inventory and reconciliation

| Layer | Final count | Result |
|---|---:|---|
| BibTeX keys | 50 | all cited; 0 uncited; 0 missing |
| source-map rows | 50 | exact key parity with BibTeX |
| manifest rows | 50 | exact bib_key parity with BibTeX |
| canonical YAML records | 36 | authoritative empirical corpus |
| record-ID map entries | 36 | exact canonical mapping |
| autonomy assignment rows | 36 | exact canonical record set |
| Table II records | 36 | exact canonical record set |
| Table IV records | 36 | exact canonical record set |
| active PDF | 18 pages | rebuilt and visually inspected |

The source-layer counts are intentionally not treated as corpus-record counts. The source map roles are 45 included_record, 3 background_anchor, and 2 loop_transition. The canonical empirical layer remains 36 records.

## Claim-level results

CLAIM_EVIDENCE_MATRIX.csv contains 76 audited claim rows:

| Support class | Count |
|---|---:|
| DIRECT | 39 |
| QUALIFIED | 33 |
| INFERRED | 3 |
| PARTIAL | 1 |
| UNSUPPORTED | 0 |

The matrix records the source locator, citation keys, support class, qualifier status, verdict, audit note, and priority for claims across the abstract, introduction, methodology, framework, discovery, AIxCC, patching, co-evolution, validity, threats, and sensitivity appendix.

Important support controls now visible in the manuscript include:

- vendor- and participant-reported figures remain attributed rather than relabeled as independent observations;
- source qualifiers and environment distinctions are retained;
- R3 is discussed as an out-of-window comparator;
- the DARPA numerator and denominator are separated;
- the GTG estimate remains a qualified vendor assessment;
- the AIxCC 23-versus-24 repository discrepancy is not silently merged;
- the A3 negative is bounded to the operational definition and corpus.

## Numerical audit

NUMERIC_FACT_AUDIT.csv contains 52 rows:

| Verdict | Count |
|---|---:|
| DIRECT | 30 |
| QUALIFIED | 21 |
| PARTIAL | 1 |
| UNSUPPORTED | 0 |

The one PARTIAL numerical issue is the Team Atlanta 44.4% → 0.9044 score modifier. The report preserves the source value and separately records the independently recomputed 0.9047 result. Other corrections include:

- 36 canonical records versus 50 source-layer entries;
- 14 in-window autonomy-assessed records;
- 1,507 vulnerabilities across 188 projects for CyberGym;
- 42 AIxCC entrants and 7 finalists;
- 54 unique synthetic vulnerabilities across 63 final challenges;
- 43 synthetic patches and 11 real-vulnerability patches;
- DARPA’s 70-to-63 administrative correction;
- distinct $29.5M cumulative commitment, $8.5M final pool, and $30.5M retrospective distribution scopes;
- explicit preservation of approximate or vendor-reported denominators.

## Contradiction and issue status

CONTRADICTION_MATRIX.md records 22 issues:

- 20 resolved;
- 1 scoped as an intentional layer distinction;
- 1 deliberately open source discrepancy: the AIxCC 23-versus-24 repository denominator.

The contradiction matrix also records the prior stale release assumptions, malformed metadata, stale key names, R3 date mismatch, R4 year mismatch, source-path drift, A3 sensitivity logic, figure-label ambiguity, and script defects.

## Corrections applied

- Reconciled refs.bib, references/source-map.csv, and references/manifest.csv at 50 keys.
- Repaired R2 author metadata, Risse/Böhme author metadata, R7 author metadata, R3 arXiv subject, R4 year/venue metadata, organizational author protection, and URL/path alignment.
- Normalized R3 to out-of-window in canonical metadata and protocol documentation.
- Cleaned locally evidenced placeholder metadata and repaired malformed CSV/YAML fields.
- Corrected the GTG uncertainty wording and preserved the vendor/hallucination caveat.
- Clarified AIxCC’s 23-versus-24 denominator discrepancy and DARPA’s 54/63 scope.
- Rewrote A3 sensitivity analysis around P, X, V, R, and E predicates with explicit counterfactual qualifier counts.
- Corrected the Team Atlanta formula discussion.
- Corrected figure comments and timeline labels.
- Updated verification scripts to use the active main.pdf, recognize citation variants, validate manifest schema/key parity, check canonical fields, and expect the audited 18-page build.
- Updated RELEASE_MANIFEST.md with the final hashes, counts, baseline commit, and visual-QA status.
- Added the claim, reference, numeric, contradiction, final-report, and fix-summary artifacts.

## Rebuild and QA evidence

Clean rebuild sequence:

    rm -f main.aux main.bbl main.blg main.log main.out main.toc main.lof main.lot
    pdflatex -interaction=nonstopmode main.tex
    bibtex main
    pdflatex -interaction=nonstopmode main.tex
    pdflatex -interaction=nonstopmode main.tex

Final checks:

- python3 scripts/verify_final.py: ALL CHECKS PASS.
- python3 scripts/scripts_audit_final.py: ALL GATES PASS.
- BibTeX parsing errors: 0.
- BibTeX entries skipped: 0.
- Citation keys: 50 cited, 0 uncited, 0 missing.
- CSV, YAML, Table II, and Table IV record sets: all 36 and equal.
- Manifest rows: 50, with no malformed rows.
- PDF: 18 pages, 276,166 bytes, letter size, unencrypted.
- SHA-256 values match RELEASE_MANIFEST.md for main.tex, refs.bib, main.pdf, evidence/autonomy-loop-assignments.csv, and references/manifest.csv.
- Rendered representative pages 1, 4, 12, 15, 16, 17, and 18 were inspected. No visible clipping, overlap, or figure overflow was observed.

The LaTeX log still contains two overfull-vbox warnings and several underfull-hbox warnings, plus nonfatal class/font warnings. These are reported rather than suppressed; the rendered pages did not show corresponding visible clipping or overlap.

## Evidence limitations

- R4: ACM DOI/index metadata was verified, but the full survey remains paywalled and is not locally full-text verified.
- R6: the full TOSEM text remains paywalled; the authors’ open repository supports bibliometric metadata, but full-text-derived nuances remain unverified.
- ARTEMIS: the local PDF/TXT supports the study setup and results, but the press phrasing “90% of pentesters” is not used as a primary claim.
- Vendor, foundation, participant, and competition reports are identified as such in the matrices and manifest.
- A stale 22-byte Not Found extract for an unmapped Anthropic filename remains outside the evidence map; the mapped summary and report extracts are used instead.
- The ARTEMIS extracted text contains NUL artifacts; relevant searches were performed after removing NUL bytes.

## Deliverables

- [FORENSIC_AUDIT_FINAL.md](</home/nixon/RESEARCH CYBER/FORENSIC_AUDIT_FINAL.md>)
- [FINAL_FIX_SUMMARY.md](</home/nixon/RESEARCH CYBER/FINAL_FIX_SUMMARY.md>)
- [CLAIM_EVIDENCE_MATRIX.csv](</home/nixon/RESEARCH CYBER/CLAIM_EVIDENCE_MATRIX.csv>)
- [REFERENCE_INVENTORY.csv](</home/nixon/RESEARCH CYBER/REFERENCE_INVENTORY.csv>)
- [NUMERIC_FACT_AUDIT.csv](</home/nixon/RESEARCH CYBER/NUMERIC_FACT_AUDIT.csv>)
- [CONTRADICTION_MATRIX.md](</home/nixon/RESEARCH CYBER/CONTRADICTION_MATRIX.md>)
- [RELEASE_MANIFEST.md](</home/nixon/RESEARCH CYBER/RELEASE_MANIFEST.md>)
- [main.pdf](</home/nixon/RESEARCH CYBER/main.pdf>)
