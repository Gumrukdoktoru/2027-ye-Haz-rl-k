# Etiketleri (etiket/*.json) kitapçık metniyle (json/<yil>_sorular.json) birleştirir, doğrular,
# tipler.csv + istatistik.json + cevap_anahtari.tsv üretir.
# Kullanım: python3 sayim.py <sorular_json_klasoru> <etiket_klasoru> <cikmis_envanter.tsv>
import json, sys, csv, re, pathlib, collections
HERE = pathlib.Path(__file__).parent
SJ, EJ, ENV = map(pathlib.Path, sys.argv[1:4])
YIL = ['2021', '2022', '2023', '2024', '2025']
C = collections.Counter

ALT = {'O': 'O1 O2 O3 O4', 'D': 'D1 D2 D3 D4 D5 D6', 'Ö': 'Ö1 Ö2 Ö3 Ö4 Ö5', 'G': 'G1 G2 G3 G4', 'V': 'V1 V2 V3 V4',
       'K': 'K1', 'B': 'B1 B2', 'E': 'E1 E2 E3', 'S': 'S1 S2', 'H': 'H1 H2 H3 H4 H5 H6 H7 H8',
       'T': 'T1 T2 T3 T4 T5', 'M': 'M1 M2 M3 M4'}
ALTLAR = [a for v in ALT.values() for a in v.split()]
ANA_AD = {'O': 'Olumsuz', 'D': 'Düz', 'Ö': 'Öncüllü', 'G': 'Doğru', 'V': 'Vaka', 'K': 'Kavram', 'B': 'Boşluk',
          'E': 'Eşleştirme', 'S': 'Sıralama', 'H': 'Hesap', 'T': 'Türkçe', 'M': 'Matematik'}
ALANLAR = ['TÜRKÇE', 'MATEMATİK', 'TARİH', 'HUKUK', 'TEMEL', 'ALT', 'KAÇAKÇILIK', 'HESAP']
BAYRAK = ['F_DAYANAK', 'F_SERI', 'F_TUZAKVERI', 'F_MADDENO', 'F_MUTLAK', 'F_MATRIS', 'F_GUNCEL', 'F_YALNIZ', 'F_TUMU']

DAYANAK = re.compile(r'(Kanun|Yönetmeli[kğ]|Karar[ıi]?\b|Kararname|Tebli[ğg]|Genelge|Sözleşme|Anlaşma|Uygulama Esasları|sayılı)', re.I)
MADDENO = re.compile(r"\b\d{1,3}\s*['’]?\s*(?:inci|ıncı|nci|ncı|üncü|uncu|ünci|'?n?c?i)?\s+madde|\bmadde(?:si|sinin|sine|sinde|nin)?\s*\d|\b(?:234|235|236|237|238|241)\s*/\s*\d|\bfıkra|\bbendi", re.I)
soru = {}
for y in YIL:
    for q in json.load(open(SJ / f'{y}_sorular.json', encoding='utf-8')):
        soru[(int(y), q['no'])] = q
E = []
for f in sorted(EJ.glob('*.json')):
    E += json.load(open(f, encoding='utf-8'))
