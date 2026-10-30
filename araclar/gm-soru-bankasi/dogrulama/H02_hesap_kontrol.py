"""H02 (Vergi matrahları ve ithalat vergileri) hesap sorularının bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/H02_hesap_kontrol.py [veri/gm_H02.py]

Her hesap sorusu için veri kökteki rakamlardan yeniden hesaplanır:
- doğru cevap (formül, kaynaktaki cümle: GVM = CIF + yurt dışı gider; KDV matrahı = CIF + yurt dışı + vergiler + yurt içi ...),
- her çeldirici (adı konmuş tipik hata).
Sonuçlar şıklardaki metinle karşılaştırılır; sıra artan olmalı, doğru şık B/C/D'de olmalıdır.
"""

import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_H02.py"
ns = {}
exec(yol.read_text(encoding="utf-8"), ns)
Q = ns["Q"]


def tl(x):
    """Sayıyı şık biçimine çevirir: binlik nokta, ondalık yoksa tam sayı."""
    x = D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
    tam, kes = divmod(x, 1)
    s = f"{int(tam):,}".replace(",", ".")
    return s if kes == 0 else s + "," + f"{kes:.2f}"[2:]


def p(x):
    return D(str(x)) / 100


def gvm(cif, yurt_disi=0):
    return D(str(cif)) + D(str(yurt_disi))


def minmax(nispi, alt, ust):
    return alt if nispi < alt else ust if nispi > ust else nispi


H = {}  # soru sırası (1'den) → (doğru, {çeldirici adı: değer})

# 1: GV
g = gvm(20000 + 2000 + 500, 1500)
H[1] = (
    g * p(10),
    {
        "FOB": D(20000) * p(10),
        "FOB+navlun": D(22000) * p(10),
        "CIF": D(22500) * p(10),
        "iç nakliye matrahta": (g + 800) * p(10),
    },
)
# 2: İGV min-max (adet)
nispi = D(40000) * p(15)
H[2] = (
    minmax(nispi, D(500) * 2, D(500) * 8),
    {"min adet": D(1000), "min kg": D(1250) * 2, "nispi": nispi, "max kg": D(1250) * 8},
)
# 3: GV min-max iki kalem
k1 = minmax(D(10000) * p(5), D(200) * D("0.40"), D(200) * D("1.50"))
k2 = minmax(D(2000) * p(5), D(1000) * D("0.40"), D(1000) * D("1.50"))
H[3] = (
    k1 + k2,
    {
        "k1 max + k2 nispi": D(300) + D(100),
        "iki min": D(80) + D(400),
        "iki nispi": D(500) + D(100),
        "k1 nispi + k2 min": D(500) + D(400),
    },
)
# 5: GV + İGV + EMY
g = gvm(40000, 2000)
gv, igv, emy = g * p(6), g * p(20), g * p(1)
H[5] = (
    gv + igv + emy,
    {
        "CIF": D(40000) * p(27),
        "EMY yok": gv + igv,
        "yurt içi matrahta": (g + 1000) * p(27),
        "İGV matrahına GV": gv + (g + gv) * p(20) + emy,
    },
)
# 6: ÇKP hurda ‰5
H[6] = (
    D(200000) * D("0.005"),
    {
        "on binde beş": D(200000) * D("0.0005"),
        "GV dahil": D(220000) * D("0.005"),
        "yakıt %1": D(200000) * p(1),
        "%5": D(200000) * p(5),
    },
)
# 7: Kültür fonu
g = gvm(27000 + 2500 + 500, 2000)
gv = g * p(5)
H[7] = (
    g * p(2),
    {
        "FOB": D(27000) * p(2),
        "CIF": D(30000) * p(2),
        "GV dahil": (g + gv) * p(2),
        "GV + yurt içi dahil": (g + gv + 1000) * p(2),
    },
)
# 8: Gümrüklenmiş değer
H[8] = (
    D(60000 + 6000 + 3000),
    {
        "İGV yok": D(66000),
        "damga dahil": D(69450),
        "kültür fonu dahil": D(70200),
        "ikisi de dahil": D(70650),
    },
)
# 10, 11: ÖTV ve KDV (aynı veri)
cif, yi = D(100000), D(2000)
gv = cif * p(10)
otv_m = cif + gv + yi
otv = otv_m * p(30)
kdv_m = otv_m + otv
H[10] = (
    otv,
    {
        "CIF": cif * p(30),
        "yurt içi yok": (cif + gv) * p(30),
        "KDV dahil": (otv_m + otv_m * p(20)) * p(30),
        "ÖTV kendi matrahında": otv_m * p(30) / (1 - p(30)),
    },
)
gv2 = (cif + yi) * p(10)  # yurt içi GV matrahına eklenmiş
otv2 = (cif + yi + gv2) * p(30)
H[11] = (
    kdv_m * p(20),
    {
        "ÖTV yok": otv_m * p(20),
        "GV hiç yok": ((cif + yi) + (cif + yi) * p(30)) * p(20),
        "yurt içi yok": ((cif + gv) + (cif + gv) * p(30)) * p(20),
        "yurt içi GV matrahında": (cif + yi + gv2 + otv2) * p(20),
    },
)
# 12: TRT bandrol
g = D(20000)
gv, igv = g * p(5), g * p(10)
bm = g + gv + igv + 500
H[12] = (
    bm * p(8),
    {
        "İGV yok": (bm - igv) * p(8),
        "yurt içi yok": (bm - 500) * p(8),
        "ÖTV dahil": (bm + bm * p(10)) * p(8),
        "KDV dahil": (bm + bm * p(20)) * p(8),
    },
)
# 14: KDV zinciri
g = gvm(50000, 2000)
gv, igv = g * p(8), g * p(10)
H[14] = (
    (g + gv + igv + 1000) * p(20),
    {
        "İGV yok": (g + gv + 1000) * p(20),
        "ambalaj yok": (D(50000) + D(50000) * p(8) + D(50000) * p(10) + 1000) * p(20),
        "yurt içi yok": (g + gv + igv) * p(20),
        "yurt içi GV matrahında": (D(53000) + D(53000) * p(8) + D(53000) * p(10))
        * p(20),
    },
)
# 16: KKDF
H[16] = (
    D(80000) * D("32.00") * p(6),
    {
        "%4": D(80000) * 32 * p(4),
        "satış kuru": D(80000) * D("32.20") * p(6),
        "CIF": D(85000) * 32 * p(6),
        "%10": D(80000) * 32 * p(10),
    },
)
# 18: KKDF + DİİB istisnası
H[18] = (
    D(25000) * 30 * p(6),
    {
        "hepsi muaf": D(0),
        "yalnız DİİB": D(40000) * 30 * p(6),
        "istisna görülmemiş": D(65000) * 30 * p(6),
        "%10": D(65000) * 30 * p(10),
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
