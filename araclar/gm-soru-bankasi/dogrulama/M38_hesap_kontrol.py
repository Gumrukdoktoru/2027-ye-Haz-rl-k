"""M38 (Tasfiye I) küçük hesap sorusunun bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/M38_hesap_kontrol.py [veri/gm_M38.py]

Satış bedelinin dağıtımı (Tasfiye Yönetmeliği md. 64; GK 180): satış bedelinden sırasıyla
hizmet karşılığı %15, gümrük vergileri, satış masrafları karşılığı %50, para cezaları ayrılır;
artan para eşya sahibi adına emanete alınır. Her çeldirici adı konmuş bir hatadan yeniden hesaplanır.
"""

import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_M38.py"
ns = {}
exec(yol.read_text(encoding="utf-8"), ns)
Q = ns["Q"]


def tl(x):
    x = D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
    tam, kes = divmod(x, 1)
    s = f"{int(tam):,}".replace(",", ".")
    return s if kes == 0 else s + "," + f"{kes:.2f}"[2:]


def p(x):
    return D(str(x)) / 100


H = {}
# 7: satış bedelinin dağıtımı ve emanete alınacak tutar
sb, gv, ceza, fiili = D(200000), D(40000), D(20000), D(6000)
hizmet, satis = sb * p(15), sb * p(50)
dogru = sb - hizmet - gv - satis - ceza
H[7] = (
    dogru,
    {
        "fiili gider de düşülmüş": dogru - fiili,
        "para cezası ayrılmamış": sb - hizmet - gv - satis,
        "%50 kalan tutara uygulanmış": (sb - hizmet - gv)
        - (sb - hizmet - gv) * p(50)
        - ceza,
        "%50 yerine fiili gider": sb - hizmet - gv - fiili - ceza,
    },
)

hata = 0
hesap_sorulari = [i for i, q in enumerate(Q, 1) if q["kalip"] == "HESAP"]
eksik = sorted(set(hesap_sorulari) - set(H))
if eksik:
    print("Doğrulaması yazılmamış hesap sorusu:", eksik)
    hata += len(eksik)
for i, (dogru, celd) in sorted(H.items()):
    q = Q[i - 1]
    if q["kalip"] != "HESAP":
        print(f'{i}: HESAP kalıbı bekleniyordu ({q["kalip"]})')
        hata += 1
        continue
    beklenen = sorted([dogru] + list(celd.values()))
    siklar = q["siklar"]
    sorun = []
    if tl(dogru) != q["d"]:
        sorun.append(f'doğru {tl(dogru)} ≠ d {q["d"]}')
    if [tl(x) for x in beklenen] != siklar:
        sorun.append(f"şıklar {siklar} ≠ hesap {[tl(x) for x in beklenen]}")
    if len({tl(x) for x in beklenen}) != 5:
        sorun.append("iki hata aynı sonucu veriyor")
    if siklar.index(q["d"]) not in (1, 2, 3):
        sorun.append("doğru şık B/C/D değil")
    if tl(dogru) not in q["g"]:
        sorun.append("gerekçede doğru sonuç geçmiyor")
    durum = "TAMAM" if not sorun else "HATA: " + "; ".join(sorun)
    hata += bool(sorun)
    print(
        f'{i:2d} d={q["d"]:>8} konum={"ABCDE"[siklar.index(q["d"])]} | '
        + ", ".join(f"{k}={tl(v)}" for k, v in celd.items())
        + f" | {durum}"
    )
print(f"\nHesap sorusu: {len(H)} · hata: {hata}")
sys.exit(1 if hata else 0)
