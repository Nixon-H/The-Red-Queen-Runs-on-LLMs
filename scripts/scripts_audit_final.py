#!/usr/bin/env python3
"""Repository-level final audit. Run after the clean LaTeX rebuild."""
import csv
import glob
import re
import subprocess
import sys
import yaml
from collections import Counter
from pathlib import Path

fails = []
root = Path('.')
bib = (root / 'refs.bib').read_text(errors='replace')
keys = re.findall(r"@\w+\{([^,\s]+),", bib)
if len(keys) != len(set(keys)):
    fails.append("duplicate bib keys")
for bad in ("VERIFY", "verify from local PDF", "authors TBD", "and others", "TODO"):
    if bad.lower() in bib.lower():
        fails.append("placeholder in refs.bib: " + bad)

tex = (root / 'main.tex').read_text(errors='replace')
cited = {
    key.strip()
    for group in re.findall(r"\\cite\w*\{([^}]+)\}", tex)
    for key in group.split(',')
    if key.strip()
}
missing = cited - set(keys)
uncited = set(keys) - cited
if missing:
    fails.append("missing bib keys: %s" % sorted(missing))
print("bibliography: %d entries, %d cited keys, uncited=%s" %
      (len(keys), len(cited), sorted(uncited) if uncited else "NONE"))

with (root / 'references/source-map.csv').open(newline='') as f:
    source_rows = list(csv.DictReader(f))
with (root / 'references/manifest.csv').open(newline='') as f:
    manifest_rows = list(csv.DictReader(f))
source_keys = {r['citation_key'] for r in source_rows}
manifest_keys = {r['bib_key'] for r in manifest_rows if r.get('bib_key')}
if source_keys != set(keys):
    fails.append("source-map key drift: bib-only=%s source-only=%s" %
                 (sorted(set(keys) - source_keys), sorted(source_keys - set(keys))))
if manifest_keys != set(keys):
    fails.append("manifest key drift: bib-only=%s manifest-only=%s" %
                 (sorted(set(keys) - manifest_keys), sorted(manifest_keys - set(keys))))
if len(source_rows) != 50 or len(manifest_rows) != 50:
    fails.append("source-layer inventory count drift: source-map=%d manifest=%d" %
                 (len(source_rows), len(manifest_rows)))
if any(r.get('citation_verified','').upper().startswith('PENDING') for r in manifest_rows):
    fails.append("manifest contains pending citation verification")

recs = [yaml.safe_load(open(p)) for p in glob.glob("corpus/included/*.yaml")]
from collections import Counter
levels = Counter(r.get("autonomy_level") for r in recs if r.get("temporal_scope") == "in-window")
bearing = {k: v for k, v in levels.items() if k in ("A0", "A1", "A2", "A3", "uncertain")}
if sum(bearing.values()) != 14:
    fails.append("autonomy-bearing != 14: %s" % bearing)
if bearing.get("A3", 0) != 0:
    fails.append("A3 nonzero without framework revision")
if len(recs) != 36:
    fails.append("canonical corpus != 36")
for r in recs:
    for field in ("bib", "result", "classification_evidence", "autonomy_note"):
        value = str(r.get(field, ''))
        if re.search(r"\[to-verify\]|\(verify[^)]*\)|\bTBD\b|\bTODO\b", value, re.I):
            fails.append("placeholder in %s.%s" % (r.get('reference_key'), field))

pdf = subprocess.run(["pdftotext", "main.pdf", "-"], capture_output=True,
                     text=True, errors='replace').stdout
flat = re.sub(r"\s+", " ", pdf.replace("-\n", "")).lower()
for phrase in ("cve-2024-9143", "cve-2025-37891", "cve-2025-6965"):
    if phrase not in flat:
        fails.append("expected CVE identifier missing from PDF: " + phrase)
for phrase in ("no included evidence met our operational definition",
               "weakest missing condition", "binding methodological constraint",
               "administrative record correction"):
    if phrase not in flat:
        fails.append("sentinel missing from PDF: " + phrase)

print("corpus: %d canonical records; autonomy-bearing=%d; source-map roles=%s" %
      (len(recs), sum(bearing.values()), Counter(r['corpus_role'] for r in source_rows)))
print("AUDIT:", "FAIL" if fails else "ALL GATES PASS", fails or "")
sys.exit(1 if fails else 0)
