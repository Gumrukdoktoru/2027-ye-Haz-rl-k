# Hap bilgi belgeleri: hap/B*.json + hap/GK.json + siniflar.json →
#   sorular/GK_Konu_Siniflari_ve_Cikan_Sorular_Hap.md  (konu sınıfları + çıkan sorulardan hap)
#   sorular/GK_Beklenen_Konular_Hap.md                 (çıkması beklenen konulardan hap)
# Kanıt kesitleri kaynakta aranır; bulunamayan hap belgeye alınmaz (liste ekrana basılır).
# Kullanım: python3 hap.py <metin_klasoru>
import json, re, sys, pathlib, unicodedata, collections
HERE = pathlib.Path(__file__).parent; OUT = HERE.parent.parent / 'sorular'; MET = pathlib.Path(sys.argv[1])
YIL = [2021, 2022, 2023, 2024, 2025]
BRAND = 'Gümrük Koçu - Ufuk Çetintaş'

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

S = json.load(open(HERE / 'siniflar.json', encoding='utf-8'))
KON = {k['konu']: k for k in S['konular']}
SIN_AD = {'ÇOK': 'Çok çıkan konular (5 yılda 10 ve üzeri soru)', 'ORTA': 'Orta çıkan konular (5 yılda 5–9 soru)',
          'AZ': 'Az çıkan konular (5 yılda 1–4 soru)', 'HİÇ': 'Hiç çıkmayan konular (2021–2025)'}
SIRA_SIN = ['ÇOK', 'ORTA', 'AZ', 'HİÇ']

def egilim(k):
    y = k['yil']; ilk, son = sum(y[:3]) / 3, sum(y[3:]) / 2
    if k['n'] == 0: return '—'
    return '↑ yükselen' if son >= ilk + 1 else ('↓ azalan' if son <= ilk - 1 else '→ sabit')

# --- hap dosyaları
konular, red = [], collections.defaultdict(list)
for f in sorted((HERE / 'hap').glob('B*.json')):
    for k in json.load(open(f, encoding='utf-8'))['konular']:
        k['_grup'] = f.stem
        if k['konu'] in KON: k['sinif'] = KON[k['konu']]['sinif']
        ch = []
        for h in k.get('cikmis_hap', []):
            if h.get('kaynakta_yok') or kanit_ok(h.get('kanit', '')): ch.append(h)
            else: red['çıkmış'].append(f"{f.stem}/{k['konu']}: {h['hap'][:70]}")
        bh = []
        for h in k.get('beklenen_hap', []):
            if kanit_ok(h.get('kanit', '')): bh.append(h)
            else: red['beklenen'].append(f"{f.stem}/{k['konu']}: {h['hap'][:70]}")
        k['cikmis_hap'], k['beklenen_hap'] = ch, bh
        konular.append(k)
GK = json.load(open(HERE / 'hap' / 'GK.json', encoding='utf-8'))
def n_of(k): return KON.get(k['konu'], {'n': 0})['n']
def sirala(sin): return sorted([k for k in konular if k['sinif'] == sin], key=lambda k: (-n_of(k), k['konu']))
def yil_s(ys): return ', '.join(sorted(ys, key=lambda y: (y[:4], int(re.sub(r'\D', '', y.split('/')[-1]) or 0))))
GUNCEL = re.compile(r'güncel|değişiklik|sınav tarihinde|yeniden değerleme', re.I)
def tek(s): return re.sub(r'\s+', ' ', s).strip()

