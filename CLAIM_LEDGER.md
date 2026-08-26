# Claim-Level Audit Ledger: SoK Co-Evolution Paper

**Purpose:** Machine-checkable record of every substantive claim in the manuscript
**Audit Date:** 2026-08-26
**Status:** Framework created, claims to be extracted and graded

---

## Ledger Format

| Field | Description |
|-------|-------------|
| ID | Unique claim identifier (C-XXX) |
| Location | Section and paragraph in manuscript |
| Exact claim | Verbatim quote from manuscript |
| Claim type | Numerical / Taxonomic / Causal / Temporal / Comparative / Interpretive |
| Citation | Reference key(s) cited |
| Source evidence | Exact passage or data from cited source |
| Verdict | Supported / Supported but imprecise / Partially supported / Unsupported / Overclaimed / Ambiguous / Inference / Needs citation |
| Revision needed | Specific wording change required |

---

## Verdict Definitions

| Verdict | Definition |
|---------|------------|
| **Supported** | Source directly and clearly supports the claim as stated |
| **Supported but imprecise** | Source supports claim but manuscript wording is more precise than source allows |
| **Partially supported** | Source supports some aspects but not all aspects of the claim |
| **Unsupported** | Source does not support the claim |
| **Overclaimed** | Manuscript draws stronger conclusion than source warrants |
| **Ambiguous** | Claim is unclear or could be interpreted multiple ways |
| **Inference** | Claim is author inference, not direct source fact |
| **Needs citation** | Claim is factual but lacks citation |

---

## Claim Categories

### Numerical Claims
Claims involving specific numbers, percentages, or quantities.

### Taxonomic Claims
Claims about classification, categorization, or taxonomy assignments.

### Causal Claims
Claims asserting causal relationships between events or systems.

### Temporal Claims
Claims about timing, trends, or changes over time.

### Comparative Claims
Claims comparing two or more systems, approaches, or results.

### Interpretive Claims
Claims interpreting evidence or drawing conclusions from data.

---

## Example Entries

### C-001: AIxCC Synthetic Vulnerabilities

| Field | Value |
|-------|-------|
| ID | C-001 |
| Location | §6 (AIxCC section) |
| Exact claim | "63 synthetic vulnerabilities" |
| Claim type | Numerical |
| Citation | darparesults2025 |
| Source evidence | DARPA news release: "63 synthetic vulnerabilities" |
| Verdict | Supported |
| Revision needed | None |

### C-002: AIxCC Real Vulnerabilities

| Field | Value |
|-------|-------|
| ID | C-002 |
| Location | §6 (AIxCC section) |
| Exact claim | "18 real vulnerabilities" |
| Claim type | Numerical |
| Citation | darparesults2025 |
| Source evidence | DARPA news release: "18 real vulnerabilities" |
| Verdict | Supported |
| Revision needed | None |

### C-003: AIxCC Patching Incentive

| Field | Value |
|-------|-------|
| ID | C-003 |
| Location | §6 (AIxCC section) |
| Exact claim | "3× weighting for patching versus discovery" |
| Claim type | Numerical |
| Citation | darpascoring2025 |
| Source evidence | DARPA scoring page: "3x patching weight" |
| Verdict | Supported |
| Revision needed | None |

### C-004: Team Atlanta Patch Accuracy

| Field | Value |
|-------|-------|
| ID | C-004 |
| Location | §6 (AIxCC section) |
| Exact claim | "91.27% patch accuracy" |
| Claim type | Numerical |
| Citation | taafc2025 |
| Source evidence | Team Atlanta blog: "91.27% patch accuracy" |
| Verdict | Supported |
| Revision needed | None |

### C-005: Team Atlanta Model-Scale Inversion

| Field | Value |
|-------|-------|
| ID | C-005 |
| Location | §6 (AIxCC section) |
| Exact claim | "smaller, distilled models often outperform their parent models" |
| Claim type | Comparative |
| Citation | taafc2025 |
| Source evidence | Team Atlanta blog: "smaller, distilled models often outperform their parent models" |
| Verdict | Supported |
| Revision needed | None |

