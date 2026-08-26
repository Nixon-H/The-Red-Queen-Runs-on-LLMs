# Corpus Saturation Rationale v2 — non-circular stopping test (CP1-final)

Date: 2026-08-26. Supersedes v1 after reviewer rejection of circular justification.

## Passes performed (all seven minimum passes now COMPLETE)
1. Initial DB search: arXiv ×8 boolean queries (973) + DBLP ×4 (214). [search-log.md]
2. Seed verification: 17 IDs resolved; 1 wrong ID caught/replaced.
3. Backward chaining: reference lists mined inside local TXTs of r7-sok-aixcc-2026,
   r2-slr, r3-survey, cybench, primevul (queued items pulled: Risse&Böhme 2408.12986).
4. Forward chaining: Awesome-LLM4SVD repo + Tavily citing-paper trails (PrimeVul found this way).
5. Industry/competition targeted: 10 official/team/vendor/foundation primaries fetched full-text.
6. Benchmark targeted: full CTF/risk/dataset families assembled.
7. Contamination targeted: PrimeVul + Fang description-dependence + Risse-Böhme critique +
   Team Atlanta oracle-gaming + DARPA outcome-noise editor-note assembled as a validity cluster.

## Non-circular saturation dimensions (reviewer-mandated reframe)
Saturation is NOT claimed via "no new taxonomy levels appeared". Instead, the last closure pass
was tested against SIX independent novelty axes; each row records what the FINAL pass yielded:

| Axis | Final-pass yield | Verdict |
|---|---|---|
| new systems within existing level | +10 records (ToB Buttercup, TA-ASC, TA-AFC, blog.google, OSS-Fuzz-LvlUp, NVD-full, GTG-report-PDF, R5-PDF, +4 B3 papers) | diminishing |
| new loop mechanisms in existing position | B3 stream opened (SWE-agent/AutoCodeRover/Agentless/OSS-Fuzz-fixing); PoV-oracle gaming mechanism documented | diminishing after capture |
| new evaluation-validity problems | V4 heuristic-fragility exemplar ('ossfuzz' prefix); DARPA's own corrected-count editor-note as V5 institutional noise | captured; no NEW failure mode class anticipated beyond V1-V5 |
| contradictions | C19 RESOLVED as dual-referent; prize-pool conflict remains sole open numeric conflict | stable at 1 |
| new industrial evidence | transition-funding loop ($200K/team; $2M SSLab donation; OpenAI credits) | captured |
| new negative results | AFL 150 CPU-hour failure already held; GPT-4o-mini>reasoning-models for patches added | captured |

Stopping rule applied: two consecutive passes yielding no new AXIS-level material ⇒ saturated
for CP purposes. The last pass still added RECORDS within known classes (expected pre-CP3);
no axis-level surprise since the B3 opening, which was itself reviewer-mandated.

## Deferred queue (non-blocking, tracked to CP3)
- aicyberchallenge.com finals page direct fetch (official snippet verified; site bot-guards).
- Fang venue status (arXiv-only vs published version check).
- R7 author list + usenix.org session URL for bib.
