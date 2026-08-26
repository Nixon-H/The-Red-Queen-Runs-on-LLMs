# CHANGES.md
## 2026-08-26 — CP3 assembly pass
- Assembled main.tex (IEEEtran conference, anonymous); integrated F2 map, T2/T4/T5/T7 tables,
  appendices A–C; fetched IEEEtran.cls/bst from CTAN into project dir for reproducible build.
- Fixed refs.bib structural error in tosemslr2026 (missing brace from earlier regex edit) that
  aborted BibTeX; added missing rissebohme2024 entry cited by §§2/9/10.
- Killed all >10pt overfull boxes via columnwidth resizebox on wide tables + framework figure;
  figure ctx bands given text-width to prevent node overflow.
- Final gates: pdflatex+bibtex+2xpdflatex clean; 0 undefined citations/references; 0 overfull
  >=10pt; 12 pages; output sok-coevolution.pdf.

## 2026-08-26 — Post-PHASE8-review corrections (P0/P1)
- P0: R7 author list corrected to authoritative 23-author arXiv metadata (Lee, Wang added;
  McDaniel recased); bib note documents title-page-rendering divergence.
- P1: NYU CTF kept at local-version title ("Bench") with documented arXiv retitle ("Dataset").
- P1: DARPA restored as PRIMARY for finals aggregates (darparesults2025, darpascoring2025);
  §6 aggregates restored; C32 CLOSED. Superseded near-duplicate entries removed (38 total).
- P1 wording: corpus-bounded "only included setting"; "largest competition-based stress test";
  PoV semantics ("behavior only for the tested proof"); maintainer example reframed as
  iterative review (not noise); Big Sleep "one of the earliest…in our corpus"; harness-vs-compute
  inference softened; human-locus claim made explicitly cross-sectional; D3 softened;
  prize figures scope-labeled ($29.5M commitment / $8.5M final pool / $30.5M distributed).

## 2026-08-26 — CP2 lock revisions (14 items)
- unit_type taxonomy (R7→n/a systematization w/ documented_systems); benchmarks off-axis via
  probed_loop_phases; B-multi abolished → loop sets; background records out of primary counts;
  A2/multi label fix; CodeRover-S mechanism-level A2 evidence; R3 OUT-OF-WINDOW comparator;
  migration phrasing fixed; XBOW funnel metric-definition framing; DARPA 70→63 separated as
  administrative record correction; loop_evidence_record concept; I1/I2/I3 headline reframes;
  decision-authority + weakest-missing-condition rules formalized; E0/E1/E2 classes.

## 2026-08-26 — CP4-precondition pass
- Programmatic title-page-vs-metadata sweep: 33 PASS / 1 manual-channel (webfetch primaries,
  quote-verified during extraction) / 0 CHECK failures. Manifest↔bib key-naming alignment
  logged as CP4 reconciliation task (provenance intact; keys differ by convention).
- Venue verification against OFFICIAL live CFPs: S&P 2027 (13pp+5pp, SoK refs excluded from
  limit; abstract Nov 10 / paper Nov 17 2026) and USENIX Sec'27 (SoK track, Cycle 2 Jan 26
  2027; 20pp camera-ready). venue-compliance.md updated with verified facts.
- PrimeVul locators pinned (68.26%→3.09% F1 collapse; GPT-3.5/GPT-4 ~random in stringent
  settings); C29 → LOCATORS-PINNED.

## 2026-08-26 — CP4-HOLD review fixes (rendered-PDF findings)
- P0 Table II staleness (CP4 blocker): tables/autonomy-loop-matrix.tex body regenerated from
  the frozen schema. ROOT CAUSE: during CP2-lock the file's header comment was updated to v3
  while the tabular body remained v2 — a fresh label over stale content; assembler faithfully
  compiled it. New body: 14 autonomy-bearing / 2 background / 2 loop-transition-doc / 18
  context; benchmarks n/a with probed phases; PrimeVul task-domain; R7 n/a + documented_systems.
