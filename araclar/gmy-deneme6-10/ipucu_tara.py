"""Cevap ipucu taraması (sınav kurnazlığı): set6–10.json.
YAKINSAMA: doğru şık öteki şıklarla en çok kelime paylaşan şık. BİLEŞEN: doğru şık, başka şıklarda da geçen bileşenleri (; , sonra ve) en çok birleştiren şık.
KÖK-ORTAK: doğru şık kökle belirgin biçimde daha çok kelime paylaşıyor. Bayraklar adaydır; T5/T3 şıklarında benzerlik doğal olabilir.
Kullanım: python3 ipucu_tara.py"""
import json, re
from kontrol import norm, STRIP, kombo
STOP = set('ve ile veya bir bu da de için olarak olan göre ki ya en çok az her ise ancak tarafından halinde hâlinde kadar sonra önce'.split())
def tok(s): return [w for w in re.findall(r'[0-9a-zçğıöşüâîû%]+', norm(STRIP(s))) if w not in STOP]
def parca(o):  # bileşen: ; , ve "sonra" ile bölünen ifadeler
    return [p.strip() for p in re.split(r';|,| sonra | ve ', norm(STRIP(o))) if len(p.strip()) > 2]
L = 'ABCDE'; res = []
for d in range(6, 11):
    for q in json.load(open(f'set{d}.json')):
        o = q['opts']; k = L.index(q['harf'])
        if all(kombo(x) for x in o): continue  # öncül merdiveni
        T = [set(tok(x)) for x in o]
        # 1) yakınsama: her şıkkın diğerleriyle ortak kelime toplamı
        sc = [sum(len(T[i] & T[j]) / max(1, len(T[i] | T[j])) for j in range(5) if j != i) for i in range(5)]
        srt = sorted(sc, reverse=True)
        yak = sc[k] == srt[0] and srt[0] - srt[1] >= 0.15
        # 2) bileşen yakınsaması: doğru şıkkın her bileşeni başka şıkta da var mı
        P = [set(parca(x)) for x in o]
        bil = [sum(1 for p in P[i] for j in range(5) if j != i and p in P[j]) for i in range(5)]
        bsrt = sorted(bil, reverse=True)
        byak = bil[k] == bsrt[0] and bsrt[0] > bsrt[1] and len(P[k]) >= 2
        # 3) kökle kelime ortaklığı
        K = set(tok(' '.join(q['kok'])))
        ko = [len(T[i] & K) for i in range(5)]
        ksrt = sorted(ko, reverse=True)
        kok = ko[k] == ksrt[0] and ksrt[0] - ksrt[1] >= 3
        if yak or byak or kok:
            res.append((q['id'], q['tip'], 'YAKINSAMA' if yak else '', 'BİLEŞEN' if byak else '', 'KÖK-ORTAK' if kok else '', [round(x, 2) for x in sc], bil, ko))
for r in res: print(*r)
print(len(res))
