# Search Log

**Date:** August 26, 2026  
**Window:** January 2024 – June 2026

I ran eight arXiv queries and four DBLP queries, then snowballed from reference lists. Here's what happened.

---

## arXiv Queries

| Query | Search string | Raw hits |
|-------|--------------|----------|
| Q1 | `"large language model" AND "vulnerability detection"` | 253 |
| Q2 | `"language model" AND "vulnerability discovery"` | 42 |
| Q3 | `"language model" AND "penetration testing"` | 67 |
| Q4 | `"language model" AND "CTF"` | 36 |
| Q5 | `"LLM agent" AND "exploit"` | 192 |
| Q6 | `"large language model" AND "program repair"` | 202 |
| Q7 | `"cyber reasoning system"` | 9 |
| Q8 | `"AI agent" AND "vulnerability"` | 172 |
| | **Total** | **973** |

After clicking through first pages and removing duplicates: 316 arXiv IDs.

**Q4 note:** Half the CTF results were picoCTF writeups with no LLM component. Only chen2024nyuctf and cybench2024 mattered.

**Q7 note:** All 9 hits were AIxCC-related. Tight, no waste.

---

## DBLP Queries

| Query | Search string | Hits |
|-------|--------------|------|
| D1 | `"large language model" vulnerability` | 174 |
| D2 | `"large language model" "penetration testing"` | 11 |
| D3 | `LLM CTF benchmark` | 5 |
| D4 | `vulnerability repair LLM` | 24 |
| | **Total** | **214** |

Most overlapped with arXiv. Only 3 DBLP-only papers made it through.

---

## Snowball / Targeted

These came from reference lists of papers I'd already included, or from blogs and NVD:

| Record | Where I found it | How I verified |
|--------|-----------------|----------------|
| bigsleep2024 | Google DeepMind blog (Nov 2024) | Quoted directly; 150 CPU-hour AFL comparison |
| taasc2024 | DARPA ASC results page | 42 teams, 7 finalists — straightforward |
| xbowtop12025 | HackerOne blog (Jun 2025) | #1 US position on HackerOne |
| bloggoogle2025 | Google Threat Intelligence (Jul 2025) | CVE-2025-6965 |
| nvd6965 | NVD | Registry lookup |
| darknavyargusee2025 | DARKNAVY blog (May 2025) | CVE-2025-37891 |
| darparesults2025 | DARPA AFC results (Aug 2025) | $9.5M total prizes |
| tobbuttercup2025 | Trail of Bits blog (Aug 2025) | ACS APC |
| taafc2025 | AFC scoring docs | Quote-level |
| darpascoring2025 | DARPA scoring algorithm | Quote-level |
| anthropicgtg2025 | Anthropic blog (Nov 2025) | GTG-1002, single-source |
| anthropicgtgreport2025 | Anthropic incident report (Nov 2025) | 80–90% execution estimate |
| openssfaixcc2026 | OpenSSF blog (2026) | CRS SIG, FuzzingBrain, OSS-CRS |

---

## Screening

- **1,200 raw records** across all streams
- **339** after first-pass screening
- **36** advanced to full assessment

**Why 303 got excluded:**

- ~280 were pre-2024 — kept as background, not corpus
- ~20 were arXiv version duplicates
- 1 was off-topic (generic AI security, no vuln/CTF angle)
- 1 was press-only (ARTEMIS "90% of pentesters" — no methodology)
- 1 had a dead link with no Wayback snapshot

I stopped at 339 because the last 50 arXiv results across Q1–Q8 turned up nothing new in-window.

---

## PDF Processing

All 72 PDFs in `references/pdf/` converted to text via `pdftotext -layout`. Zero failures. All 71 bib entries in `refs.bib` have matching `.txt` files.
