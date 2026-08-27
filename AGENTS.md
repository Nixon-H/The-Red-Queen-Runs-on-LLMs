# Research Agent Instructions

## Repository Structure

```
RESEARCH CYBER/
├── main.tex                    # Primary manuscript
├── refs.bib                    # Bibliography (49 entries)
├── main.pdf                    # Compiled output
├── evidence/
│   └── autonomy-loop-assignments.csv  # Classification source of truth
├── references/
│   ├── pdf/                    # 37 primary source PDFs
│   ├── txt/                    # 49 extracted source texts
│   ├── manifest.csv            # Reference tracking
│   └── source-map.csv          # Bib key → file mapping
├── corpus/
│   └── included/               # 36 YAML record files
└── audits/                     # Audit reports
```

## Source Hierarchy

1. **Original PDF/source document** — highest authority
2. **Official web page or report** — for non-PDF sources
3. **Extracted text file** — AI-readable working representation
4. **BibTeX metadata** — citation only, not evidence

## Claim Verification Procedure

For every factual claim in the manuscript:

### Step 1: Identify Citation
```bash
grep -n "specific claim" main.tex
```

### Step 2: Resolve Citation Key
```bash
# Look up in source-map.csv
grep "citation_key" references/source-map.csv
```

### Step 3: Locate Primary Source
```bash
# If text_file exists
cat references/txt/{text_file}.txt | grep -i "claim keywords"

# If only PDF exists
pdftotext references/pdf/{pdf_file}.pdf - | grep -i "claim keywords"
```

### Step 4: Classify Support

| Label | Definition |
|--------|------------|
| **DIRECT** | Source explicitly states the exact claim |
| **QUALIFIED** | Source states claim with qualifiers manuscript preserves |
| **INFERRED** | Claim is reasonable inference from source |
| **PARTIAL** | Source supports part of multi-part claim |
| **UNSUPPORTED** | Source does not support the claim |

### Step 5: Flag Issues

- [ ] Numerical precision: rounded vs exact
- [ ] Source qualifier: vendor-reported, foundation-relayed, etc.
- [ ] Causal interpretation: correlation vs causation
- [ ] Environmental classification: E0/E1/E2
- [ ] Autonomy level: A0/A1/A2/A3

## Corpus Roles

| Role | Count | Description |
|------|-------|-------------|
| included_record | 36 | Core empirical/system records |
| background_anchor | 2 | Pre-2024 context |
| loop_transition | 2 | B4 documentation |
| survey | 7 | Systematizations (not counted in corpus) |

## Source Types

| Type | Authority | Notes |
|------|-----------|-------|
| peer_reviewed_paper | primary | Academic publication |
| vendor_report | primary_vendor | Company-published data |
| vendor_blog | primary_vendor | Company blog post |
| foundation_report | secondary_relay | Foundation-relayed figures |
| competition_report | primary_participant | Participant-reported data |
| darpa_official | primary | DARPA-published data |
| registry_record | primary | NVD/CVE records |

## Critical Rules

1. **Do not treat citation proximity as evidence of support.** A citation at the end of a sentence does not automatically prove every clause.

2. **Decompose multi-part claims.** A sentence with four numbers needs support for all four.

3. **Preserve qualifiers.** "Vendor-reported" must not become "observed."

4. **Check rounding.** "87%" may be 86.7% in the source.

5. **Verify environmental classification.** E2 (production) vs E1 (sandboxed) must match source description.

6. **Verify autonomy level.** A2 vs A3 requires four-verb test: planning, execution, validation, reporting.

## Verification Commands

```bash
# Structural citation audit
grep -oP '\\cite\{[^}]+\}' main.tex | tr ',' '\n' | sed 's/\\cite{//;s/}//' | sort -u | wc -l

# Check uncited entries
diff <(grep -oP '\\cite\{[^}]+\}' main.tex | tr ',' '\n' | sed 's/\\cite{//;s/}//' | sort -u) \
     <(grep -E "@misc\{|@article\{|@inproceedings\{|@book\{" refs.bib | sed 's/.*{//;s/,.*//' | sort -u)

# Search source text
grep -i "keyword" references/txt/*.txt
```

## Audit Trail

All audits should be saved to `audits/` with:
- Date
- Git commit
- Scope (e.g., "§5 Discovery numerical claims")
- Findings
- Required fixes
