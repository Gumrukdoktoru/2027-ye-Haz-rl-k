"""H01 (Gümrük kıymeti hesabı) hesap sorularının bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/H01_hesap_kontrol.py [veri/gm_H01.py]

Her hesap sorusu için kökteki rakamlardan yeniden hesaplanır:
- doğru cevap (GK 24, 27, 28, 29, 30; GY 45, 51, 54, 56; KDVK 21; gözetim karşılaştırması),
- her çeldirici (adı konmuş tipik hata).
Sonuçlar şıklardaki metinle karşılaştırılır; sıra artan olmalı, doğru şık B/C/D'de olmalı,
beş değer birbirinden farklı olmalı ve doğru sonuç gerekçede geçmelidir.
"""

import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_H01.py"
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


def kdv_matrahi(kiymet, gv_orani, yurt_ici=0):
    """KDVK 21: gümrük vergisi tarhına esas kıymet + GV + tescile kadar vergilendirilmemiş giderler."""
    k = D(str(kiymet))
    return k + k * p(gv_orani) + D(str(yurt_ici))


H = {}  # soru sırası (1'den) → (doğru, {çeldirici adı: değer})

# 1–2: EXW makine (aynı veri)
kiy = D(
    40000 + 1500 + 3000 + 500 + 1200
)  # EXW + yurt dışı iç taşıma + navlun + sigorta + satış komisyonu
H[1] = (
    kiy,
    {
        "yurt dışı iç taşıma yok": kiy - 1500,
        "satış komisyonu yok": kiy - 1200,
        "satın alma komisyonu eklenmiş": kiy + 800,
        "tescil sonrası iç nakliye eklenmiş": kiy + 1000,
    },
)
H[2] = (
    kdv_matrahi(kiy, 10, 400),
    {
        "tahliye KDV matrahında yok": kdv_matrahi(kiy, 10),
        "tahliye GV matrahında": kdv_matrahi(kiy + 400, 10),
        "satın alma komisyonu kıymette": kdv_matrahi(kiy + 800, 10, 400),
        "tescil sonrası iç nakliye eklenmiş": kdv_matrahi(kiy, 10, 400 + 1000),
    },
)
# 4: CFR tişört + sigorta + marka lisansı
sb = D(2000) * 6
kiy = sb + 300 + D(2000) * 1
H[4] = (
    kiy,
    {
        "CFR bedel olduğu gibi": sb,
        "lisans yok": sb + 300,
        "sigorta yok": sb + 2000,
        "dağıtım hakkı eklenmiş": kiy + 1500,
    },
)
# 5: ton başına bedel ve navlun, satış kuru
usd = D(25) * 800 + D(25) * 40 + 150
H[5] = (
    usd * D("32.00"),
    {
        "navlun yok": (usd - 1000) * 32,
        "navlun ton başına çarpılmamış": (usd - 1000 + 40) * 32,
        "tahliye eklenmiş": (usd + 200) * 32,
        "ardiye eklenmiş": (usd + 300) * 32,
    },
)
# 6: emsal navlun %10 / sigorta %3 + aracılık komisyonu, döviz satış kuru
fob = D(30000)
usd = fob + fob * p(10) + fob * p(3) + 600
H[6] = (
    usd * D("34.20"),
    {
        "sigorta yok": (usd - fob * p(3)) * D("34.20"),
        "aracılık komisyonu yok": (usd - 600) * D("34.20"),
        "döviz alış kuru": usd * D("34.00"),
        "sigorta FOB+navlun üzerinden": (
            fob + fob * p(10) + (fob + fob * p(10)) * p(3) + 600
        )
        * D("34.20"),
    },
)
# 8–9: demuraj + dahili vergi (aynı veri)
kiy = D(60000) - 1000 + 4000 + 600 + 700
H[8] = (
    kiy,
    {
        "yükleme limanı demurajı yok": kiy - 700,
        "varış sonrası demuraj kıymette": kiy + 900,
        "dahili vergi düşülmemiş": kiy + 1000,
        "dahili vergi düşülmemiş + varış demurajı": kiy + 1000 + 900,
    },
)
H[9] = (
    kdv_matrahi(kiy, 8, 900),
    {
        "GV yok": kiy + 900,
        "varış demurajı KDV matrahında yok": kdv_matrahi(kiy, 8),
        "yükleme demurajı kıymette yok": kdv_matrahi(kiy - 700, 8, 900),
        "varış demurajı GV matrahında": kdv_matrahi(kiy + 900, 8),
    },
)
# 10: miktar iskontosu düşülür, özel iskonto düşülmez, cari faiz eklenmez, kaplar eklenir
kiy = D(50000) - 2000 + 300
H[10] = (
    kiy,
    {
        "özel iskonto da düşülmüş": kiy - 1000,
        "kaplar yok": kiy - 300,
        "cari faiz eklenmiş": kiy + 1500,
        "iki iskonto da düşülmemiş": D(50000) + 300,
    },
)
# 11: cari oranı aşan faiz → tamamı eklenir
faiz = D(2100)
kiy = D(70000) + 2500 + 300 + faiz + 900
H[11] = (
    kiy,
    {
        "faiz yok": kiy - faiz,
        "yalnız oran farkı": kiy - faiz + faiz * (D(9) - 6) / 9,
        "ambalaj yok": kiy - 900,
        "pazar araştırması eklenmiş": kiy + 1200,
    },
)
# 13: hasıla payı + satıcı borcu; temettü ve reklam hariç
kiy = D(20000) + 3500 + 1000
H[13] = (
    kiy,
    {
        "hasıla yok": kiy - 3500,
        "reklam eklenmiş": kiy + 1500,
        "temettü eklenmiş": kiy + 2000,
        "temettü + reklam": kiy + 2000 + 1500,
    },
)
# 15–16: alıcının bedelsiz sağladığı unsurlar (aynı veri)
kiy = D(80000) + 3500 + 500 + 6000 + 1000 + 1500
H[15] = (
    kiy,
    {
        "yurt dışı mühendislik yok": kiy - 1500,
        "liman gideri eklenmiş": kiy + 1200,
        "Türkiye'deki plan eklenmiş": kiy + 2500,
        "liman + plan": kiy + 1200 + 2500,
    },
)
H[16] = (
    kdv_matrahi(kiy, 5, 1200) * p(20),
    {
        "kalıp yok": kdv_matrahi(kiy - 6000, 5, 1200) * p(20),
        "GV KDV matrahında yok": (kiy + 1200) * p(20),
        "liman gideri KDV matrahında yok": kdv_matrahi(kiy, 5) * p(20),
        "Türkiye'deki plan kıymette": kdv_matrahi(kiy + 2500, 5, 1200) * p(20),
    },
)
# 17: royalti (üçüncü kişiye patent, marka); çoğaltma ve ticari isim hariç
kiy = D(45000) + 3000 + 1800
H[17] = (
    kiy,
    {
        "patent yok": kiy - 3000,
        "ticari isim eklenmiş": kiy + 2500,
        "çoğaltma hakkı eklenmiş": kiy + 4000,
        "çoğaltma + ticari isim": kiy + 4000 + 2500,
    },
)
# 19: montaj düşülür, satış koşulu eğitim eklenir; bakım ve iç nakliye hariç
kiy = D(120000) - 4000 + 2500
H[19] = (
    kiy,
    {
        "eğitim yok": kiy - 2500,
        "bakım eklenmiş": kiy + 1000,
        "iç nakliye eklenmiş": kiy + 1500,
        "montaj düşülmemiş": kiy + 4000,
    },
)
# 21: antrepoda muhafaza masrafı (ayrı satır / tek satır)
kiy = D(30000) + D(20400)
H[21] = (
    kiy,
    {
        "ayrı masraf mal bedelinden düşülmüş": kiy - 600,
        "tahliye eklenmiş": kiy + 300,
        "ayrı masraf eklenmiş": kiy + 600,
        "masraf + tahliye": kiy + 600 + 300,
    },
)
# 22: taşıyıcı ortam (CD) + yazılım → KDV
cd = D(50) * 30
yaz = D(4000) * 30
gv = cd * p(5)
kdv = (cd + gv + yaz) * p(20)
H[22] = (
    kdv,
    {
        "yazılım KDV matrahında yok": (cd + gv) * p(20),
        "GV KDV matrahında yok": (cd + yaz) * p(20),
        "GV + KDV toplamı": gv + kdv,
        "yazılım GV matrahında": kdv_matrahi(cd + yaz, 5) * p(20),
    },
)
# 24–25: gözetim (aynı veri)
cif = D(400) * 20 + 1200 + 100
goz = D(400) * 5 * 5
kiy = max(cif, goz)
H[24] = (
    kiy,
    {
        "FOB": D(400) * 20,
        "karşılaştırma yok": cif,
        "gözetime navlun-sigorta eklenmiş": goz + 1200 + 100,
        "gözetim + kıymet": goz + cif,
    },
)


