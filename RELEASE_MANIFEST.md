# Release Manifest: SoK Co-Evolution Paper

**Release Date:** 2026-08-27
**Release Version:** Forensic audit rebuild (2026-08-27)
**Status:** Clean-room current-state audit complete; residual evidence limitations and author review remain required

---

## 1. Build Information

### Compiler/Toolchain
- **LaTeX compiler:** pdfLaTeX
- **Bibliography:** BibTeX
- **Build sequence:** pdflatex → bibtex → pdflatex → pdflatex
- **Build errors:** 0
- **Build warnings:** 2 overfull vbox and several underfull hbox warnings; rendered PDF inspected with no visible clipping or overlap

### PDF Metadata
- **Page count:** 18 pages
- **File size:** 276,280 bytes
- **Build hash:** 80f6ce263b2ef78e14437752d0f54305c41ae9da (base HEAD; current clean-room audit changes remain uncommitted)
- **Build status:** Successful; BibTeX zero errors, no fatal compilation errors

---

## 2. SHA-256 Hashes

### Core Files
| File | SHA-256 Hash |
|------|--------------|
| main.tex | 54cab114610bc42a80b2142dc9a8cddda82b4fa6850b7fddf514d3881708eddc |
| refs.bib | 2f1b0f6835547bb5c4157e16d54e1a1f22efba37ae5ff9a8cf19da92310e484f |
| main.pdf | 1c781d2987e0dfe1a69bb101292193f8b100811e9643bfd1072776f1b56a1ce3 |
| evidence/autonomy-loop-assignments.csv | 1a8eead4ccc70e8560d6acc609630f1259d6713f36bb0015193eab4c0064b547 |
| references/manifest.csv | 05ff31192de6cf669fdfea2ef15945fb37f18d97c47657931fee862b6565a5bf |

### Verification Command
```bash
sha256sum main.tex refs.bib main.pdf evidence/autonomy-loop-assignments.csv references/manifest.csv
```

---

## 3. Reconciliation State

### Cross-Artifact Consistency (Verified 2026-08-27)
- **Bibliography:** 50 entries, all 50 cited, 0 uncited, 0 missing
- **Manifest:** 50 bib_key values, matches bibliography exactly
- **Source map:** 50 source-layer entries; roles are 45 included-record, 3 background-anchor, and 2 loop-transition entries
- **CSV:** 36 records
- **YAML:** 36 records (CSV = YAML)
- **Table II:** 36 records (CSV = T2)
- **Table IV:** 36 records (CSV = T4)
- **All set differences: EMPTY**

### Audit Trail

1. **Bibliography cleanup** ✓
   - Removed internal audit notes from refs.bib
   - Removed 2 uncited entries (fang2024oneday, bugdar2025)
   - Double braces removed from person-authors, preserved for corporate authors
   - All 24 arXiv entries standardized to @misc with eprint/archivePrefix/primaryClass
   - CVE-Bench: added full PMLR metadata (volume 267, pages 79850-79867)

2. **Record ID canonicalization** ✓
   - CSV is canonical source of truth
   - All bib keys, Table II, Table IV, YAML match CSV
   - Fixed: bigsleep2024, artemis2025, autocoderoever-2024, ossfuzz-aifixing-2024, ossfuzz-levelingup-2024, csev12023bg
   - Fixed: r1slr2024, r2slr2024, r3survey2026, r4csur2025, r6tosem2026, rissebohme-wrongexam2024
   - Fixed: r5usenix26agentic typo

3. **A3 sensitivity analysis** ✓
   - Defined S0-S4 scenarios
   - Reclassified all borderline records
   - Confirmed A3-negative finding robust across all scenarios

4. **I3 calibration** ✓
   - Replaced "increasingly binding" with "binding methodological"
   - Removed unsupported temporal claim

5. **E1/E2 boundary justification** ✓
   - AIxCC: E1 (competition forks, inserted bugs)
   - Big Sleep: E2 (production SQLite, real bug)
   - Argusee: E2 (production projects, real CVE)
   - XBOW: E2 (bug bounty platforms, real submissions)
   - ARTEMIS: E2 (corporate network, real vulnerabilities)

6. **Manifest reconciliation** ✓
   - 19 missing entries added to manifest.csv
   - 4 obsolete keys removed
   - Final: 50 manifest entries = 50 bib entries

---

## 4. Files Included in Release

