# SoK Co-Evolution Paper: Deep Audit Plan

## Executive Summary

Based on detailed preliminary review and analysis of the project structure, this plan addresses all critical issues to achieve a 10/10 reviewer-ready submission. The paper has strong intellectual core but requires artifact correction, citation audit, taxonomy validation, and sensitivity analysis.

## Critical Issues Identified

### Priority 0: Artifact Correctness
1. **PDF Verification**: Need to compile and verify current LaTeX source produces correct output
2. **Bibliography Check**: Verify refs.bib → main.bbl → PDF rendering chain
3. **Section Completeness**: Confirm all sections present in compiled output
4. **Build Reproducibility**: Establish SHA-256 identity for final artifact

### Priority 1: Citation Audit (36 references)
For each of the 36 references in refs.bib:
- Verify source exists and is accessible
- Check author accuracy against primary sources
- Verify title correctness
- Confirm date/venue accuracy
- Assess if cited source supports nearby claim
- Check numerical claim accuracy
- Identify primary vs secondary sources
- Flag overclaims/underclaims

**Key references requiring immediate verification:**
- `fang2024agents`: Author metadata discrepancy (Qi Zhan vs Akul Gupta/Daniel Kang)
- `bigsleep2024naptime`: Verify Project Zero claims
- `darparesults2025`: Verify DARPA numbers (63 synthetic, 54 discovered, 43 patched, 18 real, 11 patches)
- `darpascoring2025`: Verify $8.5M prize pool and 3x patching incentive
- `anthropicgtg2025`: Verify GTG-1002 campaign details

### Priority 2: Taxonomy Validation
- Single-rater classification without inter-rater statistics
- Need: second annotator, blind reclassification sample, or disagreement matrix
- Test boundary cases: XBOW, Big Sleep, AIxCC, ARTEMIS, GTG-1002
- Saturation criterion needs demonstration (two consecutive passes without novelty)

### Priority 3: Negative Result Sensitivity
A3 negative finding needs robustness analysis under:
1. Strict corpus (current inclusion rules)
2. Expanded corpus (borderline vendor claims)
3. Alternative E2 definition (production-like vs production)
4. Different human-intervention interpretations
5. Various evidence thresholds

### Priority 4: Tighten I3 Claim
Current: "Evaluation validity is an increasingly binding constraint..."
Problem: "increasingly" is temporal claim without evidence
Recommendation: Change to mechanistic claim or add temporal evidence

### Priority 5: Co-Evolution Visualization
Edge taxonomy should become first-class visual contribution with:
- Source node, destination node, edge grade
- Mechanism, alternative explanation, falsifier
- Evidence source, edge thickness/style for grade

## Current State Analysis

### Project Structure Verified
```
/home/nixon/RESEARCH CYBER/
├── main.tex (1196 lines - complete source)
├── refs.bib (310 lines - 36 references)
├── main.bbl (374 lines - generated bibliography)
├── sok-coevolution.pdf (12 pages - needs verification)
├── evidence/
│   ├── autonomy-loop-assignments.csv (37 records)
│   ├── claims/
│   ├── i1-analysis.md
│   ├── i2-analysis.md
│   └── i3-analysis.md
├── figures/
│   ├── autonomy-loop-map.tex
│   ├── prisma-flow.tex
│   └── timeline-f3.tex
├── references/pdf/ (24 reference PDFs)
└── archive/modular_sources/ (16 section files)
```

### Section Structure in main.tex
1. Introduction (line 45)
2. Background and Related Work (line 105)
3. Methodology (line 167)
4. The Autonomy × Loop Framework (line 228)
5. Discovery: From Capability Probes to Production-Oriented Agents (line 355)
6. Exploitation and Validation: The AIxCC Case Study (line 460)
7. Patching: The B3 Stream and Its Blind Spots (line 619)
8. The Co-Evolution Loop: Graded Evidence (line 674)
9. Evaluation Validity (line 815)
10. Threats to Validity (line 927)
11. Open Problems: An Experimental Roadmap (line 981)
12. Conclusion (line 1043)
- Appendix A: Included Records (line 1092)
- Appendix B: Search Log Summary (line 1154)
- Appendix C: AIxCC and Industrial Timeline (line 1170)

