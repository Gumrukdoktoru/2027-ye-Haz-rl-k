"""Deneme 6-10 soru planı: her deneme bir yılın 100 sorusunu birebir karşılar.
Çıktı: plan.json (500 satır). Mesleki (21-100) için hedef tip, şık sınıfı, ters tuzak, kök bandı ve
cevap harfi; genel kültür (1-20) için ders ve cevap harfi."""
import csv, json, random, itertools
from kumeler import KUME, DENEME
rows = list(csv.reader(open('cikmis_envanter.tsv'), delimiter='\t'))[1:]
env2k = {k2: k for k, v in KUME.items() for k2 in v['env']}
QUOTA = {'T1': 16, 'T1+T2': 8, 'T2': 10, 'T3': 11, 'T4': 10, 'T5': 6, 'T6': 5, 'T7': 5, 'T8': 4, 'T9': 3, 'T10': 2}
assert sum(QUOTA.values()) == 80
T9OK = {'K02', 'K10', 'K11', 'K12'}
AFF = {  # kalıp -> {tip: maliyet}
 'KAPSAM_DIŞI': {'T1': 0, 'T1+T2': 1, 'T2': 2, 'T10': 3, 'T4': 4},
 'YANLIŞ': {'T1': 0, 'T1+T2': .5, 'T10': 2, 'T2': 2, 'T4': 4},
 'ÖNERMELİ': {'T2': 0, 'T1+T2': .5, 'T1': 2, 'T10': 2.5},
 'SÜRE': {'T3': 0, 'T5': 2, 'T8': 3, 'T2': 3, 'T1': 3, 'T4': 3, 'T7': 4},
 'ORAN-TUTAR': {'T3': 0, 'T9': 1, 'T5': 2, 'T4': 3},
 'TANIM': {'T4': 0, 'T6': 1, 'T5': 2, 'T1': 3},
 'KAVRAM': {'T6': 0, 'T4': 1, 'T5': 2},
 'DOĞRU': {'T4': 0, 'T2': 2, 'T1': 2, 'T8': 3},
 'KAPSAM': {'T4': 0, 'T1': 1, 'T2': 2},
 'BELGE': {'T4': 0, 'T7': 2, 'T6': 2, 'T5': 2},
 'ŞART': {'T4': 0, 'T2': 1, 'T1': 2},
 'MÜEYYİDE': {'T4': 0, 'T9': 1, 'T8': 1, 'T3': 2},
 'YETKİ': {'T7': 0, 'T4': 1, 'T5': 2},
 'BOŞLUK': {'T5': 0, 'T3': 2, 'T4': 2},
 'EŞLEŞTİRME': {'T10': 0, 'T2': 2},
 'HESAP': {'T9': 0, 'T3': 2},
 'OLAY': {'T8': 0, 'T4': 2},
}
def cost(r, t):
    k = env2k[r[2]]
    if t == 'T9' and k not in T9OK: return 99
    return AFF.get(r[4], {}).get(t, 5)

def ata(R, seed):
    rnd = random.Random(seed)
    best = None
    for it in range(300):
        q = dict(QUOTA); a = {}
        pairs = sorted(((cost(r, t) + rnd.random() * .3, i, t) for i, r in enumerate(R) for t in QUOTA))
        for c, i, t in pairs:
            if i in a or q[t] == 0: continue
            a[i] = t; q[t] -= 1
        # yerel iyileştirme: ikili takas
        imp = True
        while imp:
            imp = False
            for i, j in itertools.combinations(range(len(R)), 2):
                ti, tj = a[i], a[j]
                if ti == tj: continue
                if cost(R[i], tj) + cost(R[j], ti) < cost(R[i], ti) + cost(R[j], tj) - 1e-9:
                    a[i], a[j] = tj, ti; imp = True
        tot = sum(cost(R[i], a[i]) for i in a)
        if best is None or tot < best[0]: best = (tot, dict(a))
    return best[1]

def harfler(seed):
    r = random.Random(seed)
    for _ in range(100000):
        kalan_gk = {h: 4 for h in 'ABCDE'}; kalan_m = {'A': 14, 'B': 16, 'C': 16, 'D': 17, 'E': 17}
        s = []
        ok = True
        for i in range(100):
            kal = kalan_gk if i < 20 else kalan_m
            ad = [h for h in 'ABCDE' if kal[h] and (not s or h != s[-1])]
            if not ad: ok = False; break
            m = max(kal[h] for h in ad)
            h = r.choice([h for h in ad if kal[h] >= m - 2]); s.append(h); kal[h] -= 1
        if ok: return s