### Core LaTeX Files
- `main.tex` — Primary source (1314 lines)
- `refs.bib` — Bibliography (50 entries)
- `main.pdf` — Compiled output (18 pages)

### Evidence Files
- `evidence/autonomy-loop-assignments.csv` — Classification source of truth (36 records)
- `evidence/i1-analysis.md` — I1 claim analysis (archived)
- `evidence/i2-analysis.md` — I2 claim analysis (archived)
- `evidence/i3-analysis.md` — I3 claim analysis (archived)

### Corpus
- `corpus/included/` — 36 YAML files (one per record)

### References
- `references/manifest.csv` — Reference tracking (50 entries)
- `references/pdf/` — 34 PDFs
- `references/txt/` — 45 text files

### Audit Files
- `FORENSIC_AUDIT_FINAL.md` — Final forensic audit report
- `FINAL_FIX_SUMMARY.md` — Resolved and residual issue summary
- `CLAIM_EVIDENCE_MATRIX.csv` — Claim-level support classifications
- `REFERENCE_INVENTORY.csv` — Citation/source inventory
- `NUMERIC_FACT_AUDIT.csv` — Numerical claim audit
- `CONTRADICTION_MATRIX.md` — Cross-artifact and source discrepancies
- `audits/2026-08-27-forensic-audit.md` — Dated audit-trail entry
- `audits/2026-08-27-clean-room-current-head.md` — Exact-current-state clean-room audit
### Build History
- `docs/CHANGES.md` — Build history (10+ iterations)

---

## 5. Reproducibility Instructions

### To Rebuild PDF
```bash
cd "/home/nixon/RESEARCH CYBER"
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### To Verify Reconciliation
```bash
cd "/home/nixon/RESEARCH CYBER"
python3 << 'PYEOF'
import csv, re, os

# BibTeX keys
with open('refs.bib', 'r') as f:
    bib_keys = set(re.findall(r'@\w+\{([^,]+),', f.read()))

# Citations from .aux
with open('main.aux', 'r') as f:
    cited = set()
    for m in re.findall(r'\\citation\{([^}]+)\}', f.read()):
        for k in m.split(','):
            cited.add(k.strip())

# Manifest
with open('references/manifest.csv', 'r') as f:
    manifest = {r['bib_key'] for r in csv.DictReader(f) if r.get('bib_key')}

# CSV
with open('evidence/autonomy-loop-assignments.csv', 'r') as f:
    csv_ids = {r[0] for r in csv.reader(f) if r}

# YAML
yaml_ids = {fn.replace('.yaml','') for fn in os.listdir('corpus/included') if fn.endswith('.yaml')}

print(f"BIB={len(bib_keys)} CITED={len(cited)} MANIFEST={len(manifest)} CSV={len(csv_ids)} YAML={len(yaml_ids)}")
print(f"UNCITED={bib_keys - cited or 'NONE'}")
print(f"MISSING_FROM_BIB={cited - bib_keys or 'NONE'}")
print(f"CSV=YAML:{csv_ids == yaml_ids}")
PYEOF
```

---

## 6. Submission Readiness

### Checklist

- [x] Bibliography clean (no internal notes, no uncited entries)
- [x] Author metadata correct (double-brace only on corporate authors)
- [x] Record IDs consistent across all artifacts
- [x] I3 wording calibrated (appears to be binding, pending E7)
- [x] A3 sensitivity analysis complete
- [x] E1/E2 boundary justified
- [x] Manifest-to-bibliography reconciliation proven
- [x] Cross-artifact set equality verified (CSV=YAML=T2=T4)
- [x] PDF compiles cleanly (0 errors; nonfatal layout warnings remain)
- [x] SHA-256 hashes generated
- [x] GTG-1002 qualified as single-source vendor assessment
- [x] "Twelve-fold" replaced with "more than an order of magnitude"
- [x] "4–6 human checkpoints" removed (not in primary source)
- [ ] Final review by authors
- [x] Visual PDF QA (representative pages rendered and inspected)

### Status
**The manuscript has completed three rounds of forensic audit. All critical bibliographic, methodological, and claim-level issues have been addressed. The paper is ready for final author review.**

---

*Manifest generated: 2026-08-27*
*Last updated: 2026-08-27*
*Base Git commit: 80f6ce263b2ef78e14437752d0f54305c41ae9da*
*Status: Clean-room current-state audit rebuild ready for final author review; working tree contains uncommitted audit changes*
