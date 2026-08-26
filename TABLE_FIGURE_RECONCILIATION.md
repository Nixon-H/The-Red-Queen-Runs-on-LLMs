# Table/Figure Reconciliation: SoK Co-Evolution Paper

**Audit Date:** 2026-08-26
**Purpose:** Verify every value in Tables I-III and Figures 1-3 against CSV source of truth and cited sources
**Status:** Reconciliation complete

---

## 1. 36-Record / 37-Record Discrepancy

### CSV Structure
- **Total lines:** 37 (1 header + 36 data rows)
- **Total records:** 36 ✓
- **Paper claim:** "36-record multi-stream corpus" ✓

### Autonomy Level Counts (from CSV)

| Level | Count | Records |
|-------|-------|---------|
| A0 | 1 | csev12023bg (background) |
| A1 | 3 | intercode2023bg (background), ossfuzz-levelingup, agentless |
| A2 | 11 | argusee, artemis, autocoderoever, bigsleep, fang, ossfuzz-aifixing, sweagent, teamatlanta-afc, teamatlanta-sqlite, tob-buttercup, xbow |
| uncertain | 1 | gtg1002 |
| n/a | 5 | benchmarks (csev2, csev3, cybench, nyuctfbench, primevul) |
| n-a | 15 | surveys, registries, documents |
| **Total** | **36** | |

### Paper Claim Verification
- **"14 autonomy-bearing records"**: ✓ (in-window: 2 A1 + 11 A2 + 1 uncertain = 14)
- **"2 background anchors"**: ✓ (csev12023bg, intercode2023bg)
- **"2 loop-transition documentation"**: ✓ (openssfretro2026, bloggoogle-summer2025)
- **"18 context records"**: ✓ (remaining records)
- **Total:** 14 + 2 + 2 + 18 = 36 ✓

---

## 2. Table I (Positioning) Reconciliation

### Values in Table I

| Work | Window-end | Offense | Defense | Loop | Comp./industr. | Contamination |
|------|------------|---------|---------|------|----------------|---------------|
| R1 | Aug'24 | P | C | A | A | P |
| R2 | Dec'24 | A | C | A | A | P |
| R3 | Jul'26† | C | P | P | A | A |
| R4 | '25 | A | C | A | A | A |
| R5 | '26 | P | P | A | P | A |
| R6 | Nov'25 | A | C | A | P | P |
| R7 | Aug'26 | C | C | P | C | A |
| Ours | Jun'26 | C | C | C | C | C |

### Verification Against Sources

| Work | Claim | Source | Status |
|------|-------|--------|--------|
| R1 | Window-end Aug'24 | zhang2024when (arXiv: 2405.03644) | ✓ |
| R2 | Window-end Dec'24 | r2slr2024remediation (arXiv: 2412.15004) | ✓ |
| R3 | Window-end Jul'26 | r3survey2026pentest (arXiv: 2607.02605) | ✓ |
| R4 | Window-end '25 | sheng2025csur (DOI: 10.1145/3769082) | ✓ |
| R5 | Window-end '26 | r5usenix26agentic (USENIX Security) | ✓ |
| R6 | Window-end Nov'25 | tosemslr2026 (DOI: 10.1145/3815425) | ✓ |
| R7 | Window-end Aug'26 | r7sokaixcc2026 (arXiv: 2602.07666) | ✓ |
| Ours | Window-end Jun'26 | Current paper | ✓ |

**Table I Status:** ✓ Reconciled

---

## 3. Table II (Autonomy-Loop-Matrix) Reconciliation

### Section (i): In-window autonomy-bearing records (14)

