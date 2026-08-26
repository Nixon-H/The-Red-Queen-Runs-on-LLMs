# I1 Analysis v2 — revised per CP2 review

## Headline claim (defensible formulation)
**"Evaluation, deployment, and discourse increasingly measure progress in terms of agentic
autonomy rather than model capability alone."**

Stronger causal interpretation retained explicitly as HYPOTHESIS, not finding:
"Whether this reflects a corresponding shift in underlying capability remains unresolved"
(no in-corpus work ablates autonomy contribution from base-model/scaffold improvement).

## Supporting evidence (dated)
- 2024-H1: evaluation infrastructure dominates (CSEv2/v3, Cybench, NYU CTF Bench): capability
  probes and benchmark harnesses.
- 2024-Q4: FIRST documented production-oriented A2 evidence (Big Sleep, Nov-01, seeded variant
  analysis) alongside pipeline automation incl. triage (OSS-Fuzz Leveling-Up, Nov-20); AIxCC CRSs
  already integrated $\{B1+B2+B3\}$ with real-bug spillover (TA-ASC, Aug-28).
- **2025 = PROLIFERATION year**: production-oriented A2 spreads across independent industrial
  (Argusee May, XBOW Jun), competition (AIxCC finals Aug, human interaction prohibited), and
  production-network experimental (ARTEMIS) systems — four independent sources, not one lineage;
  GTG-1002 (Sep-Nov) shows strongest autonomy jump on the offensive-misuse side, vendor-reported.
- Discourse shift measurable IN-WINDOW via R5/R6/R7 systematizations adopting agency-level
  organization (2026). [R3 is an OUT-OF-WINDOW comparator (Jul 2026): discussed in §2 only,
  excluded from migration evidence per temporal rule.]

## Contradictory evidence / alternative explanations
1. MODEL-SCALE CONFOUND: no corpus work ablates autonomy from base-model gains; TA-AFC found
   GPT-4o-mini often beat larger/reasoning models at patching — success may track scaffold
   engineering, not autonomy level.
2. HUMAN REMOVAL DID NOT OCCUR in defender deployments: PZ curated seeds; Argusee human entry
   points; XBOW policy-mandated review. Part of the gradient is improved disclosure honesty.
3. BENCHMARK-DIFFICULTY ILLUSION: CTF-suite gains may not transfer to wild base rates; only
   isolated n=1 production anecdotes break out (Big Sleep; Buttercup's PoV for a NON-inserted
   vulnerability).
4. SINGLE-SOURCE RISK: GTG-1002 is vendor-reported with hallucination caveats.

## Boundary conditions / formal classification rule adopted
"Autonomy claims are classified by the WEAKEST MISSING condition of the operational definition,
not by headline percentages." Applied: AIxCC CRSs fail the production-environment condition
("no human interaction" ≠ A3); XBOW fails independent-reporting (mandatory human review);
GTG-1002 fails independently-validated reporting.

## Confidence
Measurement/framing-shift component: HIGH. Underlying-capability component: UNRESOLVED
(hypothesis U1 feeds roadmap experiment E1: same-environment longitudinal ablation isolating
autonomy-level contribution).
