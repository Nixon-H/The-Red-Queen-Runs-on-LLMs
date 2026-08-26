# Corrected Forensic Audit Report: SoK Co-Evolution Paper

**Audit Date:** 2026-08-26
**Auditor:** Nixon (Aditya Singh)
**Current Build:** 19d8415 (git commit, 18 pages, 257769 bytes)
**Status:** Major revision required

---

## Correction Notice

This report supersedes the previous forensic audit. The original audit contained:
1. Overstated verification completeness
2. Internal numerical inconsistencies (37/38 vs 1/8)
3. Unreconciled reference counts (38 refs vs 36 URLs)

This corrected report distinguishes:
- **Bibliographic verification** — source exists, metadata correct
- **Citation verification** — cited source supports nearby sentence
- **Numerical verification** — exact number appears in source
- **Interpretive verification** — manuscript conclusion matches source strength
- **Completeness verification** — all verifiable claims are cited

---

## 1. Current State Verification

### PDF Compilation
- **Status:** ✅ PASS
- **Page count:** 18 pages
- **Build hash:** 19d8415 (git commit)
- **Build errors:** 0 LaTeX errors, 0 undefined citations
- **Build warnings:** 6 LaTeX warnings, 3 overfull boxes, 41 underfull boxes
- **File size:** 257769 bytes

### Bibliography Rendering
- **Status:** ✅ PASS (after cleanup)
- **Internal audit notes:** REMOVED (verified by pdftotext grep)
- **References [7], [8], [9]:** ✅ CORRECT (CyberSecEval v1/v2/v3)
- **Total entries:** 38
- **Entries with URLs:** 36
- **Entries without URLs:** 2 (sheng2025csur, tosemslr2026 — DOI-only)

---

## 2. Bibliography Cleanup Completed

### Changes Made

| Entry | Change | Reason |
|-------|--------|--------|
| fang2024agents | "Qi Zhan" → "Akul Gupta" | Author metadata error |
| 23 entries | Removed note fields | Internal audit notes not for publication |

### Verification of fang2024agents Correction

| Item | Value |
|------|-------|
| Paper title | "LLM Agents can Autonomously Exploit One-day Vulnerabilities" |
| arXiv ID | 2404.08144 |
| Current authors | Richard Fang, Rohan Bindu, Akul Gupta, Daniel Kang |
| Previous (incorrect) | Richard Fang, Rohan Bindu, Qi Zhan, Daniel Kang |
| Source verified | arXiv abstract page + PDF title page |

### Internal Audit Notes Removed

The following note fields were removed from refs.bib:
- "Authors verified from local PDF title page 2026-08-26" (12 entries)
- "Author list matches authoritative arXiv metadata..." (r7sokaixcc2026)
- "Background (pre-window); authors verified..." (intercode2023, csev12023)
- "Cited version (local PDF v3...)..." (nyuctfbench2024)
- "Title+authors verified on official session index..." (r5usenix26agentic)
- "ACM-format reference block; authors verified..." (ossfuzzfix2024)
- "PRIMARY official closeout..." (darparesults2025)
- "Confirms patch-vs-discovery incentive weighting..." (darpascoring2025)
- "Campaign designation GTG-1002 verified..." (anthropicgtg2025)
- "Local copy references/pdf/..." (anthropicgtgreport2025)

**Note:** Reference-audit.md and evidence/reference-provenance.json should be updated to reflect these changes.

---

## 3. Citation Verification Status

### Verification Levels Achieved

| Level | Description | Status |
|-------|-------------|--------|
| Bibliographic | Source exists, metadata correct | ✅ 38/38 verified |
| Key numerical claims | High-impact numbers checked against primary sources | ✅ Verified |
| Citation-in-context | Every citation occurrence checked in manuscript | ⚠️ Not yet completed |
| Interpretive | Conclusion strength matches source strength | ⚠️ Not yet completed |
| Completeness | All verifiable claims are cited | ⚠️ Not yet completed |

### Key Numerical Claims Verified

| Citation | Claim | Source | Status |
|----------|-------|--------|--------|
| taafc2025 | 91.27% patch accuracy | Team Atlanta blog | ✅ PASS |
| taafc2025 | 44.4% accuracy (Theori) | Team Atlanta blog | ✅ PASS |
| taafc2025 | 6 C/C++ + 12 Java bugs | Team Atlanta blog | ✅ PASS |
| taafc2025 | SQLite zero-day | Team Atlanta blog | ✅ PASS |
| tobbuttercup2025 | $181/point efficiency | Trail of Bits blog | ✅ PASS |
| tobbuttercup2025 | 28 vulns, 19 patches | Trail of Bits blog | ✅ PASS |
| tobbuttercup2025 | $200K/team transition | Trail of Bits blog | ✅ PASS |
| darpascoring2025 | $8.5M prize pool | DARPA scoring page | ✅ PASS |
| darpascoring2025 | 3x patching weight | DARPA scoring page | ✅ PASS |
| darpascoring2025 | $29.5M cumulative | DARPA scoring page | ✅ PASS |
| openssfaixcc2026 | 62 vulns/26 projects | OpenSSF blog | ✅ PASS |
| openssfaixcc2026 | 25 vulns/16 projects | OpenSSF blog | ✅ PASS |
| bigsleep2024naptime | SQLite stack buffer underflow | Project Zero blog | ✅ PASS |
| bigsleep2024naptime | 150 CPU-hours AFL failure | Project Zero blog | ✅ PASS |
| xbowtop12025 | ~1,060 submissions | XBOW blog | ✅ PASS |
| xbowtop12025 | 130 resolved, 303 triaged | XBOW blog | ✅ PASS |
| darknavyargusee2025 | CVE-2025-37891 | DARKNAVY blog | ✅ PASS |
| darknavyargusee2025 | 15 vulnerabilities | DARKNAVY blog | ✅ PASS |
| anthropicgtg2025 | 80-90% autonomous | Anthropic report | ✅ PASS |
| anthropicgtg2025 | ~30 targets | Anthropic report | ✅ PASS |