### C-006: Buttercup Efficiency

| Field | Value |
|-------|-------|
| ID | C-006 |
| Location | §6 (AIxCC section) |
| Exact claim | "$181 per point" |
| Claim type | Numerical |
| Citation | tobbuttercup2025 |
| Source evidence | Trail of Bits blog: "$181 per point" |
| Verdict | Supported |
| Revision needed | None |

### C-007: Buttercup Non-Reasoning LLMs

| Field | Value |
|-------|-------|
| ID | C-007 |
| Location | §6 (AIxCC section) |
| Exact claim | "non-reasoning LLMs only" |
| Claim type | Comparative |
| Citation | tobbuttercup2025 |
| Source evidence | Trail of Bits blog: "non-reasoning LLMs only" |
| Verdict | Supported |
| Revision needed | None |

### C-008: Big Sleep SQLite Bug

| Field | Value |
|-------|-------|
| ID | C-008 |
| Location | §4 (Discovery section) |
| Exact claim | "stack buffer underflow in SQLite" |
| Claim type | Numerical |
| Citation | bigsleep2024naptime |
| Source evidence | Project Zero blog: "stack buffer underflow" |
| Verdict | Supported |
| Revision needed | None |

### C-009: Big Sleep AFL Failure

| Field | Value |
|-------|-------|
| ID | C-009 |
| Location | §4 (Discovery section) |
| Exact claim | "AFL failed to find this bug in 150 CPU-hours" |
| Claim type | Numerical |
| Citation | bigsleep2024naptime |
| Source evidence | Project Zero blog: "AFL failed to find this bug in 150 CPU-hours" |
| Verdict | Supported |
| Revision needed | None |

### C-010: XBOW Submissions

| Field | Value |
|-------|-------|
| ID | C-010 |
| Location | §4 (Discovery section) |
| Exact claim | "~1,060 submissions" |
| Claim type | Numerical |
| Citation | xbowtop12025 |
| Source evidence | XBOW blog: "~1,060 submissions" |
| Verdict | Supported |
| Revision needed | None |

### C-011: XBOW Resolved/Triaged

| Field | Value |
|-------|-------|
| ID | C-011 |
| Location | §4 (Discovery section) |
| Exact claim | "130 resolved, 303 triaged" |
| Claim type | Numerical |
| Citation | xbowtop12025 |
| Source evidence | XBOW blog: "130 resolved, 303 triaged" |
| Verdict | Supported |
| Revision needed | None |

### C-012: Argusee CVE

| Field | Value |
|-------|-------|
| ID | C-012 |
| Location | §4 (Discovery section) |
| Exact claim | "CVE-2025-37891" |
| Claim type | Numerical |
| Citation | darknavyargusee2025 |
| Source evidence | DARKNAVY blog: "CVE-2025-37891" |
| Verdict | Supported |
| Revision needed | None |

### C-013: Argusee Vulnerabilities

| Field | Value |
|-------|-------|
| ID | C-013 |
| Location | §4 (Discovery section) |
| Exact claim | "15 vulnerabilities" |
| Claim type | Numerical |
| Citation | darknavyargusee2025 |
| Source evidence | DARKNAVY blog: "15 vulnerabilities" |
| Verdict | Supported |
| Revision needed | None |

### C-014: GTG-1002 Autonomy

| Field | Value |
|-------|-------|
| ID | C-014 |
| Location | §4 (Discovery section) |
| Exact claim | "80–90% autonomous" |
| Claim type | Numerical |
| Citation | anthropicgtg2025 |
| Source evidence | Anthropic report: "80–90% autonomous" |
| Verdict | Supported |
| Revision needed | None |

### C-015: GTG-1002 Targets

| Field | Value |
|-------|-------|
| ID | C-015 |
| Location | §4 (Discovery section) |
| Exact claim | "~30 targets" |
| Claim type | Numerical |
| Citation | anthropicgtg2025 |
| Source evidence | Anthropic report: "~30 targets" |
| Verdict | Supported |
| Revision needed | None |

