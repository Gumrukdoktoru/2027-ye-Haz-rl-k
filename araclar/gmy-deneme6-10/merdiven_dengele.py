"""Öncüllü (T2, T1+T2 ve öncüllü genel kültür) sorularda şık merdivenini öncül sıklığı ipucundan arındırır.
İpucu: şıklarda en sık geçen öncüllerden oluşan şıkkı seçen strateji (toplam / ortalama / en az sıklık) şanstan (%20) yüksek isabet eder.
Doğru kombinasyon ve planlanan harf korunur; yalnız çeldirici kombinasyonlar seçilir. Kısıtlar: merdiven artan (kontrol.py),
her öncül en az bir şıkta, doğru kombinasyona tek öncül farkla yakın en az 2 çeldirici. Mevcut merdivenden en az değişiklik tercih edilir.
Kullanım: python3 merdiven_dengele.py [--ceza=1.5] [--alti]   (yalnız rapor; --alti en az sık stratejileri de hedefler)
          python3 merdiven_dengele.py --yaz      (batch dosyalarına yazar; açıklamada geçen eski çeldirici kombinasyonlar listelenir)"""
import glob, re, sys, itertools, collections
from kontrol import kombo, PLAN
L = 'ABCDE'; ROM = ['I', 'II', 'III', 'IV', 'V']
def yazi(k, roma=True):
    s = [ROM[x - 1] if roma else str(x) for x in k]
    return f'Yalnız {s[0]}' if len(s) == 1 else (', '.join(s[:-1]) + ' ve ' + s[-1])
def skorlar(O):
    fr = collections.Counter(x for o in O for x in o)
    return [[sum(fr[x] for x in o) for o in O], [sum(fr[x] for x in o) / len(o) for o in O], [min(fr[x] for x in o) for o in O]]
def vektor(O, k):  # 6 strateji (toplam/ortalama/en az sıklık × en çok/en az seçen) için doğruyu bulma olasılığı
    v = []
    for sc in skorlar(O):
        for uc in (max, min):
            m = uc(sc); b = [i for i, s in enumerate(sc) if s == m]
            v.append(1 / len(b) if k in b else 0)
    return v
def isabet(O, k): return sum(vektor(O, k)[0::2])  # yalnız "en sık" stratejileri
def adaylar(n, d, k):
    tum = [c for r in range(1, n + 1) for c in itertools.combinations(range(1, n + 1), r) if list(c) != d]
    on = [c for c in tum if (len(c), c) < (len(d), tuple(d))]; son = [c for c in tum if (len(c), c) > (len(d), tuple(d))]
    if len(on) < k or len(son) < 4 - k: return None
    for a in itertools.combinations(on, k):
        for b in itertools.combinations(son, 4 - k):
            O = [list(x) for x in a] + [d] + [list(x) for x in b]
            if {x for o in O for x in o} != set(range(1, n + 1)): continue
            if sum(1 for o in O if o != d and len(set(o) ^ set(d)) == 1) < 2: continue
            yield O
# Açgözlü dengeleme: sorular sırayla işlenir; her soruda, 6 stratejinin birikmiş isabeti şans düzeyine (%20) en yakın kalacak
# merdiven seçilir; eşitlikte mevcut merdivenden en az değişiklik. Böylece ne "en sık" ne "en az sık" öncül stratejisi kazandırır.
yaz = '--yaz' in sys.argv; rapor = []; say = 0
HEDEF = range(6) if '--alti' in sys.argv else (0, 2, 4)  # varsayılan: yalnız "en sık öncül" stratejileri (öğrencinin kullandığı ipucu)
LAMBDA = float(next((a.split('=')[1] for a in sys.argv if a.startswith('--ceza=')), '1.5'))  # değişen her şık için ceza (1.5: ~%20 isabet, en az değişiklik)
TOP0 = [0.0] * 6; TOP1 = [0.0] * 6
SORU = []
for f in sorted(glob.glob('batch_*.py')):
    ns = {}; exec(open(f).read(), ns)
    for q in ns['Q']:
        o = q.get('opts')
        if o and all(kombo(x) for x in o): SORU.append((f, q))
SORU.sort(key=lambda t: (int(t[1]['id'].split('-')[0][1:]), int(t[1]['id'].split('-')[1])))
DEG = collections.defaultdict(list)
for f, q in SORU:
        o = q['opts']
        O = [kombo(x) for x in o]; d = kombo(q['d']); k = L.index(PLAN[q['id']]['harf']); n = max(max(x) for x in O)
        onc = [l for l in q['kok'] if re.match(r'^\s*(I|II|III|IV|V)\.\s', l)]; n = max(n, len(onc))
        say += 1; v0 = vektor(O, k); TOP0 = [a + b for a, b in zip(TOP0, v0)]
        eski = {tuple(x) for x in O}; best = None
        for Y in list(adaylar(n, d, k)) + [O]:
            v = vektor(Y, k)
            sap = sum((TOP1[j] + v[j] - 0.2 * say) ** 2 for j in HEDEF)
            kalan = len(eski & {tuple(y) for y in Y})
            key = (round(sap + LAMBDA * (5 - kalan), 6), -kalan)
            if best is None or key < best[0]: best = (key, Y)
        Y = best[1]; TOP1 = [a + b for a, b in zip(TOP1, vektor(Y, k))]
        if sorted(map(tuple, Y)) == sorted(map(tuple, O)): continue
        h0, h1 = isabet(O, k), isabet(Y, k)
        roma = not o[0].replace('Yalnız ', '')[0].isdigit()
        yopts = [yazi(x, roma) + ('.' if o[0].endswith('.') else '') for x in Y]
        cikan = [yazi(x, roma) for x in O if x not in Y]
        uyari = [c for c in cikan if c in q.get('g', '')]
        rapor.append(f"{q['id']} ({f[6:-3]}): isabet {h0:.2f} → {h1:.2f} | {' / '.join(o)}  ⇒  {' / '.join(yopts)}" + (f" | AÇIKLAMADA GEÇEN: {uyari}" if uyari else ''))
        DEG[f].append((o, yopts))
if yaz:
    for f, lst in DEG.items():
        src = open(f).read(); yeni = src
        for o, yopts in lst:
            for cand, rep in ((repr(o), repr(yopts)), (str(o).replace("'", '"'), str(yopts).replace("'", '"'))):
                if cand in yeni: yeni = yeni.replace(cand, rep, 1); break
            else: rapor.append(f'!! opts dosyada bulunamadı: {f} {o}')
        open(f, 'w').write(yeni)
print('\n'.join(rapor))
ad = ['toplam-en çok', 'toplam-en az', 'ortalama-en çok', 'ortalama-en az', 'en az sıklık-en çok', 'en az sıklık-en az']
print(f'\nöncüllü soru: {say} | değişen merdiven: {sum(len(v) for v in DEG.values())} | strateji isabeti (şans %20):')
for j in range(6): print(f'  {ad[j]}: %{100 * TOP0[j] / say:.0f} → %{100 * TOP1[j] / say:.0f}')
