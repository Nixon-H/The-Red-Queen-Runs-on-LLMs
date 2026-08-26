# Search Log — SoK: From Assistive to Autonomous (LLM-driven vuln discovery)

All searches executed 2026-08-26. Operator: Nixon (research corpus build, CP1).

## Databases & exact query strings

### arXiv (arxiv.org/search UI; filters: submitted_date 2024-01-01..2026-06-30; searchtype=all)
Saved HTML: /tmp/opencode/s_q*.html ; per-query listed IDs captured for dedup.

| Q  | Exact string                                              | Raw hits |
|----|-----------------------------------------------------------|----------|
| Q1 | "large language model" AND "vulnerability detection"      | 253 |
| Q2 | "language model" AND "vulnerability discovery"            | 42  |
| Q3 | "language model" AND "penetration testing"                | 67  |
| Q4 | "language model" AND "CTF"                                | 36  |
| Q5 | "LLM agent" AND "exploit"                                 | 192 |
| Q6 | "large language model" AND "program repair"               | 202 |
| Q7 | "cyber reasoning system"                                  | 9   |
| Q8 | "AI agent" AND "vulnerability"                            | 172 |

arXiv total identified: 973. First-page listings (50/query max) yielded a deduplicated
union of **316 distinct arXiv IDs** -> this is the screened pool for CP1.
NOTE: export.arxiv.org API returned HTTP 429 throughout session; UI used instead.

### DBLP (dblp.org/search/publ/api, format=json, h=0 counts)
| Q  | Exact string                                        | Hits |
|----|-----------------------------------------------------|------|
| D1 | "large language model" vulnerability                | 174 |
| D2 | "large language model" "penetration testing"        | 11  |
| D3 | LLM CTF benchmark                                   | 5   |
| D4 | vulnerability repair LLM                            | 24  |
DBLP total identified: 214.

### IEEE Xplore / ACM DL / USENIX / NDSS / Google Scholar
No programmatic API access this session. Coverage achieved via:
(a) USENIX Sec'26 technical-sessions index fetched and grepped (verified presence of R5+R7);
(b) backward citation chaining inside local corpus TXT/PDFs;
(c) forward chaining via Awesome-LLM4SVD repo README (fetched, 73,780 B);
(d) targeted web searches (Tavily keyless) recorded below.

## Targeted verification searches (web)
1. PrimeVul dataset arXiv ID -> RESOLVED: 2403.18624 ("Vulnerability Detection with Code
   Language Models: How Far Are We?", Ding et al.). Spec's unnumbered hint verified.
2. CSUR 58(5) 2025 candidate -> Sheng et al., "LLMs in software security: A survey of
   vulnerability detection techniques and insights", ACM Comput. Surv. 58(5?) Art.134,
   DOI 10.1145/3769082. Issue number [TO-VERIFY].
3. USENIX Sec'26 sessions page -> confirmed titles:
   "SoK: Attack and Defense Landscape of Agentic AI Systems" (R5);
   "SoK: DARPA's AI Cyber Challenge..." (R7; arXiv journal-ref also says USENIX Security 2026).
4. TOSEM SLR -> DOI 10.1145/3815425 accepted 04/2026; 263 studies Jan 2020-Nov 2025;
   artifacts repo live (github.com/hs-esslingen-it-security/Awesome-LLM4SVD). R6 CONFIRMED.
5. DARKNAVY Argusee URL -> darknavy.org/blog/argusee_a_...(May 23 2025).
6. OpenSSF retrospective URL -> openssf.org/blog/2026/05/12/hack-to-the-future-... CONFIRMED.
7. Big Sleep canonical post -> projectzero.google/2024/10/from-naptime-to-big-sleep.html,
   dateline 2024-Nov-01. FETCHED FULL TEXT.
8. blog.google CVE-2025-6965 announcement -> primary URL NOT yet resolved (404 on guessed slug);
   narrative currently supported by NVD entry (primary registry) + press quoting Google.
9. XBOW #1 posts -> xbow.com/blog/top-1-how-xbow-did-it (2025-06-24, N. Waisman) FETCHED;
   xbow.com/blog/xbow-on-hackerone-whats-next located; famous xbow.com/1 now 404 (archived copy
   to be cited as Wayback snapshot if needed).

## Seed-corpus ID verification results (arXiv abs pages fetched 2026-08-26)
| ID          | Status | Notes                                                        |
|-------------|--------|--------------------------------------------------------------|
| 2405.03644  | OK     | R1 SLR; comment says updated through Aug 31 [2024]           |
| 2412.15004  | OK     | R2 SLR                                                       |
| 2607.02605  | OK     | R3 survey (Jul 2026); title matches spec incl. "Co-Evolution"|
| 2602.07666  | OK     | R7 SoK AIxCC; journal-ref = USENIX Security 2026             |
| 2306.14898  | OK     | InterCode (pre-window -> background)                         |
| 2312.04724  | OK     | CyberSecEval v1 (pre-window -> background)                   |
| 2404.13161  | OK     | CyberSecEval 2                                               |
| 2408.01605  | OK     | CyberSecEval 3                                               |
| 2406.05590  | OK     | NYU CTF Bench                                                |
| 2408.08926  | OK     | Cybench; comment confirms ICLR 2025 Oral                     |
| 2510.16558  | OK     | MCP ecosystem study; accepted DSN 2026                       |
| 2601.17549  | OK     | MCP spec security analysis                                   |
| 2603.22489  | OK     | MCP threat modeling / tool poisoning                         |
| 2511.20920  | OK     | MCP risks/controls/governance                                |
| 2512.09882  | OK     | ARTEMIS vs professionals study                               |
| 2404.08144  | OK     | Fang et al., one-day exploitation                            |
| 2502.00930  | REJECT | control-theory paper; spec's implicit PrimeVul guess wrong    |
| 2403.18624  | OK     | PrimeVul (correct ID, found via search)                      |

## Exclusions (with reasons) — running list
- arXiv 2502.00930: wrong paper entirely (control theory). Replaced by 2403.18624.
- PentestGPT (arXiv 2308.06736): pre-window -> background-only per date discipline.
- InterCode-CTF, CyberSecEval v1: pre-window -> background-only (kept in corpus as bg anchors).
- Press-only phrasing "beats 90% of pentesters" for ARTEMIS: excluded from load-bearing claims
  (absent from paper itself; verified absent in local TXT grep during CP2 drafting).
- blog-only items without documented system/result: none admitted beyond vendor pages with
  concrete system evidence (XBOW/DARKNAVY/PZ/OpenSSF/Anthropic all document systems+results).
