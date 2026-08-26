# CP1-FINAL REPORT — corpus saturation (supersedes CP1-report.md v1)

Date: 2026-08-26 | Status: closure pass executed per reviewer 5-point order.

## Reviewer directives → disposition
1. Close mandatory primary-source gaps — **DONE (8/8)**:
   R5 full prepub PDF (Kim/Guo/Song, USENIX Sec'26, local) · ToB Buttercup primary (28v+19p
   verbatim; human-interaction prohibition verbatim; cost table cross-checks R7) · OSS-Fuzz
   "Leveling Up Fuzzing" full text (26 vulns; CVE-2024-9143 ~20yr latent) · GTG-1002 FULL
   REPORT PDF (designation ×3; changelog Nov-17-2025) · blog.google canonical post (exact
   phrases grep-verified in fetched page) · Team Atlanta ASC-SQLite post (official SQLite
   commit e9b919d5 cross-ref) + AFC retrospective (oracle-gaming taxonomy) · NVD CVE-2025-6965
   full detail page (111KB) · Fang locators pinned to local TXT lines.
2. Patching/repair search stream — **DONE**: B3 was empty; now anchored by SWE-agent (2405.15793),
   AutoCodeRover (2404.05427), Agentless (2407.01489), OSS-Fuzz AI-fixing (2411.03346) +
   competition patching evidence (TA-AFC, ToB). loop_position B3 count: 0→4 (+multi-cell CRSs).
3. PRISMA accounting — **RESTRUCTURED**: three explicit streams (A academic / B competition-
   industrial / C registry); no cross-stream denominator mixing. See prisma-counts.csv v2.
4. Schema normalization — **DONE**: every record now carries autonomy_level, loop_position,
   scope_class, access_status as separate fields; legacy buckets demoted to autonomy_note.
   Axis counts use only the two taxonomy fields.
5. Saturation re-test — **REDONE non-circularly**: six independent novelty axes tested;
   two-consecutive-pass no-new-axis rule applied. corpus/saturation-rationale.md v2.

## Final numbers (36 included records across streams)
Stream A academic: 23 OA-PDF works (incl. 2 background anchors; R5 upgraded from restricted to
full-text) + 2 restricted-metadata rows (R4 CSUR, R6 TOSEM) = 25.
Stream B competition/industrial/foundation documents: 10 full-text primaries (PZ Big Sleep,
XBOW, DARKNAVY Argusee, Anthropic summary+full report PDF, OpenSSF retro, ToB Buttercup,
Team Atlanta ASC + AFC, blog.google, OSS-Fuzz Leveling-Up).
Stream C registry: NVD CVE-2025-6965 full record. TOTAL INCLUDED: 36 records (excluded: 4,
with reasons; conversion failures: 0).

Autonomy distribution (records with system-level classification): A0×3, A1×4, A2×13,
uncertain×1 (GTG), n-a×15 (surveys/registry/infra/program records — excluded from axis counts).
Loop distribution: B1×5, B2×4, B3×4, B4×1, multi×10, n-a×12.
Access status: oa-pdf×23, html-primary×11, paywalled/metadata-only×2.

## [TO-VERIFY] ledger status (was 10 open at CP1-v1)
CLOSED this pass: C01 Fang locators · C19 challenge-count conflict (dual referent:
48 projects vs 63 synthetic vulns per DARPA editor-note) · C20 Buttercup 28v+19p ·
C21 OSS-Fuzz-LLM 26 vulns · C22 GTG-1002 designation · C23 blog.google phrase.
REMAINING (3, all non-load-bearing or fetch-mechanical): C32 DARPA finals-page direct fetch
(official snippet verified; site bot-guards curl) · R7/R4 author-list completion for bib ·
Fang venue-status check. None block framework construction.

## Contradictions register (v2)
RESOLVED: challenge counts (dual referent). OPEN (load-bearing, kept as evidence): prize pool
$29.5M-announced vs $30.5M-distributed; XBOW "fully automated" vs policy-mandated human review;
Argusee 100% CSEv2 vs human-entry-point dependency; GTG 80–90% autonomy vs hallucination
caveat; Atlantis "entirely without human intervention" vs challenge-bounded environment.

## Key wording rule adopted (protocol amendment v2)
A3-zero finding may ONLY be stated as: "No included evidence met our operational definition of
A3." Universal/existential phrasings forbidden.

## Evidence gaps (updated §11 feed)
Standalone academic vuln-repair evaluation on REAL AIxCC-style crashes exists (TA's own 2026
agent-eval post queued as chain-in); independent replication of ANY production vendor stat
still absent ecosystem-wide; contamination quantification remains negative-results-driven.

Artifacts updated: prisma-counts.csv (streams) · corpus-summary.csv (normalized distributions)
· corpus/included/*.yaml ×36 (normalized schema) · claim-verification.csv (41 rows; 6 closures)
· references/manifest.csv (provenance_type column + 11 new rows) · research-protocol.md (v2
amendments) · saturation rationale v2.