# ================= 1. belge: sınıflar + çıkan sorulardan hap
md = [f'# {BRAND}', '', '## Konu Sınıfları ve Çıkan Sorulardan Hap Bilgi (GMY 2021–2025)', '',
      '> 2021–2025 GMY sınavlarının 400 mevzuat sorusu (her yıl 21–100. sorular) konu bazında sayıldı ve konular dört sınıfa ayrıldı: '
      '**çok çıkan** (5 yılda 10 ve üzeri), **orta çıkan** (5–9), **az çıkan** (1–4), **hiç çıkmayan** (0). '
      'Hap bilgiler çıkmış soruların ölçtüğü bilgiden, resmî cevap anahtarına göre yazıldı; birden çok yılda sorulan bilgi tek satırda birleştirildi (★). '
      'Bilgisi depodaki mevzuat metinlerinde bulunmayan (ör. Form A, Seri No 10 Tebliği) haplar yalnız soru ve resmî cevaptan kuruldu (◇). '
      'Sınav tarihinden sonra değişen hükümler "Not" ile gösterildi. '
      'Hükmü kaynak metinde bulunan her hap, metindeki karşılığıyla doğrulandı.', '',
      '# 1. KONU SINIFLARI', '']
ozet = collections.Counter(k['sinif'] for k in S['konular'])
soru = collections.Counter(); [soru.update({k['sinif']: k['n']}) for k in S['konular']]
md += ['| Sınıf | Konu sayısı | 5 yılda soru | Karma testte (test başına) |', '|---|---|---|---|']
md += [f"| {SIN_AD[s].split(' (')[0]} | {ozet[s]} | {soru[s]} | {S['test_basina'][s]} |" for s in SIRA_SIN] + ['']
for s in SIRA_SIN:
    ks = sorted([k for k in S['konular'] if k['sinif'] == s], key=lambda k: (-k['n'], k['konu']))
    md += [f'## {SIN_AD[s]}', '', '| Konu | 2021 | 2022 | 2023 | 2024 | 2025 | Toplam | Son 2 yıl | Eğilim |', '|---|---|---|---|---|---|---|---|---|']
    md += [f"| {k['konu']} | " + ' | '.join(map(str, k['yil'])) + f" | **{k['n']}** | {k['son2']} | {egilim(k)} |" for k in ks] + ['']
md += ['> Eğilim: son iki yılın (2024–2025) yıllık ortalaması ilk üç yılın ortalamasından en az 1 soru fazlaysa yükselen, en az 1 soru azsa azalan.', '']

md += ['# 2. ÇIKAN SORULARDAN HAP BİLGİ (MEVZUAT)', '']
top_c = 0
for s in SIRA_SIN[:3]:
    md += [f'## {SIN_AD[s]}', '']
    for k in sirala(s):
        if not k['cikmis_hap']: continue
        n = n_of(k); md += [f"### {k['konu']} — {n} soru" + (f" ({egilim(KON[k['konu']])})" if k['konu'] in KON else ''), '']
        hs = sorted(k['cikmis_hap'], key=lambda h: -len(h.get('yillar', [])))
        for h in hs:
            ys = h.get('yillar', []); yildiz = '★ ' if len({y[:4] for y in ys}) > 1 else ''
            ek = [h['dayanak']] if h.get('dayanak') and not h['dayanak'].lower().startswith('kaynakta yok') else []
            ek.append(yil_s(ys))
            satir = f"- {yildiz}{tek(h['hap'])} *({' · '.join(e for e in ek if e)})*"
            if h.get('tuzak'): satir += f" — Tuzak: {tek(h['tuzak'])}"
            if h.get('not') and GUNCEL.search(h['not']): satir += f" — Not: {tek(h['not'])}"
            if h.get('kaynakta_yok'): satir += ' ◇'
            md.append(satir); top_c += 1
        md.append('')

md += ['# 3. ÇIKAN SORULARDAN HAP BİLGİ (GENEL KÜLTÜR)', '',
       '> Genel kültür bölümünde (her yıl 1–20. sorular) Tarih ve Hukuk haplarında bilgi yalnız soru metni ve resmî cevaptan kuruldu; Türkçe haplarında doğru cevabın dayandığı dil kuralı yazıldı.', '']
