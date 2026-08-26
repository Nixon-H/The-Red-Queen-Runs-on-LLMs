# Release Manifest: SoK Co-Evolution Paper

**Release Date:** 2026-08-27
**Release Version:** 1.2 (Final verification complete)
**Status:** Ready for submission

---

## 1. Build Information

### Compiler/Toolchain
- **LaTeX compiler:** pdfLaTeX
- **Bibliography:** BibTeX
- **Build sequence:** pdflatex → bibtex → pdflatex → pdflatex
- **Build errors:** 0
- **Build warnings:** 2 overfull vbox, several underfull hbox (cosmetic only)

### PDF Metadata
- **Page count:** 17 pages
- **File size:** 261,254 bytes
- **Build hash:** 4402a2d (git commit)
- **Build status:** Successful; BibTeX zero errors, no fatal compilation errors

---

## 2. SHA-256 Hashes

### Core Files
| File | SHA-256 Hash |
|------|--------------|
| main.tex | f301aa78f227af08b2e13f89a4617e8bd462ba557483a47ddfff0d09cc8d44e1 |
| refs.bib | edab8319201b7d905efea7e13e6efb24a79cf0f55cf0a8f0b98d626c0bc75cc4 |
| main.pdf | f19f587e7b9238e81bc91432c9eb67f251ca9bb8680e456ac85aae3abe26f298 |
| evidence/autonomy-loop-assignments.csv | e95da24dfd24d6ec8d90e5e40a51bb42fb4d849c89a169b5e60d7deb535e7259 |

### Verification Command
```bash
sha256sum main.tex refs.bib main.pdf evidence/autonomy-loop-assignments.csv
```

---

## 3. Reconciliation State

### Cross-Artifact Consistency (Verified 2026-08-27)
- **Bibliography:** 49 entries, all 49 cited, 0 uncited, 0 missing
- **Manifest:** 49 bib_key values, matches bibliography exactly
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
   - Final: 49 manifest entries = 49 bib entries

---

## 4. Files Included in Release

### Core LaTeX Files
- `main.tex` — Primary source (~1276 lines)
- `refs.bib` — Bibliography (49 entries)
- `main.pdf` — Compiled output (17 pages)

### Evidence Files
- `evidence/autonomy-loop-assignments.csv` — Classification source of truth (36 records)
- `evidence/i1-analysis.md` — I1 claim analysis
- `evidence/i2-analysis.md` — I2 claim analysis
- `evidence/i3-analysis.md` — I3 claim analysis

### Corpus
- `corpus/included/` — 36 YAML files (one per record)

### References
- `references/manifest.csv` — Reference tracking (49 entries)
- `references/pdf/` — 37 PDFs
- `references/txt/` — 49 text files

### Audit Files
- `CORRECTED_AUDIT_REPORT.md` — Corrected forensic audit
- `CLAIM_LEDGER.md` — Claim-level audit framework
- `CITATION_VERIFICATION_S1_S3.md` — §1-§3 verification
- `CLAIM_VERIFICATION_S4_S9.md` — §4-§9 verification
- `A3_SENSITIVITY_ANALYSIS.md` — A3 robustness testing
- `I3_CALIBRATION.md` — I3 wording correction
- `TABLE_FIGURE_RECONCILIATION.md` — Table/Figure verification
- `E1_E2_JUSTIFICATION.md` — Environment-class justification

### Build History
- `docs/CHANGES.md` — Build history (10+ iterations)
- `docs/reference-audit.md` — Prior citation audit

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
- [x] I3 wording calibrated
- [x] A3 sensitivity analysis complete
- [x] E1/E2 boundary justified
- [x] Manifest-to-bibliography reconciliation proven
- [x] Cross-artifact set equality verified (CSV=YAML=T2=T4)
- [x] PDF compiles cleanly (0 errors)
- [x] SHA-256 hashes generated
- [x] Inter-rater reliability paragraph added
- [ ] Final review by authors
- [ ] Visual PDF QA (figure overflow, caption placement)

### Status
**The manuscript has completed its documented internal audit and cross-artifact reconciliation. All major methodological clarifications have been incorporated. The paper is ready for final author review.**

---

*Manifest generated: 2026-08-26*
*Last updated: 2026-08-27*
*Git commit: 4402a2d*
*Status: Release ready*
