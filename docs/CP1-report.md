# CP1 REPORT — Corpus Saturation (hard stop)

Date: 2026-08-26 | Protocol: research-protocol.md | Routing: skill-routing.md

1. Total identified records: 1,210 (arXiv 973 + DBLP 214 + 23 seed/chaining)
2. Deduplicated records: 316 distinct arXiv IDs (first-page screening union, Q1–Q8) — full-pool
   dedup infeasible without publisher APIs; documented limitation.
3. Screened records: 339 (316 union IDs title/abstract-screened + 23 seed/chaining records).
4. Full texts assessed: 23 (17 OA academic PDFs converted+validated; 5 industrial primaries
   full-text extracted with verbatim quotes+locators; 1 NVD registry record).
5. Included works: 26 canonical YAML records in corpus/included/ (17 academic incl. 2
   background anchors; 6 industrial/vendor/foundation; 1 registry; 3 restricted-access
   differentiation rows R4/R5/R6 tracked with explicit source-class limits).
6. Excluded works + reasons: 4 records in corpus/excluded/ (wrong-ID rejection; press-only
   claim; out-of-window demotion; unresolvable primary URL hold).
7. Paywalled works: R4 CSUR (10.1145/3769082), R6 TOSEM paper text (10.1145/3815425; author
   repo open) — references/paywalled.md. R5 pending OA posting.
8. Failed conversions: ZERO (references/convert-failures.md). No OCR needed.
9. Primary vs secondary evidence counts: PRIMARY-fulltext 23 · SECONDARY-metadata rows 3 ·
   vendor CLAIMED stats inside primary texts flagged per-field (xbow2025, argusee2025,
   bigsleep2024 n=1, gtg1002-2025, openssfretro2026 legacy counts) · third-party verification
   exemplars: Ada Logics ×27 (AIxCC), HackerOne leaderboard rank (weak), ICLR'25 Oral status.
10. Evidence-class distribution (corpus-summary.csv): benchmark 6 · survey/meta 6 · production
    discovery 2 · controlled experiment 1 · dataset-validity 1 · competition 1 ·
    production-network experiment 1 · measurement/analysis infra 4 · incident report 1 ·
    foundation closeout 1 · registry 1 (+2 background benchmarks inside the benchmark count).
11. Provisional autonomy distribution: A0 2 · A0-A1 boundary 2 · A1 1 · A2 4 · A2-production 3 ·
    A2-contested 1 · competition-integrated 1 · infrastructure 4 · ecosystem-B4 1 · meta 6 ·
    registry 1. A3 count: ZERO with independent evidence.
12. Provisional loop distribution: B1-dominant 7 · B2-dominant 5 · B1/B2 mixed 8 ·
    integrated B1-B3 (competition) 1 · B4 1 · cross-cutting tool-layer 4 · meta/registry 7
    (multi-label counting documented; dominant-cell convention).
13. Corpus by year: 2023: 2 (background) · 2024: 9 · 2025: 8 · 2026: 7.
14. Benchmark families: interactive-CTF (InterCode→NYU CTF Bench→Cybench); risk/capability
    suites (CyberSecEval v1-v3); detection datasets (PrimeVul vs BigVul/DiverseVul);
    exploitation control sets (Fang 15×one-day CVEs); competition challenge sets (AIxCC);
    production leaderboards (HackerOne); ecosystem scans (MCP census).
15. Industrial/competition systems: AIxCC CRSs (Atlantis, Buttercup, Theori, RoboDuck,
    FuzzingBrain, Lacrosse, 42-b3yond-6ug, Shellphish) · Big Sleep · XBOW · Argusee ·
    ARTEMIS scaffold · Claude Code (misuse case) · OSS-Fuzz/OSS-Fuzz-LLM [TV].
16. Unresolved [TO-VERIFY] items: C18 prize-pool conflict ($29.5M vs $30.5M) · C19 challenge/
    repo counts (48/23 vs 63/24) · C20 Buttercup 28v+19p · C21 OSS-Fuzz-LLM 26 vulns ·
    C22 GTG-1002 designation string · C23 blog.google primary URL · C27 CSUR issue number ·
    Fang page-level locators (C01 close-read) · R5 full text · NVD full record fetch.
17. Contradictions discovered: listed in corpus/saturation-rationale.md (5 substantive,
    including two internal vendor self-tensions: XBOW "fully automated" vs mandatory human
    review; Argusee 100% CSEv2 vs human-entry-point dependency).
18. Saturation rationale: corpus/saturation-rationale.md (7 passes logged; marginal-yield test;
    expansion queue enumerated; arXiv-centric coverage limitation argued for §3).
19. Major evidence gaps (feed §11): no independently reproduced end-to-end autonomous
    discovery→patch result anywhere in corpus; all production stats vendor-reported; zero A3;
    B3 standalone literature absent from included set (repair arrives via AIxCC only so far —
    targeted repair-literature chaining queued for PHASE 9); contamination quantification
    exists mainly as negative results (PrimeVul, Fang description-dependence).

Artifacts: CP1-report.md (this file) · prisma-counts.csv · corpus-summary.csv ·
corpus/included/*.yaml ×26 · corpus/excluded/*.yaml ×4 · search-log.md · claim-verification.csv ·
references/{manifest.csv,paywalled.md,convert-failures.md} · refs.bib (draft).