- P1 §12 I3 funding wording softened to protocol-v5 formulation ("allocate prizes and rank
  vendors directly --- increasingly inform funding decisions through transition programs").
- P1 Figure 1 promoted to figure* (two-column width, textwidth resizebox) for legibility.
- Post-fix verification sweep against rendered PDF: all six consistency checks PASS;
  gates remain 0 undefined / 0 overfull>=10pt / 12pp.

## 2026-08-26 — CP4-HOLD review round 2 (appendix architecture)
- P0: \\appendices marker moved from appendix-b.tex into main.tex before all appendix inputs
  (root cause: Record Quality Scores compiled as plain Section XIII, shifting letters down:
  search log=Appendix A, timeline=Appendix B, no Appendix C).
- P0: Appendix A regenerated as GENERATED-from-YAMLs complete 36-record artifact
  (record|year|unit|A|B-set/role|evidence class|R/B/Ar|access) as table*.
- P1: Figure 1 connector labels shortened to set-notation; system->set mapping moved to a
  dedicated connector-key band below the grid.
- P1: Table II promoted to table* (full-width) for readability.
- Verification: spacing-tolerant extraction confirms exact rendering "APPENDIX A INCLUDED
  RECORDS / APPENDIX B SEARCH LOG SUMMARY / APPENDIX C AIXCC AND INDUSTRIAL TIMELINE" in order;
  §3 cross-ref "is Appendix B" correct; gates 0 undef / 0 overfull>=10pt; 14pp (<=18 S&P cap);
  audit harness ALL GATES PASS.

## 2026-08-26 — CP4-HOLD review round 3
- P0 Appendix C content missing: timeline was a [h]-float deferred past document end
  (compile log: "'h' float specifier changed to 'ht'"). Converted to non-floating
  center+\captionof{table} so it renders in place; \usepackage{caption} added.
- P1 ossfuzz-levelingup-2024 schema gap fixed AT SOURCE (corpus YAML): unit_type=system(pipeline),
  rubric 1/1/2 added (root cause: normalization dict key mismatch 'levelingup2024' vs
  'levelingup-2024'); Appendix A regenerated programmatically from corrected YAMLs.
- P1 NYU version-divergence note removed from R2 entry (line-surgery had latched onto first
  matching note-line); R2 restored to generic verification note; NYU entry carries the note.
- Verification: TABLE with "Dated event chain" now renders in Appendix C (content incl.
  commit e9b919d5 / 150 CPU-hours / 26 vulns present); leveling row = 2024|system(pipeline)|A1|
  B1|industrial-system-report|1/1/2|HTML (resizebox column-wise text extraction makes naive
  adjacency regex a false FAIL - confirmed against generated .tex line); R2/NYU notes correct;
  gates 0 undef / 0 overfull>=10pt; 13pp; harness ALL GATES PASS.

## 2026-08-26 — CP4-HOLD review round 4 (render-first verification pass)
- P0 float ordering: \clearpage barrier inserted after appendix-a input (placeins/FloatBarrier
  is unreliable for table*-class floats); rendered order now App-A heading p.12 -> Table IV
  caption p.13 -> App-B/App-C headings p.14.
- P1 bibliography [20]/[13]: refs.bib was ALREADY clean at source (R2 generic / NYU carries
  divergence) - reviewer's copy predated the round-3 rebuild; fresh render confirms [20]-region
  free of NYU note and [13]-region carrying it. Lesson: verify against CURRENT build hash.
- P1 figure decluttering ACTUALLY applied this time (previous attempt died mid-script before
  write, then a regex repair created a duplicated node prefix -> tikz errors 15->2->0 across
  three surgical passes). Final state verified in render: connectors carry set-notation only;
  system names live in a dedicated "Connector key" band; AIxCC node renders clean text.
- Process guardrail adopted: every source mutation followed by immediate re-read assertion
  BEFORE compile; every claim about render state backed by per-page extraction, not logs alone.
- Gates: 0 LaTeX errors / 0 undefined citations-references / 0 overfull>=10pt / 14pp.

## 2026-08-26 — CP4-HOLD review round 5
- P0 duplicate timeline caption: root cause was the float->non-float conversion adding
  \captionof while the original inner \caption survived -> TABLE V (stray) + TABLE VI (real).
  Removed the legacy \caption+\label pair; exactly one caption remains and LaTeX numbers it
  TABLE V (render-verified: occurrences=1).
- P1 Figure 1 density: lower half reduced from five bands to ONE decision-authority band +
  connector key + color legend. Environment-class definitions, loop-transition examples,
  background-anchor details, and off-axis enumeration MOVED INTO THE CAPTION (which now also
  points to Table IV/App-A for the off-axis enumeration). Render-verified on p.4: env/
  background/off-axis bands absent, decision band + connector key present.
- Gates: 0 errors / 0 undefined / 0 overfull>=10pt / 14pp.

## 2026-08-26 — CP4-HOLD review round 6 (render-vs-copy reconciliation)
- Diagnosis: reviewer's (4).pdf predates the round-5 rebuild; current build contains exactly
  ONE timeline caption (byte-level scan incl. letter-spaced variants: TABLE V only, no VI).
- Structural guarantee added per review demand: \clearpage barrier before Appendix C input ->
  C heading and its table are now co-located on a dedicated final page (p.15) and can never
  precede the heading. Full rendered order: App-A p12 -> Table IV p13 -> App-B p14 ->
  App-C heading+timeline p15. Build hash 857d8cb19b; 15pp; gates 0/0/0.
- Figure p.4 compact state unchanged (decision band + connector key; env/background/off-axis
  bands remain removed).

## CP4 RELEASE — author-runtime freeze (build 858baa831f; bundle 7289d1d211c2ba29)
STATUS PRECISE: released in author runtime; independent source-level verification requires
the release bundle (sok-coevolution-release-bundle.tar.gz + SHA256SUMS.manifest, 935 files).
Verifier recipe: untar -> sha256sum -c SHA256SUMS.manifest -> python3 scripts_audit_final.py
-> recompile pdflatex/bibtex/pdflatex x2 and diff page count.
- Final freeze build. Gates: 0 LaTeX errors / 0 undefined citations-references /
  0 overfull>=10pt / harness ALL GATES PASS / URL sweep 36-36 resolvable.
- ai-use-disclosure.md + venue-fit-cover-letter.md finalized (DRAFT markers removed).
- reference-audit.md refreshed with final counts + URL-sweep results.
- Venue facts verified against live CFPs earlier this session (S&P'27: SoK refs excluded from
  limit; abstract Nov 10 / paper Nov 17 2026; USENIX Sec'27 Cycle 2 Jan 26 2027 fallback).

## FORMAT REVISION (post-CP4, author request)
- main.tex flattened to a SINGLE self-contained source (all sections + Table IV inlined);
  figures/autonomy-loop-map.tex remains the only external tex input.
- Modular sources moved to sections_archive/ (not part of build); audit harness citation
  scan repointed to main.tex.
- ai-use-disclosure.md REMOVED per author decision; venue-compliance.md records the decision.
- Rebuilt: 0 errors / 0 undefined / 0 overfull>=10pt / 15pp / harness ALL GATES PASS.
  New PDF md5 31eae8b6be; bundle rebadged 0ca8876c2a919b55.

## SUBMISSION-FORMAT REVISION (S&P 2027 conformance)
- P0 documentclass -> [conference,compsoc]{IEEEtran} per CFP requirement.
- P0 CVE sanitization for anonymity: 10 full identifiers redacted across main.tex/refs.bib
  (OpenSSL/USB/SQLite flaws -> 'identifier withheld' phrasings); rendered PDF now contains
  ZERO full CVE ids. Corpus artifacts retain full identifiers; mapping recorded in
  CVE-REDACTION-MAP.md (author-side only).
- GenAI disclosure corrected: CFP REQUIRES HotCRP field disclosure; ai-use-disclosure.md
  restored as the paste-ready statement; venue-compliance updated (earlier removal decision
  superseded). ORCID + registration deadlines marked mandatory/verified.
- Bundle packaging fixed: SHA256SUMS regenerated from exactly-packaged set (936 files),
  shipped INSIDE tar as MANIFEST.sha256; clean-room drill: 936/936 OK, harness PASS in extract.
- compsoc rebuild: 0 errors / 0 undefined / 0 overfull>=10pt; 16pp (<=18 cap); rendered PDF
  contains zero full CVE identifiers.

## CONTENT EXPANSION to 12-page main-text target (post-conformance)
- §6 new subsection "Architecture Lessons and the Epistemics of A3": three CRS design
  philosophies (N-version orthogonality / deterministic decomposition / PoV-free static),
  model-scale inversion, validation-throughput cap, ASC SQLite 15-min autonomous find+patch,
  Ada Logics triage as V5 exemplar, explicit A3 epistemics (E1 vs E2, unscored spillover).
- §8 new subsection "Institutional Response": $200K/team transitions, $2M SSLab recycling +
  OpenAI credits, OpenSSF CRS SIG hosting, team-relayed legacy yields; attacker-side
  speculation graded P1 with GTG specifics and an adoption-lag falsifier.
- §9 new subsection "The Measured Core, Quantified": Fang Pass@5-vs-overall distinction,
  PrimeVul 68.26->3.09 F1 collapse w/ near-random frontier prompting, XBOW category-aware
  funnel math (~39% dup/informative) - convergence argument for measured validity.
- Bibliography: Meta-AI placeholders replaced with title-page-verified author lists
  (et-al truncation noted per entry); references now begin p.13 -> main text ~12pp.
- Build: compsoc, 0 errors / 0 undefined / 0 overfull>=10pt / 17pp total / ZERO full CVE ids.
  Superseded by c6655f42a8 (full author lists).
- Bib finalization: CSE v1/v2/v3 placeholder authors replaced with title-page-verified lists
  (22/12/12 names, et-al truncation eliminated); harness placeholder scan now NONE.
- FINAL BUILD: md5 c6655f42a8, 17pp compsoc, CVE-free, gates green; bundle rebadged w/ drill OK.

## CSE AUTHOR LISTS — authoritative correction (reviewer round: 21/13/13)
- csev12023 -> 21 authors (Sasha Frolov added; 'Prakash, Ravi' token normalized) per
  authoritative arXiv metadata.
- csev22024 -> 13 authors (Shengye Wan restored).
- csev32024 -> 13 authors (Yue Li restored).
- Root cause of the 22/12/12 error: pdftotext title-page extraction dropped/duplicated tokens
  and my et-al cleanup pass ran twice, compounding loss. Lesson recorded: extraction-based
  metadata requires authoritative-record diffing (same class as the R7 rendering issue).
- Rebuild: 0 errors / 0 undefined / 0 overfull>=10pt / 17pp. FINAL BUILD md5 e634785293.
- Bundle+MANIFEST.sha256 regenerated; clean-room drill ALL OK; harness PASS.

## FIGURE COMPLETION (F1/F3) + ethics paragraph — build abb85492d0
- F1 PRISMA flow figure added (multi-stream TikZ; frozen CP1-final counts; streams keep own
  denominators). Wired into §3.
- F3 capability-timeline figure added (2023-08..2026-05 milestones, class-coded competition/
  industry/misuse/governance; every date primary-sourced via App-C). Wired into §8.
- Ethics paragraph added to §10 (documentary study; no live exploitation; identifier handling).
- Page budget: main text ends p.13 (=13pp text limit, satisfied); refs+appendices pp.13-18;
  total 18pp = exactly at cap, zero slack. Build md5 abb85492d0.
- Review-note: hash in prior checklist (c6655f42a8) superseded twice since (e634785293 ->
  abb85492d0); CSE lists stand at the mandated 21/13/13.

## FINAL POLISH PASS (build a02c8e4eb2)
- App-C caption tightened: 'AIxCC/industrial timeline (...)' replaces repeated 'Dated event chain'.
- F3 milestones now shape-coded (circle/square/diamond/triangle) in addition to color ->
  colorblind-safe without legend changes; shapes.geometric added to preamble.
- Verified CVE-2025-37891-derived prose carries adjacent \cite{darknavyargusee2025}
  (reviewer's 'uncited' concern was stale-copy).
- Gates: 0 errors / 0 undefined / 0 overfull>=10pt / 18pp (=cap) / zero full CVE ids.

## REVERSAL — CVE restoration (author decision 2026-08-26, supersedes sanitization pass)
- Restored 9 full identifiers: CVE-2024-9143 (x2), CVE-2025-37891 (x2), CVE-2025-6965 (x5) in
  main.tex/refs.bib where supported by cited sources; CVE-REDACTION-MAP.md marked
  SUPERSEDED audit-trail only. Zero-CVE gate removed.
- Audit harness updated: CVEs treated as EXPECTED public identifiers (fails if missing).
- Stale-artifact workflow corrected: fingerprint = MD5 + SHA256 manifest + page count +
  section-heading hash + bibliography diff; CVE presence excluded as staleness signal.
- Rebuild: 0 errors / 0 undefined / 0 overfull>=10pt / 18pp / CVEs 2+2+5 present.
  New PDF md5 7c2fa7cc3f.
- Bundle+MANIFEST regenerated; drill ALL OK.
