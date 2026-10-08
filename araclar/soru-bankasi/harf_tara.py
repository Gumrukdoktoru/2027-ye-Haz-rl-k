"""Soru verisinde Türkçe karakter hatası taraması: kaynak sözlüğünde olmayan, ama ı/i, ş/s, ğ/g, ç/c, ö/o, ü/u
değişimiyle kaynakta bulunan kelimeleri listeler."""
import glob, re, runpy, sys, itertools
from collections import Counter, defaultdict
S = sys.argv[1]
def low(s): return s.replace('İ', 'i').replace('I', 'ı').lower()
W = re.compile(r"[a-zçğıöşüâîû]+")
voc = Counter()
for f in glob.glob(f'{S}/mevzuat/metin/*.txt'):
    voc.update(W.findall(low(open(f, encoding='utf-8', errors='ignore').read())))
# prompt ve tanıdık genel kelimeler için soru verisinin kendi sözlüğü de sayılır (çoğunluk doğru yazılmıştır)
qv = Counter(); yer = defaultdict(list)
alan = ('kok', 'd', 'c', 'siklar', 'g', 'cek', 'madde')
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    for i, q in enumerate(runpy.run_path(f)['Q'], 1):
        for a in alan:
            v = q.get(a)
            if not v: continue
            txt = ' '.join(v) if isinstance(v, list) else str(v)
            for w in W.findall(low(txt)):
                qv[w] += 1; yer[w].append(f'SB{no}-{i:02d}:{a}')
PAR = {'ı': 'i', 'i': 'ı', 's': 'ş', 'ş': 's', 'g': 'ğ', 'ğ': 'g', 'c': 'ç', 'ç': 'c', 'o': 'ö', 'ö': 'o', 'u': 'ü', 'ü': 'u'}
def varyant(w):
    idx = [k for k, ch in enumerate(w) if ch in PAR]
    if len(idx) > 10: idx = idx[:10]
    for r in range(1, min(3, len(idx)) + 1):
        for comb in itertools.combinations(idx, r):
            l = list(w)
            for k in comb: l[k] = PAR[l[k]]
            yield ''.join(l)
    if 'ı' in w: yield w.replace('ı', 'i')
    if 'i' in w: yield w.replace('i', 'ı')
bul = []
for w, n in qv.items():
    if voc[w] or len(w) < 3: continue
    best = max(((voc[v] + qv[v], v) for v in varyant(w) if v != w and (voc[v] or qv[v] > n)), default=None)
    if best and best[0] >= 2:
        bul.append((w, best[1], n, yer[w][:4]))
for w, v, n, y in sorted(bul, key=lambda x: -x[2]):
    print(f'{w} → {v} ({n}) {y}')
print(len(bul), 'şüpheli')
