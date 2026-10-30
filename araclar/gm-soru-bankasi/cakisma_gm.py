#!/usr/bin/env python3
"""GM soru bankası — tekrar (çakışma) taraması: bölüm içi, bölümler arası ve GMY bankasıyla çapraz.

Kullanım:
    python3 araclar/gm-soru-bankasi/cakisma_gm.py            # tarama + özet
    python3 araclar/gm-soru-bankasi/cakisma_gm.py --liste    # GM aday çiftlerini okunabilir biçimde yazdır
    python3 araclar/gm-soru-bankasi/cakisma_gm.py --gmy      # GMY bankasıyla çapraz adayları yazdır

Veri: araclar/gm-soru-bankasi/veri/gm_<KOD>.py (Q listesi), GMY: araclar/soru-bankasi/veri/sb_XX.py.
Soru dosyalarına yazmaz; yalnız dogrulama/tekrar_adaylari.json üretir. Adayların TEKRAR / KOMŞU
sınıflandırması elle yapılır ve dogrulama/tekrar_raporu.md'ye yazılır.

GM içi ölçütler (bir çift en az birini sağlarsa aday olur):
  (a) KANIT    — kanıt alıntılarından biri normalize edildiğinde kelime kümesiyle >= %80 örtüşür
                 (kısa alıntı en az 6 kelime; örtüşme = kesişim / kısa alıntının kelime sayısı).
  (b) ÇEKİRDEK — çekirdek (cek) + doğru cevap kaba kökleri (ilk 5 harf) IDF ağırlıklı Jaccard >= 0.25;
                 ya da doğru cevap difflib >= 0.85 (en az 3 kelime) ve kök+çekirdek Jaccard >= 0.30.
  (c) MADDE    — aynı mevzuat + ortak madde numarası (tarifede ortak pozisyon) ve aynı doğru cevap
                 (normalize eşit ya da difflib >= 0.85; önermeli "I ve II" türü cevaplar hariç).
  (t) TARİFE   — T/M09 bölümlerinde aynı eşya tanımı (Jaccard >= 0.45) ve ortak pozisyon kodu
                 (doğru cevapta ya da kökte), ya da eşya tanımı Jaccard >= 0.60.
  (s) ŞIK      — 5 şıktan en az 3'ü normalize eşit ve doğru cevap aynı, ya da en az 4'ü eşit.
  (k) KÖK      — kök metni difflib >= 0.80 ve bulanık eşleşen (difflib >= 0.85) en az 3 şık,
                 ya da metin cevaplı (sayısal olmayan) sorularda doğru cevap difflib >= 0.80 ve kök difflib >= 0.60.

GMY çapraz (kök + doğru cevap Jaccard >= 0.25 olan çiftlerde):
  BİREBİR       — doğru cevap aynı (sayısal cevapta tam eşit, metinde difflib >= 0.80) ve
                  (kök difflib >= 0.60 ya da bulanık ortak şık >= 3).
  KÖK-ÇELDİRİCİ — kök difflib >= 0.80 ve bulanık ortak şık >= 3 (doğru cevap farklı olabilir).
"""

import difflib
import glob
import itertools
import json
import math
import pathlib
import re
import sys
import unicodedata
from collections import Counter

KOK = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(KOK / "araclar" / "gmy-deneme3"))
from kontrol5 import yukle  # noqa: E402

GM_VERI = KOK / "araclar" / "gm-soru-bankasi" / "veri"
GMY_VERI = KOK / "araclar" / "soru-bankasi" / "veri"
CIKTI = KOK / "araclar" / "gm-soru-bankasi" / "dogrulama" / "tekrar_adaylari.json"

