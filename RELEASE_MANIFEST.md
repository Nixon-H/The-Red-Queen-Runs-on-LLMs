# Release Manifest: SoK Co-Evolution Paper

**Release Date:** 2026-08-26
**Release Version:** 1.0 (Pre-submission audit complete)
**Status:** Ready for submission after final review

---

## 1. Build Information

### Compiler/Toolchain
- **LaTeX compiler:** pdfLaTeX
- **Bibliography:** BibTeX
- **Build sequence:** pdflatex → bibtex → pdflatex → pdflatex
- **Build errors:** 0
- **Build warnings:** 6 LaTeX warnings (caption, font, balance), 3 overfull boxes, 41 underfull boxes

### PDF Metadata
- **Page count:** 18 pages
- **File size:** 257,769 bytes
- **Build hash:** 19d8415 (git commit)
- **Build status:** Successful; no fatal compilation errors observed

---

## 2. SHA-256 Hashes

### Core Files
| File | SHA-256 Hash |
|------|--------------|
| main.tex | 1bdef803d2bcf9323c8b7125f1e79e9adbc311879e5e883a3d71b739a7673c30 |
| refs.bib | ec8df3882ee1e8f945cc36a8087d305cb2698e27f430c491d6a69aa09b4feb3f |
| main.pdf | 589736ecc220714339915899716a61ebd8bec1cda6abd638f72a023cf77ef574 |
| evidence/autonomy-loop-assignments.csv | e95da24dfd24d6ec8d90e5e40a51bb42fb4d849c89a169b5e60d7deb535e7259 |

### Verification Command
```bash
sha256sum main.tex refs.bib main.pdf evidence/autonomy-loop-assignments.csv
```

### Expected Output
```
1bdef803d2bcf9323c8b7125f1e79e9adbc311879e5e883a3d71b739a7673c30  main.tex
ec8df3882ee1e8f945cc36a8087d305cb2698e27f430c491d6a69aa09b4feb3f  refs.bib
589736ecc220714339915899716a61ebd8bec1cda6abd638f72a023cf77ef574  main.pdf
e95da24dfd24d6ec8d90e5e40a51bb42fb4d849c89a169b5e60d7deb535e7259  evidence/autonomy-loop-assignments.csv
```

---

## 3. Audit Trail

### Completed Audit Steps

1. **Bibliography cleanup** ✓
   - Removed internal audit notes from refs.bib (23 entries)
   - Fixed fang2024agents author metadata (Qi Zhan → Akul Gupta)
   - Verified clean bibliography rendering

2. **A3 sensitivity analysis** ✓
   - Defined S0-S4 scenarios
   - Reclassified all borderline records
   - Confirmed A3-negative finding robust across all scenarios

3. **I3 calibration** ✓
   - Replaced "increasingly binding" with "binding methodological"
   - Removed unsupported temporal claim
   - Updated §1 (Insights) wording

4. **Citation verification** ✓
   - §1-§3: 26 claims verified
   - §4-§9: 52 claims verified
   - Total: 78 claims audited; 77 initially supported and 1 wording overclaim corrected. Final manuscript claims are reconciled with the audit record.

5. **Table/Figure reconciliation** ✓
   - Table I: All values verified against sources
   - Table II: All 36 records match CSV
   - Table III: All 5 systems match CSV and sources
   - Figure 1-3: All visual elements correct

6. **E1/E2 boundary justification** ✓
   - AIxCC: E1 (competition forks, inserted bugs)
   - Big Sleep: E2 (production SQLite, real bug)
   - Argusee: E2 (production projects, real CVE)
   - XBOW: E2 (bug bounty platforms, real submissions)
   - ARTEMIS: E2 (corporate network, real vulnerabilities)

---

## 4. Files Included in Release

### Core LaTeX Files
- `main.tex` — Primary source (1196 lines)
- `refs.bib` — Bibliography (231 lines, 38 entries)
- `main.pdf` — Compiled output (18 pages)

### Evidence Files
- `evidence/autonomy-loop-assignments.csv` — Classification source of truth (36 records)
- `evidence/i1-analysis.md` — I1 claim analysis
- `evidence/i2-analysis.md` — I2 claim analysis
- `evidence/i3-analysis.md` — I3 claim analysis

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

### To Verify Hashes
```bash
sha256sum main.tex refs.bib main.pdf evidence/autonomy-loop-assignments.csv
```

### To Verify Claims
- See `CLAIM_LEDGER.md` for claim-level verification framework
- See `CITATION_VERIFICATION_S1_S3.md` for §1-§3 verification
- See `CLAIM_VERIFICATION_S4_S9.md` for §4-§9 verification

---

## 6. Known Limitations

### Acknowledged in Paper
1. Single-team classification without inter-rater statistics
2. Publisher APIs unavailable (IEEE, ACM)
3. English-language sources only
4. Vendor-reported statistics labeled as CLAIMED
5. Rapid model churn may affect conclusions

### Addressed in Audit
1. Bibliography cleaned (internal notes removed)
2. Author metadata error corrected (fang2024agents)
3. I3 wording corrected (removed "increasingly")
4. A3 sensitivity analysis performed
5. E1/E2 boundary justified explicitly

---

## 7. Submission Readiness

### Checklist

- [x] Bibliography clean (no internal notes)
- [x] Author metadata correct
- [x] I3 wording calibrated
- [x] A3 sensitivity analysis complete
- [x] E1/E2 boundary justified
- [x] All claims audited (78 claims audited; 77 initially supported, 1 overclaim corrected)
- [x] All tables/figures reconciled (Tables I-III, Figures 1-3)
- [x] PDF compiles cleanly (0 errors)
- [x] SHA-256 hashes generated
- [x] A3 sensitivity analysis added to paper
- [x] E1/E2 justification added to paper
- [ ] Final review by authors
- [ ] Inter-rater reliability (optional but recommended)

### Status
**The manuscript has completed its documented internal audit and is ready for final author review. All major methodological clarifications have been incorporated into the manuscript.**

---

*Manifest generated: 2026-08-26*
*Last updated: 2026-08-26*
*Git commit: 19d8415*
*Status: Release ready*