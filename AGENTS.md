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
│   ├── source-map.csv          # Bib key → file mapping (49 entries)
│   └── record-id-map.csv       # Record ID ↔ bib key mapping (36 entries)
├── corpus/
│   └── included/               # 36 YAML record files
└── audits/                     # Audit reports
```

## Important: Record Counts Are Layer-Specific

Different repository artifacts track different units of analysis.

| Artifact | Count | What it tracks |
|----------|-------|----------------|
| `corpus/included/` | 36 YAML files | Structured empirical records with autonomy classifications |
| `references/source-map.csv` | 49 entries | All bibliography entries mapped to source files |
| `evidence/autonomy-loop-assignments.csv` | 36 rows | Empirical records with A0–A3 and B1–B4 classifications |
| `references/record-id-map.csv` | 36 entries | Mapping from corpus record IDs to bibliography keys |

**Do not assume that the number of YAML records must equal the number of `included_record` entries in `source-map.csv`.**

When auditing empirical corpus membership, use `corpus/included/` and `references/record-id-map.csv` as the source of truth. When resolving manuscript citations to source material, use `references/source-map.csv`.

## Source Hierarchy

1. **Original PDF/source document** — highest authority
2. **Official web page or report** — for non-PDF sources
3. **Extracted text file** — AI-readable working representation
4. **BibTeX metadata** — citation only, not evidence

## Agent Operating Rules

1. **Do not infer missing evidence from citation metadata, filenames, abstracts, surrounding prose, or citation proximity.**

2. **Do not silently repair inconsistencies between repository artifacts.** Report the inconsistency and identify which artifact is authoritative for the task being performed.

3. **`refs.bib` is a citation registry, not an evidence database.** It controls rendering, not truth.

4. **`source-map.csv` resolves citations to source artifacts, but corpus membership must be determined from the corpus records and record-ID mapping.**

5. **When source text and PDF disagree due to extraction artifacts, inspect the original PDF before making a support classification.**

6. **Never convert INFERRED or PARTIAL support into DIRECT support merely because the manuscript wording appears plausible.**

7. **Preserve uncertainty in audit outputs.** An unresolved claim is preferable to a fabricated verification result.

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

## Corpus Roles in source-map.csv

| Role | Count | Description |
|------|-------|-------------|
| included_record | 45 | All bibliography entries associated with included corpus records |
| background_anchor | 2 | Pre-2024 context sources |
| loop_transition | 2 | B4 documentation sources |

**Note:** The `source-map.csv` includes 45 `included_record` entries because some bibliography entries map to the same underlying corpus record (e.g., multiple citations to different parts of the same DARPA report). The canonical empirical corpus is the 36 YAML files in `corpus/included/`.

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

# Validate CSV schema
awk -F',' 'NF != 6 { print "INVALID:", NR, "fields=" NF, $0 }' references/source-map.csv

# Count corpus roles
tail -n +2 references/source-map.csv | awk -F',' '{print $6}' | sort | uniq -c
```

## Audit Trail

All audits should be saved to `audits/` with:
- Date
- Git commit
- Scope (e.g., "§5 Discovery numerical claims")
- Findings
- Required fixes
