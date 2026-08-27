# Clean-Room Current-State Forensic Audit — 2026-08-27

## Audit target

- Repository: `/home/nixon/RESEARCH CYBER`
- Base HEAD: `80f6ce263b2ef78e14437752d0f54305c41ae9da`
- HEAD title: `Comprehensive forensic audit: 50 files, all verification gates pass`
- Final audit state: base HEAD plus the uncommitted audit documentation recorded in this worktree
- Pre-existing unrelated untracked audit file preserved: `audits/cleanup-audit-2026-08-27.md`
- Scope: bibliography and source inventory, every AIxCC/GTG-1002 occurrence, numeric ledger, all 36 canonical records, source-access boundaries, clean rebuild, warning map, PDF text, and all 18 rendered pages

The earlier audit at `2eacec1` was treated as historical input rather than proof of the current state.

## Inventory

| Artifact | Current result |
|---|---:|
| BibTeX entries | 50 |
| Unique cited keys | 50 |
| Citation commands / key occurrences | 132 / 152 |
| `references/source-map.csv` rows | 50; 6 columns |
| `references/manifest.csv` rows | 50; 21 columns |
| Canonical YAML records | 36 |
| Record-ID map rows | 36 |
| Assignment rows | 36 |
| Reference PDFs / extracted texts | 37 / 49 |
| In-window autonomy-bearing records | 14 |

Source-map roles remain source-layer counts: 45 `included_record`, 3 `background_anchor`, and 2 `loop_transition`. They are not substituted for the 36-record canonical corpus count.

## Findings confirmed against the exact HEAD

1. The manifest repairs are present in the exact HEAD: the R6 row parses at the required 21-field width, and the Risse/Böhme row no longer has malformed CSV quoting.
2. Fourteen late manifest rows are populated from current BibTeX/source-map/local-artifact metadata. The R4 author identity matches the current BibTeX/DOI metadata. R4 and R6 remain explicitly marked metadata-only/paywalled; no full-text claim is promoted from metadata.
3. The MCP record records its intentional dual dating: 2025 arXiv preprint versus accepted DSN 2026 publication year. CyberGym retains its ICLR 2026 identity while documenting the legacy local filename.
4. GTG-1002 discussion and timeline call 80--90% an execution estimate and retain the single-source, unresolved qualification. No GTG-1002 occurrence makes it an established A3 result.
5. The previous numeric ledger contains a stale CyberGym `1,507 vulnerabilities / 188 projects` row. Those figures are absent from the current manuscript, so the current audit records that row as removed from the current claim set rather than treating it as current evidence.

## Bibliographic and source-access audit

The fresh 50-row inventory is in [CURRENT_HEAD_REFERENCE_AUDIT.csv](</home/nixon/RESEARCH CYBER/CURRENT_HEAD_REFERENCE_AUDIT.csv>).

- 33 entries have local PDF and extracted text; first-page source-identity checks passed.
- 12 entries have extracted primary/participant/official text without a local PDF.
- 3 DARPA entries are official web-source records without local text artifacts.
- R4 and R6 are the two genuine metadata-only/paywalled boundaries. Their DOI/venue/year identity is recorded, but detailed empirical use remains qualified and cannot be independently checked against full text in this repository.
- Current structural checks are exact: BibTeX = cited keys = manifest keys = 50, and every manifest row has the required 21 columns.

This is a current-state semantic inventory with explicit access labels; it is not a claim that paywalled full text was inspected.

## AIxCC and GTG-1002 occurrence audit

The fresh occurrence ledger is [CURRENT_HEAD_AIXCC_GTG_AUDIT.csv](</home/nixon/RESEARCH CYBER/CURRENT_HEAD_AIXCC_GTG_AUDIT.csv>), containing 80 relevant current-manuscript occurrence rows.

- Trail of Bits account: 48 challenges / 23 repositories.
- R7 systematization: 48 scored challenge projects / 24 OSS-Fuzz repositories.
- DARPA closeout: 54 unique synthetic vulnerabilities across 63 final challenges, 43 patches / 68%.
- OpenSSF retrospective values remain separately identified as team/foundation-relayed.
- No occurrence merges 23 with 24 or treats the two repository denominators as the same universe.
- GTG-1002 occurrences are either explicitly qualified as single-source/vendor-reported and unresolved, or are named boundary-case references without an autonomy assertion.

## Numeric and record-level checks

- [CURRENT_HEAD_NUMERIC_AUDIT.csv](</home/nixon/RESEARCH CYBER/CURRENT_HEAD_NUMERIC_AUDIT.csv>) rechecks all 52 rows of the prior numeric ledger against current `main.tex`, preserving DIRECT/QUALIFIED/PARTIAL distinctions and flagging the removed CyberGym row.
- [CURRENT_HEAD_RECORD_AUDIT.csv](</home/nixon/RESEARCH CYBER/CURRENT_HEAD_RECORD_AUDIT.csv>) independently reconciles all 36 records across YAML, record-ID map, assignment CSV, and Appendix Table IV.
- All 36 record predicates pass: identity, year, unit, autonomy level, loop position, table presence, and access representation. Presentation-only `n-a`/`n/a` and descriptive loop suffixes were normalized for comparison.
- Boundary records receiving explicit attention include Agentless, ARTEMIS, XBOW, Big Sleep, GTG-1002, the AIxCC cluster, Argusee, and Fang.

## Build and PDF verification

Clean sequence executed:

```text
pdflatex → bibtex → pdflatex → pdflatex
```

Results:

- 0 fatal TeX errors
- 0 BibTeX parsing errors
- 50/50 citation keys resolved
- 18 pages, letter size
- `scripts/verify_final.py`: PASS
- `scripts/scripts_audit_final.py`: PASS
- CSV schema checks: PASS for source map, manifest, assignments, record map, and all current audit ledgers
- YAML parsing: 36/36
- PDF text sentinels and expected Table IV/timeline/sensitivity rows present

The final log retains two nonfatal overfull vertical boxes:

| Page | Warning | Location interpretation |
|---:|---:|---|
| 16 | 10.89452 pt | Appendix A / Table IV transition |
| 17 | 113.32794 pt | Appendix C timeline transition |

Underfull boxes remain around dense tables and the timeline. Fresh PNG renders of all 18 pages were inspected. No visible clipping, overlap, missing table row, or caption loss was found. Page 18 contains substantial whitespace around the compact sensitivity table, but no visible defect.

## Final verdict

The exact current state passes the structural, citation, record-reconciliation, build, and visual-integrity gates. The earlier version-drift concern was valid; this clean-room pass independently confirmed the manifest repairs and GTG-1002 qualification already present in HEAD.

The project should not be described as having “nothing remaining” in an evidentiary sense. The residual open boundaries are:

- R4/R6 full-text access limitations;
- the explicitly scoped AIxCC 23-versus-24 repository denominator discrepancy;
- GTG-1002’s unresolved, vendor/threat-intelligence-only autonomy assessment; and
- nonfatal LaTeX layout warnings, despite clean visual inspection.

No commit was created by this audit. The rebuilt PDF and release hashes now correspond to the documented current worktree state.