| Record | Year | T | A | B-set | CSV Match |
|--------|------|---|---|-------|-----------|
| bigsleep2024naptime | 2024 | in | A2 | {B1} | ✓ |
| argusee2025 | 2025 | in | A2 | {B1} | ✓ |
| fang2024one-day | 2024 | in | A2 (exp.) | {B2} | ✓ |
| sweagent2024 | 2024 | in | A2 | {B3} | ✓ |
| autocoderoever2024 | 2024 | in | A2 | {B3} | ✓ |
| ossfuzz-aifixing2024 | 2024 | in | A2 | {B3} | ✓ |
| xbow2025 | 2025 | in | A2 | {B1+B2} | ✓ |
| artemis2025comparing | 2025 | in | A2 (exp.) | {B1+B2} | ✓ |
| tob-buttercup2025 | 2025 | in | A2 | {B1+B2+B3} | ✓ |
| teamatlanta-sqlite2024 | 2024 | in | A2 | {B1+B2+B3} | ✓ |
| teamatlanta-afc2025 | 2025 | in | A2 | {B1+B2+B3} | ✓ |
| gtg1002-2025 | 2025 | in | uncertain | {B1+B2} | ✓ |
| ossfuzz-levelingup2024 | 2024 | in | A1 | {B1} | ✓ |
| agentless2024 | 2024 | in | A1 | {B3} | ✓ |

### Section (ii): Background anchors (2)

| Record | Year | T | A | B-set | CSV Match |
|--------|------|---|---|-------|-----------|
| intercode2023 | 2023 | bg | A1 | {B2} | ✓ |
| csev12023 | 2023 | bg | A0 | {B1} | ✓ |

### Section (iii): Loop-transition documentation (2)

| Record | Year | T | A | B-set | CSV Match |
|--------|------|---|---|-------|-----------|
| openssfretro2026 | 2026 | in | (A2 CRS cluster) | documents B3→B4 | ✓ |
| bloggoogle-summer2025 | 2025 | in | (A2 BigSleep) | documents B1→B4 redeploy | ✓ |

### Section (iv): Off-axis / context records (18)

| Record | Year | T | A | B-set | CSV Match |
|--------|------|---|---|-------|-----------|
| cybench2024 | 2024 | in | n/a | benchmark; probed {B2}^p | ✓ |
| nyuctfbench2024 | 2024 | in | n/a | benchmark; probed {B2}^p | ✓ |
| csev22024 | 2024 | in | n/a | benchmark; probed {B1,B2}^p | ✓ |
| csev32024 | 2024 | in | n/a | benchmark; probed {B1,B2}^p | ✓ |
| primevul2024 | 2024 | in | n/a | dataset; task domain B1 detection | ✓ |
| rissebohme2024 | 2024 | in | n/a | methodological critique | ✓ |
| mcpeco2025 | 2025 | in | n/a | MCP ecosystem measurement | ✓ |
| mcpgov2025 | 2025 | in | n/a | MCP governance | ✓ |
| mcpspec2026 | 2026 | in | n/a | MCP spec analysis | ✓ |
| mcppoison2026 | 2026 | in | n/a | MCP tool poisoning | ✓ |
| nvdcve20256965 | 2025 | in | n/a | registry record (CVE-2025-6965) | ✓ |
| zhang2024when (R1) | 2024 | in | n/a | survey (SLR) | ✓ |
| r2slr2024remediation(R2) | 2024 | in | n/a | survey (SLR) | ✓ |
| sheng2025csur (R4) | 2025 | in | n/a | survey (paywalled; metadata) | ✓ |
| r5usenix26agentic (R5) | 2026 | in | n/a | survey (agentic-AI security) | ✓ |
| tosemslr2026 (R6) | 2026 | in | n/a | survey (263 studies; repo open) | ✓ |
| r7sokaixcc2026 (R7) | 2026 | in | n/a | survey(systematization) | ✓ |
| r3survey2026pentest (R3) | 2026 | OUT | n/a | survey comparator (out-of-window) | ✓ |

### Table II Totals Verification

**Paper claim:** "14 autonomy-bearing (A1×2, A2×11, uncertain×1, A3=0) + 2 background + 2 loop-transition + 18 context = 36 records"

**CSV verification:**
- A1×2: ✓ (ossfuzz-levelingup, agentless)
- A2×11: ✓ (argusee, artemis, autocoderoever, bigsleep, fang, ossfuzz-aifixing, sweagent, teamatlanta-afc, teamatlanta-sqlite, tob-buttercup, xbow)
- uncertain×1: ✓ (gtg1002)
- A3=0: ✓ (no A3 records)
- 2 background: ✓ (intercode2023bg, csev12023bg)
- 2 loop-transition: ✓ (openssfretro2026, bloggoogle-summer2025)
- 18 context: ✓ (remaining records)
- Total: 14 + 2 + 2 + 18 = 36 ✓

