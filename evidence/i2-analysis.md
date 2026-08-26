# I2 Analysis v2 — revised per CP2 review

## Headline claim (defensible formulation)
**"We identify multiple documented offense↔defense coupling edges — including one explicit
cross-program causal statement — but the evidence is insufficient to establish field-wide
causal co-evolution."**

## Coupling edges, graded (strongest → weakest)
1. DOCUMENTED RESPONSE (explicit cross-program causality): Project Zero states Big Sleep's
   SQLite target was INSPIRED BY Team Atlanta's AIxCC ASC discovery [PZ post, intro]. Direction:
   competition → industrial research program.
2. DOCUMENTED RESPONSE (maintainer-side): after Atlantis' report on the FTS5 trigram bug, the
   SQLite maintainer patched SIBLING tokenizer functions beyond the report, then revised his own
   patch in b651084 [TA-ASC post + official commits e9b919d5/b651084].
3. DOCUMENTED RESPONSE (institutional/funding): DARPA+ARPA-H $200K/team transition funding;
   Team Atlanta's $2M (50% prize) donation to continuous hunting + OpenAI credits; OpenSSF CRS
   SIG hosting OSS-CRS/FuzzingBrain; legacy stats (62v/26proj/43conf/36patched etc.) [ToB;
   TA-AFC; OpenSSF retro]. B4 exists as funded, governed activity.
4. DOCUMENTED RESPONSE (threat-seeded defense): CVE-2025-6965 discovered via Google Threat
   Intelligence seeding and disclosed pre-exploitation [blog.google; NVD; full report PDF].
   Caveat: threat-intel assertion unverifiable; foiling claim counterfactual.
5. PLAUSIBLE COUPLING: attacker-side agentic adoption (GTG-1002) within ~12 months of defender
   agentic publicity; direction unverifiable without adversary telemetry.
6. TEMPORAL ASSOCIATION ONLY: most benchmark releases trailing industrial demos; press
   arms-race narratives.

## Attempted falsification
- SHARED-CAUSE OBJECTION: frontier-model releases could drive both sides without coupling.
  Counters only LOCAL survival: edges #1/#2 are stated-response with named mechanisms,
  independent of release timing. The objection stands globally — hence the hedged headline.
- CHRONOLOGY-ONLY OBJECTION: weakened by money/institution flows along loop edges (prizes →
  donations → SIG hosting → transition funding).
- RECORD-RELIABILITY THREAT: prize-pool discrepancy ($29.5M announced vs $30.5M distributed) and
  DARPA's corrected vulnerability count show loop bookkeeping noise; co-evolution claims must
  cite corrected primaries, never press figures.

## Boundary conditions
Holds for: documented edges concentrated around the AIxCC hub and Google's program family.
Does NOT establish: continuous field-wide co-evolution; any attacker-side response edge; or
deterrence effects.

## Confidence
Existence of multiple coupling edges: HIGH. Field-wide causal co-evolution: NOT ESTABLISHED
(and not claimed).

## Unresolved questions
U3: methodology for measuring adversary-side responses. U4: whether competition-derived tooling
changes ecosystem patch latency (requires DARPA telemetry not yet released to teams).
