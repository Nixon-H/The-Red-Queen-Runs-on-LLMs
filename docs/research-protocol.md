# research-protocol.md — formal research configuration (PHASE 1)

## Title
SoK: From Assistive to Autonomous — The Co-Evolution of LLM-Driven Vulnerability Discovery,
Exploitation and Patching

## Temporal window & background rule
- Inclusion window: publications/system events 2024-01-01 .. 2026-06-30.
- Pre-2024 material: BACKGROUND only (historical provenance; e.g., InterCode-CTF,
  CyberSecEval v1, PentestGPT). Never load-bearing for capability claims.
- Post-window material: EXCLUDED unless verifying a historical fact or marked [OUT-OF-WINDOW]
  (e.g., OpenSSF retro 2026-05-12 is IN-window; DSN 2026 acceptance note is metadata).

## Research questions
RQ1 assistive→autonomous shift in discovery (2024→Jun 2026)?
RQ2 how are discovery/exploitation-validation/patching/redeployment integrated into a loop?
RQ3 evidence that academic+competition+industrial tracks CO-EVOLVE (vs independent progress)?
RQ4 how much reported capability survives V1–V5 validity controls?
RQ5 which empirical gaps block credible autonomous-production claims?
RQ6 what experimental roadmap resolves those gaps most efficiently?

## Inclusion criteria
peer-reviewed OR influential preprint OR documented industrial system AND relevant to ≥1 cell
of the A(0–3)×B(1–4) framework.

## Exclusion criteria
duplicate venue versions; pure malware-dev guides; blog-only material without documented
system/result; out-of-window items (unless background/historical-provenance); press claims not
present in any primary artifact.

## Databases searched
arXiv (UI boolean, date-filtered), DBLP API; IEEE Xplore/ACM DL/USENIX/NDSS via chaining +
official indexes (API access unavailable — logged limitation); Google Scholar: manual chaining
only. Exact strings + hit counts: see search-log.md.

## Source-quality hierarchy (spec §3.5, adopted)
PRIMARY (full text inspected: arXiv/darpa/projectzero/blog.google/xbow/trailofbits/usenix-
index/nyu-llm-ctf/aclanthology/oaklandsok) > registry primary (NVD) > SECONDARY (press/
aggregator/snippet). SECONDARY never load-bearing.

## Quality rubric (every included work)
reproducibility 0–3 · baseline rigor 0–3 · artifact availability 0–3; plus benchmark
provenance, data availability, evaluator independence, public-vuln reuse flag, label/metadata
exposure flag.

## Autonomy axis (assign HIGHEST level DOCUMENTED BEHAVIOR supports)
A0 assistive · A1 pipeline-orchestrated · A2 semi-autonomous task/CTF agent ·
A3 autonomous production hunter. Branding ("agentic", "fully autonomous") insufficient alone;
record who picks actions/tools/targets, who validates, who reviews/submits/applies patches,
supervision mode, internet access. Insufficient evidence ⇒ A?[uncertain] or multi-level.

## Loop axis
B1 discovery · B2 triage/validation/exploitation · B3 patching/repair ·
B4 redeployment/regression/monitoring. Multi-cell allowed with justification.

## Evaluation-validity taxonomy (first-class extraction field)
V1 data leakage · V2 temporal leakage/hindsight · V3 label-oracle leakage ·
V4 environment leakage · V5 outcome-definition noise. Quantify where measurable else
confirmed/plausible/unresolved/unsupported.

## Evidence policy
claimed vs independently-reproduced distinguished everywhere; vendor stats = CLAIMED;
Ada Logics AIxCC pass = third-party verification exemplar; every numeric claim maps to
claim-verification.csv row with locator; [TO-VERIFY] must be zero before CP4.

## Corpus saturation rule
Saturation = further passes cease yielding NEW works/autonomy levels/loop positions/benchmark
families/validity failure modes/competition-industrial evidence/contradictions. Minimum passes:
initial DB search; backward chaining; forward chaining; industry/competition targeted;
benchmark targeted; contamination targeted. Rationale recorded in corpus/saturation-rationale.md.

