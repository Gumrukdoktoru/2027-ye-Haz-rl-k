"""GM (Gümrük Müşavirliği) soru bankası denetimi.

GMY denetimini (gmy-deneme3/kontrol5.py) değiştirmeden içe aktarır ve GM'ye göre genişletir.

Kullanım:
  python3 kontrol_gm.py METIN_TUM veri/gm_M44.py [veri/gm_T03.py ...]

METIN_TUM: bütün bölüm metinlerinin tek düz klasörü (mevzuat NN-*.txt, tarife TNN-*.txt, hesap HNN-*.txt).

Bölüm türü sorunun `blok` alanının ilk harfinden okunur: M (mevzuat), T (tarife), H (hesaplama).
kontrol5'e göre farklar:
- Kalıp kümesine GTİP eklenir (tarife sınıflandırma sorusu). HESAP zaten vardır.
- Kökte mevzuat adı (dayanak türü):
    M → kontrol5 kuralı (Kanun | Yönetmelik | Tebliğ | Karar) ve ayrıca Genelge (Genelgesi), Talimat,
        İzahname, Tarife Cetveli, Cumhurbaşkanı Kararı.
    T → bunlara ek olarak "Genel Yorum Kuralları", "Armonize Sistem" kabul edilir.
    H → HESAP kalıbında kök hesaplanan büyüklüğü adlandırır (tutar, matrah, kıymet, değer, toplam);
        sözel H sorusunda mevzuat adı (yukarıdaki türler) ya da vergi/matrah/fon/kıymet terimi yeterlidir.
- Madde numarası denetiminde yıl/sayı biçimli karar, tebliğ ve genelge sayıları ("2009/15481", "99/13812",
  "94/6401", "2008-32/34", "2006/10895") madde numarası sayılmaz.
- Gerekçe sonundaki "(MD …)" parantezi bir kat iç parantez içerebilir ("(MD GYK 3(c); Fasıl 95 Notu)").
- Sayısal şık: yalnız sayı/para/oran ağırlıklı şık sayısal sayılır (sayıdan sonra en çok üç kelimelik birim,
  noktalı virgül/iki nokta/tire ile açıklama yok). "%6; Fon kesintisinin …" gibi metin ağırlıklı şıklar
  sayısal değildir; sirali=True şartı ve artan sıra denetimi bunlara uygulanmaz.
- Kanıt karşılaştırması: tarife metnindeki markdown italik yıldızları (*), yumuşak tire ve
  Türkçe "İ" küçültmesindeki birleşik nokta (U+0307) iki tarafta da yok sayılır.
- HESAP kalıbında gerekçe adım adım hesap içerir ("=" ya da "×").
- Gerekçe şıklara harf ya da sırayla atıf yapmaz ("A şıkkı", "son seçenek" vb.).
- Gerekçe doğru cevabı "çeldirici" diye anmaz (doğru şıkkın metni "çeldirici" geçen cümlede aranır).
- Kökte gg.aa.yyyy biçiminde tarih varsa hafta içine denk gelmelidir.
GMY dosyaları bu denetçiden geçirilmez; GMY için kontrol5.py aynen kullanılır.
"""

import datetime
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "gmy-deneme3"))
import kontrol5  # noqa: E402
from kontrol5 import (
    ALAN,
    DUZ,
    GYASAK,
    KARAR_KALIP,
    MADDE,
    TUZ,
    YAK,
    YAPAY,
    sayi,  # noqa: E402
    yukle,
)

KAL_GM = set(kontrol5.KAL) | {"GTİP"}
# kökte dayanak türü: kontrol5 türleri + Genelge/Genelgesi, Talimat, İzahname, Tarife Cetveli, Cumhurbaşkanı Kararı
DAYANAK = r"Kanun|Yönetmeli|Tebliğ|Karar|Genelge|Talimat|İzahname|Tarife Cetvel|Cumhurbaşkanı Kararı"
TARIFE_AD = DAYANAK + r"|Genel Yorum Kural|Armonize"
HESAP_KOK = r"tutar|matrah|kıymet|değer|toplam"
H_SOZEL = DAYANAK + r"|vergi|matrah|fon|kıymet|değer"
# yıl/sayı biçimli karar, tebliğ, genelge sayıları (madde numarası değildir): 2009/15481, 99/13812, 2008-32/34
YIL_SAYI = r"\b(?:\d{4}(?:-\d+)?/\d+|\d{2}/\d{3,})\b"
# gerekçe sonu: (MD …) — bir kat iç parantez serbest: (MD GYK 3(c); Fasıl 95 Notu)
MD_SON = r"\(MD (?:[^()]|\([^()]*\))*\)\s*$"
HARF_ATIF = (
    r"\b[A-E]\s*(şıkkı|şıkkın|şıkkında|şıkta|seçenek|seçeneğ)|\([A-E]\)\s*(şık|seçenek)"
    r"|son seçenek|ilk seçenek|ilk şık|son şık|birinci seçenek|ikinci seçenek|üçüncü seçenek"
    r"|dördüncü seçenek|beşinci seçenek"
)


