# Forensic Audit Report: SoK Co-Evolution Paper

**Audit Date:** 2026-08-26
**Auditor:** Nixon (Aditya Singh)
**Current Build:** 7c2fa7cc3f (18 pages)
**Status:** Major revision required

---

## Executive Summary

The paper has a strong intellectual core but requires significant revision before submission. The current compilation produces an 18-page PDF with all sections present, but contains internal audit notes in the rendered bibliography and has one confirmed author metadata error. The taxonomy is well-designed but lacks inter-rater validation. The A3 negative finding is defensible but needs explicit sensitivity analysis. I3 is overclaimed relative to current evidence.

**Current score:** 7.5–8.2/10
**Potential after revision:** 9.5+/10

---

## 1. Current State Verification

### PDF Compilation
- **Status:** ✅ PASS
- **Page count:** 18 pages (matches expected)
- **Build command:** pdflatex + bibtex + pdflatex x2
- **Build errors:** 0 LaTeX errors, 0 undefined citations, 0 overfull ≥10pt

### Bibliography Rendering
- **Status:** ⚠️ PARTIAL PASS
- **References [7], [8], [9]:** ✅ CORRECT (CyberSecEval v1/v2/v3, not broken)
- **Internal audit notes:** ❌ FAIL - Notes like "PRIMARY official closeout..." and "authors verified..." appear in rendered PDF
- **Total references:** 38 (all cited)

---

## 2. Citation Audit Results

### Key Citations Verified Against Primary Sources

| Citation | Claim | Source | Status |
|----------|-------|--------|--------|
| `taafc2025` | 91.27% patch accuracy, 0.9999 modifier | Team Atlanta blog | ✅ PASS |
| `taafc2025` | 44.4% accuracy, 0.9044 modifier (Theori) | Team Atlanta blog | ✅ PASS |
| `taafc2025` | 6 C/C++ + 12 Java bugs | Team Atlanta blog | ✅ PASS |
| `taafc2025` | SQLite zero-day at semifinals | Team Atlanta blog | ✅ PASS |
| `taafc2025` | String matching bug ("ossfuzz") | Team Atlanta blog | ✅ PASS |
| `taafc2025` | Smaller models outperform larger | Team Atlanta blog | ✅ PASS |
| `taafc2025` | 10+ minutes per nginx patch | Team Atlanta blog | ✅ PASS |
| `tobbuttercup2025` | $181 per point efficiency | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | 28 vulns, 19 patches | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | 20 CWEs, 90% accuracy | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | Non-reasoning LLMs only | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | $200K per team transition funding | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | PoV for non-inserted vulnerability | Trail of Bits blog | ✅ PASS |
| `tobbuttercup2025` | Team costs $103.3K/$39.6K/$31.8K | Trail of Bits blog | ✅ PASS |
| `darpascoring2025` | $8.5M final prize pool | DARPA scoring page | ✅ PASS |
| `darpascoring2025` | 3x patching weight | DARPA scoring page | ✅ PASS |
| `darpascoring2025` | $29.5M cumulative prizes | DARPA scoring page | ✅ PASS |
| `openssfaixcc2026` | 62 vulns/26 projects (FuzzingBrain) | OpenSSF blog | ✅ PASS |
| `openssfaixcc2026` | 25 vulns/16 projects (OSS-CRS) | OpenSSF blog | ✅ PASS |
| `openssfaixcc2026` | 27 candidate issues (Ada Logics) | OpenSSF blog | ✅ PASS |
| `openssfaixcc2026` | 12 kernel + 10 userspace (42-b3yond-6ug) | OpenSSF blog | ✅ PASS |
| `bigsleep2024naptime` | SQLite stack buffer underflow | Project Zero blog | ✅ PASS |
| `bigsleep2024naptime` | 150 CPU-hours AFL failure | Project Zero blog | ✅ PASS |
| `bigsleep2024naptime` | AIxCC inspiration | Project Zero blog | ✅ PASS |
| `bigsleep2024naptime` | Gemini 1.5 Pro | Project Zero blog | ✅ PASS |
| `bigsleep2024naptime` | No CVE assigned | Project Zero blog | ✅ PASS |
| `xbowtop12025` | Top US leaderboard position | XBOW blog | ✅ PASS |
| `xbowtop12025` | ~1,060 submissions | XBOW blog | ✅ PASS |
| `xbowtop12025` | 130 resolved, 303 triaged | XBOW blog | ✅ PASS |
| `xbowtop12025` | 33 new, 125 pending | XBOW blog | ✅ PASS |
| `xbowtop12025` | Human review required | XBOW blog | ✅ PASS |
| `fang2024agents` | 87% with CVE descriptions | arXiv abstract | ✅ PASS |
| `fang2024agents` | 7% without descriptions | arXiv abstract | ✅ PASS |
| `darknavyargusee2025` | CVE-2025-37891 | DARKNAVY blog | ✅ PASS |
| `darknavyargusee2025` | 15 vulnerabilities | DARKNAVY blog | ✅ PASS |
| `darknavyargusee2025` | 100% on CyberSecEval-2 | DARKNAVY blog | ✅ PASS |
| `anthropicgtg2025` | 80-90% autonomous | Anthropic report | ✅ PASS |
| `anthropicgtg2025` | ~30 targets | Anthropic report | ✅ PASS |
| `anthropicgtg2025` | 4-6 human checkpoints | Anthropic report | ✅ PASS |
| `anthropicgtg2025` | GTG-1002 designation | Anthropic report (local) | ✅ PASS |

