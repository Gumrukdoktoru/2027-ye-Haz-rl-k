# Bağımsız doğrulama sonuçlarını (dogrulama/V_<G>.json) grup dosyalarına (json/<G>.json) uygular.
# key = "<G>-<sıra>" (json/<G>.json içindeki 1 tabanlı sıra). DUZELT öğesindeki tam soru eskisinin yerine geçer.
# Kullanım: python3 dogrulama_uygula.py B2 [B5 ...]
import json, sys, pathlib
HERE = pathlib.Path(__file__).parent
ALAN = ['test', 'konu', 'sinif', 'tur', 'cikmis', 'alt_tip', 'kalip', 'z', 'madde', 'cek', 'kok', 'd', 'c', 'sabit', 'g', 'kanit']
for g in sys.argv[1:]:
    Q = json.load(open(HERE / 'json' / f'{g}.json', encoding='utf-8'))
    V = json.load(open(HERE / 'dogrulama' / f'V_{g}.json', encoding='utf-8'))
    n_ok = len(V['ok']); n_d = 0
    for x in V['duzelt']:
        i = int(x['key'].split('-')[1]) - 1
        yeni = x['soru']; eski = Q[i]
        if 'uygulandi' in eski.get('dogrulama', ''): continue
        eksik = [a for a in ALAN if a not in yeni]
        if eksik: print(f'  {x["key"]}: eksik alan {eksik}'); continue
        if (yeni['test'], yeni['konu']) != (eski['test'], eski['konu']): print(f'  {x["key"]}: test/konu değişmiş, atlandı'); continue
        Q[i] = {a: yeni[a] for a in ALAN}; Q[i]['dogrulama'] = 'DUZELT uygulandi: ' + x.get('gerekce', '')[:300]; n_d += 1
    assert n_ok + len(V['duzelt']) == len(Q), (g, n_ok, len(V['duzelt']), len(Q))
    json.dump(Q, open(HERE / 'json' / f'{g}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(g, 'ok', n_ok, '| düzeltme uygulandı', n_d)