DUR = set(
    """ve veya ile bir bu için olan olarak ise de da ki göre her ancak hâlinde halinde gibi daha en kadar içinde
sonra önce tarafından aşağıdakilerden aşağıdaki hangisi hangisidir hangileri hangisinde hangisine doğrudur yanlıştır
değildir sayılı ifadelerden ifade ilişkin olup olması olan olduğu edilir edilen yapılan şunlardır bilgiler
yukarıdaki cümlede boş bırakılan yere gelmelidir verilen durum durumda durumunda kapsamında uyarınca dair hakkında
türk cetveline cetvelinin pozisyonlarından pozisyonunda sınıflandırılır sınıflandırılmaz sınıflandırılması
mümkün değil""".split()
)

# norm() 'I' harfini 'ı' yapar; Roma rakamları bu yüzden [ıivx] ile yakalanır.
ONERMELI = re.compile(r"^(yalnız\s+)?[ıivx]+((\s*,\s*|\s+ve\s+|\s+)[ıivx]+)*$")
POZ = re.compile(r"\b\d{2}\.\d{2}(?:\.\d{2})*\b|\b\d{4}\.\d{2}(?:\.\d{2})*\b")
SAYISAL = re.compile(r"^[\d.,% ]+$")


def tr_lower(s):
    s = unicodedata.normalize("NFC", s)
    return s.replace("İ", "i").replace("I", "ı").lower()


