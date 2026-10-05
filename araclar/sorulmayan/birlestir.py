# Sorulmayan konular soru–cevap seti: grup JSON'larını birleştirir, kanıt kesitlerini
# kaynak metinde doğrular, kural denetimi yapar, analiz + soru–cevap Markdown'larını üretir.
# Kullanım: python3 birlestir.py <metin_klasoru> <cikmis_envanter.tsv>
import json, re, sys, unicodedata, collections, pathlib
HERE = pathlib.Path(__file__).parent
MET = pathlib.Path(sys.argv[1]); TSV = pathlib.Path(sys.argv[2])
OUT = HERE.parent.parent / 'sorular'

def norm(s):
    s = unicodedata.normalize('NFC', s).replace('\xa0', ' ')
    s = s.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '–': '-', '—': '-', '​': ''}))
    return re.sub(r'\s+', ' ', s).strip().lower()

src = {f.name: norm(f.read_text(encoding='utf-8')) for f in MET.glob('*.txt')}
allsrc = ' '.join(src.values())

def kanit_ok(k, kaynak):
    parts = [p.strip(' .;,:') for p in re.split(r'\s*(?:\.\.\.|…|\[\.\.\.\])\s*', k) if p.strip()]
    parts = [norm(p) for p in parts if len(p.strip()) >= 12]
    if not parts: return False
    hay = src.get(kaynak, allsrc)
    return all(p in hay or p in allsrc for p in parts)

# Kaynak dosya sırası: numaralı dosyalar numara sırasıyla, diğerleri sonra
def sira(name):
    m = re.match(r'(\d+)-', name)
    if m: return (0, int(m.group(1)), name)
    order = ['5607_sayili_kacakcilikla_mucadele_kanunu.txt']
    return (1, 0 if name in order else 1, name)

D = []
for f in sorted((HERE / 'json').glob('G*.json')):
    g = json.load(open(f, encoding='utf-8'))
    for x in g['dosyalar']:
        x['grup'] = g['grup']; D.append(x)
D.sort(key=lambda x: sira(x['kaynak']))

# Denetimler
sorun = collections.defaultdict(list)
madde_re = re.compile(r'(\b\d+\s*(?:\'?\s*(?:inci|ıncı|nci|ncı|üncü|uncu|ünci|uncı))\s+madde|\bmadde(?:si|sinin|sine|sinde)?\s*\d|\bmd\.|\bfıkra|\bbendi)', re.I)
gor = set()
for x in D:
    temiz = []
    for q in x['soru_cevap']:
        k = (x['kaynak'], q['soru'][:80])
        if not kanit_ok(q.get('kanit', ''), x['kaynak']):
            sorun['kanit'].append((x['kaynak'], q['soru'], q.get('kanit', ''))); continue
        if madde_re.search(q['soru']): sorun['madde_no'].append((x['kaynak'], q['soru']))
        if '2009/15481' in q.get('dayanak', '') and q['soru'].lstrip().startswith('4458'):
            sorun['karar_kok'].append((x['kaynak'], q['soru']))
        if norm(q['soru']) in gor:
            sorun['tekrar'].append((x['kaynak'], q['soru'])); continue
        gor.add(norm(q['soru'])); temiz.append(q)
    x['soru_cevap'] = temiz

# Envanter: çıkmış soruların yıl dağılımı
env = [l.split('\t') for l in TSV.read_text(encoding='utf-8').splitlines()[1:] if l.strip()]
env_by_file = collections.defaultdict(list)
for r in env: env_by_file[r[5]].append(r)
YIL = ['2021', '2022', '2023', '2024', '2025']
# Envanter konusu bu dosyaya benzese de hükmü başka kaynakta olan sorular (dosyanın hükümleri sorulmamış)
HARIC = {'13-TAŞITLAR.txt': {'2021-32'}, '14-KABOTAJ.txt': {'2021-70'}}
# Ajanların "ilişkili / çapraz / dolaylı / bu dosyada değil" diye işaretlediği çıkmışlar konu sayımına girmez
ILGILI = re.compile(r'\[çapraz|\((?:[^)]*, )?ilişkili[;)]|\(dolaylı|bu dosyada değil|kaynak: [^;)]*; bu dosyada karşılığı yok')
def yillar(x):
    refs = set()
    for r in env_by_file.get(x['kaynak'], []): refs.add(f'{r[0]}-{r[1]}')
    for c in x.get('cikmis', []):
        if ILGILI.search(c): continue  # başka konunun/dosyanın sorusu; yalnız ilgili hükme değdiği için listelenir
        m = re.match(r'\s*(20\d\d)\s*[-/]\s*(\d+)', c)
        if m: refs.add(f'{m.group(1)}-{m.group(2)}')
    return sorted(refs - HARIC.get(x['kaynak'], set()))

no = 0
for x in D:
    x['refs'] = yillar(x)
    h = HARIC.get(x['kaynak'], set())
    x['haric'] = [c for c in x.get('cikmis', []) if c.split(':')[0].strip() in h]
    x['cikmis'] = [c for c in x.get('cikmis', []) if c.split(':')[0].strip() not in h]
    for q in x['soru_cevap']:
        no += 1; q['no'] = no; q['id'] = f'SC-{no:04d}'
        for k in ('soru', 'cevap'):  # kaynak metindeki dipnot işaretlerini ([12]) temizle
            q[k] = re.sub(r'\s+', ' ', re.sub(r'\[\d{1,3}\]', '', q[k])).strip()
    st = collections.Counter(a['durum'] for a in x['alt_konular'])
    x['st'] = st

json.dump(D, open(HERE / 'sc.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('dosya:', len(D), '| soru–cevap:', no)
for k, v in sorun.items():
    print(f'-- {k}: {len(v)}')
    for t in v[:60]: print('   ', ' | '.join(s[:150] for s in t))