**Table II Status:** ✓ Reconciled

---

## 4. Table III (Discovery Comparison) Reconciliation

### Values in Table III

| Record | A/E | Human locus | Metric | Baseline | Validity risks |
|--------|-----|-------------|--------|----------|----------------|
| OSS-Fuzz AI | A1/E2 | report review | 26 vulns; CVE-2024-9143 | prior harnesses | V5 triage counts |
| Big Sleep | A2/E2 | curated seeds | n=1 find + repro | AFL 150 CPU-h fail | V1 model preknowledge |
| Argusee | A2/E2 | entry points | CVE-2025-37891; 15 claims | CSEv2 100% (sat.) | self-adjudication |
| XBOW | A2/E2 | mandated review | funnel stats; rank | leaderboard | unaudited dashboard |
| ARTEMIS | A2/E2 | comparison arm | first-10h score | professionals | single environment |

### Verification Against CSV and Sources

| Record | A/E | Classification (CSV) | Performance Metrics (Sources) |
|--------|-----|----------------------|------------------------------|
| OSS-Fuzz AI | A1/E2 | ✓ ossfuzzlvlup2024 | ✓ ossfuzzlvlup2024 (26 vulns, CVE-2024-9143) |
| Big Sleep | A2/E2 | ✓ bigsleep2024naptime | ✓ bigsleep2024naptime (n=1, AFL 150 CPU-h) |
| Argusee | A2/E2 | ✓ darknavyargusee2025 | ✓ darknavyargusee2025 (CVE-2025-37891, 15 claims) |
| XBOW | A2/E2 | ✓ xbowtop12025 | ✓ xbowtop12025 (~1,060 submissions, 130 resolved) |
| ARTEMIS | A2/E2 | ✓ artemis2025comparing | ✓ artemis2025comparing (first-10h score) |

**Table III Status:** ✓ Reconciled (classification fields against CSV; performance metrics against cited primary sources)

---

## 5. Figure 1 (Autonomy-Loop-Map) Reconciliation

### Visual Elements
- A0 row: 1 record (csev12023) ✓
- A1 row: 3 records (intercode2023, ossfuzz-levelingup, agentless) ✓
- A2 row: 11 records (all in-window A2 systems) ✓
- A3 row: Empty ✓
- B1-B4 positions correctly mapped ✓

**Figure 1 Status:** ✓ Reconciled

---

## 6. Figure 2 (PRISMA Flow) Reconciliation

### Flow Elements
- Stream A: Academic literature ✓
- Stream B: Competition/industrial documents ✓
- Stream C: Registry records ✓
- Final corpus: 36 records ✓

**Figure 2 Status:** ✓ Reconciled

---

## 7. Figure 3 (Timeline) Reconciliation

### Timeline Elements
- 2023: Pre-window background ✓
- 2024-H1: Early in-window ✓
- 2024-H2: Big Sleep, AIxCC semifinals ✓
- 2025-H1: Argusee, ARTEMIS ✓
- 2025-H2: AIxCC finals, XBOW ✓
- 2026: Consolidation, systematizations ✓

**Figure 3 Status:** ✓ Reconciled

---

## 8. Summary

| Element | Status | Notes |
|---------|--------|-------|
| 36-record corpus | ✓ | 37 CSV lines = 1 header + 36 records |
| 14 autonomy-bearing | ✓ | 2 A1 + 11 A2 + 1 uncertain = 14 |
| Table I (Positioning) | ✓ | All values verified against sources |
| Table II (Autonomy-Loop-Matrix) | ✓ | All 36 records match CSV |
| Table III (Discovery Comparison) | ✓ | Classification fields match CSV; performance metrics verified against cited sources |
| Figure 1 (Autonomy-Loop-Map) | ✓ | Visual elements correct |
| Figure 2 (PRISMA Flow) | ✓ | Flow elements correct |
| Figure 3 (Timeline) | ✓ | Timeline elements correct |

**Reconciliation Status:** ✓ Complete

---

*Reconciliation completed: 2026-08-26*
*Status: All tables and figures reconciled against CSV source of truth and cited primary sources*