"""GM kitap PDF'inde bölüm testi, çözüm ve ek başlangıç sayfalarını bulur (içindekiler için ikinci geçiş).

Kullanım: python3 sayfa_gm.py KITAP.pdf SAYFA_HARITASI.json
Çıktı anahtarları: "M44" (test sayfası), "cM44" (çözüm sayfası), "EkA", "EkB".
"""

import json
import re
import sys

import pdfplumber

pdf, cikti = sys.argv[1:3]
harita = {}
with pdfplumber.open(pdf) as p:
    for i, sf in enumerate(p.pages, 1):
        t = sf.extract_text() or ""
        m = re.search(r"BÖLÜM ([MTH]\d\d) ·", t)
        if m and m.group(1) not in harita:
            harita[m.group(1)] = i
        for m in re.finditer(r"Bölüm ([MTH]\d\d) ·", t):
            if (
                "Cevap Anahtarı ve Çözümler"
                in " ".join(t[m.start() : m.start() + 250].split())
                and f"c{m.group(1)}" not in harita
            ):
                harita[f"c{m.group(1)}"] = i
        for ek in ("EkA", "EkB"):
            if ek not in harita and re.search(rf"^Ek {ek[-1]} —", t, re.M):
                harita[ek] = i
json.dump(harita, open(cikti, "w"), ensure_ascii=False, indent=0)
print(f"{len(harita)} başlangıç sayfası → {cikti}")