def gv_kdv(k):
    return k * p(10) + kdv_matrahi(k, 10) * p(20)


H[25] = (
    gv_kdv(kiy),
    {
        "yalnız KDV": kdv_matrahi(kiy, 10) * p(20),
        "karşılaştırma yok": gv_kdv(cif),
        "GV KDV matrahında yok": kiy * p(10) + kiy * p(20),
        "gözetime navlun-sigorta eklenmiş": gv_kdv(goz + 1300),
    },
)
# 27–28: Türk lirası tutarlar (aynı veri)
kiy = D(300000) + 18000 + 2000 + 6000
H[27] = (
    kiy,
    {
        "tellâliye yok": kiy - 6000,
        "iç nakliye eklenmiş": kiy + 3000,
        "ardiye eklenmiş": kiy + 4000,
        "müşavirlik eklenmiş": kiy + 5000,
    },
)
H[28] = (
    kdv_matrahi(kiy, 6, 4000),
    {
        "GV yok": kiy + 4000,
        "ardiye KDV matrahında yok": kdv_matrahi(kiy, 6),
        "ardiye GV matrahında": kdv_matrahi(kiy + 4000, 6),
        "KDV'li müşavirlik eklenmiş": kdv_matrahi(kiy, 6, 4000 + 5000),
    },
)
# 29: posta ve kargo ücretleri
kiy = D(1200) + 150 + 20
H[29] = (
    kiy,
    {
        "yalnız mal bedeli": D(1200),
        "kargo yok": kiy - 150,
        "sigorta yok": kiy - 20,
        "ilave kargo eklenmiş": kiy + 30,
    },
)
# 31–32: FCA (aynı veri), 1 Avro = 35 TL
kur = D("35.00")
eur = D(15000) + 600 + 250 + 1400 + 150
H[31] = (
    eur * kur * p(4),
    {
        "kara + yükleme yok": (eur - 600 - 250) * kur * p(4),
        "kara taşıması yok": (eur - 600) * kur * p(4),
        "yükleme-elleçleme yok": (eur - 250) * kur * p(4),
        "boşaltma eklenmiş": (eur + 350) * kur * p(4),
    },
)
bos = D(350) * kur
H[32] = (
    kdv_matrahi(eur * kur, 4, bos) * p(20),
    {
        "boşaltma KDV matrahında yok": kdv_matrahi(eur * kur, 4) * p(20),
        "yükleme-elleçleme kıymette yok": kdv_matrahi((eur - 250) * kur, 4, bos)
        * p(20),
        "boşaltma GV matrahında": kdv_matrahi((eur + 350) * kur, 4) * p(20),
        "tescil sonrası nakliye eklenmiş": kdv_matrahi(eur * kur, 4, bos + D(200) * kur)
        * p(20),
    },
)

hata = 0
hesap_sorulari = [i for i, q in enumerate(Q, 1) if q["kalip"] == "HESAP"]
eksik = sorted(set(hesap_sorulari) - set(H))
if eksik:
    print("Doğrulaması yazılmamış hesap sorusu:", eksik)
    hata += len(eksik)
konumlar = {}
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
    for v in celd.values():
        if tl(v) not in q["g"]:
            sorun.append(f"gerekçede çeldirici {tl(v)} geçmiyor")
    durum = "TAMAM" if not sorun else "HATA: " + "; ".join(sorun)
    hata += bool(sorun)
    harf = "ABCDE"[siklar.index(q["d"])]
    konumlar[harf] = konumlar.get(harf, 0) + 1
    print(
        f'{i:2d} d={q["d"]:>10} konum={harf} | '
        + ", ".join(f"{k}={tl(v)}" for k, v in celd.items())
        + f" | {durum}"
    )
print(f"\nSabit konumlar: {dict(sorted(konumlar.items()))}")
print(f"Hesap sorusu: {len(H)} · çeldirici: {4 * len(H)} · hata: {hata}")
sys.exit(1 if hata else 0)
