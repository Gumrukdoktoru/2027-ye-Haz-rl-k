"""H04 (Fark vergi, cezalar, uzlaşma, gecikme zammı) hesap sorularının bağımsız sayısal doğrulaması.

Kullanım: python3 dogrulama/H04_hesap_kontrol.py [veri/gm_H04.py]

Her hesap sorusu için veri kökteki rakamlardan yeniden hesaplanır:
- doğru cevap (GK 234 katları ve %10 oranı, GK 235 gümrüklenmiş değer, GK 237 noksan kap, uzlaşma kapsamı,
  peşin ödeme indirimi, gecikme zammı aylık/günlük formülü, GK 207 nakit teminat, GY 527 götürü teminat),
- her çeldirici (adı konmuş tipik hata).
Sonuçlar şıklardaki metinle karşılaştırılır; sıra artan olmalı, doğru şık B/C/D'de olmalıdır.
Ayrıca sözel yetki sorusundaki (11) tutar–komisyon eşleşmesi aynı kuralla yeniden kurulur.
2 ve 7'de GK 234/2'nin güncel metni (07.11.2019; ceza doğrudan vergi farkının yarısı) denetlenir: kök yürürlükteki
metne göre hesaplandığını söyler, eski "üç katın yarısı" yöntemi yalnız çeldiricidir ve gerekçe neden yanlış olduğunu açıklar.
"""

import math
import pathlib
import sys
from decimal import Decimal as D, ROUND_HALF_UP

KOK = pathlib.Path(__file__).resolve().parent.parent
yol = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else KOK / "veri" / "gm_H04.py"
ns = {}
exec(yol.read_text(encoding="utf-8"), ns)
Q = ns["Q"]


def tl(x):
    """Sayıyı şık biçimine çevirir: binlik nokta, ondalık varsa virgülle iki hane."""
    x = D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
    tam, kes = divmod(x, 1)
    s = f"{int(tam):,}".replace(",", ".")
    return s if kes == 0 else s + "," + f"{kes:.2f}"[2:]


def p(x):
    return D(str(x)) / 100


H = {}  # soru sırası (1'den) → (doğru, {çeldirici adı: değer})

# 1: GK 234/1-a — fark %5'i aşar → üç kat
fark = D(180000) - D(160000)
assert fark / D(160000) > p(5)
H[1] = (
    fark * 3,
    {
        "%10": fark * 3 * p(10),
        "yarısı": fark / 2,
        "fark kadar": fark,
        "fark + ceza": fark + fark * 3,
    },
)
# 2: GK 234/2 — DİR: vergi farkının yarısı
fark = D(240000) - D(200000)
H[2] = (
    fark / 2,
    {
        "yarı × %10": fark / 2 * p(10),
        "fark kadar": fark,
        "üç katın yarısı": fark * 3 / 2,
        "üç kat": fark * 3,
    },
)
# 3–4: Noksan kıymet (aynı veri) — fark vergiler; ceza üç kat × %10
dk = D(40000)
dgv, demy = dk * p(10), dk * p(2)
dkdv = (dk + dgv + demy) * p(20)
fv = dgv + demy + dkdv
H[3] = (
    fv,
    {
        "KDV farkı yok": dgv + demy,
        "EMY unutulmuş": dgv + (dk + dgv) * p(20),
        "EMY KDV matrahında yok": dgv + demy + (dk + dgv) * p(20),
        "EMY matrahına GV": dgv
        + (dk + dgv) * p(2)
        + (dk + dgv + (dk + dgv) * p(2)) * p(20),
    },
)
H[4] = (
    fv * 3 * p(10),
    {
        "yarı × %10": fv / 2 * p(10),
        "üç kat yok, %10": fv * p(10),
        "yarısı": fv / 2,
        "üç kat, %10 yok": fv * 3,
    },
)
# 5: Kendiliğinden bildirim, son 6 ayda tespit → %10 uygulanmaz
fark, tespit_ay_once = D(24000), 2
yuzde_on = tespit_ay_once > 6  # 6 ay içinde tespit varsa %10 hükmü uygulanmaz
H[5] = (
    fark * 3 * (p(10) if yuzde_on else 1),
    {
        "%10 uygulanmış": fark * 3 * p(10),
        "yarısı": fark / 2,
        "fark kadar": fark,
        "fark + ceza": fark * 4,
    },
)
# 6: GK 234/1-c — miktar farkı %5'i geçmez → yarısı
assert D(300) / D(10000) <= p(5)
fark = D(6000)
H[6] = (
    fark / 2,
    {
        "yarı × %10": fark / 2 * p(10),
        "fark kadar": fark,
        "üç katın yarısı": fark * 3 / 2,
        "üç kat": fark * 3,
    },
)
# 8: GK 235/1-a — gümrüklenmiş değerin dört katı
gd = D(250000) + D(100000)
H[8] = (
    gd * 4,
    {
        "%10": gd * 4 * p(10),
        "iki kat": gd * 2,
        "CIF × 4": D(250000) * 4,
        "beş kat": gd * 5,
    },
)
# 9: GK 237/1 — noksan kaplara ait gümrük vergileri (GV + KDV)
cif = D(20000) * D("40.00")
gv = cif * p(8)
kdv = (cif + gv) * p(20)
H[9] = (
    gv + kdv,
    {
        "yalnız GV": gv,
        "KDV matrahında GV yok": gv + cif * p(20),
        "iki kat": (gv + kdv) * 2,
        "CIF kadar": cif,
    },
)
# 10: Uzlaşma kapsamı — ek tahakkuk + ceza; takip edilmeyen mali yük ve kaçakçılık hariç
vergi, ceza, mali_yuk, kacak = D(60000), D(180000), D(12000), D(90000)
H[10] = (
    vergi + ceza,
    {
        "yalnız ceza": ceza,
        "mali yük dahil": vergi + ceza + mali_yuk,
        "kaçakçılık dahil": vergi + ceza + kacak,
        "hepsi": vergi + ceza + mali_yuk + kacak,
    },
)
# 12: Uzlaşılan cezada peşin ödeme indirimi yok; diğerinde %25
uz, digr = D(60000), D(40000)
ind = 1 - p(25)
H[12] = (
    uz + digr * ind,
    {
        "ikisine indirim": uz * ind + digr * ind,
        "yalnız uzlaşılana": uz * ind + digr,
        "indirim yok": uz + digr,
        "uzlaşma öncesi": D(80000) + digr,
    },
)
# 14: Gecikme zammı — aylık + günlük esas; cezaya uygulanmaz
v, c_, o, ay, gun = D(50000), D(150000), p(4), 3, 12


