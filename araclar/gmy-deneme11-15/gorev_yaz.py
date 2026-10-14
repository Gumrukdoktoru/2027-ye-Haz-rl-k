"""plan.json + üretim hafızası → gorev/<yazar>.md ve hafiza/<yazar>.txt (Deneme 11–15 yazar girdileri).
Hafıza: önceki 1015 satır (Karar seti + GMY deneme S1–S10). Genel kültür satırları soru numarasına göre
(1–5 Türkçe, 6–10 Matematik, 11–15 Tarih, 16–20 Anayasa/Uluslararası), gümrük satırları konu adına göre kümelenir."""
import json, re, collections
from kumeler import KUME
PLAN = json.load(open('plan.json'))
EK = {'Gümrükçe Onaylanmış İşlem veya Kullanım': 'K01', 'Belge Saklama': 'K01', 'Gümrük Rejimleri': 'K01', 'Taşıtlar': 'K01',
      'Mücbir Sebep': 'K01', 'Gümrük İdaresi': 'K01', 'Yasaklama ve Kısıtlama Yetkisi': 'K01', 'Süreler': 'K01',
      'Türkiye Gümrük Bölgesi': 'K01', 'Karar': 'K01', 'Bağlayıcı Bilgi / Tarife Bilgisi': 'K15', 'Eşyanın Ağırlığı ve Kapları': 'K02',
      'Dış Ticaret Belgeleri': 'K04'}
haf2k = {h: k for k, v in KUME.items() for h in v['haf']}; haf2k.update(EK)
GKW = lambda n: 'GTR' if n <= 5 else 'GMA' if n <= 10 else 'GTA' if n <= 15 else 'GAN'
HAF = collections.defaultdict(list); bos = collections.Counter()
for l in open('../../sorular/hafiza/URETIM-HAFIZASI.md'):
    p = [x.strip() for x in l.split('|')]
    if len(p) < 8 or not re.match(r'(KAR|GMY)', p[0]) or re.match(r'GMY(11|12|13|14|15)-', p[0]): continue
    n = int(p[0].split('-')[1]); k = GKW(n) if p[0].startswith('GMY') and n <= 20 else haf2k.get(p[1])
    if k is None: bos[p[1]] += 1; continue
    HAF[k].append(l.rstrip('\n'))
if bos: print('!! kümelenemeyen hafıza konuları:', dict(bos))
ONCEKI = {}  # aynı çıkmış soruyu Deneme 6–10'da karşılayan soru
for d in range(6, 11):
    for q in json.load(open(f'../gmy-deneme6-10/set{d}.json')): ONCEKI[q['cikmis']] = q
by = collections.defaultdict(list)
for p in PLAN: by[p['yazar']].append(p)
for k, L in by.items():
    gk = k.startswith('G')
    head = [f"# Görev {k}" + ('' if gk else f" — {KUME[k]['ad']}"), '',
            f"Toplam {len(L)} soru. Batch dosyası: `batch_{k}.py`. Hafıza (tekrar etme): `hafiza/{k}.txt` ({len(HAF[k])} satır; Deneme 1–10 ve Karar seti).", '']
    if gk: head += ['Kaynak: `metin/Canli_7_24_Genel_Kultur_Kitabi.txt`.', '']
    else: head += ['Ana kaynak dosyaları (metin/): ' + ', '.join(f'`{s}.txt`' for s in KUME[k]['src']) + ' — gerekirse metin/ altındaki diğer gümrük mevzuatı dosyalarına da bak.', '']
    for p in L:
        o = ONCEKI.get(p['cikmis']); y = p['cikmis'].split('/')[0]; ham = 'sinav/2025B_duz.txt' if y == '2025' else f'sinav/{y}_duz.txt'
        head.append(f"### {p['id']}  ←  {p['cikmis']} ({ham})")
        if gk:
            head.append(f"- Ders: {p['ders']} · **doğru cevap harfi {p['harf']}**")
        else:
            head += [f"- Konu: {p['konu']} · eski kalıp: {p['kalip_eski']} · resmî cevap: {p['resmi']} · kaynak: {p['kaynak']}",
                     f"- Çıkmışın ölçtüğü bilgi: {p['olculen']}",
                     f"- **Plan:** tip **{p['tip']}** · şık sınıfı **{p['sinif']}** · ters tuzak **{'EVET' if p['tuzak'] else 'hayır'}** · kök bandı **{p['bant']}** · doğru cevap harfi **{p['harf']}**"]
        if o: head.append(f"- Aynı çıkmış soru Deneme {o['id'][1:o['id'].index('-')]}'da ({o['id']}) şu hükümle karşılandı — **bunu da sorma**: {o.get('madde')} · {o['cek']}")
        head.append('')
    open(f'gorev/{k}.md', 'w').write('\n'.join(head))
    open(f'hafiza/{k}.txt', 'w').write('ID | KONU | MADDE | ÇEKİRDEK | TİP | ZORLUK | CEVAP | SET\n' + '\n'.join(HAF[k]) + '\n')
print({k: (len(v), len(HAF[k])) for k, v in sorted(by.items())}); print('hafıza toplam:', sum(len(v) for v in HAF.values()))