### Author Metadata Error Found

| Citation | Paper Lists | Actual Source | Status |
|----------|-------------|---------------|--------|
| `fang2024agents` | Qi Zhan | Akul Gupta | ❌ FAIL |

**Note:** The arXiv page lists authors as "Richard Fang, Rohan Bindu, Akul Gupta, Daniel Kang" but the paper's bibliography lists "Qi Zhan" instead of "Akul Gupta".

---

## 3. Numerical Claims Verification

### AIxCC Statistics (DARPA Primary Sources)
- **63 synthetic vulnerabilities:** ✅ PASS (corrected from 70)
- **54 discovered (86%):** ✅ PASS
- **43 patched (68%):** ✅ PASS
- **18 real vulnerabilities:** ✅ PASS
- **11 real-vuln patches:** ✅ PASS
- **$8.5M final prize pool:** ✅ PASS
- **3x patching weight:** ✅ PASS
- **$29.5M cumulative prizes:** ✅ PASS

### Team Statistics (Cross-verified)
- **Team Atlanta costs:** $103.3K (matches ToB blog)
- **Trail of Bits costs:** $39.6K (matches ToB blog)
- **Theori costs:** $31.8K (matches ToB blog)
- **Trail of Bits efficiency:** $181/point (matches ToB blog)
- **Buttercup:** 28 vulns, 19 patches (matches ToB blog)

### OpenSSF Legacy Statistics
- **FuzzingBrain:** 62 vulns/26 projects, 43 confirmed, 36 patched (matches OpenSSF blog)
- **OSS-CRS:** 25 vulns/16 projects (matches OpenSSF blog)
- **42-b3yond-6ug:** 12 kernel + 10 userspace (matches OpenSSF blog)

---

## 4. Taxonomy Validation

### A0-A3 Classification
- **A0 (assistive):** 1 record (csev12023 background)
- **A1 (pipeline):** 3 records (ossfuzz-levelingup, agentless, intercode background)
- **A2 (task agent):** 14 records (all verified against sources)
- **A3 (autonomous production hunter):** 0 records ✅ DEFENSIBLE
- **Uncertain:** 1 record (gtg1002)

### Boundary Case Justifications

| System | Classification | Justification | Status |
|--------|----------------|---------------|--------|
| XBOW | A2 | Policy-mandated human review | ✅ DEFENSIBLE |
| Big Sleep | A2 | Human-curated seed set | ✅ DEFENSIBLE |
| AIxCC | A2/E1 | Competition environment, not production | ✅ DEFENSIBLE |
| ARTEMIS | A2/E2 | Corporate-style network (~8K hosts) | ⚠️ NEEDS EXPLICIT JUSTIFICATION |
| GTG-1002 | Uncertain | Vendor-reported, human target selection | ✅ DEFENSIBLE |

### E0/E1/E2 Classification
- **E0 (synthetic/benchmark):** Benchmarks, datasets
- **E1 (realistic-sandboxed/competition):** AIxCC competition forks
- **E2 (production/production-like):** Big Sleep, Argusee, XBOW, ARTEMIS

**Issue:** ARTEMIS is described as "production-network experimental settings" and "corporate-style network". The paper should explicitly justify why this qualifies as E2 rather than E1.

---

## 5. I1/I2/I3 Claim Strength Assessment

### I1: Autonomy Measurement Shift
**Claim:** "Evaluation, deployment, and discourse increasingly measure progress in terms of agentic autonomy rather than model capability alone."