### Claims Data Available
- `i1-analysis.md`: Analysis of I1 insight
- `i2-analysis.md`: Analysis of I2 insight  
- `i3-analysis.md`: Analysis of I3 insight
- `evidence/claims/`: Supporting evidence files

## Audit Methodology

### Phase 1: Artifact Verification
1. Compile main.tex and verify PDF output
2. Check page count matches expected 17 pages
3. Verify bibliography rendering (no broken references)
4. Confirm all sections present
5. Compare with referenced build `c6655f42a8`

### Phase 2: Citation Audit
For each of 36 references:
1. **Existence**: Source exists and is accessible
2. **Author Accuracy**: Authors match primary source
3. **Title Correctness**: Title matches primary source
4. **Date/Venue Accuracy**: Publication details correct
5. **Claim Support**: Cited source actually supports nearby claim
6. **Numerical Accuracy**: Numbers reproduced correctly
7. **Source Classification**: Primary/secondary/vendor-reported/independent
8. **Overclaim/Underclaim**: Claim strength vs source strength

### Phase 3: Taxonomy Validation
1. Review A0-A3 classification criteria definitions
2. Test each boundary case with explicit reasoning
3. Document classification decisions with evidence
4. Consider inter-rater reliability analysis
5. Test saturation criterion with order analysis

### Phase 4: Sensitivity Analysis
Test A3 negative finding under variations:
1. **Corpus variations**: strict vs expanded inclusion
2. **E2 definition**: production-like vs production
3. **Human-intervention**: different thresholds
4. **Evidence quality**: different evidence standards
5. **Show A3 remains empty under defensible variations**

### Phase 5: Claim Verification
1. Verify I1, I2, I3 insights against evidence
2. Check temporal claims in I3
3. Assess causal claims in co-evolution section
4. Verify all numerical claims in text
5. Check figure/table data matches text claims

### Phase 6: Structure and Writing
1. Verify section structure matches description
2. Check figure/table integrity
3. Assess writing quality and clarity
4. Review logical flow
5. Check for AI writing patterns

## Expected Deliverables

1. **Comprehensive Audit Report** with:
   - Every factual claim and its citation
   - Source verification results
   - Numeric verification results
   - Claim-strength assessment
   - Overclaim/underclaim flags
   - Citation metadata errors
   - Taxonomy consistency check
   - Figure/table audit
   - Line-by-line revision recommendations

2. **P0/P1/P2 Revision Checklist**

3. **Final Acceptance-Style Reviewer Report**

4. **Updated Paper with All Corrections**

## Success Criteria

The paper will be considered 10/10 reviewer-ready when:
1. All 36 citations verified and accurate
2. Bibliography complete and properly formatted
3. All 12 sections + 3 appendices present
4. Taxonomy validated with explicit classification reasoning
5. Sensitivity analysis demonstrates A3 robustness
6. I3 claim properly supported or weakened
7. Co-evolution visualization implemented
8. All numerical claims verified
9. Writing quality meets publication standards
10. Artifact pipeline reproducible with SHA-256 identity

## Build History Analysis (from CHANGES.md)

### Key Milestones
1. **CP3 assembly**: 12 pages, basic structure
2. **CP4-HOLD reviews**: 14-15 pages, multiple corrections
3. **CP4 RELEASE**: Build 858baa831f, 15 pages
4. **Format revision**: 15 pages, single self-contained source
5. **Submission-format revision**: 16 pages, S&P 2027 conformance
6. **Content expansion**: 17 pages, new subsections added
7. **CSE author lists**: 17 pages, corrected 21/13/13 authors
8. **Figure completion**: 18 pages, F1/F3 added
9. **Final polish**: 18 pages, build a02c8e4eb2
10. **CVE restoration**: 18 pages, build 7c2fa7cc3f (CURRENT)