def gz(t, ay, gun):
    return t * o * ay + t * o / 30 * gun


H[14] = (
    gz(v, ay, gun),
    {
        "kesir yok": gz(v, ay, 0),
        "kesir tam ay": gz(v, ay + 1, 0),
        "ceza dahil": gz(v + c_, ay, gun),
        "ceza dahil, tam ay": gz(v + c_, ay + 1, 0),
    },
)
# 15: GK 207 — şartlı muafiyet; nakit teminat hariç; tescilden başlar
vergi, nakit, mektup, oran, sure, ihlal = D(120000), D(30000), D(30000), p(3), 5, 3
H[15] = (
    (vergi - nakit) * oran * sure,
    {
        "yalnız mektup": mektup * oran * sure,
        "ihlalden başlatılmış": (vergi - nakit) * oran * (sure - ihlal),
        "yalnız teminatsız": (vergi - nakit - mektup) * oran * sure,
        "nakit düşülmemiş": vergi * oran * sure,
    },
)


# 16: GY 527 — götürü teminat; %75 yalnız 5 ve üzeri antrepoda
def goturu(olcu, birim, tamamla=True, ilk_dilim_sayilir=False):
    """birim: 'm2' (ilk 1.000, dilim 1.000) ya da 'm3' (ilk 2.000, dilim 2.000)."""
    ilk = 1000 if birim == "m2" else 2000
    if ilk_dilim_sayilir:
        dilim = math.ceil(olcu / ilk)
    else:
        artis = max(0, olcu - ilk)
        dilim = math.ceil(artis / ilk) if tamamla else artis // ilk
    return D(3000000) + D(1000000) * dilim


A = [(900, "m2"), (3200, "m2"), (15000, "m3"), (7400, "m2")]
top = sum(goturu(o_, b) for o_, b in A)
assert len(A) < 5  # %75 indirimi uygulanmaz
assert all(goturu(o_, b) <= 40000000 for o_, b in A)
H[16] = (
    top,
    {
        "%75 uygulanmış": top * p(75),
        "kesir tamamlanmamış": sum(goturu(o_, b, tamamla=False) for o_, b in A),
        "ilk dilim de bölünmüş": sum(
            goturu(o_, b, ilk_dilim_sayilir=True) for o_, b in A
        ),
        "m³ m² gibi": sum(goturu(o_, "m2") for o_, _ in A),
    },
)

