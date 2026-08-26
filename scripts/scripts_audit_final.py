#!/usr/bin/env python3
"""CP4 final audit: run AFTER reviewer markup applied. Fails hard on any gate."""
import re,glob,csv,yaml,subprocess,sys
fails=[]
bib=open("refs.bib").read()
keys=re.findall(r"@\w+\{([^,\s]+),",bib)
if len(keys)!=len(set(keys)): fails.append("duplicate bib keys")
for bad in ("VERIFY","verify from local PDF","authors TBD","and others","TODO"):
    if bad in bib: fails.append("placeholder: "+bad)
cited=set()
for f in ["main.tex"]:
    cited|= {k.strip() for g in re.findall(r"\\cite\{([^}]+)\}",open(f).read()) for k in g.split(",")}
miss=cited-set(keys)
if miss: fails.append("missing bib keys: %s"%sorted(miss))
never=[k for k in keys if k not in cited]
print("never-cited entries (deliberate-inclusion review):",never or "NONE")
recs=[yaml.safe_load(open(p)) for p in glob.glob("corpus/included/*.yaml")]
from collections import Counter
lv=Counter(r.get("autonomy_level") for r in recs if r.get("temporal_scope")=="in-window")
bearing={k:v for k,v in lv.items() if k in("A0","A1","A2","A3","uncertain")}
if sum(bearing.values())!=14: fails.append("autonomy-bearing != 14: %s"%bearing)
if bearing.get("A3",0)!=0: fails.append("A3 nonzero without framework revision!")
if len(recs)!=36: fails.append("corpus != 36")
txt=subprocess.run(["pdftotext","sok-coevolution.pdf","-"],capture_output=True,text=True).stdout
flat=re.sub(r"\s+"," ",txt.replace("-\n","")).lower()
for ph in ("CVE-2024-9143","CVE-2025-37891","CVE-2025-6965"): 
    if ph.lower() not in flat: fails.append("expected CVE identifier missing from PDF: "+ph)
for ph in ("no included evidence met our operational definition","weakest missing condition",
           "increasingly binding constraint","administrative record correction"):
    if ph.lower() not in flat: fails.append("sentinel missing from PDF: "+ph)
print("AUDIT:", "FAIL" if fails else "ALL GATES PASS", fails or "")
sys.exit(1 if fails else 0)
