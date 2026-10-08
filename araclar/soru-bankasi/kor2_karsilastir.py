import json, glob, sys
S = sys.argv[1]
K = {q['id']: q for b in json.load(open(f'{S}/sbson3/kitap.json', encoding='utf-8')) for q in b['sorular']}
top = uy = 0
for f in sorted(glob.glob(f'{S}/sb/kor2_cevap/grup_*.json')):
    for qid, v in json.load(open(f, encoding='utf-8')).items():
        q = K[qid]; top += 1; ok = v.get('cevap') == q['harf']; uy += ok
        if not ok or v.get('sorun') or v.get('emin') != 'yüksek':
            print(f"{qid} anahtar={q['harf']} kör={v.get('cevap')} emin={v.get('emin')} {'UYUŞMUYOR' if not ok else ''} sorun={v.get('sorun')}")
print(f'{uy}/{top} uyuşuyor')