### Critical Findings
- **Broken references [7], [8], [9]**: CHANGES.md mentions "Meta-AI placeholders replaced with title-page-verified author lists" in content expansion section
- **Page count**: Current build is 18 pages (not 12 as user reported)
- **Build hash**: Current is 7c2fa7cc3f (not c6655f42a8 as user mentioned)
- **CSE author lists**: Corrected to 21/13/13 (not 22/12/12)

### Immediate Verification Needed
1. **Compile main.tex** and verify PDF output matches expected 18 pages
2. **Check bibliography rendering** - verify no broken references
3. **Verify section structure** - confirm all subsections present
4. **Check figure/table integrity** - F1, F3, Table IV, Table V

## Citation Audit Status (from reference-audit.md)

### Completed Verification
- **Total references**: 38 (all cited)
- **OA PDFs downloaded**: 22 (+1 GTG report = 23)
- **HTML/primary sources**: 10 (+2 DARPA remote-verified)
- **Metadata-only entries**: 2 (R4 CSUR, R6 TOSEM)
- **BibTeX errors**: 0 (post-fix)
- **Missing citations**: 0
- **URL resolution**: 36/36 resolvable

### Key Spot Checks Passed
1. Fang 87%/7%/0% baselines → PASS
2. XBOW funnel 1060/130/303/33/125/208/209/36 → PASS
3. BigSleep seriesBestIndex/generate_series/Gemini1.5/AFL150CPUh/no-CVE → PASS
4. AIxCC finals aggregates 63/54(86%)/43(68%)/18real/11patches → PASS
5. Scoring incentive 3x + $8.5M pool → PASS
6. Team costs $103.3K/$39.6K/$31.8K → PASS
7. Buttercup 28v+19p / non-reasoning LLMs / $181-per-point → PASS
8. ASC SQLite bug + official fix e9b919d5 + sibling patching → PASS
9. GTG 80-90%/30 targets/weakest-missing handling → PASS
10. OSS-Fuzz 26 vulns/CVE-2024-9143/steps1-4 → PASS
11. CodeRover-S mechanism quote → PASS
12. Argusee entry-points quote + CVE-2025-37891 → PASS
13. OpenSSF legacy stats → PASS
14. PrimeVul claims → PASS*

### Known Residual Items
1. DARPA sources: PRIMARY-official via independent web verification; local fetch blocked
2. Three agent-lineage bib notes need final CP4 sweep
3. NYU CTF version divergence documented
4. Uncited-at-compile entries: none expected

## Claims Analysis Status

### I1 Analysis (Complete)
- **Claim**: "Evaluation, deployment, and discourse increasingly measure progress in terms of agentic autonomy rather than model capability alone"
- **Evidence**: Dated timeline from 2024-H1 to 2026
- **Contradictions**: Model-scale confound, human removal didn't occur, benchmark-difficulty illusion, single-source risk
- **Confidence**: Measurement/framing-shift: HIGH; Underlying-capability: UNRESOLVED

### I2 Analysis (Complete)
- **Claim**: "Multiple documented offense↔defense coupling edges exist — including one explicit cross-program causal statement — but the evidence is insufficient to establish field-wide causal co-evolution"
- **Evidence**: 6 graded edges (D1-D4 documented, P1 plausible, temporal only)
- **Falsification**: Shared-cause objection survives globally; defeated only for D1/D2
- **Confidence**: Existence of coupling edges: HIGH; Field-wide causal co-evolution: NOT ESTABLISHED

### I3 Analysis (Complete)
- **Claim**: "Evaluation validity is an increasingly binding constraint on LLM-security capability claims"
- **Evidence**: Three-tier progression (information leakage → dataset leakage → oracle manipulation)
- **Boundary conditions**: STRONG for static detection; MODERATE for agentic CTF
- **Unresolved**: U5 (contamination-controlled design), U6 (time-split protocol), U7 (decision-impact study)

