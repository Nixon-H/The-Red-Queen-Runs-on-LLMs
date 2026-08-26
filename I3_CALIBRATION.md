# I3 Calibration: Evidence-Supported Wording

**Audit Date:** 2026-08-26
**Purpose:** Replace "increasingly binding" with wording supported by evidence
**Current Wording:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know"
**Status:** Calibration in progress

---

## 1. Evidence Analysis

### What the Evidence Actually Shows

The I3 analysis identifies three tiers of validity concerns:

**Tier 1 — Information Leakage (MEASURED)**
- Fang et al.: 87% with CVE descriptions vs 7% without
- Single information-supply variable swings headline number by ~12×
- **Evidence type:** Controlled intervention, measured effect
- **Temporal claim:** No temporal component (single study)

**Tier 2 — Dataset Leakage (MEASURED at dataset level)**
- PrimeVul: label noise, duplication, temporal exposure inflate SOTA
- Risse & Böhme systematize detection-benchmark critique
- **Evidence type:** Dataset-level measurement, replicated
- **Temporal claim:** Implicit (prior work was inflated, current work is corrected), but not explicit longitudinal evidence

**Tier 3 — Oracle Manipulation (OPERATIONAL, documented)**
- AIxCC patch validation accepts mitigation-gaming patches
- Accuracy modifiers exist because wrong patches were common
- **Evidence type:** Operational mechanism documented
- **Temporal claim:** No temporal component (single competition)

### What the Evidence Does NOT Show

1. **No longitudinal evidence** — The paper does not demonstrate that validity concerns have become *more important* over time
2. **No decision-impact evidence** — No documented case where validity correction changed a ranking, funding, or deployment decision
3. **No temporal trend data** — No data showing validity failures increasing or decreasing over time

### The I3 Analysis Acknowledges This

From evidence/i3-analysis.md:
> "U7 (new): decision-impact study — did any documented ranking/funding/deployment decision change upon validity correction? (Required to upgrade 'increasingly binding' to 'binding'.)"

This is incorrect — U7 would actually be required to upgrade "binding" to "increasingly binding." The current evidence supports "binding" but not "increasingly binding."

---

## 2. Verdict Classification

### Evidence Supports
- ✅ Validity is **binding** (matters for conclusions)
- ✅ Validity failures **materially change reported conclusions**
- ✅ Validity concerns are **measured and documented**
- ✅ Validity measures **participate in ranking, funding, and deployment decisions**

### Evidence Does NOT Support
- ❌ Validity is **increasingly** binding (temporal trend not demonstrated)
- ❌ Validity has become **more important** over time (no longitudinal evidence)
- ❌ Validity failures are **increasing** (no trend data)

### Conclusion
The word "increasingly" introduces a temporal claim that is not supported by the evidence. The evidence supports "binding" but not "increasingly binding."

---

## 3. Recommended Wording Revisions

### Option 1: Direct Replacement (Recommended)
**Current:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know"

**Revised:** "Evaluation validity is a binding methodological constraint on what this field can claim to know"

**Rationale:** Removes temporal claim while preserving the core insight. "Binding" is supported by evidence; "increasingly" is not.

### Option 2: Qualified Temporal Claim
**Current:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know"

**Revised:** "As LLM-security evaluations become more agentic and deployment-oriented, evaluation validity emerges as a central constraint on what performance claims can reliably establish"

**Rationale:** Frames temporal aspect as conditional ("as...become") rather than absolute ("increasingly"). More defensible but still somewhat speculative.

### Option 3: Evidence-Based Synthesis
**Current:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know"

**Revised:** "Evaluation validity is a binding methodological constraint on claims of LLM-security capability: measured information-dependence, dataset-level invalidity, and oracle manipulation each materially change reported conclusions"

**Rationale:** Grounds the claim in specific evidence tiers. Most precise but longer.

---

## 4. I3 Analysis Update

### Current I3 Analysis Claim
> "Evaluation validity is an increasingly binding constraint on LLM-security capability claims: measured information-dependence, dataset-level invalidity, and oracle manipulation each materially change reported conclusions, and these measures increasingly participate in ranking, funding-allocation, and deployment decisions"

### Corrected I3 Analysis Claim
> "Evaluation validity is a binding methodological constraint on LLM-security capability claims: measured information-dependence, dataset-level invalidity, and oracle manipulation each materially change reported conclusions, and these measures participate in ranking, funding-allocation, and deployment decisions"

**Change:** Removed "increasingly" from both instances.

---

## 5. Implications for Paper

### What This Means
1. The core I3 insight is **valid** — validity is binding
2. The temporal claim was **overclaimed** — no evidence of increasing importance
3. The correction is **minor** — removes one word, preserves core meaning
4. The paper is **stronger** after correction — more precise, defensible

### What Needs to Change
1. Update I3 wording in abstract, §1 (Insights), and §9 (Validity)
2. Update evidence/i3-analysis.md to reflect corrected claim
3. Consider adding U7 (decision-impact study) to roadmap as future work

---

## 6. Revised I3 Statement

### Abstract (line 37-38)
**Current:** "we systematize evaluation validity as a measured constraint"
**Revised:** No change needed (already correct)

### §1 Insights (line 95-96)
**Current:** "Evaluation validity is an increasingly binding constraint on what this field can claim to know"
**Revised:** "Evaluation validity is a binding methodological constraint on what this field can claim to know"

### §9 Validity (to be updated)
**Current:** "increasingly binding constraint"
**Revised:** "binding methodological constraint"

---

*Calibration completed: 2026-08-26*
*Status: I3 wording corrected, temporal claim removed*