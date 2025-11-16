#!/usr/bin/env python3
"""
aggregate_results.py
Reads detection JSONs from detection/bandit and detection/semgrep and produces master CSV.
Usage:
  python3 aggregate_results.py ~/LLM-Vuln-Project
Output:
  ~/LLM-Vuln-Project/summaries/master_detection.csv
"""
import os, sys, json, csv, glob

def parse_bandit(jsonpath):
    rows=[]
    with open(jsonpath,'r',encoding='utf-8') as f:
        data=json.load(f)
    for r in data.get('results',[]):
        rows.append({
            'tool':'bandit',
            'cwe_folder': os.path.basename(jsonpath).replace('_bandit.json',''),
            'file': r.get('filename'),
            'issue': r.get('issue_text'),
            'test_name': r.get('test_name'),
            'severity': r.get('issue_severity'),
            'confidence': r.get('issue_confidence')
        })
    return rows

def parse_semgrep(jsonpath):
    rows=[]
    with open(jsonpath,'r',encoding='utf-8') as f:
        data=json.load(f)
    for r in data.get('results',[]):
        rows.append({
            'tool':'semgrep',
            'cwe_folder': os.path.basename(jsonpath).replace('_semgrep.json',''),
            'file': r.get('path'),
            'issue': r.get('extra',{}).get('message'),
            'check_id': r.get('check_id'),
            'severity': r.get('extra',{}).get('severity')
        })
    return rows

def main(base):
    base = os.path.abspath(base)
    bandit_dir = os.path.join(base,'detection','bandit')
    semgrep_dir = os.path.join(base,'detection','semgrep')
    outdir = os.path.join(base,'summaries')
    os.makedirs(outdir, exist_ok=True)
    rows=[]
    for bf in glob.glob(os.path.join(bandit_dir,'*_bandit.json')):
        rows += parse_bandit(bf)
    for sf in glob.glob(os.path.join(semgrep_dir,'*_semgrep.json')):
        rows += parse_semgrep(sf)
    outcsv = os.path.join(outdir,'master_detection.csv')
    keys = sorted({k for r in rows for k in r.keys()}) if rows else ['tool','cwe_folder','file','issue']
    with open(outcsv,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print("Wrote", outcsv)

if __name__=='__main__':
    if len(sys.argv)!=2:
        print("Usage: aggregate_results.py /path/to/LLM-Vuln-Project")
        sys.exit(1)
    main(sys.argv[1])