## Immediate Actions Required

### Phase 1: Artifact Verification (CRITICAL)
1. **Compile main.tex** and verify PDF output
   - Expected: 18 pages total
   - Expected: 0 LaTeX errors, 0 undefined citations, 0 overfull ≥10pt
   - Expected: Build hash 7c2fa7cc3f
2. **Verify bibliography chain**
   - refs.bib → main.bbl → PDF rendering
   - Check for broken references [7], [8], [9]
   - Verify CSE author lists (21/13/13)
3. **Check section structure**
   - Verify all 12 sections + 3 appendices present
   - Confirm subsections "Architecture Lessons and the Epistemics of A3" (§6) and "Institutional Response" (§8)
4. **Verify figures/tables**
   - F1 PRISMA flow (§3)
   - F3 capability-timeline (§8)
   - Table IV (autonomy-loop-matrix)
   - Table V (timeline)

### Phase 2: Citation Audit (PRIORITY 1)
1. **Verify key references** against primary sources
   - fang2024agents: Author metadata discrepancy
   - bigsleep2024naptime: Project Zero claims
   - darparesults2025: DARPA numbers
   - darpascoring2025: $8.5M prize pool
   - anthropicgtg2025: GTG-1002 details
2. **Check numerical claims** in text against sources
3. **Verify author accuracy** for all 38 references
4. **Confirm date/venue accuracy**

### Phase 3: Taxonomy Validation (PRIORITY 2)
1. **Review A0-A3 classification criteria**
2. **Test boundary cases**:
   - XBOW: A2 (policy-mandated pre-submission review)
   - Big Sleep: A2 (human-curated seed set)
   - AIxCC: A2/E1 (competition environment)
   - ARTEMIS: A2 (comparison arm)
   - GTG-1002: uncertain (vendor-reported)
3. **Assess construct validity** of thresholds
4. **Document classification decisions**

### Phase 4: Sensitivity Analysis (PRIORITY 3)
Test A3 negative finding under:
1. **Corpus variations**: strict vs expanded inclusion
2. **E2 definition**: production-like vs production
3. **Human-intervention**: different thresholds
4. **Evidence quality**: different evidence standards
5. **Show A3 remains empty** under defensible variations

### Phase 5: Claim Verification (PRIORITY 4)
1. **Verify I1, I2, I3 insights** against evidence
2. **Check temporal claims** in I3
3. **Assess causal claims** in co-evolution section
4. **Verify all numerical claims** in text
5. **Check figure/table data** matches text claims

### Phase 6: Structure and Writing (PRIORITY 5)
1. **Verify section structure** matches description
2. **Check figure/table integrity**
3. **Assess writing quality** and clarity
4. **Review logical flow**
5. **Check for AI writing patterns**

## Expected Deliverables

1. **Comprehensive Audit Report** with:
   - Every factual claim and its citation
   - Source verification results
   - Numeric verification results
   - Claim-strength assessment
   - Overclaim/underclaim flags
   - Citation metadata errors
   - Taxonomy consistency check
   - Figure/table audit
   - Line-by-line revision recommendations

2. **P0/P1/P2 Revision Checklist**

3. **Final Acceptance-Style Reviewer Report**

4. **Updated Paper with All Corrections**

## Success Criteria

The paper will be considered 10/10 reviewer-ready when:
1. All 38 citations verified and accurate
2. Bibliography complete and properly formatted
3. All 12 sections + 3 appendices present
4. Taxonomy validated with explicit classification reasoning
5. Sensitivity analysis demonstrates A3 robustness
6. I3 claim properly supported or weakened
7. Co-evolution visualization implemented
8. All numerical claims verified
9. Writing quality meets publication standards
10. Artifact pipeline reproducible with SHA-256 identity

---

*Plan created: 2026-08-26*
*Status: Ready for execution*
*Priority: Critical - artifact verification blocking audit*
*Current build: 7c2fa7cc3f (18 pages)*
*Expected build: 7c2fa7cc3f (18 pages)*