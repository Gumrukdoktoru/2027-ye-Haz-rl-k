"""H03 (Özel hesaplamalar) hesap sorularının bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/H03_hesap_kontrol.py [veri/gm_H03.py]

Her hesap sorusu için veri kökteki rakamlardan yeniden hesaplanır:
- doğru cevap (kaynaktaki formül: ÖTV nispi / asgari maktu / maktu, saat min-maks, has altın-gümüş,
  tarım payı, DFİF, TEV, kısmi muafiyet %3, kullanılmış araç amortismanı, (I) sayılı liste teminatı),
- her çeldirici (adı konmuş tipik hata).
Sonuçlar şıklardaki metinle karşılaştırılır; sıra artan olmalı, doğru şık B/C/D'de olmalıdır.
"""

import math
import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_H03.py"
ns = {}
exec(yol.read_text(encoding="utf-8"), ns)
Q = ns["Q"]


def tl(x):
    """Sayıyı şık biçimine çevirir: binlik nokta, ondalık varsa virgülle iki hane."""
    x = D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
    tam, kes = divmod(x, 1)
    s = f"{int(tam):,}".replace(",", ".")
    return s if kes == 0 else s + "," + f"{kes:.2f}"[2:]


def yuzde(x):
    return "%" + tl(x)


def p(x):
    return D(str(x)) / 100


def minmax(nispi, alt, ust):
    return alt if nispi < alt else ust if nispi > ust else nispi


H = {}  # soru sırası (1'den) → (doğru, {çeldirici adı: değer}, biçimleyici)

