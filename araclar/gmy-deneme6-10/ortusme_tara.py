"""Metin düzeyinde örtüşme taraması: Deneme 6–10'daki her gümrük sorusunun doğru şıkkı ve öncülleri,
Deneme 1–5'in (sorular/*.md) ve 2021–2025 sınavlarının (sinav/*_duz.txt) şık/öncül parçalarıyla karşılaştırılır.
Ölçüt: yeni parçanın içerik kelimelerinin ≥%75'i eski parçada var ve Jaccard ≥0.45 (en az 5 içerik kelimesi).
Kullanım: python3 ortusme_tara.py → dogrulama/ortusme_aday.txt"""
import json, re, glob, collections
from kontrol import norm, STRIP
STOP = set(('ve ile veya bir bu şu da de için olarak olan olanlar göre ki ya en çok az her ise ancak tarafından halinde hâlinde '
            'kadar sonra önce aşağıdakilerden hangisi hangileri yukarıdakilerden değildir yanlıştır doğrudur ilişkin itibaren '
            'gibi dair olup olması olduğu edilir edilen eden yapılır yapılan'.split()))
def kel(s): return {w for w in re.findall(r'[0-9a-zçğıöşüâîû%]+', norm(STRIP(s))) if w not in STOP and len(w) > 1}
def bol(metin):
    t = re.sub(r'\s+', ' ', metin)
    return [p.strip() for p in re.split(r'(?=\b[A-E]\) )|(?=\b(?:I|II|III|IV|V)\. )|(?=\*\*\d{1,3}[-.]\*\*)|(?=\bSORU \d)|(?= \d{1,3}\. [A-ZÇĞİÖŞÜ])', t) if len(p.strip()) > 25]
ESKI = []
for f in glob.glob('../../sorular/GK_GMY2025_Deneme_S1_100soru.md') + glob.glob('../../sorular/GK_GMY_Deneme[2-5]_100soru.md'):
    ad = 'D1' if 'S1' in f else 'D' + re.search(r'Deneme(\d)', f).group(1)
    ESKI += [(ad, p) for p in set(bol(open(f).read()))]
for f in sorted(glob.glob('sinav/*_duz.txt')):
    ESKI += [(f.split('/')[-1][:5], p) for p in set(bol(open(f).read()))]
EK = [(a, p, kel(p)) for a, p in ESKI]
INV = collections.defaultdict(set)
for i, (_, _, k) in enumerate(EK):
    for w in k: INV[w].add(i)
out = []; say = collections.Counter()
for d in range(6, 11):
    for q in json.load(open(f'set{d}.json')):
        if q['blok'] != 'GÜMRÜK': continue
        birim = [('doğru şık', q['d'])] + [('öncül', x) for x in q['kok'][1:-1] if re.match(r'(I|II|III|IV|V)\. ', STRIP(x))]
        for tur, s in birim:
            N = kel(s)
            if len(N) < 5: continue
            aday = collections.Counter(i for w in N for i in INV[w])
            for i, n in aday.most_common(30):
                a, p, O = EK[i]
                c = n / len(N); j = n / len(N | O)
                if c >= 0.75 and j >= 0.45:
                    out.append(f"{q['id']} [{q['tip']}] {tur} ~ {a} (kapsama {c:.2f}, jaccard {j:.2f})\n   YENİ: {STRIP(s)[:220]}\n   ESKİ: {p[:260]}")
                    say[q['id']] += 1
open('dogrulama/ortusme_aday.txt', 'w').write('\n'.join(out) + '\n')
print('aday soru:', len(say), '| eşleşme:', len(out))
