"""Prompt 5 (GMY mevzuat sorusu hazırlama) denetimi.

Kullanım: python3 kontrol5.py METIN_KLASORU batch_A.py [batch_B.py ...]

METIN_KLASORU: kaynak mevzuatın düz metinleri (araclar/metin_cikar.py çıktısı).

Soru alanları (dict):
  konu, blok, kalip, z (ÇK/K/O/Z/ÇZ), madde (başlık satırı; ör. "4458 sayılı Gümrük Kanunu md. 46"),
  cek (≤25 kelime), kok (liste; önermeli ise öncüller "I. ..." satırları),
  d (doğru şık), c (4 çeldirici), sirali (True ise 'siklar' 5 şıkkı nihai sırasıyla verir),
  g (gerekçe: "... Bu nedenle doğru cevap '<d>' seçeneğidir. (MD ...)"),
  kanit ("dosya | birebir alıntı", birden çok alıntı " || " ile), yuva (4 çeldiricinin metindeki gerçek yeri),
  yakinlik (BİREBİR/PARAFRAZ/ÇIKARIM), tuzak (liste), duzey (liste), profil (1–5 listesi),
  olumsuz (bool), vaka (bool), baslangic (bool, süre sorusunda başlangıç anı ölçülüyorsa),
  eksen (ikiz eksen no veya 0), ayna (ayna çift etiketi veya ''), guncellik ('' veya değişiklik tarihi),
  cikmis ('2024/56; 2025/27' veya ''), kapsamli (önermelide en kapsamlı şık doğruysa True).
"""
import pathlib
import re
import sys
import unicodedata
from collections import Counter

KAL = {'TANIM', 'KAVRAM', 'KAPSAM', 'KAPSAM_DIŞI', 'DOĞRU', 'YANLIŞ', 'ÖNERMELİ', 'SÜRE', 'ORAN-TUTAR', 'YETKİ',
       'BELGE', 'ŞART', 'HESAP', 'BOŞLUK', 'EŞLEŞTİRME', 'MÜEYYİDE', 'OLAY', 'TABİ', 'ZORUNLULUK', 'MATRAH',
       'DAYANAK', 'SONUÇ', 'MUAFİYET', 'KISA_AD'}
TUZ = {'SAYI', 'YAKIN-SAYI', 'BAŞLANGIÇ', 'MAKAM', 'TERİM', 'KOMŞU', 'TERSİNE', 'MUTLAK', 'UNSUR', 'LİSTE-DIŞI',
       'İSTİSNA', 'ŞART', 'AD-HESAP', 'SAĞDUYU'}
DUZ = {'HATIRLAMA', 'TANIMA', 'AYIRT', 'UYGULAMA', 'BÜTÜNLEŞİK'}
YAK = {'BİREBİR', 'PARAFRAZ', 'ÇIKARIM'}
YAPAY = r'temel özellik|temel kural|kritik husus|en önemli düzenleme'
GYASAK = r'madde hükmüdür|temel düzenlemedir|madde bunu söylemektedir|kaynak metne göre|verilen kaynağa göre|kaynakta belirtildiği'
MADDE = (r'\b\d+\s*[’\']?\s*(inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu)\s*madde|madde(si(nin|ne)?)?\s*\d|\bfıkra|\bbendi?\b'
         r'|\b\d{2,3}/\d')
KARAR_KALIP = '2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"'
ALAN = ['konu', 'blok', 'kalip', 'z', 'madde', 'cek', 'kok', 'd', 'c', 'g', 'kanit', 'yuva', 'yakinlik', 'tuzak',
        'duzey', 'profil', 'olumsuz', 'vaka', 'baslangic', 'eksen', 'ayna', 'guncellik', 'cikmis']