**Evidence:**
- Dated timeline from 2024-H1 to 2026
- Multiple independent sources (Big Sleep, Argusee, XBOW, AIxCC, ARTEMIS)
- Discourse shift via systematizations (R5/R6/R7)

**Contradictions:**
- Model-scale confound (no ablation study)
- Human removal didn't occur in defender deployments
- Benchmark-difficulty illusion
- Single-source risk (GTG-1002)

**Assessment:** ✅ DEFENSIBLE (measurement/framing-shift component HIGH confidence)

### I2: Coupling Edges
**Claim:** "Multiple documented offense↔defense coupling edges exist — including one explicit cross-program causal statement — but the evidence is insufficient to establish field-wide causal co-evolution."

**Evidence:**
- D1: Competition → industrial research (Project Zero citing AIxCC)
- D2: Maintainer-side variant response (SQLite)
- D3: Institutional/funding flows
- D4: Threat-seeded defense (CVE-2025-6965)
- P1: Plausible coupling (GTG-1002)
- Temporal association only

**Assessment:** ✅ DEFENSIBLE (existence of coupling edges HIGH confidence)

### I3: Evaluation Validity
**Claim:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know."

**Evidence:**
- Tier 1: Information leakage (Fang 87%/7%)
- Tier 2: Dataset leakage (PrimeVul)
- Tier 3: Oracle manipulation (AIxCC)

**Issue:** The word "increasingly" is temporal and requires evidence of temporal increase. The paper itself proposes U7 (decision-impact study) because no documented case exists where validity correction changed a decision.

**Assessment:** ⚠️ OVERCLAIMED - Should be weakened to "binding methodological constraint" or "increasingly important constraint"

---

## 6. Figure/Table Audit

### Table I (Positioning)
- **Status:** ✅ PASS
- **Content:** Correctly differentiates 7 prior systematizations

### Table II (Autonomy-Loop-Matrix)
- **Status:** ✅ PASS
- **Content:** 36 records correctly classified
- **Consistency:** Matches evidence/autonomy-loop-assignments.csv

### Table III (Discovery Comparison)
- **Status:** ✅ PASS
- **Content:** 5 systems with A/E classification, human locus, metrics, baselines, validity risks
- **Consistency:** Matches text claims

### Figure 1 (Autonomy-Loop-Map)
- **Status:** ✅ PASS
- **Content:** Visual representation of A×B framework

### Figure 2 (PRISMA Flow)
- **Status:** ✅ PASS
- **Content:** Multi-stream evidence flow

### Figure 3 (Capability Timeline)
- **Status:** ✅ PASS
- **Content:** 2023-2026 milestones with class coding

---

## 7. Bibliography Issues

### Internal Audit Notes in Rendered PDF
**Status:** ❌ FAIL

The following notes appear in the rendered bibliography and should be removed:

1. `darparesults2025`: "PRIMARY official closeout: 63 synthetic vulns..."
2. `r7sokaixcc2026`: "Author list matches authoritative arXiv metadata (23 authors); supersedes..."
3. `csev12023`: "Background (pre-window); complete 21-author list..."
4. `nyuctfbench2024`: "Cited version (local PDF v3, 2025-02-18) title page reads..."
5. `r5usenix26agentic`: "Title+authors verified on official session index..."
6. `mcpfirstlook2025`: "Authors verified from local PDF title page 2026-08-26"
7. `mcppoisoning2026`: "Authors verified from local PDF title page 2026-08-26"
8. `mcpspec2026`: "Authors verified from local PDF title page 2026-08-26"
9. `mcpgovernance2025`: "Authors verified from local PDF title page 2026-08-26"
10. `ossfuzzfix2024`: "ACM-format reference block; authors verified from local PDF 2026-08-26"

**Recommendation:** Remove all internal audit notes from refs.bib note fields. These belong in reference-audit.md, not in the rendered bibliography.

### Author Metadata Error
- `fang2024agents`: Lists "Qi Zhan" but actual author is "Akul Gupta"

---

## 8. P0/P1/P2 Revision Checklist

### P0 — Must Fix Before Submission

1. **Fix author metadata error in fang2024agents**
   - Change "Qi Zhan" to "Akul Gupta" in refs.bib
   - Verify against arXiv metadata

2. **Remove internal audit notes from bibliography**
   - Clean all note fields in refs.bib
   - Move verification notes to reference-audit.md

3. **Recompile and verify final PDF**
   - Build hash should be new value
   - Page count should remain 18
   - All references should render correctly

4. **Generate SHA-256 manifest**
   - Record commit hash, build command, TeX environment
   - Create SHA256SUMS.manifest for reproducibility