def norm_gm(s):
    """kontrol5.norm + tarife/sunum metni toleransı (yıldız, yumuşak tire, İ'nin birleşik noktası)."""
    s = (
        unicodedata.normalize("NFC", s)
        .replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
    )
    s = s.replace("*", "").replace(chr(0xAD), "")
    s = s.lower().replace(chr(0x307), "")
    return re.sub(r"\s+", " ", s).strip()


def sayi_gm(s):
    """kontrol5.sayi, yalnız sayı/para/oran ağırlıklı şıkta.

    Sayıdan sonra kalan metin en çok üç kelimelik birim olabilir ("20.000 ABD Doları", "3 iş günü", "%18");
    noktalı virgül, iki nokta ya da tireyle açıklama eklenmiş ya da dörtten çok kelime taşıyan şık
    ("%6; Fon kesintisinin …", "20.000.000 TL – asgari üç yıl") sayısal sayılmaz (None).
    """
    n = sayi(s)
    if n is None:
        return None
    kalan = re.sub(r"^\s*(yüzde\s*)?%?\s*[\d.,]+\s*", "", s, flags=re.I)
    if re.search(r"[;:–—]|\s-\s", kalan):
        return None
    if len(re.findall(r"[^\W\d_]+", kalan)) > 3:
        return None
    return n


def tur(q):
    b = str(q.get("blok", "")).strip().upper()
    return b[:1] if b[:1] in "MTH" else "M"


_KAYNAK = {}


def kaynak_yukle(klasor):
    if klasor not in _KAYNAK:
        k = {
            f.name: norm_gm(f.read_text(encoding="utf-8"))
            for f in pathlib.Path(klasor).glob("*.txt")
        }
        _KAYNAK[klasor] = (k, " ".join(k.values()))
    return _KAYNAK[klasor]