---

## 4. Taxonomy Validation

### A0-A3 Classification

| Level | Count | Records | Status |
|-------|-------|---------|--------|
| A0 | 1 | csev12023 (background) | ✅ |
| A1 | 3 | ossfuzz-levelingup, agentless, intercode | ✅ |
| A2 | 14 | All verified against sources | ✅ |
| A3 | 0 | No systems meet definition | ✅ DEFENSIBLE |
| Uncertain | 1 | gtg1002 | ✅ |

### Boundary Case Justifications

| System | Classification | Justification | Status |
|--------|----------------|---------------|--------|
| XBOW | A2 | Policy-mandated human review | ✅ DEFENSIBLE |
| Big Sleep | A2 | Human-curated seed set | ✅ DEFENSIBLE |
| AIxCC | A2/E1 | Competition environment | ✅ DEFENSIBLE |
| ARTEMIS | A2/E2 | Corporate-style network | ⚠️ NEEDS EXPLICIT JUSTIFICATION |
| GTG-1002 | Uncertain | Vendor-reported | ✅ DEFENSIBLE |

---

## 5. I1/I2/I3 Claim Assessment

### I1: Autonomy Measurement Shift
**Status:** ✅ DEFENSIBLE
- Measurement/framing-shift component: HIGH confidence
- Multiple independent sources
- Dated timeline from 2024-H1 to 2026

### I2: Coupling Edges
**Status:** ✅ DEFENSIBLE
- D1-D4 documented edges
- P1 plausible coupling
- Temporal association only
- Existence claim, not causal claim

### I3: Evaluation Validity
**Status:** ⚠️ OVERCLAIMED
- Current wording: "increasingly binding constraint"
- Issue: Temporal trend not supported by evidence
- Recommended: "binding methodological constraint" or "increasingly important constraint"

---

## 6. Figure/Table Audit

| Element | Status | Notes |
|---------|--------|-------|
| Table I (Positioning) | ✅ PASS | Correctly differentiates 7 prior systematizations |
| Table II (Autonomy-Loop-Matrix) | ✅ PASS | 36 records correctly classified |
| Table III (Discovery Comparison) | ✅ PASS | 5 systems with A/E classification |
| Figure 1 (Autonomy-Loop-Map) | ✅ PASS | Visual representation correct |
| Figure 2 (PRISMA Flow) | ✅ PASS | Multi-stream evidence flow |
| Figure 3 (Capability Timeline) | ✅ PASS | 2023-2026 milestones with class coding |

---

## 7. Honest Assessment

### What Is Solidly Established

✅ Manuscript has 18-page compiled state
✅ Internal audit notes removed from bibliography
✅ Author metadata error corrected
✅ Key high-value citations verified against primary sources
✅ I1 and I2 appear well-calibrated
✅ Taxonomy design is legitimate contribution
✅ A3 negative finding is defensible

### What Remains Unverified

⚠️ Full citation-in-context audit not completed
⚠️ Every numerical claim traced to source not demonstrated
⚠️ A3 sensitivity analysis not performed
⚠️ Inter-rater reliability not tested
⚠️ I3 wording needs calibration
⚠️ E1/E2 boundary justification incomplete (ARTEMIS)

### Scoring

| Dimension | Assessment |
|-----------|------------|
| Research contribution | Strong (9/10 potential) |
| Artifact hygiene | Improved (bibliography cleaned) |
| Citation discipline | Appears strong, not comprehensively proven |
| Methodological rigor | Promising, unresolved validation concerns |
| Submission readiness | **Not ready** |

**Overall:** 8–8.5/10 potential quality, not yet independently established as reviewer-ready.

---

## 8. P0/P1/P2 Revision Checklist

### P0 — Must Fix Before Submission

1. ~~Fix author metadata error in fang2024agents~~ ✅ DONE
2. ~~Remove internal audit notes from bibliography~~ ✅ DONE
3. ~~Recompile and verify final PDF~~ ✅ DONE
4. Generate SHA-256 manifest for reproducibility
5. Update reference-audit.md to reflect cleanup

### P1 — Methodological Issues Likely to Matter to Reviewers

1. Add inter-rater validation or documented robustness procedure
2. Add A3 sensitivity analysis (S1-S4 scenarios)
3. Tighten I3 claim wording
4. Formalize E0/E1/E2 criteria with explicit justification for ARTEMIS
5. Separate evidence types (documented fact, vendor claim, author inference)

### P2 — Improvements That Could Materially Raise Review Score

1. Add evidence graph for D1-D4/P1
2. Add temporal visualization
3. Add reproducibility manifest
4. Complete citation-in-context audit

---

## 9. Next Steps

1. **Claim-level audit:** Extract every factual claim, trace to source, grade wording
2. **A3 sensitivity analysis:** Test under S1-S4 scenarios
3. **I3 calibration:** Revise wording to match evidence strength
4. **E1/E2 justification:** Explicitly justify ARTEMIS classification
5. **SHA-256 manifest:** Record build metadata for reproducibility

---

*Report generated: 2026-08-26*
*Status: Major revision required*
*Recommendation: Do not submit until P1 issues resolved*