### P1 — Methodological Issues Likely to Matter to Reviewers

1. **Add inter-rater validation**
   - Second independent annotator for A0-A3 classification
   - Blind classification of 14 autonomy-bearing records
   - Cohen's κ or Krippendorff's α statistic
   - Disagreement table and adjudication rules

2. **Add A3 sensitivity analysis**
   - Test under expanded E2 definition
   - Test with human-review requirement relaxed
   - Test with GTG-1002 included
   - Show A3 remains empty under defensible variations

3. **Tighten I3 claim**
   - Change "increasingly binding" to "binding methodological constraint" or "increasingly important constraint"
   - Remove temporal claim unless supported by evidence

4. **Formalize E0/E1/E2 criteria**
   - Add environment-class decision rubric
   - Explicitly justify ARTEMIS as E2
   - Distinguish between production and production-like

5. **Separate evidence types**
   - Explicitly distinguish documented fact, vendor claim, author inference, causal inference
   - Label confidence levels for each claim type

### P2 — Improvements That Could Materially Raise Review Score

1. **Add evidence graph for D1-D4/P1**
   - Source node, destination node, edge grade
   - Mechanism, alternative explanation, falsifier
   - Evidence source, edge thickness/style

2. **Add temporal visualization**
   - Show autonomy-bearing records over time
   - Dated counts with confidence intervals

3. **Make autonomy/workflow/human boundaries visually explicit**
   - Distinguish system autonomy, workflow autonomy, organizational human boundaries

4. **Add reproducibility manifest**
   - One-page summary of build process
   - SHA-256 of final PDF
   - Link to release bundle

---

## 9. Final Assessment

### Strengths
1. **Taxonomy design:** A0-A3 with weakest-missing-condition rule is legitimate contribution
2. **Negative finding discipline:** "No included evidence meets A3" is defensible
3. **AIxCC treatment:** Nuanced, distinguishes competition vs production autonomy
4. **Co-evolution evidence grading:** Documented edges vs plausible coupling vs temporal association
5. **Citation discipline:** Most numerical claims verified against primary sources

### Weaknesses
1. **Internal audit notes in bibliography:** Unprofessional, should be removed
2. **Author metadata error:** fang2024agents lists wrong author
3. **No inter-rater validation:** Classification is load-bearing but single-rater
4. **No sensitivity analysis:** A3 negative finding needs robustness testing
5. **I3 overclaimed:** "Increasingly binding" unsupported by evidence

### Scores

| Dimension | Current | After P0 | After P1 | Potential |
|-----------|---------|----------|----------|-----------|
| Research question | 9.0 | 9.0 | 9.0 | 9.5 |
| Novelty of framing | 9.0 | 9.0 | 9.0 | 9.5 |
| Taxonomy | 8.5 | 8.5 | 9.0 | 9.5 |
| Evidence discipline | 8.0 | 8.0 | 9.0 | 9.5 |
| Citation correctness | 7.0 | 8.5 | 9.0 | 9.5 |
| Methodological rigor | 7.5 | 7.5 | 8.5 | 9.5 |
| Reproducibility | 7.0 | 8.0 | 8.5 | 9.5 |
| Internal consistency | 7.5 | 8.5 | 9.0 | 9.5 |
| Writing/structure | 8.5 | 8.5 | 8.5 | 9.0 |
| **Overall** | **7.8** | **8.3** | **8.8** | **9.5** |

---

## 10. Conclusion

The paper has the ingredients of a very strong SoK. The taxonomy, weakest-missing-condition principle, disciplined A3 negative result, graded co-evolution evidence, and unusually careful AIxCC treatment give this paper a serious foundation.

However, the current artifact has credibility problems:
1. Internal audit notes in bibliography
2. Author metadata error
3. No inter-rater validation
4. No sensitivity analysis
5. I3 overclaimed

**My honest assessment:**
- **Current PDF:** approximately **7.8/10**
- **After P0 fixes only:** approximately **8.3/10**
- **After taxonomy reliability + A3 sensitivity + I3 correction:** potentially **9.5+/10**

The next correct step is a full forensic audit of the exact submission artifact: every citation occurrence, every numerical claim, every taxonomy assignment, every causal edge, every figure/table value, and every conclusion traced back to its evidence and graded for whether the manuscript's wording is stronger than what the source actually establishes.

---

*Report generated: 2026-08-26*
*Status: Major revision required*
*Recommendation: Do not submit until P0 and P1 issues resolved*