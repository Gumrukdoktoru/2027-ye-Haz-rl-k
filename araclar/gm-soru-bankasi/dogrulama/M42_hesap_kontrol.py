"""M42 (Gümrük Kanunu cezaları) küçük hesap sorusunun bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/M42_hesap_kontrol.py [veri/gm_M42.py]

Kıymet noksanlığında ceza (GK 234/1-b ve 234/3): vergi farkının üç katı; aykırılık idarenin
tespitinden önce beyan sahibince bildirilirse ceza yüzde on nispetinde uygulanır.
Her çeldirici adı konmuş bir hatadan yeniden hesaplanır.
"""

import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_M42.py"
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
# 1: kıymet noksanlığı, kendiliğinden bildirim
beyan, gercek, gd = D(400000), D(500000), D(2400000)
fark = gercek - beyan
H[1] = (
    fark * 3 * p(10),
    {
        "üç kat atlanmış (farkın %10'u)": fark * p(10),
        "yarısı (miktar farkı/maddi hata sanılmış)": fark / 2,
        "bildirim indirimi uygulanmamış": fark * 3,
        "gümrüklenmiş değerin iki katının %10'u": gd * 2 * p(10),
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
