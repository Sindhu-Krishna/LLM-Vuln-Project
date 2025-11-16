#!/usr/bin/env python5
"""
extract_code_blocks.py
- Input: path to a folder that contains model .txt outputs (chatgpt.txt, gemini.txt, etc.)
- Output: for each model file found, creates:
    model_insecure.<ext>
    model_secure.<ext>
    model_extracted_meta.json  (contains 'insecure_block_info' + 'secure_block_info')
Rules:
- Looks for fenced code blocks like ```python or ```js
- If no fence found, attempts to heuristically split by "INSECURE" / "SECURE" headings
- Defaults to .txt if language cannot be determined
"""
import re, sys, os, json

# mapping fence -> extension
lang_map = {
    'python':'py', 'py':'py', 'javascript':'js', 'js':'js', 'php':'php',
    'html':'html', 'bash':'sh', 'sh':'sh', 'shell':'sh', 'java':'java',
    'c':'c','cpp':'cpp'
}

def detect_lang(fence_info):
    if not fence_info:
        return 'txt'
    lang = fence_info.lower().strip()
    return lang_map.get(lang, 'txt')

def extract_from_text(text):
    # find fenced code blocks
    fences = re.findall(r'```([\w+-]*)\n(.*?)```', text, flags=re.S)
    if fences:
        return fences  # list of (lang, code)
    # fallback: split around common headings
    markers = re.split(r'\n-{2,}\n', text)
    candidates = []
    for part in markers:
        m_insecure = re.search(r'INSECURE', part, flags=re.I)
        m_secure = re.search(r'SECURE', part, flags=re.I)
    # last resort: try to find "INSECURE" and "SECURE" zones
    insecure = None; secure = None
    m_insecure = re.search(r'(INSECURE.*?)(?=SECURE|$)', text, flags=re.I|re.S)
    if m_insecure:
        insecure = m_insecure.group(1)
    m_secure = re.search(r'(SECURE.*?)(?=INSECURE|$)', text, flags=re.I|re.S)
    if m_secure:
        secure = m_secure.group(1)
    blocks = []
    if insecure:
        blocks.append(('txt', insecure.strip()))
    if secure:
        blocks.append(('txt', secure.strip()))
    return blocks

def write_block(outdir, modelname, suffix, ext, code):
    fname = os.path.join(outdir, f"{modelname}_{suffix}.{ext}")
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(code.strip() + '\n')
    return fname

def main(folder):
    folder = os.path.abspath(folder)
    for fname in os.listdir(folder):
        if not fname.lower().endswith('.txt'):
            continue
        modelname = os.path.splitext(fname)[0]  # chatgpt
        path = os.path.join(folder, fname)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        fences = re.findall(r'```([\w+-]*)\n(.*?)```', text, flags=re.S)
        outmeta = {'model': modelname, 'src_file': fname, 'extracted': []}
        if fences:
            # multiple fences: heuristics: first fence -> insecure, second -> secure if present
            if len(fences) >= 1:
                lang, code = fences[0]
                ext = detect_lang(lang)
                p = write_block(folder, modelname, 'insecure', ext, code)
                outmeta['extracted'].append({'type':'insecure','file':os.path.basename(p),'lang':lang})
            if len(fences) >= 2:
                lang, code = fences[1]
                ext = detect_lang(lang)
                p = write_block(folder, modelname, 'secure', ext, code)
                outmeta['extracted'].append({'type':'secure','file':os.path.basename(p),'lang':lang})
            # any remaining fences ignored
        else:
            # fallback: try to find INSECURE / SECURE sections
            m_insecure = re.search(r'INSECURE[\s\S]*?(?=SECURE|$)', text, flags=re.I)
            m_secure = re.search(r'SECURE[\s\S]*?(?=INSECURE|$)', text, flags=re.I)
            if m_insecure:
                code = m_insecure.group(0)
                # strip header
                code = re.sub(r'INSECURE[:\-\s]*','', code, flags=re.I).strip()
                p = write_block(folder, modelname, 'insecure', 'txt', code)
                outmeta['extracted'].append({'type':'insecure','file':os.path.basename(p),'lang':'txt'})
            if m_secure:
                code = m_secure.group(0)
                code = re.sub(r'SECURE[:\-\s]*','', code, flags=re.I).strip()
                p = write_block(folder, modelname, 'secure', 'txt', code)
                outmeta['extracted'].append({'type':'secure','file':os.path.basename(p),'lang':'txt'})
        # save meta
        meta_file = os.path.join(folder, f"{modelname}_extracted_meta.json")
        with open(meta_file, 'w', encoding='utf-8') as mf:
            json.dump(outmeta, mf, indent=2)
        print(f"[+] processed {fname} -> {outmeta['extracted']} (meta={os.path.basename(meta_file)})")

if __name__=='__main__':
    if len(sys.argv)!=2:
        print("Usage: extract_code_blocks.py /path/to/CWE-folder")
        sys.exit(1)
    main(sys.argv[1])