## Checkpoints (hard stops, spec §14)
CP1 corpus saturation → approval; CP2 §4 framework only → approval; CP3 full LaTeX+gates →
approval; CP4 final release after freeze/venue audit.

## Canonical record schema
corpus/included/<key>.yaml with fields per PHASE 4 list (bib identity … limitations).
Exclusions: corpus/excluded/. Aggregate: corpus-summary.csv. Claims ledger: claim-verification.csv.

## AMENDMENTS v2 (2026-08-26, post-reviewer-rejection of CP1 v1)

### Multi-stream evidence architecture (mandatory accounting)
The SoK corpus is NOT one PRISMA flow. Three streams are tracked separately and only summed
at the top level:
- Stream A (academic literature): classic identified→dedup→screened→full-text→included flow.
- Stream B (competition/industrial/foundation documents): targeted acquisition, quote-level
  extraction; no database-flow denominators claimed.
- Stream C (registry/documentary): CVE/NVD records; existence-verified, not screened.
Any "included" aggregate MUST be decomposed by stream in every table/report.

### Normalized record schema (taxonomy ≠ metadata)
Every included record carries SEPARATE fields:
autonomy_level ∈ {A0,A1,A2,A3,uncertain,n-a}; loop_position ∈ {B1,B2,B3,B4,multi,n-a};
evidence_class; scope_class; access_status ∈ {oa-pdf, html-primary, paywalled, metadata-only}.
Axis counts use ONLY autonomy_level × loop_position. Research buckets (e.g., "A2-production")
may exist only as autonomy_note strings.

### Mandatory wording discipline (A3-zero finding)
The finding must be written ONLY as:
"No included evidence met our operational definition of A3."
FORBIDDEN phrasings: "no autonomous hunters exist", "A3 = zero", or any existential/universal
formulation. The claim is bounded by this corpus+window+definition. Same discipline applies to
all capability claims: preserve supplied-information conditions, human-review qualifiers,
vendor-reported status.

### Provenance-type discipline
references/manifest.csv provenance_type distinguishes: PDF+TXT / HTML+EXTRACT /
HTML+GREP-VERIFIED / WEBFETCH-FULLTEXT / METADATA-ONLY / REPO-METADATA-ONLY.
Only PDF+TXT and WEBFETCH/HTML-FULLTEXT count as full-text assessed; METADATA-ONLY rows can
never support load-bearing claims.

## AMENDMENTS v3 (2026-08-26, CP2 revision pass — reviewer 14-point correction)

1. TEMPORAL SCOPE FIELD: every record carries temporal_scope = in-window | background | out-of-window.
   Primary A x B counts, migration percentages, and center-of-gravity claims use
   temporal_scope = in-window ONLY. Background anchors remain visible in a separate figure band.
2. LOOP SET REPRESENTATION: Axis B remains strictly {B1,B2,B3,B4}. Multi-phase systems carry
   loop_position as a SET (e.g., "B1+B2+B3"); B-multi is a visualization overlay (spanning
   arrows), never an axis value. Evaluation suites probing thematically use "{B1+B2}(probed)".
3. DECISION-AUTHORITY TEST (centerpiece A-axis definition): "Who chooses the next action?"
   Model acts only inside a fixed controller = A1; model selects actions/tools within task = A2;
   independent planning+execution+validation+reporting in realistic production environment = A3
   (four-verb test). Explicit corollary: no-human-interaction != A3; tool use != autonomy.
4. WEAKEST-MISSING-CONDITION RULE: autonomy claims are classified by the weakest missing
   condition of the operational definition, never by headline percentages (formalizes the
   GTG-1002/XBOW/AIxCC handling).
5. LOOP-EVIDENCE-RECORD CONCEPT: sources documenting a system's B4 transition are typed as
   loop-transition-documentation with documents_system + documented_transition fields;
   they inherit attributed autonomy from the documented system (e.g., Big Sleep A2) rather than
   being scored n-a/B4 as if autonomous actors themselves.
6. OUT-OF-WINDOW COMPARATOR DISCIPLINE: R3 (Jul 2026) is discussed in related work but excluded
   from all in-window migration/discourse-shift evidence. publication_scope vs
   related_work_scope kept distinct in prose.