def denetle(Q, metin_klasoru, sessiz=False):
    kaynak, hepsi = kaynak_yukle(metin_klasoru)
    hata = 0
    for i, q in enumerate(Q, 1):
        e = []
        eksik = [k for k in ALAN if k not in q]
        if eksik:
            if not sessiz:
                print(f'{i} ({q.get("_dosya")}): eksik alan {eksik}')
            hata += 1
            continue
        t = tur(q)
        siklar = q["siklar"] if q.get("sirali") else [q["d"]] + q["c"]
        if q.get("sirali"):
            if len(q["siklar"]) != 5 or q["d"] not in q["siklar"]:
                e.append("sirali: siklar 5 olmalı ve d içermeli")
            else:
                q["c"] = [s for s in q["siklar"] if s != q["d"]]
        if q["kalip"] not in KAL_GM:
            e.append("kalip?")
        if q["z"] not in {"ÇK", "K", "O", "Z", "ÇZ"}:
            e.append("zorluk?")
        if q["yakinlik"] not in YAK:
            e.append("yakinlik?")
        if not set(q["tuzak"]) <= TUZ or not q["tuzak"]:
            e.append(f'tuzak? {q["tuzak"]}')
        if not set(q["duzey"]) <= DUZ or not q["duzey"]:
            e.append(f'duzey? {q["duzey"]}')
        if len(q["c"]) != 4:
            e.append("4 çeldirici olmalı")
        if len(set(siklar)) != 5:
            e.append("tekrarlı şık")
        if len(q["yuva"]) != 4:
            e.append("yuva 4 olmalı")
        if len(q["cek"].split()) > 25:
            e.append("çekirdek >25 kelime")
        metin = re.sub(YIL_SAYI, " ", " ".join(q["kok"] + siklar))
        if re.search(MADDE, metin, re.I):
            e.append("kökte/şıkta madde-fıkra-bent no")
        if re.search(r"\b(hepsi|hiçbiri)\b", " ".join(siklar), re.I):
            e.append("yasak şık hepsi/hiçbiri")
        if re.search(YAPAY, " ".join(q["kok"]), re.I):
            e.append("yapay niteleme kökte")
        if re.search(GYASAK, q["g"], re.I):
            e.append("gerekçede yasak ifade")
        if not re.search(MD_SON, q["g"].strip()):
            e.append("gerekçe '(MD …)' ile bitmeli")
        if not re.search(r"Bu nedenle doğru cevap '.+' seçeneğidir\.", q["g"]):
            e.append("gerekçe \"Bu nedenle doğru cevap '<d>' seçeneğidir.\" içermeli")
        elif (
            f"'{q['d']}' seçeneğidir" not in q["g"]
            and f"'{q['d'].rstrip('.')}' seçeneğidir" not in q["g"]
        ):
            e.append("gerekçedeki alıntı d ile aynı değil")
        kok = " ".join(q["kok"])
        # kökte mevzuat adı (bölüm türüne göre)
        if t == "M" and not re.search(DAYANAK, kok):
            e.append("kökte mevzuat adı yok")
        if t == "T" and not re.search(TARIFE_AD, kok):
            e.append(
                'tarife sorusunda kökte "Türk Gümrük Tarife Cetveli" / Genel Yorum Kuralları yok'
            )
        if t == "H":
            if q["kalip"] == "HESAP" and not re.search(HESAP_KOK, kok, re.I):
                e.append("hesap kökü hesaplanan büyüklüğü adlandırmıyor")
            if q["kalip"] != "HESAP" and not re.search(H_SOZEL, kok, re.I):
                e.append("sözel hesap bölümü sorusunda kökte mevzuat/terim yok")
        if (
            re.search(r"2009/15481|Bazı Maddelerinin Uygulanması", q["madde"])
            and KARAR_KALIP not in kok
        ):
            e.append("Karar dayanaklı soruda kurum kalıbı yok")
        if re.match(
            r"^[^.?]{0,80}(göre|uyarınca),? aşağıdakilerden hangisi (doğrudur|yanlıştır)\?$",
            q["kok"][0].strip(),
        ):
            e.append("bağlamsız genel kök")
        onc = [l for l in q["kok"] if re.match(r"^(I|II|III|IV|V)\.\s", l.strip())]
        if q["kalip"] == "ÖNERMELİ" and len(onc) < 3:
            e.append("önermeli en az 3 önerme")
        nums = [sayi_gm(s) for s in siklar]
        if q.get("sirali") and all(n is not None for n in nums):
            if nums != sorted(nums):
                e.append("sayısal şıklar artan sırada değil")
            if q["siklar"].index(q["d"]) not in (1, 2, 3):
                e.append("sayısal doğru şık B/C/D olmalı")
        elif all(n is not None for n in nums):
            e.append("sayısal şıklı soru sirali=True olmalı")
        # GM ek kuralları
        if q["kalip"] == "HESAP" and not re.search(r"[=×]", q["g"]):
            e.append("hesap gerekçesinde adım adım hesap yok (= / ×)")
        if re.search(HARF_ATIF, q["g"], re.I):
            e.append("gerekçe şıkka harf/sıra ile atıf yapıyor")
        bas = norm_gm(q["d"])[:30]
        for cumle in re.split(r"(?<=[.!?])\s+", q["g"]):
            if (
                "çeldirici" in cumle.lower()
                and bas
                and bas in norm_gm(cumle)
                and "doğru cevap" not in cumle
            ):
                e.append('gerekçe doğru cevabı "çeldirici" diye anıyor olabilir')
                break
        for g_, a_, y_ in re.findall(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b", kok):
            try:
                if datetime.date(int(y_), int(a_), int(g_)).weekday() >= 5:
                    e.append(f"kökteki tarih hafta sonu: {g_}.{a_}.{y_}")
            except ValueError:
                e.append(f"geçersiz tarih: {g_}.{a_}.{y_}")
        # kanıt: her alıntı kaynakta birebir
        for parca in q["kanit"].split(" || "):
            if "|" not in parca:
                e.append('kanit "dosya | alıntı" biçiminde olmalı')
                continue
            dosya, alinti = [x.strip() for x in parca.split("|", 1)]
            govde = kaynak.get(dosya, hepsi)
            if dosya not in kaynak:
                e.append(f"kanıt dosyası yok: {dosya}")
            parcalar = [
                p.strip(" .…;,")
                for p in re.split(r"\.\.\.|…", norm_gm(alinti))
                if len(p.strip()) > 12
            ]
            if not parcalar or not all(p in govde for p in parcalar):
                eks = [p for p in parcalar if p not in govde]
                e.append(
                    f"kanıt alıntısı kaynakta birebir yok: {(eks[0] if eks else alinti)[:70]}…"
                )
        if e:
            hata += 1
            if not sessiz:
                print(f'{i} ({q.get("_dosya")}, {q.get("blok")}): ' + "; ".join(e))
    return hata


def tip(q):
    """GM sınav analizi tip etiketi (tek etiket; öncelik: hesap > GTİP > önermeli > eşleştirme > boşluk > vaka > tanım > olumsuz > klasik)."""
    k = q["kalip"]
    if k == "HESAP":
        return "hesap"
    if k == "GTİP":
        return "GTİP"
    if k == "ÖNERMELİ":
        return "önermeli"
    if k == "EŞLEŞTİRME":
        return "eşleştirme"
    if k == "BOŞLUK":
        return "boşluk"
    if q["vaka"]:
        return "vaka"
    if k in ("TANIM", "KAVRAM"):
        return "tanım"
    if q["olumsuz"]:
        return "olumsuz"
    return "klasik"


# Mevzuat bölümü tip kotası (talimat_gm.md tablosu): olumsuz, klasik, önermeli, diğer (tanım/boşluk/eşleştirme/vaka)
KOTA_M = {
    8: (3, 2, 2, 1),
    9: (4, 2, 2, 1),
    10: (4, 3, 2, 1),
    11: (4, 3, 2, 2),
    12: (5, 3, 2, 2),
    13: (5, 4, 2, 2),
    14: (6, 4, 2, 2),
    15: (6, 4, 3, 2),
    16: (6, 5, 3, 2),
    18: (7, 5, 3, 3),
}


def profil(Q):
    C = Counter
    n = len(Q)
    tipler = C(tip(q) for q in Q)
    print(f"\nSoru: {n}")
    print("Tip (GM analizi etiketi):", dict(tipler.most_common()))
    print(
        "Kökü olumsuz (bütün tipler):",
        sum(q["olumsuz"] for q in Q),
        f'(%{round(100 * sum(q["olumsuz"] for q in Q) / max(n, 1))})',
    )
    print("Yakınlık:", dict(C(q["yakinlik"] for q in Q)))
    on = [q for q in Q if q["kalip"] == "ÖNERMELİ"]
    print(
        "Önermeli:",
        len(on),
        "| doğru kombinasyonlar:",
        [q["d"] for q in on],
        "| en kapsamlı doğru:",
        sum(bool(q.get("kapsamli")) for q in on),
        "| yanlış yönlü:",
        sum(q["olumsuz"] for q in on),
    )
    print(
        "Sıralı (sabit harfli) soru:",
        sum(bool(q.get("sirali")) for q in Q),
        "| sabit konumlar:",
        "".join(
            "ABCDE"[q["siklar"].index(q["d"])] if q.get("sirali") else "·" for q in Q
        ),
    )
    print(
        "Süre soruları:",
        sum(q["kalip"] == "SÜRE" for q in Q),
        "| başlangıç anı ölçülen:",
        sum(q["baslangic"] for q in Q),
    )
    print("Tuzak:", dict(C(t for q in Q for t in q["tuzak"]).most_common()))
    print("Düzey:", dict(C(t for q in Q for t in q["duzey"]).most_common()))
    print("Profil:", dict(sorted(C(p for q in Q for p in q["profil"]).items())))
    print(
        "Eksen:",
        sorted({q["eksen"] for q in Q if q["eksen"]}),
        "| ayna:",
        [q["ayna"] for q in Q if q["ayna"]],
    )
    print("Güncellik:", [q["guncellik"] for q in Q if q["guncellik"]])
    print("Çıkmış alanı karşılayan:", sum(bool(q["cikmis"]) for q in Q))
    print("Kalıp:", dict(C(q["kalip"] for q in Q).most_common()))
    turler = {tur(q) for q in Q}
    bloklar = sorted({str(q.get("blok", "")).strip().upper() for q in Q})
    # T25 (genelgeler, BTB, karar tebliğleri) Profil A kotasıyla yazılır (talimat_gm.md bölüm 5)
    profil_a = turler == {"M"} or (turler == {"T"} and bloklar == ["T25"])
    if profil_a and n in KOTA_M:
        o, k, on_, d = KOTA_M[n]
        dig = (
            tipler["tanım"]
            + tipler["boşluk"]
            + tipler["eşleştirme"]
            + tipler["vaka"]
            + tipler["hesap"]
        )
        print(
            f"Kota (olumsuz/klasik/önermeli/diğer) hedef {o}/{k}/{on_}/{d} · gerçek "
            f'{tipler["olumsuz"]}/{tipler["klasik"]}/{tipler["önermeli"]}/{dig} (her biri ±1 serbest)'
        )
    if turler == {"T"}:
        yer = sum(q["kalip"] == "GTİP" for q in Q)
        print(
            f"Tarife: eşyanın yeri (GTİP) {yer}/{n} (%{round(100 * yer / max(n, 1))}; hedef ≈%70)"
        )
    if turler == {"H"}:
        h = sum(q["kalip"] == "HESAP" for q in Q)
        print(f"Hesaplama: sayısal {h}/{n}")


if __name__ == "__main__":
    Q = yukle(sys.argv[2:])
    h = denetle(Q, sys.argv[1])
    profil(Q)
    print("\nHatalı soru:", h)