# 1: Bira — nispi ile AMV (derece × litre × AMV), büyük olan
litre = D(1200) * 50 / 100
nispi, amv = D(30000) * p(25), D(5) * litre * D("3.00")
H[1] = (
    max(nispi, amv),
    {
        "viski formülü": litre * D("3.00") * D(5) / 100,
        "derece yok": litre * D("3.00"),
        "nispi": nispi,
        "toplam": nispi + amv,
    },
    tl,
)
# 2: Şarap — AMV litre başına; nispi yüksek
litre = D(800) * 75 / 100
nispi, amv = D(60000) * p(18), litre * D("12.00")
H[2] = (
    max(nispi, amv),
    {
        "AMV seçilmiş": amv,
        "KDV ÖTV matrahında": D(60000) * (1 + p(20)) * p(18),
        "toplam": nispi + amv,
        "bira formülü": D(12) * litre * D("12.00"),
    },
    tl,
)
# 3: Sigara 20'li — max(nispi, AMV) + maktu
paket, dal = D(2000), D(20)
nispi, amv, mv = paket * 100 * p(60), paket * dal * D("3.50"), paket * D("2.00")
H[3] = (
    max(nispi, amv) + mv,
    {
        "düşük seçilmiş + MV": min(nispi, amv) + mv,
        "MV yok": max(nispi, amv),
        "MV dal başına": max(nispi, amv) + paket * dal * D("2.00"),
        "üçü toplam": nispi + amv + mv,
    },
    tl,
)
# 4: Viski — AMV = litre × AMV × derece / 100
litre = D(600) * 70 / 100
nispi, amv = D(240000) * p(50), litre * 800 * D(40) / 100
H[4] = (
    max(nispi, amv),
    {
        "nispi": nispi,
        "toplam": nispi + amv,
        "alkol oranı yok": litre * 800,
        "şişe başına": D(600) * 800,
    },
    tl,
)
# 5: Sigara 25'li — maktu vergi oranlanır
paket, dal = D(1000), D(25)
nispi, amv = paket * 120 * p(60), paket * dal * D("2.50")
mv = paket * D("4.00") * dal / 20
H[5] = (
    max(nispi, amv) + mv,
    {
        "düşük seçilmiş + MV": min(nispi, amv) + mv,
        "MV yok": max(nispi, amv),
        "MV oranlanmamış": max(nispi, amv) + paket * D("4.00"),
        "üçü toplam": nispi + amv + mv,
    },
    tl,
)
# 6: Makaron — AMV adet; maktu 50'li
adet = D(400) * 200
nispi, amv, mv = D(400) * 150 * p(40), adet * D("0.40"), adet / 50 * D("1.50")
H[6] = (
    max(nispi, amv) + mv,
    {
        "düşük seçilmiş + MV": min(nispi, amv) + mv,
        "MV yok": max(nispi, amv),
        "MV 20'lik ölçü": max(nispi, amv) + adet / 20 * D("1.50"),
        "üçü toplam": nispi + amv + mv,
    },
    tl,
)
# 7: Puro — AMV gram; maktu 50 gram
gram = D(500) * 100
nispi, amv, mv = D(500) * 800 * p(30), gram * D("2.00"), gram / 50 * D("6.00")
H[7] = (
    max(nispi, amv) + mv,
    {
        "düşük seçilmiş + MV": min(nispi, amv) + mv,
        "MV yok": max(nispi, amv),
        "MV kutu başına": max(nispi, amv) + D(500) * D("6.00"),
        "üçü toplam": nispi + amv + mv,
    },
    tl,
)
# 9: (I) sayılı liste — ÖTV teminata, KDV matrahına girer
gv, otv = D(200000) * p(4), D(10000) * D("3.00")
kdv = (D(200000) + gv + otv) * p(20)
kdv_otvsuz = (D(200000) + gv) * p(20)
H[9] = (
    gv + kdv,
    {
        "yalnız KDV": kdv,
        "ÖTV KDV matrahında yok": gv + kdv_otvsuz,
        "ÖTV tahsil, matrahta yok": gv + otv + kdv_otvsuz,
        "ÖTV tahsil ve matrahta": gv + otv + kdv,
    },
    tl,
)
# 10: Saat (Avro) — ambalaj kıymete; adet başı < 0,30 → minimum
adet = D(4000)
matrah = D(20000) + adet * D("0.50")
birim = matrah * p("4.5") / adet
H[10] = (
    minmax(birim, D("0.30"), D("0.80")) * adet,
    {
        "min kg": D(600) * D("0.30"),
        "ambalajsız nispi": D(20000) * p("4.5"),
        "nispi": matrah * p("4.5"),
        "max": adet * D("0.80"),
    },
    tl,
)
# 11: Saat (TL) — adet başı Avroya çevrilir; aradaysa nispi
adet, kur = D(2000), D("40.00")
nispi_tl = D(1000000) * p("4.5")
birim_eur = nispi_tl / adet / kur
assert D("0.30") <= birim_eur <= D("0.80")
H[11] = (
    minmax(birim_eur, D("0.30"), D("0.80")) * adet * kur,
    {
        "TL'ye çevrilmemiş": nispi_tl / kur,
        "min": D("0.30") * adet * kur,
        "ardiye matrahta": D(1040000) * p("4.5"),
        "TL ile kıyas → max": D("0.80") * adet * kur,
    },
    tl,
)
# 13: Altın — has = net × 750/1000; matrah = bedel − has kıymet
has_k = D(400) * D(750) / 1000 * 80
H[13] = (
    D(36000) - has_k,
    {
        "milyem yok": D(36000) - D(400) * 80,
        "brüt": D(36000) - D(420) * D("0.75") * 80,
        "has kıymet": has_k,
        "mal bedeli": D(36000),
    },
    tl,
)
# 14: Gümüş — has = net × 0,925
has_k = D(2000) * D("0.925") * D("1.20")
H[14] = (
    D(5000) - has_k,
    {
        "has kıymet": has_k,
        "milyem yok": D(5000) - D(2000) * D("1.20"),
        "brüt": D(5000) - D(2100) * D("0.925") * D("1.20"),
        "750 milyem": D(5000) - D(2000) * D("0.75") * D("1.20"),
    },
    tl,
)
# 16: Tarım payı — AB → T2; net / 100 × tutar
T1, T2 = D("85.76"), D("73.30")
H[16] = (
    D(2400) / 100 * T2,
    {
        "1.000 kg": D(2400) / 1000 * T2,
        "brüt T2": D(2600) / 100 * T2,
        "net T1": D(2400) / 100 * T1,
        "brüt T1": D(2600) / 100 * T1,
    },
    tl,
)
# 18: DFİF kabuklu fındık — (4 − 2) Cent × kg × kur
kg, kur = D(20000), D("40.00")
H[18] = (
    kg * (D("0.04") - D("0.02")) * kur,
    {
        "natürel indirimi (4 Cent)": kg * (D("0.04") - D("0.04")) * kur,
        "indirim yok": kg * D("0.04") * kur,
        "iç fındık − 2 Cent": kg * (D("0.08") - D("0.02")) * kur,
        "iç fındık indirimsiz": kg * D("0.08") * kur,
    },
    tl,
)
# 19: DFİF kromlu deri 4105.10 — FOB × %20
fob, kur = D(50000), D("40.00")
H[19] = (
    fob * kur * p(20),
    {
        "kur yok": fob * p(20),
        "50 Cent/kg": D(15000) * D("0.50") * kur,
        "FOB + navlun": (fob + 2000) * kur * p(20),
        "CIF": (fob + 2000 + 500) * kur * p(20),
    },
    tl,
)
# 20: TEV — kullanılan girdi CIF × GB tescil tarihi satış kuru × o tarihteki GV oranı
cif_kullanilan = D(20000) * 1200 / 2000
H[20] = (
    cif_kullanilan * D("35.00") * p(6),
    {
        "alış kuru": cif_kullanilan * D("34.80") * p(6),
        "ithalat tarihi oranı": cif_kullanilan * D("35.00") * p(8),
        "tüm ithalat": D(20000) * D("35.00") * p(6),
        "ihracat FOB": D(60000) * D("35.00") * p(6),
    },
    tl,
)
# 21–22: Kısmi muafiyet — 7 ay 10 gün = 8 ay (ay kesri tam ay); aynı veri
V, ay, gun = D(200000), 7, 10
ay_tam = ay + (1 if gun else 0)
aylik = V * p(3)
H[21] = (
    ay_tam * aylik,
    {
        "bir ay": aylik,
        "kesir yok": ay * aylik,
        "gün oranı": aylik * (D(ay) + D(gun) / 30),
        "CIF üzerinden": ay_tam * D(500000) * p(3),
    },
    tl,
)
H[22] = (
    V - ay_tam * aylik,
    {
        "ödenen tutar": ay_tam * aylik,
        "gün oranı": V - aylik * (D(ay) + D(gun) / 30),
        "kesir yok": V - ay * aylik,
        "düşülmemiş": V,
    },
    tl,
)


