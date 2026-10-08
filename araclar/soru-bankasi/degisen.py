"""Yedek ile güncel soru dosyalarını karşılaştırır; kök/şık/cevabı değişen soruların kök metinlerini listeler."""
import glob, json, re, runpy, sys
S, yedek = sys.argv[1], sys.argv[2]
def imza(q): return json.dumps([q['kok'], q['d'], sorted(q.get('c') or []), q.get('siklar')], ensure_ascii=False)
out = {}
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    eski = {imza(q) for q in runpy.run_path(f'{yedek}/sb_{no}.py')['Q']}
    yeni = runpy.run_path(f)['Q']
    out[no] = [q['kok'][0][:80] for q in yeni if imza(q) not in eski]
json.dump(out, open(f'{S}/sb/degisen.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(sum(len(v) for v in out.values()), {k: len(v) for k, v in out.items()})