def norm(s):
    s = unicodedata.normalize('NFC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()


def sayi(s):
    t = s.replace('.', '').replace(',', '.').replace('%', '')
    m = re.fullmatch(r'\s*(yüzde\s*)?(\d+(\.\d+)?)\s*[^\d]*', t, re.I)
    return float(m.group(2)) if m else None


def yukle(yollar):
    Q = []
    for y in yollar:
        ns = {}
        exec(open(y, encoding='utf-8').read(), ns)
        for q in ns['Q']:
            q['_dosya'] = pathlib.Path(y).name
            Q.append(q)
    return Q


def denetle(Q, metin_klasoru):
    kaynak = {f.name: norm(f.read_text(encoding='utf-8')) for f in pathlib.Path(metin_klasoru).glob('*.txt')}
    hepsi = ' '.join(kaynak.values())
    hata = 0
    for i, q in enumerate(Q, 1):
        e = []
        eksik = [k for k in ALAN if k not in q]
        if eksik:
            print(f'{i} ({q.get("_dosya")}): eksik alan {eksik}')
            hata += 1
            continue
        siklar = q['siklar'] if q.get('sirali') else [q['d']] + q['c']
        if q.get('sirali'):
            if len(q['siklar']) != 5 or q['d'] not in q['siklar']:
                e.append('sirali: siklar 5 olmalı ve d içermeli')
            else:
                q['c'] = [s for s in q['siklar'] if s != q['d']]
        if q['kalip'] not in KAL: e.append('kalip?')
        if q['z'] not in {'ÇK', 'K', 'O', 'Z', 'ÇZ'}: e.append('zorluk?')
        if q['yakinlik'] not in YAK: e.append('yakinlik?')
        if not set(q['tuzak']) <= TUZ or not q['tuzak']: e.append(f'tuzak? {q["tuzak"]}')
        if not set(q['duzey']) <= DUZ or not q['duzey']: e.append(f'duzey? {q["duzey"]}')
        if len(q['c']) != 4: e.append('4 çeldirici olmalı')
        if len(set(siklar)) != 5: e.append('tekrarlı şık')
        if len(q['yuva']) != 4: e.append('yuva 4 olmalı')
        if len(q['cek'].split()) > 25: e.append('çekirdek >25 kelime')
        metin = ' '.join(q['kok'] + siklar)
        if re.search(MADDE, metin, re.I): e.append('kökte/şıkta madde-fıkra-bent no')
        if re.search(r'\b(hepsi|hiçbiri)\b', ' '.join(siklar), re.I): e.append('yasak şık hepsi/hiçbiri')
        if re.search(YAPAY, ' '.join(q['kok']), re.I): e.append('yapay niteleme kökte')
        if re.search(GYASAK, q['g'], re.I): e.append('gerekçede yasak ifade')
        if not re.search(r'\(MD [^)]*\)\s*$', q['g'].strip()): e.append("gerekçe '(MD …)' ile bitmeli")
        if not re.search(r"Bu nedenle doğru cevap '.+' seçeneğidir\.", q['g']):
            e.append("gerekçe \"Bu nedenle doğru cevap '<d>' seçeneğidir.\" içermeli")
        elif f"'{q['d']}' seçeneğidir" not in q['g'] and f"'{q['d'].rstrip('.')}' seçeneğidir" not in q['g']:
            e.append('gerekçedeki alıntı d ile aynı değil')
        kok = ' '.join(q['kok'])
        if not re.search(r'Kanun|Yönetmeli|Tebliğ|Karar', kok): e.append('kökte mevzuat adı yok')
        if re.search(r'2009/15481|Bazı Maddelerinin Uygulanması', q['madde']) and KARAR_KALIP not in kok:
            e.append('Karar dayanaklı soruda kurum kalıbı yok')
        if re.match(r'^[^.?]{0,80}(göre|uyarınca),? aşağıdakilerden hangisi (doğrudur|yanlıştır)\?$', q['kok'][0].strip()):
            e.append('bağlamsız genel kök')
        onc = [l for l in q['kok'] if re.match(r'^(I|II|III|IV|V)\.\s', l.strip())]
        if q['kalip'] == 'ÖNERMELİ' and len(onc) < 3: e.append('önermeli en az 3 önerme')
        nums = [sayi(s) for s in siklar]
        if q.get('sirali') and all(n is not None for n in nums):
            if nums != sorted(nums): e.append('sayısal şıklar artan sırada değil')
            if q['siklar'].index(q['d']) not in (1, 2, 3): e.append('sayısal doğru şık B/C/D olmalı')
        elif all(n is not None for n in nums):
            e.append('sayısal şıklı soru sirali=True olmalı')
        # kanıt: her alıntı kaynakta birebir bulunmalı
        for parca in q['kanit'].split(' || '):
            if '|' not in parca:
                e.append('kanit "dosya | alıntı" biçiminde olmalı')
                continue
            dosya, alinti = [x.strip() for x in parca.split('|', 1)]
            govde = kaynak.get(dosya, hepsi)
            if dosya not in kaynak: e.append(f'kanıt dosyası yok: {dosya}')
            parcalar = [p.strip(' .…;,') for p in re.split(r'\.\.\.|…', norm(alinti)) if len(p.strip()) > 12]
            if not parcalar or not all(p in govde for p in parcalar):
                e.append(f'kanıt alıntısı kaynakta birebir yok: {alinti[:60]}…')
        if e:
            hata += 1
            print(f'{i} ({q["_dosya"]}, {q["konu"]}): ' + '; '.join(e))
    return hata


def profil(Q):
    C = Counter
    n = len(Q)
    print(f'\nSoru: {n}')
    print('Yakınlık:', dict(C(q['yakinlik'] for q in Q)))
    print('Olumsuz kök:', sum(q['olumsuz'] for q in Q), '| Önermeli:', sum(q['kalip'] == 'ÖNERMELİ' for q in Q),
          '| en kapsamlı doğru:', sum(bool(q.get('kapsamli')) for q in Q),
          '| önermeli+olumsuz:', sum(q['kalip'] == 'ÖNERMELİ' and q['olumsuz'] for q in Q))
    print('Vaka/uygulama/hesap:', sum(q['vaka'] for q in Q), '| Tanım/kavram:', sum(q['kalip'] in ('TANIM', 'KAVRAM') for q in Q),
          '| Boşluk+eşleştirme:', sum(q['kalip'] in ('BOŞLUK', 'EŞLEŞTİRME') for q in Q))
    sure = [q for q in Q if q['kalip'] == 'SÜRE' or 'SAYI' in q['tuzak'] and re.search(r'gün|ay|yıl|saat', ' '.join(q['kok']))]
    print('Süre soruları:', len(sure), '| başlangıç anı ölçülen:', sum(q['baslangic'] for q in Q))
    print('Tuzak:', dict(C(t for q in Q for t in q['tuzak']).most_common()))
    print('Düzey:', dict(C(t for q in Q for t in q['duzey']).most_common()))
    print('Profil:', dict(sorted(C(p for q in Q for p in q['profil']).items())))
    print('Eksen:', sorted({q['eksen'] for q in Q if q['eksen']}), '| ayna:', [q['ayna'] for q in Q if q['ayna']])
    print('Güncellik:', [q['guncellik'] for q in Q if q['guncellik']])
    print('Çıkmış alanı karşılayan:', sum(bool(q['cikmis']) for q in Q))
    print('Kalıp:', dict(C(q['kalip'] for q in Q).most_common()))


if __name__ == '__main__':
    Q = yukle(sys.argv[2:])
    h = denetle(Q, sys.argv[1])
    profil(Q)
    print('\nHatalı soru:', h)