# 24–25: Kullanılmış araç amortismanı
def amortisman(model, fatura, ithal):
    """Model ve fatura yılı aynı ya da farkı bir yıl: fatura yılından sonraki (aynıysa) / fatura yılından
    itibaren (fark 1) ilk yıl %20, sonra %10. Fark bir yıldan fazla: fatura yılından sonra her yıl %10.
    """
    if fatura - model > 1:
        yillar = range(fatura + 1, ithal + 1)
        return D(10) * len(yillar)
    bas = fatura + 1 if fatura == model else fatura
    yillar = list(range(bas, ithal + 1))
    return D(20) + D(10) * (len(yillar) - 1) if yillar else D(0)


oran = amortisman(2023, 2023, 2026)
assert oran == 40
H[24] = (
    D(30000) * (1 - p(oran)),
    {
        "her yıl %20": D(30000) * (1 - p(60)),
        "fatura yılı dahil": D(30000) * (1 - p(50)),
        "her yıl %10": D(30000) * (1 - p(30)),
        "yalnız ilk yıl": D(30000) * (1 - p(20)),
    },
    tl,
)
oran = amortisman(2021, 2023, 2026)
H[25] = (
    oran,
    {
        "yalnız ithal yılı": D(10),
        "ilk yıla %20": D(20) + 10 + 10,
        "model yılından %10": D(10) * (2026 - 2021),
        "model yılından, ilk yıl %20": D(20) + D(10) * (2026 - 2022),
    },
    yuzde,
)

hata = 0
hesap_sorulari = [i for i, q in enumerate(Q, 1) if q["kalip"] == "HESAP"]
eksik = sorted(set(hesap_sorulari) - set(H))
if eksik:
    print("Doğrulaması yazılmamış hesap sorusu:", eksik)
    hata += len(eksik)
konumlar = []
for i, (dogru, celd, bic) in sorted(H.items()):
    q = Q[i - 1]
    if q["kalip"] != "HESAP":
        print(f'{i}: HESAP kalıbı bekleniyordu ({q["kalip"]})')
        hata += 1
        continue
    beklenen = sorted([dogru] + list(celd.values()))
    siklar = q["siklar"]
    sorun = []
    if bic(dogru) != q["d"]:
        sorun.append(f'doğru {bic(dogru)} ≠ d {q["d"]}')
    if [bic(x) for x in beklenen] != siklar:
        sorun.append(f"şıklar {siklar} ≠ hesap {[bic(x) for x in beklenen]}")
    if len({bic(x) for x in beklenen}) != 5:
        sorun.append("iki hata aynı sonucu veriyor")
    if siklar.index(q["d"]) not in (1, 2, 3):
        sorun.append("doğru şık B/C/D değil")
    if bic(dogru) not in q["g"]:
        sorun.append("gerekçede doğru sonuç geçmiyor")
    for ad, v in celd.items():
        if bic(v) not in q["g"]:
            sorun.append(f"gerekçede çeldirici sonucu geçmiyor: {ad}={bic(v)}")
    durum = "TAMAM" if not sorun else "HATA: " + "; ".join(sorun)
    hata += bool(sorun)
    konumlar.append("ABCDE"[siklar.index(q["d"])])
    print(
        f'{i:2d} d={q["d"]:>9} konum={"ABCDE"[siklar.index(q["d"])]} | '
        + ", ".join(f"{k}={bic(v)}" for k, v in celd.items())
        + f" | {durum}"
    )
print("\nDoğru şık konumları:", {h: konumlar.count(h) for h in "BCD"})
print(f"Hesap sorusu: {len(H)} · hata: {hata}")
sys.exit(1 if hata else 0)
