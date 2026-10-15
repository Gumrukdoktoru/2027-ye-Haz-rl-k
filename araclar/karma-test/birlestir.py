# Karma test (3 × 50): grup çıktılarını (json/B*.json) birleştirir, Prompt 3 ve kanıt denetimi yapar,
# soruları sınav düzeninde konu bloklarına dizer, cevap harflerini dağıtır (her harf 10, art arda aynı harf yok),
# gerekçeye harfi yazar → test1..3.json + hafıza satırları.
# Kullanım: python3 birlestir.py <metin_klasoru>
import json, re, sys, random, unicodedata, pathlib, collections
HERE = pathlib.Path(__file__).parent; MET = pathlib.Path(sys.argv[1])
L = 'ABCDE'; C = collections.Counter

def norm(s):
    s = unicodedata.normalize('NFC', s).replace('\xa0', ' ')
    s = s.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '–': '-', '—': '-'}))
    return re.sub(r'\s+', ' ', re.sub(r'\[\d{1,3}\]', '', s)).strip().lower()
src = {f.name: norm(f.read_text(encoding='utf-8')) for f in MET.glob('*.txt')}
allsrc = ' '.join(src.values())
def kanit_ok(k):
    if not k: return False
    for blok in k.split('||'):                       # birden çok dosya: "dosyaA | kesit || dosyaB | kesit"
        dosya, _, govde = blok.partition('|') if '|' in blok else ('', '', blok)
        parca = [norm(p.strip(' .;,:"')) for p in re.split(r'\s*(?:\.\.\.|…)\s*', govde) if len(p.strip()) >= 12]
        hay = src.get(dosya.strip(), allsrc)
        if not parca or not all(p in hay or p in allsrc for p in parca): return False
    return True


SIRA = ['Temel Tanımlar', 'Temsil', 'Gümrük Müşavirliği', 'Disiplin', 'YGM', 'Yetkilendirilmiş Yükümlü', 'Onaylanmış Kişi',
        'Sonradan Kontrol', 'Bağlayıcı Bilgi (BTB/BMB)', 'Tarife', 'Gümrük Vergileri', 'Gümrük Kıymeti', 'Menşe', 'Ticaret Politikası',
        'İthalat Rejim Kararı', 'Taşıtların Giriş-Çıkışı ve Fazla Çalışma', 'Özet Beyan', 'Geçici Depolama/GOBİK', 'Fikri-Sınai Haklar',
        'Beyan', 'Muayene/Tahlil', 'Serbest Dolaşıma Giriş', 'Nihai Kullanım', 'Şartlı Muafiyet/EEGR', 'Transit', 'TIR', 'Antrepo',
        'Dahilde İşleme', 'GKAİR', 'Geçici İthalat', 'Hariçte İşleme', 'İhracat', 'Geri Gelen Eşya', 'Serbest Bölge', 'Muafiyetler',
        'Posta/Hızlı Kargo', 'Sınır Ticareti', 'Gümrüksüz Satış', 'Akaryakıt-Kumanya', 'Tasfiye', 'Gümrük Yükümlülüğü', 'Teminat ve Faiz',
        'Tahakkuk-Tebliğ-Ödeme', 'Geri Verme-Kaldırma', 'Cezalar', 'İtiraz', 'Uzlaşma', 'Kaçakçılık']
KAL = {'TANIM', 'KAVRAM', 'KAPSAM', 'KAPSAM_DIŞI', 'DOĞRU', 'YANLIŞ', 'ÖNERMELİ', 'SÜRE', 'ORAN-TUTAR', 'YETKİ', 'BELGE', 'ŞART', 'HESAP',
       'BOŞLUK', 'EŞLEŞTİRME', 'MÜEYYİDE', 'OLAY', 'TABİ', 'ZORUNLULUK', 'MATRAH', 'DAYANAK', 'SONUÇ', 'MUAFİYET', 'KISA_AD'}
MADDE = re.compile(r"\b\d{1,3}\s*['’]?\s*(inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu)\s+madde|madde(si(nin|ne)?)?\s*\d|\bfıkra|\bbendi?\b|\b\d{2,3}/\d", re.I)

Q = []
for f in sorted((HERE / 'json').glob('B*.json')):
    for q in json.load(open(f, encoding='utf-8')):
        q['grup'] = f.stem; Q.append(q)
siniflar = json.load(open(HERE / 'siniflar.json', encoding='utf-8'))
hata = collections.defaultdict(list)
for q in Q:
    sab = q.get('sabit') or None
    if sab:
        q['_siklar'], q['_dogru'] = sab['siklar'], sab['dogru']
    else:
        q['_siklar'], q['_dogru'] = None, None
    secenek = sab['siklar'] if sab else [q['d']] + q['c']
    kim = f"{q['grup']}/T{q['test']}/{q['konu']}/{q['cek'][:40]}"
    if len(set(map(str.strip, secenek))) != 5: hata['tekrarlı/eksik şık'].append(kim)
    if not sab and len(q['c']) != 4: hata['4 çeldirici değil'].append(kim)
    if q.get('kalip') not in KAL: hata['kalıp'].append(kim)
    if MADDE.search(' '.join(q['kok'] + secenek)): hata['kökte/şıkta madde no'].append(kim)
    if re.search(r'\b(hepsi|hiçbiri)\b', ' '.join(secenek), re.I): hata['hepsi/hiçbiri şıkkı'].append(kim)
    if not re.search(r'\(MD (?:[^()]|\([^()]*\))+\)\s*$', q['g'].strip()): hata['gerekçe (MD …) ile bitmiyor'].append(kim)
    if re.search(r'madde hükmüdür|kaynak metne göre|temel kural|kritik husus', q['g'] + ' '.join(q['kok']), re.I): hata['yasak ifade'].append(kim)
    if '2009/15481' in q.get('madde', '') + q['g'] and q['kok'][0].lstrip().startswith('4458'): hata['Karar kökü 4458 ile başlıyor'].append(kim)
    if not kanit_ok(q.get('kanit', '')): hata['kanıt bulunamadı'].append(kim)
    on = [k for k in q['kok'] if re.match(r'\s*(I|II|III|IV|V)\s*[.)]', k)]
    q['_oncul'] = len(on)
    if q.get('alt_tip', '').startswith('Ö') and len(on) < 3: hata['önermelide 3ten az öncül'].append(kim)

