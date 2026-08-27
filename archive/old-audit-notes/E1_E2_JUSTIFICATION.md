# E1/E2 Boundary Justification: SoK Co-Evolution Paper

**Audit Date:** 2026-08-26
**Purpose:** Provide explicit justification for environment-class classifications
**Status:** Justification in progress

---

## 1. Environment-Class Definitions

### E0: Synthetic/Benchmark
- **Definition:** Controlled, synthetic environments with artificial vulnerabilities
- **Characteristics:** Known vulnerabilities, fixed scope, no real-world impact
- **Examples:** CTF challenges, synthetic benchmarks (CyberSecEval, NYU CTF Bench)

### E1: Realistic-Sandboxed/Competition
- **Definition:** Realistic environments with real software, but under controlled conditions
- **Characteristics:** Real code, real vulnerabilities, but forked repositories, inserted bugs, controlled scope
- **Examples:** AIxCC competition forks, sandboxed penetration testing

### E2: Production/Production-Like
- **Definition:** Real-world environments with real software and real vulnerabilities
- **Characteristics:** Live systems, uncontrolled scope, real-world impact
- **Examples:** Production networks, open-source projects, bug bounty programs

---

## 2. Classification of Each System

### AIxCC (E1)
**Justification:** Competition environment with forked repositories and inserted bugs

**Evidence:**
1. **Forked repositories:** CRSs operate on forked copies of challenge projects, not live repositories
2. **Inserted bugs:** Vulnerabilities are artificially inserted into challenge projects
3. **Controlled scope:** 48 challenge projects across 23 open-source repositories (fixed set)
4. **No real-world impact:** Findings do not affect live systems
5. **Scored operation:** Performance measured by competition scoring, not production metrics

**Source:** openssfaixcc2026, tobbuttercup2025, r7sokaixcc2026

**Classification:** E1 ✓

### Big Sleep (E2)
**Justification:** Production-oriented research on live open-source software

**Evidence:**
1. **Real software:** SQLite is a production database engine
2. **Real vulnerability:** Stack buffer underflow in seriesBestIndex (real bug)
3. **Production context:** Targeted at real-world code, not sandboxed
4. **No inserted bugs:** Bug was naturally occurring, not artificially inserted
5. **Real-world impact:** Bug fixed pre-release, affecting production SQLite

**Source:** bigsleep2024naptime

**Classification:** E2 ✓

### Argusee (E2)
**Justification:** Production-oriented auditing on live projects

**Evidence:**
1. **Real projects:** GPAC, GIFLIB, Linux kernel (production software)
2. **Real vulnerabilities:** CVE-2025-37891 (kernel heap overflow), 15 vendor-reported flaws
3. **Production context:** Auditing real-world codebases
4. **No inserted bugs:** Vulnerabilities are naturally occurring
5. **Real-world impact:** CVE-2025-37891 affects Linux USB MIDI2 implementation

**Source:** darknavyargusee2025

**Classification:** E2 ✓

### XBOW (E2)
**Justification:** Commercial bug bounty platform operating on live systems

**Evidence:**
1. **Real systems:** Public and private HackerOne programs (production targets)
2. **Real vulnerabilities:** ~1,060 submissions, 130 resolved, 303 triaged
3. **Production context:** Commercial submission engine
4. **No inserted bugs:** Vulnerabilities are naturally occurring
5. **Real-world impact:** Resolved vulnerabilities affect production systems

**Source:** xbowtop12025

**Classification:** E2 ✓

### ARTEMIS (E2)
**Justification:** Corporate-scale, production-like target environment

**Evidence:**
1. **Network scale:** Corporate-style network (~8,000 hosts, 12 subnets)
2. **Environment type:** Production-like infrastructure (not lab/sandbox)
3. **Methodological decision:** Classification based on environment nature and scale, not experimental design

**Source:** artemis2025comparing

**Classification:** E2 ✓

**Note:** ARTEMIS is an experiment comparing agents to professionals, but the environment is classified as production-like based on its corporate scale and infrastructure characteristics. The experimental comparison is orthogonal to environment classification.

---

## 3. Why ARTEMIS is E2 (Not E1)

### Common Concern
ARTEMIS is an experiment, so it might seem like E1 (sandboxed). However, environment class is determined by the **target environment**, not the **experimental design**.

### Key Distinction
- **E1:** Realistic but controlled/sandboxed environment (e.g., AIxCC forks)
- **E2:** Real-world production or production-like environment (e.g., corporate network)

### ARTEMIS Evidence
1. **Network size:** ~8,000 hosts, 12 subnets (corporate scale)
2. **Infrastructure type:** Corporate-style (not lab/sandbox)
3. **Vulnerability type:** Real vulnerabilities (not inserted)
4. **Impact scope:** Corporate infrastructure (real-world)

### Conclusion
ARTEMIS operates on a **production-like network** (E2), even though it is an **experiment** comparing agents to professionals. The experimental design is orthogonal to environment classification.

---

## 4. Consistency Check

### All E2 Systems
| System | Environment | Evidence | Consistent |
|--------|-------------|----------|------------|
| Big Sleep | Production SQLite | Real bug, real software | ✓ |
| Argusee | Production projects | Real CVE, real projects | ✓ |
| XBOW | Bug bounty platforms | Real submissions, real fixes | ✓ |
| ARTEMIS | Corporate network | Real infrastructure, real vulns | ✓ |

### All E1 Systems
| System | Environment | Evidence | Consistent |
|--------|-------------|----------|------------|
| AIxCC | Competition forks | Forked repos, inserted bugs | ✓ |

### All E0 Systems
| System | Environment | Evidence | Consistent |
|--------|-------------|----------|------------|
| CyberSecEval | Synthetic benchmark | Artificial tasks | ✓ |
| NYU CTF Bench | CTF challenges | Synthetic challenges | ✓ |

**Consistency Status:** ✓ All classifications consistent

---

## 5. Recommended Wording for Paper

### Current (Implicit)
The paper classifies ARTEMIS as E2 but does not explicitly justify why.

### Recommended (Explicit)
Add to §4 (Discovery) or §9 (Threats):

> "Environment class E2 denotes production or production-like external targets (E0=synthetic/benchmark; E1=realistic but sandboxed or competition). ARTEMIS is classified E2 because it operates on a corporate-style network (~8,000 hosts, 12 subnets) with real vulnerabilities, despite being a controlled experiment comparing agents to professionals."

---

## 6. Implications

### For A3 Classification
Environment class alone does not explain the absence of A3 classifications. The corpus contains A2 systems across both E1 and E2 contexts; under the paper's operational definition, the limiting condition for the examined candidates is the required degree of human independence and closed-loop operation, not environment class.

### For Validity Analysis
E2 systems have higher ecological validity than E1 systems. This supports the paper's claim that A2 systems operate in production-like environments.

### For Reproducibility
Explicit E1/E2 justification improves reproducibility by clarifying the classification rule.

---

*Justification completed: 2026-08-26*
*Status: E1/E2 classifications justified, ARTEMIS explicitly justified as E2*