for alan, bas in (('tarih', 'Tarih'), ('hukuk', 'Hukuk (Anayasa ve temel kavramlar)'), ('turkce', 'Türkçe')):
    md += [f'## {bas}', '']
    for h in GK.get(alan, []):
        ys = h.get('yillar', []); yildiz = '★ ' if len({y[:4] for y in ys}) > 1 else ''
        satir = f"- {yildiz}{tek(h['hap'])} *({yil_s(ys)})*"
        if h.get('tuzak'): satir += f" — Tuzak: {tek(h['tuzak'])}"
        if h.get('not'): satir += f" — Not: {tek(h['not'])}"
        md.append(satir); top_c += 1
    md.append('')
mk = GK.get('matematik_konulari', {})
if mk:
    md += ['## Matematik — yıllara göre soru konuları', '', '| Yıl | Konular |', '|---|---|']
    md += [f"| {y} | {', '.join(v) if isinstance(v, list) else v} |" for y, v in sorted(mk.items())] + ['']
md += ['---', f'**{BRAND}**']
(OUT / 'GK_Konu_Siniflari_ve_Cikan_Sorular_Hap.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

# ================= 2. belge: çıkması beklenen konular
md = [f'# {BRAND}', '', '## Çıkması Beklenen Konulardan Hap Bilgi (GMY 2027 hazırlık)', '',
      '> Hap bilgiler 2021–2025 GMY sınavlarında **hiç sorulmamış hükümlerden** seçildi. Öncelik sırası: (1) çok ve orta çıkan konuların sorulmamış sayı, süre, makam ve şart hükümleri; '
      '(2) kaynak metinde yakın tarihli değişiklik notu taşıyan hükümler; (3) son iki yılda yükselen konuların sorulmamış alt başlıkları. '
      'Her hap kaynak metindeki karşılığıyla doğrulandı; çıkmış sorulardaki bilgi burada tekrarlanmadı.', '',
      '# 1. ÖNCELİK TABLOSU', '', '| Konu | Sınıf | 5 yılda soru | 2024–2025 | Eğilim | Hap |', '|---|---|---|---|---|---|']
for s in SIRA_SIN:
    for k in sirala(s):
        if not k['beklenen_hap']: continue
        kk = KON.get(k['konu'], {'n': 0, 'son2': 0, 'yil': [0] * 5})
        md.append(f"| {k['konu']} | {s} | {kk['n']} | {kk['son2']} | {egilim(kk) if k['konu'] in KON else '—'} | {len(k['beklenen_hap'])} |")
md.append('')
degisik = []
top_b = 0
for s in SIRA_SIN:
    md += [f"# {SIRA_SIN.index(s) + 2}. {SIN_AD[s]}", '']
    for k in sirala(s):
        if not k['beklenen_hap']: continue
        md += [f"## {k['konu']}", '']
        if k.get('beklenen_neden'): md += [f"> {tek(k['beklenen_neden'])}", '']
        for h in k['beklenen_hap']:
            nd = tek(h.get('neden', ''))
            etiket = ' **[Yeni]**' if 'değişiklik' in nd.lower() else ''
            md.append(f"- {tek(h['hap'])}{etiket} *({h.get('dayanak', '')})*"); top_b += 1
            if 'değişiklik' in nd.lower(): degisik.append((k['konu'], h, nd))
        md.append('')
if degisik:
    md += ['# 6. SON DEĞİŞİKLİKLER — TOPLU LİSTE', '', '> Kaynak metinde yakın tarihli değişiklik notu taşıyan hükümler ([Yeni]).', '',
           '| Konu | Hap | Dayanak | Değişiklik |', '|---|---|---|---|']
    SD = re.compile(r'(?i)^.*?son değişiklik:?\s*')
    md += [f"| {ko} | {tek(h['hap'])} | {h.get('dayanak', '')} | {SD.sub('', nd)} |" for ko, h, nd in degisik] + ['']
md += ['---', f'**{BRAND}**']
(OUT / 'GK_Beklenen_Konular_Hap.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

print('çıkan hap:', top_c, '| beklenen hap:', top_b, '| son değişiklik:', len(degisik))
for k, v in red.items():
    print('-- kanıtı bulunamayan', k, len(v)); [print('   ', x) for x in v[:40]]
