"""Kitap PDF'inde bölüm, çözüm ve ek başlangıç sayfalarını bulur (içindekiler için ikinci geçiş).

Kullanım: python3 sayfa.py KITAP.pdf SAYFA_HARITASI.json
"""
import json
import re
import sys

import pdfplumber

pdf, cikti = sys.argv[1:3]
harita = {}
with pdfplumber.open(pdf) as p:
    for i, sf in enumerate(p.pages, 1):
        t = sf.extract_text() or ''
        m = re.search(r'BÖLÜM (\d\d) ·', t)
        if m and str(int(m.group(1))) not in harita:
            harita[str(int(m.group(1)))] = i
        # çözüm başlığı: "Bölüm 07 · … — Cevap Anahtarı ve Çözümler" (uzun başlık satır kırabilir)
        for m in re.finditer(r'Bölüm (\d\d) ·', t):
            if 'Cevap Anahtarı ve Çözümler' in ' '.join(t[m.start():m.start() + 250].split()) and f'c{int(m.group(1))}' not in harita:
                harita[f'c{int(m.group(1))}'] = i
        for ek in ('EkA', 'EkB'):
            if ek not in harita and re.search(rf'^Ek {ek[-1]} —', t, re.M):
                harita[ek] = i
json.dump(harita, open(cikti, 'w'), ensure_ascii=False, indent=0)
print(f'{len(harita)} başlangıç sayfası → {cikti}')