E.sort(key=lambda e: (e['yil'], e['no']))
hata = []
assert len({(e['yil'], e['no']) for e in E}) == len(E) == 500, f'etiket sayısı {len(E)}'
for e in E:
    q = soru[(e['yil'], e['no'])]
    e['kok'], e['siklar'] = q['kok'], q['siklar']
    if e['yil'] < 2025:
        if e.get('dogru') != q['kirmizi'][0]: hata.append((e['yil'], e['no'], 'dogru≠resmî', e.get('dogru'), q['kirmizi']))
        e['dogru'], e['cevap_kaynagi'] = q['kirmizi'][0], 'resmi'
    if e['alt_tip'] not in ALTLAR or e['alt_tip'][0] != e['ana_tip']: hata.append((e['yil'], e['no'], 'alt_tip', e['alt_tip']))
    if e['alt_alan'] not in ALANLAR: hata.append((e['yil'], e['no'], 'alt_alan', e['alt_alan']))
    e['bayraklar'] = [b for b in e.get('bayraklar', []) if b in BAYRAK]
    # F_DAYANAK ve F_MADDENO metinden kuralla yeniden hesaplanır (ajanlar arası tutarlılık için)
    e['bayraklar'] = [b for b in e['bayraklar'] if b not in ('F_DAYANAK', 'F_MADDENO')]
    if e['alan'] == 'GÜMRÜK' and DAYANAK.search(e['kok']): e['bayraklar'].append('F_DAYANAK')
    if MADDENO.search(e['kok'] + ' ' + ' '.join(e['siklar'].values())): e['bayraklar'].append('F_MADDENO')
    # doğru şıkkın uzunluk konumu (yalnız cümle/eşleşme şıklı)
    L = {h: len(v) for h, v in e['siklar'].items()}
    d = e['dogru']
    if e.get('sik_turu') in ('cumle', 'eslesme') and len(L) == 5 and d in L:
        e['uzunluk'] = 'en_uzun' if L[d] == max(L.values()) else 'en_kisa' if L[d] == min(L.values()) else 'orta'
    else:
        e['uzunluk'] = ''
    # öncüllü cevap biçimi
    s = e['siklar'].get(d, '')
    e['oncul_cevap'] = ('yalniz' if re.match(r'\s*Yalnız', s) else
                        'tumu' if 'F_TUMU' in e['bayraklar'] else 'ara') if e['ana_tip'] == 'Ö' or e['alt_tip'] == 'E2' else ''
print('doğrulama hataları:', len(hata)); [print('  ', h) for h in hata[:30]]

# ---- tipler.csv
alanlar = ['yil', 'no', 'alan', 'alt_alan', 'konu', 'dayanak', 'ana_tip', 'alt_tip', 'bayraklar', 'kok_yuklem', 'sik_turu',
           'oncul_sayisi', 'dogru', 'cevap_kaynagi', 'guven', 'uzunluk', 'teknik', 'kurulum', 'tartismali', 'sinir']
