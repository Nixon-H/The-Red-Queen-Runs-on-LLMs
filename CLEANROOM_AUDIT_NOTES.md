# Clean-Room Audit Notes — Current Repository State

Audit target: /home/nixon/RESEARCH CYBER  
Exact HEAD: 80f6ce263b2ef78e14437752d0f54305c41ae9da  
HEAD title: Comprehensive forensic audit: 50 files, all verification gates pass  
Working tree at start: no tracked manuscript-core changes; preserve the pre-existing unrelated audit file `audits/cleanup-audit-2026-08-27.md`.

The prior audit at 2eacec1 is not treated as proof for this state.
HEAD 80f6ce2 already contains the prior audit artifacts and fixes. The only pre-existing worktree modification was task_plan.md; this audit added only the clean-room plan and notes so far.
Inventory: 50 unique BibTeX entries; 132 citation commands; 152 citation-key occurrences; 50 unique cited keys; 50 source-map rows; 50 manifest rows; 36 YAML records; 36 record-map rows; 36 assignment rows; 37 PDFs; 49 extracted texts.

Fresh semantic sweep findings: all 50 current manifest rows parse at the 21-field schema width. The earlier sparse rows are expanded from current BibTeX/source-map/local-PDF metadata. R4 and R6 remain metadata-only/paywalled and are explicitly marked as such. The R4 author identity matches the current BibTeX/DOI metadata; R6 is a valid metadata-only row; the Risse/Böhme row is valid CSV without malformed LaTeX quoting.

Current HEAD content confirmed during this audit: GTG-1002 discussion and timeline call the 80--90% value an execution estimate and explicitly retain the single-source, unresolved qualification. The MCP record documents its 2025 arXiv preprint versus accepted DSN 2026 publication-year distinction.

New audit artifacts: CURRENT_HEAD_REFERENCE_AUDIT.csv (50 rows) and CURRENT_HEAD_AIXCC_GTG_AUDIT.csv (80 scoped occurrence rows). The latter found no unchecked AIxCC denominator or GTG autonomy-claim occurrence after local-context review.

Numeric sweep: 52 prior numeric-ledger rows were cross-checked against current main.tex. N017's prior CyberGym 1,507/188 entry is not present in current main.tex and is recorded as removed from the current claim set; this is not treated as a supported current claim. The other rows remain present, with the prior DIRECT/QUALIFIED/PARTIAL distinctions preserved.

Clean rebuild: pdflatex -> bibtex -> pdflatex -> pdflatex; 18 pages; 0 fatal errors; 50 cited keys resolved; final scripts/verify_final.py and scripts/scripts_audit_final.py pass. Final log retains two nonfatal overfull vboxes: 10.89452pt on page 16 at the Appendix A/Table IV transition and 113.32794pt on page 17 at the Appendix C timeline transition. All 18 fresh PNG renders were inspected; no clipping, overlap, or missing table/caption content was visible. Page 18 has substantial intentional whitespace around the compact sensitivity table.
