"""GM kör çözüm sonuçlarını kitap anahtarıyla karşılaştırır.

Kullanım: python3 kor_karsilastir_gm.py KITAP.json [KITAP2.json ...]
kor_cozum/<KOD>.json: {"M44-01": {"cevap": "C", "emin": "yüksek", "dayanak": "...", "sorun": []}, ...}
Kör çözüm cevap anahtarı görülmeden, yalnız cevapsız soru metni (kök + şıklar) ve bölüm kaynak metniyle yapılır.
"""
import json
import pathlib
import sys

KOR = pathlib.Path(__file__).resolve().parent / 'kor_cozum'
K = {q['id']: q for yol in sys.argv[1:] for b in json.load(open(yol, encoding='utf-8')) for q in b['sorular']}
top = uy = 0
for f in sorted(KOR.glob('*.json')):
    C = json.load(open(f, encoding='utf-8'))
    b_top = b_uy = 0
    for qid, v in C.items():
        q = K.get(qid)
        if not q:
            continue
        top += 1
        b_top += 1
        ok = v.get('cevap') == q['harf']
        uy += ok
        b_uy += ok
        if not ok or v.get('sorun') or v.get('emin') != 'yüksek':
            print(f"{qid} anahtar={q['harf']} kör={v.get('cevap')} emin={v.get('emin')} "
                  f"{'UYUŞMUYOR' if not ok else ''} sorun={v.get('sorun')}")
    if b_top:
        print(f'{f.stem}: {b_uy}/{b_top}')
print(f'Toplam: {uy}/{top} uyuşuyor')