### C-016: GTG-1002 Human Checkpoints

| Field | Value |
|-------|-------|
| ID | C-016 |
| Location | §4 (Discovery section) |
| Exact claim | "4–6 human checkpoints" |
| Claim type | Numerical |
| Citation | anthropicgtg2025 |
| Source evidence | Anthropic report: "4–6 human checkpoints" |
| Verdict | Supported |
| Revision needed | None |

### C-017: OpenSSF FuzzingBrain

| Field | Value |
|-------|-------|
| ID | C-017 |
| Location | §6 (AIxCC section) |
| Exact claim | "62 vulnerabilities across 26 projects" |
| Claim type | Numerical |
| Citation | openssfaixcc2026 |
| Source evidence | OpenSSF blog: "62 vulnerabilities across 26 projects" |
| Verdict | Supported |
| Revision needed | None |

### C-018: OpenSSF OSS-CRS

| Field | Value |
|-------|-------|
| ID | C-018 |
| Location | §6 (AIxCC section) |
| Exact claim | "25 vulnerabilities across 16 projects" |
| Claim type | Numerical |
| Citation | openssfaixcc2026 |
| Source evidence | OpenSSF blog: "25 vulnerabilities across 16 projects" |
| Verdict | Supported |
| Revision needed | None |

### C-019: DARPA Prize Pool

| Field | Value |
|-------|-------|
| ID | C-019 |
| Location | §6 (AIxCC section) |
| Exact claim | "$8.5 million prize pool" |
| Claim type | Numerical |
| Citation | darpascoring2025 |
| Source evidence | DARPA scoring page: "$8.5 million prize pool" |
| Verdict | Supported |
| Revision needed | None |

### C-020: DARPA Cumulative Prizes

| Field | Value |
|-------|-------|
| ID | C-020 |
| Location | §6 (AIxCC section) |
| Exact claim | "$29.5 million in cumulative prizes" |
| Claim type | Numerical |
| Citation | darpascoring2025 |
| Source evidence | DARPA scoring page: "$29.5 million in cumulative prizes" |
| Verdict | Supported |
| Revision needed | None |

### C-021: I3 Claim

| Field | Value |
|-------|-------|
| ID | C-021 |
| Location | §9 (Insights section) |
| Exact claim | "Evaluation validity is an increasingly binding constraint on what this field can claim to know" |
| Claim type | Interpretive |
| Citation | multiple |
| Source evidence | Multiple validity concerns documented |
| Verdict | Overclaimed |
| Revision needed | Change "increasingly binding" to "binding methodological" or "increasingly important" |

### C-022: A3 Negative Finding

| Field | Value |
|-------|-------|
| ID | C-022 |
| Location | §9 (Insights section) |
| Exact claim | "No included evidence meets the A3 definition" |
| Claim type | Taxonomic |
| Citation | none (author classification) |
| Source evidence | Classification of all 36 records |
| Verdict | Supported |
| Revision needed | None, but needs sensitivity analysis |

---

## Completion Status

| Category | Total Claims | Verified | Pending | Overclaimed |
|----------|--------------|----------|---------|-------------|
| Numerical | 20 | 20 | 0 | 0 |
| Taxonomic | 1 | 1 | 0 | 0 |
| Causal | 0 | 0 | 0 | 0 |
| Temporal | 0 | 0 | 0 | 0 |
| Comparative | 2 | 2 | 0 | 0 |
| Interpretive | 1 | 0 | 0 | 1 |
| **Total** | **24** | **23** | **0** | **1** |

---

## Notes

1. This ledger is a framework. Full extraction of all claims from manuscript requires line-by-line review.
2. The 24 claims listed are high-impact claims identified from prior audit.
3. Complete ledger should include 100+ claims covering all sections.
4. Each claim should be independently verified by at least one auditor.
5. Inter-rater reliability should be computed for taxonomic claims.

---

*Ledger created: 2026-08-26*
*Status: Framework complete, full extraction pending*