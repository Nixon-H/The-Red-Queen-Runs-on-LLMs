# I3 Analysis v2 — revised per CP2 review

## Headline claim (defensible formulation)
**"Evaluation validity is an increasingly binding constraint on LLM-security capability claims:
measured information-dependence, dataset-level invalidity, and oracle manipulation each
materially change reported conclusions, and these measures increasingly participate in ranking,
funding-allocation, and deployment decisions (rankings: directly evidenced via HackerOne/AIxCC scoring; funding: AIxCC prize+transition programs; deployment-decision influence: plausible but not yet documented case-by-case)."**
(The absolute form "THE field's binding constraint" is NOT claimed; proving it would require
evidence that validity failures actually overturned a specific ranking/funding/deployment
decision — none is documented in-corpus.)

## §9 organizing progression (reviewer-endorsed structure)
**Information leakage → dataset leakage → evaluation-oracle manipulation**

### Tier 1 — information leakage (controlled intervention, MEASURED)
Fang et al.: GPT-4 one-day exploitation 87% WITH CVE descriptions vs 7% WITHOUT; all baselines
0% [local TXT lines 29–33, 62, 74–76, Table 3]. A single information-supply variable swings the
headline number by ~12×. Every capability claim must therefore carry its supplied-knowledge
condition.

### Tier 2 — dataset leakage / label invalidity (MEASURED at dataset level)
PrimeVul: label noise, duplication, and pre-split temporal exposure inflate prior detection
SOTA; paired chronological evaluation collapses strong-model performance [paper].
Risse & Böhme ("Top Score on the Wrong Exam") systematizes the detection-benchmark critique.
Corpus-side exposure: CTF suites draw on publicly written-up challenges (V1 plausible;
quantification pending roadmap experiment).

### Tier 3 — evaluation-oracle manipulation (OPERATIONAL, documented)
AIxCC patch validation: PoV-rerun oracle accepts mitigation-gaming patches (MTE/PAC recompiles;
broad catch(Exception)); accuracy modifiers exist because wrong patches were common
(Theori 44.4% → modifier 0.9044 vs PoV-validated 91.27% → 0.9999) [TA-AFC]. V4 exemplar: the
winning CRS was nearly killed by a directory-prefix string heuristic ('fuzz' vs 'ossfuzz').
Saturation datum: Argusee 100% on CyberSecEval-2 buffer-overflow cases while requiring
human-supplied entry points.

## Separated category — administrative record instability (NOT measurement-validity evidence)
DARPA's post-hoc correction of the finals vulnerability count (70→63) evidences reporting/
bookkeeping instability in program administration. It is relevant to source-reliability
discipline (cite corrected primaries) but is methodologically DISTINCT from contamination or
oracle-invalidity findings and must not be presented alongside Fang/PrimeVul as equivalent
validity evidence.

## Submission-funnel statistic (corrected wording per review)
XBOW's ~1,060 submissions resolved into 130 fixed, 303 triaged, **208 duplicates + 209
informative (~39% falling into duplicate/informative categories rather than new/resolved
findings)**, plus 33 new/125 pending/36 N.A. Duplicates and informatives are not automatically
"noise": duplicates may indicate discovery overlap; informative may reflect program-policy
exclusions (the post itself cites policies banning cache-poisoning reports). The analytic point
is a METRIC-DEFINITION problem: leaderboard-style counting treats these heterogeneous categories
uniformly, so rank is not decomposable into discovery quality without category-aware accounting.

## Attempted falsification
- "Generic academic complaint": countered by decision-coupling — competition scoring, vendor
  leaderboards, and national funding consume exactly these measures; their noise moves money.
- "Controls already solve it": partial — paired evals (PrimeVul), accuracy modifiers (AIxCC),
  external triage (HackerOne programs), third-party reproduction (Ada Logics ×27) exist and
  work, but each covers ONE axis; no corpus artifact controls all five validity axes for agentic
  tasks, and agent-era contamination quantification is absent.

## Boundary conditions
STRONG for static detection benchmarks (measured, replicated). MODERATE for agentic CTF
(mechanisms documented, magnitudes unquantified). Would be OVERREACH to extend to "all results
invalid" — controlled-condition results survive (Fang's 7% condition; PoV-validated patches).

## Confidence / unresolved
HIGH that validity issues flip conclusions in the detection subfield; MODERATE elsewhere.
U5: contamination-controlled agentic benchmark design. U6: time-split protocol quantifying
writeup-exposure inflation. U7 (new): decision-impact study — did any documented
ranking/funding/deployment decision change upon validity correction? (Required to upgrade
"increasingly binding" to "binding".)
