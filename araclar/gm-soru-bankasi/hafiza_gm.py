"""GM soru bankası sorularını üretim hafızasına ekler (her bölüm ayrı set: GM-M01 … GM-H05).

Kullanım: python3 hafiza_gm.py URETIM-HAFIZASI.md KITAP.json [KITAP2.json ...] [--yenile]
Aynı ID zaten varsa satır yeniden eklenmez; --yenile verilirse önce bütün GM- satırları silinip kitaplardan yeniden yazılır.
Toplam satırı yeniden hesaplanır.
"""

import json
import re
import sys

arg = [a for a in sys.argv[1:] if not a.startswith("--")]
yol, kitaplar = arg[0], arg[1:]
s = open(yol, encoding="utf-8").read()
bas, son = s.index("```\n") + 4, s.rindex("\n```")
satirlar = s[bas:son].split("\n")
if "--yenile" in sys.argv:
    satirlar = [x for x in satirlar if " | GM-" not in x]
var = {x.split(" | ")[0] for x in satirlar}
yeni = []
for kitap in kitaplar:
    for b in json.load(open(kitap, encoding="utf-8")):
        for q in b["sorular"]:
            if q["id"] in var:
                continue
            kod = q["id"].split("-")[0]
            cek = q["cek"].replace("|", "/").replace("\n", " ")
            yeni.append(
                f"{q['id']} | {q['konu']} | {q['madde']} | {cek} | {q['kalip']} | {q['z']} | {q['harf']} | GM-{kod}"
            )
satirlar += yeni
veri = [x for x in satirlar[1:] if x.strip()]
say = {
    "Karar": 0,
    "GMY deneme S1": 0,
    "GMY deneme S2": 0,
    "GMY deneme S3": 0,
    "Soru bankası": 0,
    "GM soru bankası": 0,
}
for x in veri:
    k = x.split(" | ")[-1]
    if k.startswith("GM-"):
        say["GM soru bankası"] += 1
    else:
        say[
            (
                "Karar"
                if k == "S1" and x.startswith("KAR")
                else {
                    "GMY-S1": "GMY deneme S1",
                    "GMY-S2": "GMY deneme S2",
                    "GMY-S3": "GMY deneme S3",
                }.get(k, "Soru bankası")
            )
        ] += 1
toplam = (
    f"Toplam: {len(veri)} satır ("
    + " · ".join(f"{k}: {v}" for k, v in say.items() if v)
    + ")"
)
kuyruk = re.sub(r"Toplam: \d+ satır \([^)]*\)", toplam, s[son:])
open(yol, "w", encoding="utf-8").write(s[:bas] + "\n".join(satirlar) + kuyruk)
print(f"{len(yeni)} satır eklendi. {toplam}")