7. CLAIM WORDING LEDGER (binding for §§5-12):
   - I1 headline: "Evaluation, deployment, and discourse increasingly measure progress in terms
     of agentic autonomy rather than model capability alone." Capability-substance reading =
     hypothesis only.
   - I2 headline: "Multiple documented offense-defense coupling edges; insufficient evidence for
     field-wide causal co-evolution."
   - I3 headline: "Evaluation validity is an increasingly binding constraint..." (absolute form
     reserved pending decision-impact evidence U7).
   - A3 finding: ONLY "No included evidence met our operational definition of A3."
   - XBOW funnel: "208 duplicates + 209 informative (~39% of submissions) fell into duplicate/
     informative categories rather than new/resolved findings" -> metric-definition problem;
     'noise' wording prohibited.
   - DARPA 70->63: administrative record instability category; never presented as equivalent to
     measured contamination/oracle findings.

## AMENDMENTS v4 (2026-08-26, CP2 lock pass — final three changes)

1. UNIT-OF-ANALYSIS TAXONOMY: every record carries unit_type in {system, experiment, benchmark,
   dataset, survey(systematization), program-record, incident-documentation, measurement-study,
   documentary-source, registry, methodological-paper}. ONLY system/experiment/incident-
   documentation records receive A-levels. Surveys/systematizations carry documented_systems
   lists (R7 lists Atlantis/Buttercup/Theori-SRS/RoboDuck/FuzzingBrain/Lacrosse/Shellphish and
   is n/a on both axes). Benchmarks carry probed_loop_phases and/or embedded_scaffold fields
   instead of axis placement. Terminology: "in-window classified records" for autonomy-bearing
   set; never "primary cells" as shorthand implying all are systems.
2. AXIS SEMANTICS PURITY: loop_position records a SYSTEM's actual offense/defense operation.
   Thematic capability coverage of benchmarks = probed_loop_phases (off-axis); dataset domain =
   task_domain. CSEv2/v3: probed_loop_phases={B1,B2}; PrimeVul: task_domain=B1 detection,
   loop_position=n/a.
3. ENVIRONMENT CLASSES (A3 operationalization): E0 synthetic/benchmark; E1 realistic-sandboxed/
   competition; E2 production or production-like external target. A3 requires independent
   P/E/V/R AND E2. AIxCC CRSs = A2 under E1; BigSleep/XBOW/Argusee/ARTEMIS/GTG targets = E2.
4. VISUAL GRAMMAR: multi-phase coverage drawn with neutral connectors labeled "documented
   multi-phase coverage"; directional arrows reserved for DOCUMENTED transition flows only.
5. DECISION-IMPACT FIELD (I3 upgrade path): extraction field recording whether a validity issue
   demonstrably changed a ranking/funding/deployment decision (U7); I3 wording stays
   "increasingly binding constraint" until U7 yields documented cases.

## AMENDMENTS v5 (CP3 gate definition)
1. CITATION-SUPPORT GATE (all seven must hold): key exists in refs.bib AND metadata verified
   against authoritative record AND URL/DOI resolves AND cited source-version verified AND
   source supports the cited proposition AND placement adjacent to proposition AND material
   qualifiers preserved. Structural key-existence alone is insufficient.
2. PROVENANCE WORDING: use 'PRIMARY - official page, independently web-verified [date];
   local automated fetch unavailable'. 'Supervisor-verified' is not an evidentiary category.
3. PRIZE-SCOPE DISCIPLINE: $29.5M = cumulative program commitment (2024 announcement);
   $8.5M = final competition pool (scoring guide); $30.5M = distributed across rounds (OpenSSF).
   Never present as competing totals of one boundary.
4. UNCITED-REFERENCE POLICY: entries enter the final bibliography only by deliberate role
   (background / related work / validity evidence / ecosystem evidence / methodological
   contrast). Non-contributing entries are removed at the final audit.
5. ADMINISTRATIVE RECORD CORRECTION is the standing term for primary-source count revisions
   (e.g., 70->63); primary-source preference does not eliminate version/date-aware verification.
