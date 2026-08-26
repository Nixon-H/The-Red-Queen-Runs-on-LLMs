#!/usr/bin/env python3
"""
Final Verification Script for SoK Co-Evolution Paper
Run this script to verify the paper is correct and ready for submission.

Usage: python3 scripts/verify_final.py
"""

import csv
import os
import re
import subprocess
import sys


def run_command(cmd):
    """Run a command and return output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='replace')
    return result.stdout.strip()


def check_bibliography():
    """Check bibliography consistency."""
    print("1. BIBLIOGRAPHY CHECK")
    
    # Parse bib keys
    with open('refs.bib') as f:
        bib_content = f.read()
    bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))
    
    # Parse citations from .aux
    with open('main.aux') as f:
        aux_content = f.read()
    cited_keys = set()
    for match in re.findall(r'\\citation\{([^}]+)\}', aux_content):
        for key in match.split(','):
            cited_keys.add(key.strip())
    
    uncited = bib_keys - cited_keys
    missing = cited_keys - bib_keys
    
    print(f"   BibTeX entries: {len(bib_keys)}")
    print(f"   Cited keys: {len(cited_keys)}")
    print(f"   Uncited: {sorted(uncited) if uncited else 'NONE'}")
    print(f"   Missing from bib: {sorted(missing) if missing else 'NONE'}")
    
    return len(uncited) == 0 and len(missing) == 0


def check_manifest():
    """Check manifest consistency."""
    print("\n2. MANIFEST CHECK")
    
    # Parse bib keys
    with open('refs.bib') as f:
        bib_content = f.read()
    bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))
    
    # Parse manifest
    manifest_bib = set()
    with open('references/manifest.csv') as f:
        for row in csv.DictReader(f):
            if row.get('bib_key'):
                manifest_bib.add(row['bib_key'])
    
    missing = bib_keys - manifest_bib
    extra = manifest_bib - bib_keys
    
    print(f"   Manifest entries: {len(manifest_bib)}")
    print(f"   BIB - MANIFEST: {sorted(missing) if missing else 'NONE'}")
    print(f"   MANIFEST - BIB: {sorted(extra) if extra else 'NONE'}")
    
    return len(missing) == 0 and len(extra) == 0


def check_record_sets():
    """Check record set consistency."""
    print("\n3. RECORD SET CHECK")
    
    # CSV IDs
    csv_ids = set()
    with open('evidence/autonomy-loop-assignments.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row:
                csv_ids.add(row[0])
    
    # YAML IDs
    yaml_ids = set()
    for fn in os.listdir('corpus/included'):
        if fn.endswith('.yaml'):
            yaml_ids.add(fn.replace('.yaml', ''))
    
    # Table II IDs
    with open('main.tex') as f:
        tex = f.read()
    t2_start = tex.find('\\caption{Complete record-level classification')
    t2_end = tex.find('\\end{table*}', t2_start)
    t2_section = tex[t2_start:t2_end]
    table2_ids = set()
    for line in t2_section.split('\n'):
        m = re.match(r'\s*\\?(?:quad\s+)?([a-z][a-z0-9-]+)(?:\s*\([A-Z0-9]+\))?\s+&', line)
        if m:
            raw = m.group(1).strip()
            if raw and raw != 'r7-CRS-cluster':
                table2_ids.add(raw)
    
    # Table IV IDs
    t4_start = tex.find('\\caption{All 36 included records')
    t4_end = tex.find('\\end{table*}', t4_start)
    t4_section = tex[t4_start:t4_end]
    table4_ids = set()
    for line in t4_section.split('\n'):
        m = re.match(r'\s*([a-z][a-z0-9-]+)\s*&', line)
        if m:
            table4_ids.add(m.group(1).strip())
    
    print(f"   CSV: {len(csv_ids)}")
    print(f"   YAML: {len(yaml_ids)}")
    print(f"   Table II: {len(table2_ids)}")
    print(f"   Table IV: {len(table4_ids)}")
    
    csv_yaml = csv_ids == yaml_ids
    csv_t2 = csv_ids == table2_ids
    csv_t4 = csv_ids == table4_ids
    
    print(f"   CSV == YAML: {csv_yaml}")
    print(f"   CSV == T2: {csv_t2}")
    print(f"   CSV == T4: {csv_t4}")
    
    return csv_yaml and csv_t2 and csv_t4


def check_build():
    """Check PDF build status."""
    print("\n4. BUILD CHECK")
    
    # Check if main.pdf exists
    if not os.path.exists('main.pdf'):
        print("   main.pdf: MISSING")
        return False
    
    # Get PDF info
    pages = run_command("pdfinfo main.pdf | grep Pages | awk '{print $2}'")
    size = run_command("pdfinfo main.pdf | grep 'File size' | awk '{print $3}'")
    
    print(f"   Pages: {pages}")
    print(f"   Size: {size} bytes")
    
    return int(pages) == 17


def check_hashes():
    """Check SHA-256 hashes against RELEASE_MANIFEST.md."""
    print("\n5. HASH CHECK")
    
    # Get current hashes
    current = run_command("sha256sum main.tex refs.bib main.pdf evidence/autonomy-loop-assignments.csv")
    
    # Parse RELEASE_MANIFEST.md
    with open('RELEASE_MANIFEST.md') as f:
        manifest = f.read()
    
    # Extract expected hashes
    expected = {}
    for line in manifest.split('\n'):
        if '|' in line and 'SHA-256' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) == 2 and len(parts[1]) == 64:
                expected[parts[0]] = parts[1]
    
    print("   Current vs Expected:")
    all_match = True
    for line in current.split('\n'):
        if line:
            parts = line.split()
            if len(parts) == 2:
                fname = parts[1]
                current_hash = parts[0]
                if fname in expected:
                    match = current_hash == expected[fname]
                    status = "OK" if match else "MISMATCH"
                    print(f"     {fname}: {status}")
                    if not match:
                        all_match = False
    
    return all_match


def main():
    """Run all checks."""
    print("=" * 70)
    print("FINAL VERIFICATION — SoK Co-Evolution Paper")
    print("=" * 70)
    
    os.chdir("/home/nixon/RESEARCH CYBER")
    
    results = []
    results.append(("Bibliography", check_bibliography()))
    results.append(("Manifest", check_manifest()))
    results.append(("Record Sets", check_record_sets()))
    results.append(("Build", check_build()))
    results.append(("Hashes", check_hashes()))
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    all_pass = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"   {name}: {status}")
        if not passed:
            all_pass = False
    
    print("\n" + "=" * 70)
    if all_pass:
        print("ALL CHECKS PASS — Paper is ready for submission")
        return 0
    else:
        print("SOME CHECKS FAILED — Review issues above")
        return 1


if __name__ == '__main__':
    sys.exit(main())
