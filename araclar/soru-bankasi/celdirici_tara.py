"""Gerekçede 'çeldirici' diye anılan şeyin doğru cevap olup olmadığını tarar (veri dosyaları üzerinde)."""
import glob, re, runpy, sys
from difflib import SequenceMatcher
S = sys.argv[1]
def n(s): return re.sub(r'\s+', ' ', s.replace('İ', 'i').replace('I', 'ı').lower().strip(" .;:'\""))
def ws(s): return set(w for w in re.findall(r'[a-zçğıöşü0-9.,]+', n(s)) if len(w) > 2)
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    for i, q in enumerate(runpy.run_path(f)['Q'], 1):
        g = re.sub(r"Bu nedenle doğru cevap.*$", "", q['g'])
        for sent in re.split(r'(?<=[.!?])\s+', g):
            if 'çeldirici' not in sent.lower(): continue
            # tırnaklı alıntı
            qs = re.findall(r"(?i)çeldirici[^'‘\"“.:]{0,40}['‘\"“]([^'’\"”]{3,300})['’\"”]", sent)
            hit = None
            for t in qs:
                if n(t) == n(q['d']) or (len(n(t)) > 10 and n(t) in n(q['d'])): hit = ('ALINTI=DOĞRU', t)
            if not hit:
                d_ov = len(ws(q['d']) & ws(sent)) / max(1, len(ws(q['d'])))
                c_ov = max(len(ws(c) & ws(sent)) / max(1, len(ws(c))) for c in (q['c'] or [x for x in q.get('siklar', []) if x != q['d']]))
                if d_ov >= 0.6 and d_ov > c_ov + 0.2: hit = ('ÖRTÜŞME', f'd={d_ov:.2f} c={c_ov:.2f}')
            if hit:
                print(f"SB{no}-?? (dosya Q{i}) {hit[0]} | d: {q['d'][:70]} | {sent[:160]}")