def gk_ders(y, n):
    if n <= 5: return 'Türkçe'
    if n <= 10: return 'Matematik'
    if n <= 15: return 'Tarih'
    if y == '2021' and n in (17, 18): return 'Uluslararası Kuruluşlar'
    return 'Anayasa'
GKW = {'Türkçe': 'GTR', 'Matematik': 'GMA', 'Tarih': 'GTA', 'Anayasa': 'GAN', 'Uluslararası Kuruluşlar': 'GAN'}

plan = []
for d, y in DENEME.items():
    L = harfler(1000 + d)
    for n in range(1, 21):
        plan.append(dict(id=f'D{d}-{n:03d}', deneme=d, no=n, cikmis=f'{y}/{n}', blok='GK', ders=gk_ders(y, n),
                         yazar=GKW[gk_ders(y, n)], harf=L[n - 1]))
    R = sorted([r for r in rows if r[0] == y], key=lambda r: int(r[1]))
    assert len(R) == 80
    a = ata(R, d)
    rnd = random.Random(50 + d)
    idx = {t: [i for i in range(80) if a[i] == t] for t in QUOTA}
    sinif, tuzak, bant = {}, {}, {}
    def dag(lst, spec):  # lst indeksleri spec'e göre rastgele dağıt
        lst = lst[:]; rnd.shuffle(lst); out = {}; p = 0
        for val, k in spec:
            for i in lst[p:p + k]: out[i] = val
            p += k
        assert p == len(lst), (spec, len(lst))
        return out
    sinif.update({i: 'kısa' for t in ('T2', 'T1+T2', 'T6', 'T9', 'T10') for i in idx[t]})
    sinif.update(dag(idx['T3'], [('kısa', 3), ('orta', 8)]))
    sinif.update({i: 'orta' for t in ('T5', 'T7') for i in idx[t]})
    sinif.update(dag(idx['T1'], [('uzun', 12), ('orta', 4)]))
    sinif.update(dag(idx['T4'], [('uzun', 5), ('orta', 5)]))
    sinif.update(dag(idx['T8'], [('uzun', 3), ('orta', 1)]))
    uz = [i for i in range(80) if sinif[i] == 'uzun']; ort = [i for i in range(80) if sinif[i] == 'orta' and a[i] in ('T1', 'T4', 'T7', 'T8')]
    rnd.shuffle(uz); rnd.shuffle(ort)
    for i in uz[:8] + ort[:4]: tuzak[i] = True
    t2 = idx['T2'] + idx['T1+T2']
    bant.update(dag(t2, [('>700', 1), ('350-700', 13), ('120-350', 4)]))
    bant.update(dag(idx['T8'], [('>700', 3), ('350-700', 1)]))
    bant.update(dag(idx['T9'], [('>700', 2), ('350-700', 1)]))
    bant.update({i: '>700' for i in idx['T10']})
    bant.update(dag(idx['T5'], [('350-700', 1), ('120-350', 5)]))
    bant.update({i: '120-350' for i in idx['T6']})
    bant.update(dag(idx['T1'], [('120-350', 9), ('≤120', 7)]))
    bant.update(dag(idx['T4'], [('120-350', 6), ('≤120', 4)]))
    bant.update(dag(idx['T3'], [('120-350', 2), ('≤120', 9)]))
    bant.update(dag(idx['T7'], [('120-350', 1), ('≤120', 4)]))
    for i, r in enumerate(R):
        n = int(r[1])
        plan.append(dict(id=f'D{d}-{n:03d}', deneme=d, no=n, cikmis=f'{y}/{n}', blok='GÜMRÜK', yazar=env2k[r[2]],
                         konu=r[2], olculen=r[3], kalip_eski=r[4], kaynak=r[5], resmi=r[7], tip=a[i], sinif=sinif[i],
                         tuzak=tuzak.get(i, False), bant=bant[i], harf=L[n - 1]))
json.dump(plan, open('plan.json', 'w'), ensure_ascii=False, indent=0)
import collections as C
for d in DENEME:
    P = [p for p in plan if p['deneme'] == d and p['blok'] == 'GÜMRÜK']
    deg = sum(1 for p in P if AFF.get(p['kalip_eski'], {}).get(p['tip'], 5) > 0)
    print(d, 'tip değişen:', deg, dict(C.Counter(p['sinif'] for p in P)), 'tuzak', sum(p['tuzak'] for p in P),
          dict(C.Counter(p['bant'] for p in P)), ''.join(p['harf'] for p in plan if p['deneme'] == d))
print(dict(C.Counter(p['yazar'] for p in plan)))
