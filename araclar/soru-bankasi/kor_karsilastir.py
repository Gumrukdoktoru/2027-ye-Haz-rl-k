import json, glob, re, sys
S = sys.argv[1]
K = {q['id']: q for b in json.load(open(f'{S}/sbson1/kitap.json', encoding='utf-8')) for q in b['sorular']}
top = uy = 0
for f in sorted(glob.glob(f'{S}/sb/kor_cevap/sb_*.json')):
    C = json.load(open(f, encoding='utf-8'))
    for qid, v in C.items():
        q = K.get(qid)
        if not q: continue
        top += 1
        ok = v.get('cevap') == q['harf']
        uy += ok
        if not ok or v.get('sorun') or v.get('emin') != 'yüksek':
            print(f"{qid} anahtar={q['harf']} kör={v.get('cevap')} emin={v.get('emin')} {'UYUŞMUYOR' if not ok else ''} sorun={v.get('sorun')}")
print(f'{uy}/{top} uyuşuyor')