# kotalar
kota = {t: C() for t in (1, 2, 3)}
for q in Q: kota[q['test']][q['konu']] += 1
for t in (1, 2, 3):
    if kota[t] != C({k: v for k, v in siniflar['test'][str(t)].items()}): hata['kota'].append((t, dict(kota[t] - C(siniflar['test'][str(t)])), dict(C(siniflar['test'][str(t)]) - kota[t])))
# tekrar: aynı çekirdek
cek = C(norm(q['cek']) for q in Q)
hata['aynı çekirdek'] += [k for k, v in cek.items() if v > 1]

# yerleşim ve harf
r = random.Random(2027)
TESTLER = {}
for t in (1, 2, 3):
    xs = sorted([q for q in Q if q['test'] == t], key=lambda q: (SIRA.index(q['konu']) if q['konu'] in SIRA else 99, q['alt_tip']))
    bloklar = collections.OrderedDict()
    for q in xs: bloklar.setdefault(q['konu'], []).append(q)
    sabit_say = C(q['_dogru'] for q in xs if q['_dogru'])
    if any(v > 10 for v in sabit_say.values()): hata['sabit harf 10u aşıyor'].append((t, dict(sabit_say)))
    # her denemede: blok içi sıra (aynı alt tip art arda gelmesin) + harf dağıtımı
    # (sabitler belli; diğerleri her harf en çok 10 olacak, art arda aynı harf olmayacak biçimde)
    taban = list(bloklar.values())
    for deneme in range(20000):
        sira, bs = [], list(taban)
        for _ in range(0 if deneme < 100 else 1 + deneme // 4000):   # gerekirse komşu konu bloklarının yerini değiştir
            j = r.randrange(len(bs) - 1); bs[j], bs[j + 1] = bs[j + 1], bs[j]
        for b in bs:
            for _ in range(50):
                r.shuffle(b)
                if all(b[i]['alt_tip'] != b[i + 1]['alt_tip'] for i in range(len(b) - 1)): break
            sira += b
        kalan = C({h: 10 for h in L}); kalan.subtract(sabit_say)
        harfler, ok = [], True
        for i, q in enumerate(sira):
            if q['_dogru']:
                h = q['_dogru']
                if harfler and harfler[-1] == h: ok = False; break
            else:
                sonraki = sira[i + 1]['_dogru'] if i + 1 < len(sira) else None
                aday = [x for x in L if kalan[x] > 0 and (not harfler or x != harfler[-1]) and x != sonraki]
                if not aday: ok = False; break
                m = max(kalan[x] for x in aday); aday = [x for x in aday if kalan[x] >= m - 1]
                h = r.choice(aday); kalan[h] -= 1
            harfler.append(h)
        if ok and len(harfler) == len(sira): break
    else:
        hata['harf dağıtılamadı'].append(t)
        harfler += ['A'] * (len(sira) - len(harfler))
    for i, (q, h) in enumerate(zip(sira, harfler), 1):
        q['no'], q['harf'] = i, h
        if q['_siklar']: q['opts'] = q['_siklar']
        else:
            dist = list(q['c']); k = L.index(h); q['opts'] = [q['d'] if j == k else dist.pop(0) for j in range(5)]
        g = q['g'].strip(); md = g.rfind('(MD')
        bas = re.sub(r'\s*Bu nedenle doğru cevap [A-E]? ?seçeneğidir\.?\s*$', '', g[:md].rstrip())
        q['gerekce'] = f"{bas} Bu nedenle doğru cevap {h} seçeneğidir. {g[md:]}"
        q['id'] = f'KT{t}-{i:02d}'
    TESTLER[t] = sira
    json.dump([{k: v for k, v in q.items() if not k.startswith('_')} for q in sira], open(HERE / f'test{t}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

H = [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['kalip']} | {q['z']} | {q['harf']} | KT{t}" for t in (1, 2, 3) for q in TESTLER[t]]
(HERE / 'hafiza_satirlari.txt').write_text('\n'.join(H) + '\n', encoding='utf-8')
print('soru:', len(Q), '| test:', {t: len(v) for t, v in TESTLER.items()})
for t, v in TESTLER.items():
    hs = [q['harf'] for q in v]
    print(f' T{t} harf', dict(sorted(C(hs).items())), '| art arda aynı:', sum(a == b for a, b in zip(hs, hs[1:])),
          '| alt tip', dict(C(q['alt_tip'] for q in v).most_common()), '| sınıf', dict(C(q['sinif'] for q in v)))
for k, v in hata.items():
    if v: print('--', k, len(v)); [print('   ', x) for x in v[:15]]