def norm(s):
    s = tr_lower(s).replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^0-9a-zçğıöşüâîû%.,/ ]+", " ", s)
    s = re.sub(r"(?<!\d)[.,]|[.,](?!\d)", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def kelimeler(s):
    return [
        w for w in norm(s).split() if (len(w) > 2 or w[:1].isdigit()) and w not in DUR
    ]


def kokler(s, n=5):
    """Kaba Türkçe kök: ilk n harf (sayılar olduğu gibi)."""
    return {w if w[:1].isdigit() else w[:n] for w in kelimeler(s)}


def kanit_alintilari(q):
    out = []
    for parca in q["kanit"].split("||"):
        if "|" in parca:
            parca = parca.split("|", 1)[1]
        parca = parca.strip().strip("|").strip()
        w = set(kelimeler(parca))
        if len(w) >= 6:
            out.append((parca, frozenset(w)))
    return out


KAYNAK_ESLE = [
    (r"\b4458\b|\bgk\b|gümrük kanunu", "GK"),
    (r"gümrük yönetmeliği", "GY"),
    (r"\b5607\b|\bkmk\b|kaçakçılıkla mücadele kanunu", "5607"),
    (r"\b3065\b|kdv kanunu|katma değer vergisi kanunu", "3065"),
    (r"\b4760\b|ötv kanunu|özel tüketim vergisi kanunu", "4760"),
    (r"\b6183\b", "6183"),
    (r"2009/15481", "2009/15481"),
    (r"\b3218\b|serbest bölgeler kanunu", "3218"),
    (r"\btgtc\b|tarife cetvel", "TGTC"),
]


def madde_anahtarlari(madde):
    """{(kaynak, madde no)} ve tarifede {('TGTC', pozisyon)} kümeleri."""
    anahtar = set()
    for seg in madde.split(";"):
        s = tr_lower(seg)
        kaynak = None
        for desen, ad in KAYNAK_ESLE:
            if re.search(desen, s):
                kaynak = ad
                break
        on = re.split(r"\bmd\.|\bmadde", s)[0]
        if kaynak is None:
            kaynak = " ".join(norm(on).split()[:6])
        for grup in re.findall(
            r"\bmd\.?\s*((?:\d+(?:/\d+)?[a-z]?(?:\s*[,\-–]\s*|\s+ve\s+)?)+)", s
        ):
            nolar = [int(x) for x in re.findall(r"(?<![/\d])(\d+)", grup)]
            ar = re.search(r"(\d+)\s*[\-–]\s*(\d+)", grup)
            if ar and 0 < int(ar.group(2)) - int(ar.group(1)) <= 15:
                nolar += list(range(int(ar.group(1)), int(ar.group(2)) + 1))
            for n in nolar:
                anahtar.add((kaynak, str(n)))
        for p in POZ.findall(seg):
            anahtar.add(("TGTC", p[:5]))
        if kaynak == "TGTC":
            for m in re.findall(r"(fasıl|bölüm)\s+([0-9ivxl]+)\s+not", s):
                anahtar.add(("TGTC", f"{m[0]} {m[1]} notu"))
    return anahtar


def esya_tanimi(q):
    """Tarife sorusunda sınıflandırılan eşyanın tanımı ve sorudaki pozisyon kodları."""
    kok = " ".join(q["kok"])
    pozlar = {p[:5] for p in POZ.findall(q["d"])} | {p[:5] for p in POZ.findall(kok)}
    if POZ.fullmatch(q["d"].strip()):
        t = re.sub(
            r"türk gümrük tarife cetvel\w*\s*(ne|nin)?\s*(göre)?", " ", tr_lower(kok)
        )
        t = re.split(r"aşağıdaki (tarife )?pozisyon|hangi (tarife )?pozisyon", t)[0]
        return t, pozlar
    return q["d"], pozlar


def sik_listesi(q):
    siklar = (
        q["siklar"] if q.get("sirali") and q.get("siklar") else [q["d"]] + list(q["c"])
    )
    return [re.sub(r"\s*tl$", "", norm(s)) for s in siklar if norm(s)]


def oran(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def bulanik_ortak(a, b):
    """a'nın şıklarından b'de difflib >= 0.85 karşılığı olanların sayısı (önermelide 0)."""
    if a["_onermeli"] or b["_onermeli"]:
        return 0
    return sum(
        1 for x in a["_sikl"] if any(x == y or oran(x, y) >= 0.85 for y in b["_sikl"])
    )


def wjac(a, b, idf):
    if not a or not b:
        return 0.0
    k = sum(idf.get(w, 1.0) for w in a & b)
    u = sum(idf.get(w, 1.0) for w in a | b)
    return k / u if u else 0.0


def hazirla(Q, onek_fn):
    for q in Q:
        q["_id"] = onek_fn(q)
        q["_dn"] = re.sub(r"\s*tl$", "", norm(q["d"]))  # "170.000 TL" = "170.000"
        q["_sayisal"] = bool(SAYISAL.match(q["_dn"]))
        q["_kokn"] = norm(" ".join(q["kok"]))
        q["_cekd"] = kokler(q["cek"] + " " + q["d"])
        q["_kokd"] = kokler(" ".join(q["kok"]) + " " + q["d"])
        q["_kokcek"] = kokler(" ".join(q["kok"]) + " " + q["cek"])
        q["_kanit"] = kanit_alintilari(q)
        q["_madde"] = madde_anahtarlari(q["madde"])
        q["_onermeli"] = bool(ONERMELI.match(q["_dn"]))
        q["_sikl"] = sik_listesi(q)
        # önermeli şıklar (I ve II …) her soruda aynıdır; ortak şık sinyali sayılmaz
        q["_siklar"] = set() if q["_onermeli"] else set(q["_sikl"])
        q["_tarife"] = q["blok"].startswith("T") or q["blok"] == "M09"
        if q["_tarife"]:
            t, p = esya_tanimi(q)
            q["_esya"] = kokler(t)
            q["_poz"] = p
    return Q


def _yukle(desen, kod_re, onek):
    Q = []
    for f in sorted(glob.glob(desen)):
        m = re.search(kod_re, f)
        if not m:
            continue
        qs = yukle([f])
        for i, q in enumerate(qs, 1):
            q["_kod"] = onek + m.group(1)
            q["_no"] = i
        Q += qs
    return hazirla(Q, lambda q: f"{q['_kod']}-{q['_no']:02d}")


def gm_yukle():
    return _yukle(str(GM_VERI / "gm_*.py"), r"gm_([A-Z]\d\d)\.py$", "")


def gmy_yukle():
    return _yukle(str(GMY_VERI / "sb_[0-9][0-9].py"), r"sb_(\d\d)\.py$", "SB")


def idf_hesapla(*listeler):
    df = Counter()
    n = 0
    for Q in listeler:
        for q in Q:
            n += 1
            df.update(q["_kokd"] | q["_cekd"])
    return {w: math.log((n + 1) / (c + 1)) + 1.0 for w, c in df.items()}


def kanit_ortusme(a, b):
    en, ornek = 0.0, None
    for ta, wa in a["_kanit"]:
        for tb, wb in b["_kanit"]:
            m = min(len(wa), len(wb))
            if m < 6:
                continue
            o = len(wa & wb) / m
            if o > en:
                en, ornek = o, (ta if len(wa) <= len(wb) else tb)
    return en, ornek


def cevap_benzerligi(a, b):
    """(aynı mı, oran). Önermeli cevaplar karşılaştırılmaz; sayısal cevapta yalnız tam eşitlik geçerli."""
    if a["_onermeli"] or b["_onermeli"]:
        return False, 0.0
    if a["_dn"] == b["_dn"]:
        return True, 1.0
    if a["_sayisal"] or b["_sayisal"]:
        return False, 0.0
    r = oran(a["_dn"], b["_dn"])
    return r >= 0.85, r


def cift_olc(a, b, idf):
    olcut = []
    k_o, k_ornek = kanit_ortusme(a, b)
    if k_o >= 0.8:
        olcut.append("a")
    j_cekd = wjac(a["_cekd"], b["_cekd"], idf)
    j_kokcek = wjac(a["_kokcek"], b["_kokcek"], idf)
    d_ayni, d_oran = cevap_benzerligi(a, b)
    if j_cekd >= 0.25 or (
        len(a["_dn"].split()) >= 3 and d_oran >= 0.85 and j_kokcek >= 0.30
    ):
        olcut.append("b")
    ortak_madde = sorted(a["_madde"] & b["_madde"])
    if ortak_madde and d_ayni:
        olcut.append("c")
    j_esya = None
    if a["_tarife"] and b["_tarife"]:
        j_esya = wjac(a["_esya"], b["_esya"], idf)
        if (j_esya >= 0.45 and a["_poz"] & b["_poz"]) or j_esya >= 0.60:
            olcut.append("t")
    ortak_sik = len(a["_siklar"] & b["_siklar"])
    if ortak_sik >= 3 and (d_ayni or ortak_sik >= 4):
        olcut.append("s")
    k_oran = None
    if wjac(a["_kokd"], b["_kokd"], idf) >= 0.20:
        k_oran = oran(a["_kokn"], b["_kokn"])
        bul = bulanik_ortak(a, b) if k_oran >= 0.80 else 0
        if (k_oran >= 0.80 and bul >= 3) or (d_oran >= 0.80 and k_oran >= 0.60):
            olcut.append("k")
    return olcut, dict(
        kanit=round(k_o, 2),
        kanit_ornek=k_ornek,
        cekd=round(j_cekd, 2),
        kokcek=round(j_kokcek, 2),
        d_oran=round(d_oran, 2),
        kok_oran=None if k_oran is None else round(k_oran, 2),
        ortak_madde=[" ".join(m) for m in ortak_madde],
        esya=None if j_esya is None else round(j_esya, 2),
        ortak_sik=ortak_sik,
    )


def gm_tara(Q, idf):
    adaylar = []
    for a, b in itertools.combinations(Q, 2):
        if not (a["_kokcek"] & b["_kokcek"]):  # hızlı ön eleme
            continue
        olcut, skor = cift_olc(a, b, idf)
        if olcut:
            adaylar.append(
                dict(
                    a=a["_id"],
                    b=b["_id"],
                    tur="İÇ" if a["_kod"] == b["_kod"] else "ARA",
                    olcut="".join(olcut),
                    **skor,
                )
            )
    return adaylar


def gmy_tara(Q, G, idf):
    out = []
    for a in Q:
        for b in G:
            j = wjac(a["_kokd"], b["_kokd"], idf)
            if j < 0.25:
                continue
            d_ayni, r_d = cevap_benzerligi(a, b)
            d_ayni = d_ayni or (r_d >= 0.80)
            if not d_ayni and j < 0.45:
                continue
            r_kok = oran(a["_kokn"], b["_kokn"])
            bul = bulanik_ortak(a, b)
            tur = None
            if d_ayni and (r_kok >= 0.60 or bul >= 3):
                tur = "BİREBİR"
            elif r_kok >= 0.80 and bul >= 3:
                tur = "KÖK-ÇELDİRİCİ"
            if tur:
                out.append(
                    dict(
                        gm=a["_id"],
                        gmy=b["_id"],
                        tur=tur,
                        kok_oran=round(r_kok, 2),
                        d_oran=round(r_d, 2),
                        ortak_sik=bul,
                        kokd=round(j, 2),
                    )
                )
    return out


def ozet(q, n=150):
    kok = " ".join(q["kok"])
    return (
        f"  {q['_id']} [{q['kalip']}] {q['madde']}\n"
        f"     ÇEK: {q['cek']}\n     KÖK: {kok[:n]}{'…' if len(kok) > n else ''}\n     D  : {q['d']}"
    )


def main():
    argv = sys.argv[1:]
    Q = gm_yukle()
    G = gmy_yukle()
    dizin = {q["_id"]: q for q in Q}
    gdiz = {q["_id"]: q for q in G}
    idf = idf_hesapla(Q, G)
    adaylar = gm_tara(Q, idf)
    capraz = gmy_tara(Q, G, idf)
    sayac = Counter(x["tur"] for x in adaylar)
    olc = Counter(c for x in adaylar for c in x["olcut"])
    print(f'GM: {len({q["_kod"] for q in Q})} bölüm, {len(Q)} soru; GMY: {len(G)} soru')
    print(
        f'GM aday çift: {len(adaylar)} (bölüm içi {sayac["İÇ"]}, bölümler arası {sayac["ARA"]}); '
        f"ölçüt sayıları {dict(sorted(olc.items()))}"
    )
    print(f'GMY çapraz aday: {len(capraz)} {dict(Counter(x["tur"] for x in capraz))}')
    CIKTI.parent.mkdir(parents=True, exist_ok=True)
    CIKTI.write_text(
        json.dumps(dict(gm=adaylar, gmy=capraz), ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    print("Yazıldı:", CIKTI.relative_to(KOK))
    if "--liste" in argv:
        for tur in ("ARA", "İÇ"):
            print(f"\n==================== {tur} ====================")
            for x in sorted(
                (x for x in adaylar if x["tur"] == tur), key=lambda x: (x["a"], x["b"])
            ):
                print(
                    f"\n## {x['a']} ↔ {x['b']}  ölçüt={x['olcut']} kanıt={x['kanit']} çek+d={x['cekd']} "
                    f"kök={x['kok_oran']} d={x['d_oran']} şık={x['ortak_sik']} madde={x['ortak_madde']}"
                    + (f" eşya={x['esya']}" if x["esya"] is not None else "")
                )
                print(ozet(dizin[x["a"]]))
                print(ozet(dizin[x["b"]]))
    if "--gmy" in argv:
        print("\n==================== GMY ÇAPRAZ ====================")
        for x in sorted(capraz, key=lambda x: (x["tur"], x["gm"])):
            print(
                f"\n## {x['gm']} ↔ {x['gmy']} {x['tur']} kök={x['kok_oran']} d={x['d_oran']} şık={x['ortak_sik']}"
            )
            print(ozet(dizin[x["gm"]]))
            print(ozet(gdiz[x["gmy"]]))


if __name__ == "__main__":
    main()
