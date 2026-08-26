# reference-audit.md — CP3 citation/integrity audit (2026-08-26)

## Summary counts
Total bibliography entries: 38 (all cited; never-cited=NONE at final audit)
OA PDFs downloaded + converted (PDF+TXT pairs): 22 (+1 GTG report PDF = 23)
HTML/primary evidence-extract sources: 10 (+2 DARPA remote-verified primaries)
Metadata-only entries: 2 (R4 CSUR, R6 TOSEM-paper-text; R6 repo = author-primary metadata)
OCR-needed: 0 | Broken/unresolvable URLs in final text: 0 known (see URL sweep note)
BibTeX errors: 0 (post-fix) | Missing citations: 0 | Duplicate keys: 0
Placeholders (VERIFY/TBD/'and others'): 0
Undefined LaTeX citations/references: 0 | Overfull >=10pt boxes: 0
URL resolution sweep (final): 36/36 resolvable (HTTP 200/3xx)
Final build hash: see CHANGES.md CP4 entry

## Seven-part citation-support gate (protocol v5)
Automated parts: key existence, duplicate scan, placeholder scan — PASS for all cited keys.
Manual load-bearing spot checks (source vs proposition):
- Fang 87%/7%/0% baselines -> fang-agents txt lines 29-33/62/74-76/Table3 [PASS]
- XBOW funnel 1060/130/303/33/125/208/209/36 + human-review quote -> extract verbatim [PASS]
- BigSleep seriesBestIndex/generate_series/Gemini1.5/AFL150CPUh/no-CVE -> PZ post verbatim [PASS]
- AIxCC finals aggregates 63/54(86%)/43(68%)/18real/11patches + editor-note -> darparesults2025
  (PRIMARY official; independently web-verified; local fetch unavailable) [PASS w/ channel note]
- Scoring incentive 3x + $8.5M pool -> darpascoring2025 [PASS]
- Team costs $103.3K/$39.6K/$31.8K -> cross-checked R7 table vs ToB blog [PASS x2 sources]
- Buttercup 28v+19p / non-reasoning LLMs / $181-per-point -> ToB verbatim [PASS]
- ASC SQLite bug + official fix e9b919d5 + sibling patching -> TA post + commit hash [PASS]
- GTG 80-90%/30 targets/weakest-missing handling -> full report PDF (GTG-1002 x3) [PASS]
- OSS-Fuzz 26 vulns/CVE-2024-9143/steps1-4 -> Google Security Blog verbatim [PASS]
- CodeRover-S mechanism quote -> local TXT ~lines205-210 [PASS]
- Argusee entry-points quote + CVE-2025-37891 -> DARKNAVY post verbatim [PASS]
- OpenSSF legacy stats -> retro verbatim, labeled team-relayed [PASS]
- PrimeVul claims -> local PDF (numbers to exact pages at camera-ready pass) [PASS*]

## Known residual items (non-blocking, tracked)
1. darparesults2025/darpascoring2025: PRIMARY-official via independent web verification;
   local automated fetch blocked (CDN). Provenance labeled per protocol v5 #2.
2. Three agent-lineage bib notes now carry verified-from-PDF statements; final CP4 sweep must
   re-run the programmatic title-page comparison across ALL entries (reviewer directive).
3. NYU CTF version divergence (Bench vs Dataset) documented in-entry; do not "normalize".
4. Uncited-at-compile entries: none expected after drafting; audit shows every section cites.
   Final pass will re-check for never-cited entries and remove per protocol v5 #4 if any.

## Verdict
All hard gates GREEN in author runtime. Epistemic scope note: these results are executable
claims, not transferable facts -- independent verification requires the release bundle
(untar -> sha256sum -c SHA256SUMS.manifest -> scripts_audit_final.py -> recompile).
