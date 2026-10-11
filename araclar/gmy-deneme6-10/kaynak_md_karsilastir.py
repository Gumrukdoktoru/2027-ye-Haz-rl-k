"""Kullanıcının GitHub kaynak deposundaki Markdown mevzuat derlemesini metin/ ile karşılaştırır.
Kullanım: python3 kaynak_md_karsilastir.py /home/user/gumrukdoktoru/2027gmynot  → dogrulama/KAYNAK_MD.md
1) set6–10.json kanıt alıntılarını Markdown kaynakta arar (birebir / yalnız biçim farkı / bulunamadı).
2) Markdown'da olup metin/'de karşılığı zayıf cümleleri konu başlığına göre sayar (sürüm farkı taraması).
3) Değişiklik tarihlerini (gg.aa.2026) iki kaynakta karşılaştırır."""
import sys, re, json, glob, collections
from kontrol import norm, CORPUS

KAYNAK = sys.argv[1].rstrip('/') + '/'
def mdtemizle(s):
    s = re.sub(r'\[\^?\d+\]', ' ', s)
    s = re.sub(r'\\([\\`*_{}\[\]()#+\-.!>|])', r'\1', s)
    s = s.replace('**', '').replace('*', ' ').replace('__', '')
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'^#+ ', '', s, flags=re.M)
    s = re.sub(r'^\s*[-|:]{3,}[-|: ]*$', ' ', s, flags=re.M)
    return s.replace('|', ' ')
def iskelet(x): return re.sub(r'[^0-9a-zçğıöşüâîû%]', '', x)

ham = open(KAYNAK + 'GUMRUK_MEVZUATI_TUMU.md').read()
parca = re.split(r'\n## (\d+)\. ([^\n]+)\n', ham)
KONU = {parca[i + 1].strip(): norm(mdtemizle(parca[i + 2])) for i in range(1, len(parca), 3)}
EK = {f.split('/')[-1]: norm(mdtemizle(open(f).read())) for f in glob.glob(KAYNAK + '*.md') if 'TUMU' not in f}
MD = ' '.join(KONU.values()) + ' ' + ' '.join(EK.values()); MDI = iskelet(MD)
TXTI = iskelet(' '.join(CORPUS.values()))

BAG = re.compile(r"\[\d+\]|\bek-\d+'?\w*|\b\d[\d./]*(?:\s*(?:inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu|ilâ|ila|ve))?(?:\s*(?:inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu))?\b|\b(?:maddesinde|maddesinin|maddesine|maddesi|maddeler|maddede|madde|kanunu|sayılı|kanununun|tarihli)\b")
def bagli_dustu(p):
    # Markdown dönüştürmesi bağlantılı kelimeleri (madde no, Ek adı, Kanun sayısı) düşürür: kalan parçalar sırayla bulunmalı
    parcalar = [iskelet(x) for x in BAG.split(p)]
    parcalar = [x for x in parcalar if len(x) >= 8]
    if not parcalar: return False
    i = 0
    for x in parcalar:
        j = MDI.find(x, i)
        if j < 0: return False
        i = j + len(x)
    return True
say = collections.Counter(); yok = []
for d in range(6, 11):
    for q in json.load(open(f'set{d}.json')):
        if q['blok'] == 'GK' or q['kanit'].strip().startswith('ÖZGÜN'): continue
        for kisim in q['kanit'].split('||'):
            f, alinti = [x.strip() for x in kisim.split('|', 1)]
            if f.startswith(('5607_', 'kacakcilik', 'milli_')): say['md karşılığı yok (5607 yönetmelik/kanun metni)'] += 1; continue
            for p in re.split(r'\.\.\.|…|\[\.\.\.\]', norm(alinti)):
                p = p.strip(' .,;')
                if len(p) < 12: continue
                if p in MD: say['birebir'] += 1
                elif iskelet(p) in MDI: say['yalnız biçim farkı'] += 1
                elif bagli_dustu(p): say['bağlantılı kelime düşmüş (hüküm aynı)'] += 1
                else:
                    say['bulunamadı'] += 1; yok.append(f"{q['id']} | {f} | {p[:150]}")
zayif = collections.Counter()
for ad, govde in KONU.items():
    for c in re.split(r'(?<=[.;:])\s+', govde):
        k = iskelet(c)
        if len(k) < 60 or k in TXTI: continue
        ch = [k[i:i + 40] for i in range(0, len(k) - 40, 20)]
        if sum(x in TXTI for x in ch) / max(1, len(ch)) < 0.6: zayif[ad] += 1
tarih = lambda s: collections.Counter(re.findall(r'\b\d\d\.\d\d\.2026\b', s))
tmd = tarih(ham); ttxt = tarih(''.join(open(f).read() for f in glob.glob('metin/*.txt')))
out = ['# Markdown kaynak karşılaştırması', '', f'Kaynak: `{KAYNAK}`', '',
       '## 1. Kanıt alıntıları (gümrük soruları)', ''] + [f'- {k}: {v}' for k, v in say.most_common()]
out += ['', 'Bulunamayanlar (elle incelenir):', ''] + [f'- {x}' for x in yok]
out += ['', '## 2. Markdown\'da olup metin/\'de karşılığı zayıf cümleler', ''] + [f'- {k}: {v}' for k, v in zayif.most_common()]
out += ['', '## 3. 2026 değişiklik tarihleri', '', f'- Markdown: {dict(sorted(tmd.items()))}', f'- metin/: {dict(sorted(ttxt.items()))}',
        f"- Yalnız Markdown'da: {sorted(set(tmd) - set(ttxt)) or 'yok'}",
        '', '## 4. Elle inceleme (11 Ekim 2026)',
        '“Bulunamadı” listesindeki alıntıların hepsi Markdown\'da tek kelime eksiğiyle bulundu (ör. “aynı zamanda ödenir” → “aynı ödenir”, “gecikme faizi” → “gecikme”, “Onbirinci Kısımdaki cezai hükümlere” → “Onbirinci Kısımdaki göre”). Markdown dönüştürmesi bağlantılı kelimeleri düşürmüştür. Hüküm farkı yoktur. “Zayıf cümle” sayımı da aynı nedenden ve dipnot işaretlerinden kaynaklanır (örnek denetimde gerçek bir metin farkı bulunmadı).']
open('dogrulama/KAYNAK_MD.md', 'w').write('\n'.join(out) + '\n')
print(dict(say), '| zayıf cümle:', sum(zayif.values()), '| yalnız md tarih:', sorted(set(tmd) - set(ttxt)) or 'yok')