with open(HERE / 'tipler.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, delimiter=';')
    w.writerow(alanlar)
    for e in E:
        w.writerow([' '.join(e[k]) if k == 'bayraklar' else e.get(k, '') for k in alanlar])

# ---- cevap anahtarı + envanter karşılaştırması
env = {}
for l in ENV.read_text(encoding='utf-8').splitlines()[1:]:
    r = l.split('\t'); env[(int(r[0]), int(r[1]))] = (r[6].strip() if len(r) > 6 else '')
with open(HERE / 'cevap_anahtari.tsv', 'w', encoding='utf-8') as fh:
    fh.write('YIL\tSORU\tCEVAP\tKAYNAK\tGUVEN\tENVANTER_CEVAP\tFARK\n')
    for e in E:
        ev = env.get((e['yil'], e['no']), '')
        fh.write(f"{e['yil']}\t{e['no']}\t{e['dogru']}\t{e['cevap_kaynagi']}\t{e.get('guven', '')}\t{ev}\t{'*' if ev and ev != e['dogru'] else ''}\n")

# ---- istatistikler
def yilsay(xs): c = C(str(e['yil']) for e in xs); return [c.get(y, 0) for y in YIL]
st = {'toplam': len(E), 'ana': {}, 'alt': {}, 'alan': {}, 'bayrak': {}, 'bicim': {}}
for a in ALT:
    xs = [e for e in E if e['ana_tip'] == a]
    st['ana'][a] = {'ad': ANA_AD[a], 'yil': yilsay(xs), 'n': len(xs)}
for a in ALTLAR:
    xs = [e for e in E if e['alt_tip'] == a]
    if not xs: continue
    res = [e for e in xs if e['cevap_kaynagi'] == 'resmi']
    st['alt'][a] = {
        'n': len(xs), 'yil': yilsay(xs), 'alan': dict(C(e['alt_alan'] for e in xs)),
        'son2': sum(1 for e in xs if e['yil'] >= 2024),
        'harf_resmi': dict(sorted(C(e['dogru'] for e in res).items())),
        'uzunluk': dict(C(e['uzunluk'] for e in xs if e['uzunluk'])),
        'dayanak_kokte': sum('F_DAYANAK' in e['bayraklar'] for e in xs),
        'teknik': dict(C(t for e in xs for t in (e.get('teknik') or '').split('+') if t).most_common()),
        'sik_turu': dict(C(e.get('sik_turu', '') for e in xs)),
        'oncul_sayisi': dict(C(e.get('oncul_sayisi', 0) for e in xs if e.get('oncul_sayisi'))),
        'oncul_cevap': dict(C(e['oncul_cevap'] for e in xs if e['oncul_cevap'])),
        'bayrak': dict(C(b for e in xs for b in e['bayraklar'])),
        'yuklem': dict(C(e.get('kok_yuklem', '') for e in xs).most_common(8)),
    }
for al in ALANLAR:
    xs = [e for e in E if e['alt_alan'] == al]
    son = [e for e in xs if e['yil'] >= 2024]
    c5, c2 = C(e['alt_tip'] for e in xs), C(e['alt_tip'] for e in son)
    st['alan'][al] = {'n': len(xs), 'yil': yilsay(xs), 'ilk5': [(a, n, round(100 * n / len(xs)), round(100 * c2.get(a, 0) / max(len(son), 1)))
                                                              for a, n in c5.most_common(5)],
                      'ilk5_pay': round(100 * sum(n for _, n in c5.most_common(5)) / max(len(xs), 1))}
for b in BAYRAK:
    xs = [e for e in E if b in e['bayraklar']]
    st['bayrak'][b] = {'yil': yilsay(xs), 'n': len(xs), 'son2': sum(1 for e in xs if e['yil'] >= 2024)}
res = [e for e in E if e['cevap_kaynagi'] == 'resmi']
uz = lambda xs: dict(C(e['uzunluk'] for e in xs if e['uzunluk']))
st['bicim'] = {
    'harf_resmi': dict(sorted(C(e['dogru'] for e in res).items())),
    'harf_resmi_yil': {y: dict(sorted(C(e['dogru'] for e in res if str(e['yil']) == y).items())) for y in YIL[:4]},
    'harf_2025_turetilmis': dict(sorted(C(e['dogru'] for e in E if e['yil'] == 2025).items())),
    'guven_2025': dict(C(e.get('guven', '') for e in E if e['yil'] == 2025)),
    'uzunluk_tum': uz(E), 'n_uzunluk_tum': sum(1 for e in E if e['uzunluk']),
    'uzunluk_O2O3': uz([e for e in E if e['alt_tip'] in ('O2', 'O3')]),
    'uzunluk_G': uz([e for e in E if e['ana_tip'] == 'G']),
    'oncul_cevap': dict(C(e['oncul_cevap'] for e in E if e['oncul_cevap'])),
    'oncul_sayisi': dict(sorted(C(e.get('oncul_sayisi', 0) for e in E if e['ana_tip'] == 'Ö').items())),
    'O3_tumu': [sum(1 for e in E if e['alt_tip'] == 'Ö3' and e['oncul_cevap'] == 'tumu'), sum(1 for e in E if e['alt_tip'] == 'Ö3')],
    'hesap_harf_resmi': dict(sorted(C(e['dogru'] for e in res if e['ana_tip'] == 'H').items())),
    'mat_harf_resmi': dict(sorted(C(e['dogru'] for e in res if e['ana_tip'] == 'M').items())),
    'D1_harf_resmi': dict(sorted(C(e['dogru'] for e in res if e['alt_tip'] == 'D1').items())),
    'ardisik_ayni_harf_resmi': {y: sum(1 for a, b in zip(sorted([e for e in res if str(e['yil']) == y], key=lambda e: e['no']),
                                                          sorted([e for e in res if str(e['yil']) == y], key=lambda e: e['no'])[1:])
                                       if a['dogru'] == b['dogru']) for y in YIL[:4]},
    'tartismali': [(e['yil'], e['no'], e['tartismali']) for e in E if e.get('tartismali')],
    'envanter_fark': [(e['yil'], e['no'], env.get((e['yil'], e['no'])), e['dogru']) for e in E
                      if e['yil'] < 2025 and env.get((e['yil'], e['no'])) and env[(e['yil'], e['no'])] != e['dogru']],
}
json.dump(st, open(HERE / 'istatistik.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(E, open(HERE / 'etiketler_tam.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ana tip:', {a: v['n'] for a, v in st['ana'].items()})
print('harf (resmî 400):', st['bicim']['harf_resmi'], '| 2025 türetilmiş:', st['bicim']['harf_2025_turetilmis'], st['bicim']['guven_2025'])
print('envanter farkı:', st['bicim']['envanter_fark'])
