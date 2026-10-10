"""Batch dosyalarını birleştirir → set6.json … set10.json ve deneme düzeyi denetim raporu.
Kullanım: python3 birlestir.py   (eksik soru varsa yalnız rapor verir, json yazmaz)"""
import json, re, glob, collections, itertools, sys
from kontrol import PLAN, STRIP, sinif, bant, kanit_ok, TOK, jac, HAF, denetle
L = 'ABCDE'
QUOTA = {'T1': 16, 'T1+T2': 8, 'T2': 10, 'T3': 11, 'T4': 10, 'T5': 6, 'T6': 5, 'T7': 5, 'T8': 4, 'T9': 3, 'T10': 2}
HEDEF_HARF_M = {'A': 14, 'B': 16, 'C': 16, 'D': 17, 'E': 17}
ALL = {}
for f in sorted(glob.glob('batch_*.py')):
    ns = {}; exec(open(f).read(), ns)
    for q in ns['Q']:
        q['batch'] = f[6:-3]
        if q['id'] in ALL: print('!! iki batchte aynı id', q['id'])
        ALL[q['id']] = q
eksik = [i for i in PLAN if i not in ALL]
print(f'Toplam yazılan: {len(ALL)} / {len(PLAN)}; eksik: {len(eksik)}')
if eksik: print('   ', ' '.join(eksik[:60]), '…' if len(eksik) > 60 else '')
C = collections.Counter

def harfle(g, h):
    md = g.rfind('(MD'); bas, son = g[:md].rstrip(), g[md:]
    return f'{bas} Bu nedenle doğru cevap {h} seçeneğidir. {son}'

rapor = []
for d in range(6, 11):
    ids = [f'D{d}-{n:03d}' for n in range(1, 101)]
    if any(i not in ALL for i in ids): print(f'D{d}: eksik soru var, atlanıyor'); continue
    Q = []
    for i in ids:
        q = dict(ALL[i]); P = PLAN[i]; h = P['harf']
        if q.get('opts'):
            opts = list(q['opts'])
        else:
            k = L.index(h); dist = list(q['c']); opts = [q['d'] if j == k else dist.pop(0) for j in range(5)]
        assert opts[L.index(h)] == q['d'], i
        q.update(no=P['no'], harf=h, opts=opts, blok=P['blok'], cikmis=P['cikmis'], ders=P.get('ders'), g_harfli=harfle(q['g'], h))
        Q.append(q)
    M = [q for q in Q if q['blok'] == 'GÜMRÜK']
    hata = denetle(Q, f'D{d}') if '--denetle' in sys.argv else 0
    ard = [q['no'] for a, q in zip(Q, Q[1:]) if a['harf'] == q['harf']]
    tip = C(q['tip'] for q in M)
    tipfark = {t: tip.get(t, 0) - v for t, v in QUOTA.items() if tip.get(t, 0) != v}
    sn = C(sinif(q['opts']) for q in M)
    bn = C(bant(len(STRIP(' '.join(q['kok'])))) for q in M)
    tz = sum(bool(q.get('tuzak')) for q in M)
    lng = sum(len(STRIP(q['d'])) > max(len(STRIP(x)) for x in q['c']) for q in M)
    print(f"\n=== DENEME {d} ===")
    print(' harf (1-100):', dict(sorted(C(q['harf'] for q in Q).items())), '| 21-100:', dict(sorted(C(q['harf'] for q in M).items())), '| art arda aynı:', ard or 'yok')
    print(' tip (21-100):', dict(sorted(tip.items())), '| kota farkı:', tipfark or 'yok')
    print(' şık sınıfı:', dict(sn), '(hedef kısa 31 · orta 29 · uzun 20) | ters tuzak:', tz, '(12) | doğru en uzun:', lng)
    print(' kök bandı:', dict(sorted(bn.items())), '(hedef ≤120 24 · 120-350 32 · 350-700 16 · >700 8)')
    print(' zorluk:', dict(C(q['z'] for q in Q)), '| sapma:', [q['id'] for q in Q if q.get('sapma')])
    json.dump(Q, open(f'set{d}.json', 'w'), ensure_ascii=False, indent=0)
# denemeler arası ve hafıza ile çekirdek benzerliği
yeni = [(i, q['cek'], TOK(q['cek'])) for i, q in ALL.items()]
print('\n=== ÇEKİRDEK BENZERLİĞİ (≥0.45) ===')
n = 0
for (a, ca, ta), (b, cb, tb) in itertools.combinations(yeni, 2):
    if jac(ta, tb) >= 0.45: n += 1; print(f' YENİ {a} ~ {b}: {ca[:70]} | {cb[:70]}')
for a, ca, ta in yeni:
    for h, ch, th in HAF:
        if jac(ta, th) >= 0.45: n += 1; print(f' HAFIZA {a} ~ {h}: {ca[:70]} | {ch[:70]}')
print(' aday:', n)