hata = 0
hesap_sorulari = [i for i, q in enumerate(Q, 1) if q["kalip"] == "HESAP"]
eksik = sorted(set(hesap_sorulari) - set(H))
if eksik:
    print("Doğrulaması yazılmamış hesap sorusu:", eksik)
    hata += len(eksik)
konumlar = []
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
    for ad, val in celd.items():
        if tl(val) not in q["g"]:
            sorun.append(f"gerekçede çeldirici sonucu geçmiyor: {ad}={tl(val)}")
    durum = "TAMAM" if not sorun else "HATA: " + "; ".join(sorun)
    hata += bool(sorun)
    konumlar.append("ABCDE"[siklar.index(q["d"])])
    print(
        f'{i:2d} d={q["d"]:>11} konum={"ABCDE"[siklar.index(q["d"])]} | '
        + ", ".join(f"{k}={tl(val)}" for k, val in celd.items())
        + f" | {durum}"
    )

# 11 (sözel, YETKİ): komisyon ve tutar aynı kuralla — vergi + bağlı ceza; fer'i ve usulsüzlük ayrı
q = Q[10]
esas = D(1600000) + D(4800000)
komisyon = (
    "Gümrük ve Dış Ticaret Bölge Müdürlüğü Uzlaşma Komisyonu"
    if esas <= 7000000
    else "Merkezi Uzlaşma Komisyonu"
)
beklenen_d = f"{komisyon} – {tl(esas)} TL"
yanlis = {
    "yalnız vergi": D(1600000),
    "faiz dahil": esas + 900000,
    "faiz + usulsüzlük": esas + 900000 + 50000,
    "faiz vergiye, ceza ayrı": D(1600000) + 900000,
}
s11 = []
if q["kalip"] != "YETKİ" or q["d"] != beklenen_d:
    s11.append(f"11: d {q['d']} ≠ {beklenen_d}")
for ad, val in yanlis.items():
    if not any(f"– {tl(val)} TL" in s for s in q["c"]):
        s11.append(f"11: çeldiricide {ad}={tl(val)} yok")
    if tl(val) not in q["g"]:
        s11.append(f"11: gerekçede {ad}={tl(val)} yok")
hata += len(s11)
print("11 (YETKİ)", beklenen_d, "|", "TAMAM" if not s11 else "; ".join(s11))

# 2 ve 7: GK 234/2'nin güncel metni (07.11.2019) — ceza doğrudan vergi farkının yarısı.
# Kök güncel metne göre hesaplandığını açıkça söylemeli; eski "üç katın yarısı" yöntemi yalnız çeldiricidir
# ve gerekçe neden yanlış olduğunu açıklamalıdır.
s_guncel = []
q2, q7 = Q[1], Q[6]
kok2, kok7 = " ".join(q2["kok"]), " ".join(q7["kok"])
if "07.11.2019" not in kok2 or "yürürlükteki" not in kok2:
    s_guncel.append(
        "2: kökte güncel (07.11.2019 sonrası, yürürlükteki) metin belirtilmemiş"
    )
if tl(D(240000 - 200000) * 3 / 2) not in q2["siklar"]:
    s_guncel.append("2: eski yöntem (üç katın yarısı) çeldiricisi yok")
if (
    "yürürlükteki metne uymaz" not in q2["g"]
    or "doğrudan vergi farkının yarısına" not in q2["g"]
):
    s_guncel.append("2: gerekçe eski yöntemin neden yanlış olduğunu söylemiyor")
if "07.11.2019" not in kok7 or "yürürlükteki" not in kok7:
    s_guncel.append(
        "7: kökte güncel (07.11.2019 sonrası, yürürlükteki) metin belirtilmemiş"
    )
if not any(c.endswith("– vergi farkının yarısı") for c in q7["c"]):
    s_guncel.append(
        "7: DİR/GKAİR – vergi farkının yarısı (doğru eşleştirme) çeldiricisi yok"
    )
if "eski usul" not in q7["g"]:
    s_guncel.append(
        "7: gerekçe eski usulün (üç katın yarısı) güncel metinde olmadığını söylemiyor"
    )
hata += len(s_guncel)
print(
    "2, 7 (GK 234/2 güncel metin)",
    "|",
    "TAMAM" if not s_guncel else "; ".join(s_guncel),
)

print("\nDoğru şık konumları:", {h: konumlar.count(h) for h in "BCD"})
print(f"Hesap sorusu: {len(H)} · hata: {hata}")
sys.exit(1 if hata else 0)
