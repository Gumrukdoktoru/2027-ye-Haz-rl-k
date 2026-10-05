# Bağımsız doğrulama turunun (DUZELT / SIL) kararlarını grup çıktılarına uygular.
# Kullanım: python3 dogrulama_uygula.py <ham_grup_klasoru> <dogrulama_out_klasoru>
# Sonuç: json/Gxx.json (düzeltilmiş) + dogrulama_ozeti.json
import json, sys, pathlib, collections
HERE = pathlib.Path(__file__).parent
HAM, DOG = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
G = {f.stem: json.load(open(f, encoding='utf-8')) for f in sorted(HAM.glob('G*.json'))}
oz = {'parca': {}, 'duzelt': [], 'sil': []}
silinecek = collections.defaultdict(set)
for f in sorted(DOG.glob('V*.json')):
    v = json.load(open(f, encoding='utf-8'))
    oz['parca'][f.stem] = {k: (len(v[k]) if isinstance(v[k], list) else v[k]) for k in ('toplam', 'ok', 'duzelt', 'sil')}
    for d in v['duzelt']:
        g, fi, qi = d['key'].split('|'); q = G[g]['dosyalar'][int(fi)]['soru_cevap'][int(qi)]
        eski = {k: q[k] for k in ('soru', 'cevap', 'dayanak')}
        for k in ('soru', 'cevap', 'dayanak', 'kanit'):
            if d.get(k): q[k] = d[k]
        oz['duzelt'].append({'key': d['key'], 'eski': eski, 'yeni': {k: q[k] for k in ('soru', 'cevap', 'dayanak')}, 'gerekce': d.get('gerekce', '')})
    for s in v['sil']:
        g, fi, qi = s['key'].split('|'); silinecek[(g, int(fi))].add(int(qi))
        q = G[g]['dosyalar'][int(fi)]['soru_cevap'][int(qi)]
        oz['sil'].append({'key': s['key'], 'soru': q['soru'], 'cevap': q['cevap'], 'gerekce': s.get('gerekce', '')})
for (g, fi), qs in silinecek.items():
    x = G[g]['dosyalar'][fi]
    x['soru_cevap'] = [q for i, q in enumerate(x['soru_cevap']) if i not in qs]
(HERE / 'json').mkdir(exist_ok=True)
for g, d in G.items():
    json.dump(d, open(HERE / 'json' / f'{g}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(oz, open(HERE / 'dogrulama_ozeti.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
t = collections.Counter()
for p in oz['parca'].values(): t.update(p)
print(dict(t), '| düzeltilen', len(oz['duzelt']), '| silinen', len(oz['sil']))
