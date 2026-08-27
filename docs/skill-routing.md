# skill-routing.md — SoK execution routing (PHASE 0 output)

Generated 2026-08-26. Governing authority order:
1. Master SoK specification (user prompt) — WHAT to produce, all hard gates.
2. `deep-research` skill (systematic-review mode) — HOW the PRISMA/search/verification
   mechanics are executed.
3. Remaining agents — supporting roles as routed below.
No new parallel workflow is created; overlapping duties defer to the authoritative row.

| skill / agent | tool location | purpose in this SoK | stage used | required inputs | expected outputs |
|---|---|---|---|---|---|
| deep-research (skill) | academic-research-skills/deep-research/SKILL.md (LOADED into session) | systematic-review protocol, PRISMA discipline, source-quality hierarchy, failure-path handling | PHASES 2–5, CP1 | spec RQs, seed corpus, search strings | search-log.md, current corpus/audit records, screening decisions |
| bibliography_agent | .../deep-research/agents/bibliography_agent.md | reproducible multi-database search strategy + annotated records | PHASE 2 | query strings, window filters | search-log.md entries, candidate ID pool |
| source_verification_agent | .../source_verification_agent.md | evidence grading (primary/secondary/claimed), predatory/COI flags, claim-vs-source checks | PHASES 3–4, 13 | fetched full texts, vendor pages | references/txt/*.txt evidence extracts, manifest.csv verification columns |
| risk_of_bias_agent | .../risk_of_bias_agent.md | bias domains adapted from RoB/ROBINS-I → our validity taxonomy V1–V5 | PHASE 5 | included-work records | per-work validity_concerns fields, §9 material |
| synthesis_agent | .../synthesis_agent.md | cross-source integration, contradiction resolution, gap mapping | PHASES 7, 9 | verified corpus YAMLs | i1/i2/i3-analysis.md, co-evolution chain |
| timeline_extraction_agent | .../timeline_extraction_agent.md | dated event extraction for Appendix C / F3 | PHASE 12 | industrial primaries, competition docs | evidence/timelines/aixcc-industrial.csv |
| devils_advocate_agent | .../devils_advocate_agent.md | mandatory falsification attacks on I1–I3, taxonomy, causal claims | PHASE 11 (3 checkpoints) | draft sections + evidence ledger | review/devils-advocate.md |
| editor_in_chief_agent | .../editor_in_chief_agent.md | Q1-editor internal review verdict pre-CP3 | PHASE 11 | full draft | review/internal-review.md |
| ethics_review_agent | .../ethics_review_agent.md | dual-use screening of exploit-detail exposition; AI-disclosure compliance | PHASES 9, 15 | draft | ethics notes in venue-compliance.md |
| report_compiler_agent | .../report_compiler_agent.md | section assembly discipline, writing-quality check | PHASES 8–9, 12 | outline, framework, tables/figs | modular .tex sections |
| meta_analysis_agent | n/a | NOT ROUTED — no quantitative pooling in this SoK (heterogeneous evidence classes); documented decision | — | — | — |
| socratic_mentor_agent | n/a | NOT ROUTED — RQs are fixed by spec; no elicitation needed | — | — | — |
| monitoring_agent | deferred | post-CP4 literature monitoring only | optional post-release | — | — |
| academic-paper (skill) | academic-research-skills/academic-paper/SKILL.md | paper structure, argument construction, LaTeX conventions, citation placement rules | PHASES 8–9, 12 (load at CP2 approval) | approved framework + outline | sections/*.tex |
| academic-paper-reviewer (skill) | .../academic-paper-reviewer/SKILL.md | multi-persona peer-review simulation as CP3 pre-check complement | PHASE 11 end | compiled draft | review notes feeding CHANGES.md |
| academic-pipeline (skill) | .../academic-pipeline/SKILL.md | research-state management, passport/integrity controls across phases | continuous (light use; master spec's checkpoint system supersedes its own gating) | artifacts on disk | state consistency checks |
| obsidian/wiki family (~30 skills) | ~/.opencode/skills/* | NOT ROUTED — this project targets IEEE S&P LaTeX deliverables, not a vault KB. Documented non-use decision. | — | — | — |
| claude-code/ dir | ./claude-code | NOT ROUTED — upstream agent-tooling repo, no research content | — | — | — |

Routing decisions recorded: (a) deep-research's IRON RULE "gray zone = FAIL" is adopted
verbatim for reference integrity; (b) its APA-report output format is OVERRIDDEN by the
spec's IEEE S&P LaTeX structure; (c) devil's-advocate 3-checkpoint rule maps to spec §18
falsification tests at CP2, PHASE 11, and CP3.
