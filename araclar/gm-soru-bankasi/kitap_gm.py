"""GM (Gümrük Müşavirliği) Soru Bankası kitabı: iki cilt (mevzuat | tarife-hesap).

GMY kitap üreticisini (soru-bankasi/kitap.py) değiştirmeden içe aktarır; bölüm kodlarını (M01–M64, T01–T25,
H01–H05), cilt seçimini, GM kapaklarını ve GM denetimini (kontrol_gm.py) ekler.

Kullanım:
  python3 kitap_gm.py METIN_TUM BOLUMLER.json VERI_KLASORU CIKTI_ADI [SAYFA_HARITASI.json]
                      --cilt mevzuat|tarife-hesap [--cozumsuz] [--bolum M44,T03]

VERI_KLASORU: gm_<KOD>.py (soru verisi) ve gm_<KOD>_rapor.json dosyaları. Verisi olmayan bölüm atlanır.
CIKTI_ADI: CIKTI_ADI.html ve CIKTI_ADI.json (harfli, şıkları dizilmiş sorular) yazılır; çözümlü sürümde
  bölüm md'leri CIKTI_ADI_md/ klasörüne yazılır.
SAYFA_HARITASI: sayfa_gm.py çıktısı ({"M44": test sayfası, "cM44": çözüm sayfası, "EkA", "EkB"}); verilirse
  içindekiler sayfa numarasıyla basılır (iki geçişli üretim).
Kitap: ön kapak (büyük sarı "GM"), bu kitap hakkında, içindekiler (tıklanabilir), bölümler (test çift sütun,
  çözüm tek sütun), ekler, arka kapak (arka_kapak_reklam.jpg). Filigran ve üst bilgi GMY kitabıyla aynıdır.
--cozumsuz: çözümler ve set raporları basılmaz; testler + kitabın sonunda toplu cevap anahtarları (Ek A) + cevap formu (Ek B).
"""

import json
import math
import pathlib
import re
import sys
from collections import Counter

BURA = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(BURA.parent / "soru-bankasi"))
sys.path.insert(0, str(BURA))
import kitap as gmy  # noqa: E402  (GMY kitap.py; yalnız fonksiyonları kullanılır)
from kitap import (
    L,
    cozum_soru,
    e,
    gomulu,
    filigran_html,
    harf_plan,
    harfle,
    test_soru,
    tr_upper,
)  # noqa: E402
from kontrol_gm import denetle, tip, yukle  # noqa: E402

MARKA = "Gümrük Koçu - Ufuk Çetintaş"
CILTLER = {
    "mevzuat": {
        "baslik": "GM Mevzuat Soru Bankası",
        "kapak": "Mevzuat<br>Soru Bankası",
        "alt": "Gümrük müşavirliği mevzuatı",
    },
    "tarife-hesap": {
        "baslik": "GM Tarife ve Hesaplama Soru Bankası",
        "kapak": "Tarife ve Hesaplama<br>Soru Bankası",
        "alt": "Tarife sınıflandırması ve vergi, kıymet, ceza hesapları",
    },
}


def kisa(baslik, uzunluk=64):
    """Üst bilgi ve test başlığı için kısa bölüm adı (parantez içi kaynak notları atılır)."""
    m = re.match(r"^(Fasıl [\d–\-]+[a-z]?)\s*\((.*)\)\s*$", baslik)
    if m:
        ic = re.sub(r"^GTP[\w\-]+\s*·\s*", "", m.group(2))
        ic = re.sub(r"^Bölüm [IVXL]+:\s*", "", ic)
        s = f"{m.group(1)} · {ic}"
    else:
        s = re.sub(r"\s*\([^)]*\)", "", baslik).strip()
    return s if len(s) <= uzunluk else s[: uzunluk - 1].rstrip(" ,;·—-") + "…"


def dakika(kod, n):
    return round(n * (2 if kod.startswith("H") else 1.5))


def css_str(s):
    return gmy.css_str(s)


CIZGI = gmy.CIZGI
SAG_SOL = gmy.SAG_SOL


def sayfa_kurallari(kitap, cozumsuz):
    k = []
    for kod, baslik, *_ in kitap:
        k.append(
            f"@page t{kod} {{ margin: 19mm 13mm 16mm 13mm; "
            + SAG_SOL.replace("BORDER", CIZGI)
            + f"@top-center {{ content: {css_str(kisa(baslik, 58))}; font: bold 9pt 'Liberation Serif', serif; color: #000; {CIZGI} }}"
            "@bottom-center { content: counter(page); font: bold 9pt 'Liberation Serif', serif; color: #000; } }"
        )
        k.append(
            f"@page c{kod} {{ @top-center {{ content: {css_str(kisa(baslik, 46) + ' · Çözümler')}; "
            "font: bold 8pt 'Liberation Sans', Arial; color: #333; } }"
        )
    k.append(
        f"@page ekA {{ @top-center {{ content: {css_str('Cevap Anahtarları' if cozumsuz else 'Set Raporları')}; "
        "font: bold 8pt 'Liberation Sans', Arial; color: #333; } }"
    )
    k.append(
        "@page ekB { @top-center { content: 'Cevap Formu'; font: bold 8pt 'Liberation Sans', Arial; color: #333; } }"
    )
    k.append(
        "@page icindekiler { @top-center { content: 'İçindekiler'; font: bold 8pt 'Liberation Sans', Arial; color: #333; } }"
    )
    bos = "@top-left { content: none; } @top-center { content: none; } @top-right { content: none; } @bottom-center { content: none; }"
    k.append(f"@page onkapak {{ margin: 0; {bos} }}")
    k.append(f"@page arkakapak {{ margin: 0; {bos} }}")
    return "\n".join(k)


CSS_EK = """
.ok-buyuk { font-size: 150pt; line-height: .92; margin: 12mm 0 2mm; letter-spacing: -.02em; }
.ok-baslik { font-size: 34pt; }
.ic-no { width: 11mm; }
"""


def on_kapak(toplam, bolum_sayisi, cozumsuz, cilt):
    c = CILTLER[cilt]
    desen = "".join(
        '<div class="s"><i>'
        + str(i + 1)
        + "</i>"
        + "".join(f'<span class="{"d" if h == dolu else ""}">{h}</span>' for h in L)
        + "</div>"
        for i, dolu in enumerate("DACEBDAECB")
    )
    logo = gomulu("filigran_canli.png", "image/png")
    return "".join(
        [
            '<section class="onkapak"><div class="ok-desen">',
            desen,
            '</div><div class="ok-ic">',
            '<div class="ok-etiket">GÜMRÜK MÜŞAVİRLİĞİ SINAVINA HAZIRLIK</div>',
            f'<div class="ok-buyuk">GM</div><div class="ok-baslik">{c["kapak"]}</div><div class="ok-cizgi"></div>',
            f'<p class="ok-alt">{c["alt"]} · {bolum_sayisi} konu · {toplam} soru<br>Test kâğıdı düzeninde, '
            + ("cevap anahtarlı" if cozumsuz else "gerekçeli çözümlü")
            + "</p>",
            f'<div class="ok-rozet">{"CEVAP ANAHTARLI SÜRÜM" if cozumsuz else "ÇÖZÜMLÜ SÜRÜM"}</div></div>',
            f'<div class="ok-rakam"><div><b>{toplam}</b>SORU</div><div><b>{bolum_sayisi}</b>KONU</div>'
            + (
                "<div><b>1,5 dk</b>SORU BAŞINA SÜRE</div></div>"
                if cozumsuz
                else "<div><b>%100</b>GEREKÇELİ ÇÖZÜM</div></div>"
            ),
            '<div class="ok-taban">'
            + (f'<img src="{logo}" alt="">' if logo else "<span></span>"),
            '<div class="ok-marka"><b>Gümrük Koçu</b><span>Ufuk Çetintaş</span></div></div></section>',
        ]
    )


def arka_kapak(cilt):
    ilan = gomulu("arka_kapak_reklam.jpg", "image/jpeg")
    logo = gomulu("filigran_canli.png", "image/png")
    return "".join(
        [
            '<section class="arkakapak">',
            f'<img class="ak-ilan" src="{ilan}" alt="">' if ilan else "",
            '<div class="ak-taban">',
            f'<div class="ak-logo"><img src="{logo}" alt=""></div>' if logo else "",
            f'<div class="ak-yazi"><b>{CILTLER[cilt]["baslik"]}</b><span>Gümrük Koçu · Ufuk Çetintaş</span></div></div></section>',
        ]
    )


def bolum_hazirla(kod, sira, Q):
    """Harfleri dağıtır, şıkları dizer, gerekçeye harfi yazar (GMY bolum_hazirla ile aynı kural, kod kimlikli)."""

    def sabit(q):
        return q["siklar"].index(q["d"]) if q.get("sirali") else None

    for i in range(len(Q) - 1):
        if sabit(Q[i]) is not None and sabit(Q[i]) == sabit(Q[i + 1]):
            j = next((j for j in range(i + 2, len(Q)) if sabit(Q[j]) is None), None)
            if j is not None:
                Q[i + 1], Q[j] = Q[j], Q[i + 1]
    plan = None
    for tohum in range(1, 20000):
        plan = harf_plan(Q, tohum + sira * 100)
        if plan:
            break
    if not plan:
        raise SystemExit(f"{kod}: harf planı kurulamadı")
    for i, (q, h) in enumerate(zip(Q, plan), 1):
        q["no"], q["harf"], q["id"] = i, h, f"{kod}-{i:02d}"
        if q.get("sirali"):
            q["opts"] = list(q["siklar"])
        else:
            k = L.index(h)
            dist = list(q["c"])
            q["opts"] = [q["d"] if j == k else dist.pop(0) for j in range(5)]
        assert q["opts"][L.index(h)] == q["d"]
        q["g"] = harfle(q)
        q.pop("_dosya", None)
    harfler = "".join(q["harf"] for q in Q)
    assert all(
        harfler[i] != harfler[i + 1] for i in range(len(harfler) - 1)
    ), f"{kod}: art arda aynı harf"
    return Q


def profil(Q):
    n = len(Q)
    yk = Counter(q["yakinlik"] for q in Q)
    on = [q for q in Q if q["kalip"] == "ÖNERMELİ"]
    hf = Counter(q["harf"] for q in Q)
    tp = Counter(tip(q) for q in Q)
    return [
        (
            "Soru tipi (GM sınav analizi)",
            ", ".join(f"{k} {v}" for k, v in tp.most_common()),
        ),
        ("Kökü olumsuz", f"{sum(q['olumsuz'] for q in Q)} / {n}"),
        (
            "Birebir / parafraz / çıkarım",
            f"{yk['BİREBİR']} / {yk['PARAFRAZ']} / {yk['ÇIKARIM']}",
        ),
        ("Önermeli", f"{len(on)} ({', '.join(q['d'] for q in on) or '—'})"),
        (
            "Tuzaklar",
            ", ".join(
                f"{k} {v}"
                for k, v in Counter(t for q in Q for t in q["tuzak"]).most_common(6)
            ),
        ),
        ("Ayna çift", ", ".join(sorted({q["ayna"] for q in Q if q["ayna"]})) or "—"),
        ("Güncellik", "; ".join(q["guncellik"] for q in Q if q["guncellik"]) or "—"),
        ("Çıkmış bilgi alanı karşılayan", str(sum(bool(q["cikmis"]) for q in Q))),
        ("Cevap harfleri", " · ".join(f"{h} {hf[h]}" for h in L)),
    ]


def md_bolum(kod, baslik, kaynak, Q, R):
    m = [
        f"# {MARKA}",
        "",
        f"## Bölüm {kod} — {baslik}",
        "",
        f"Kaynak: {kaynak} · {len(Q)} soru",
        "",
        "### Sorular",
        "",
    ]
    for q in Q:
        m += [f"**{q['no']}-** {q['kok'][0]}", ""]
        m += [l + "  " for l in q["kok"][1:]] + ([""] if len(q["kok"]) > 1 else [])
        m += [f"{L[j]}) {o}  " for j, o in enumerate(q["opts"])] + [""]
    m += [
        "### Cevap Anahtarı",
        "",
        "| " + " | ".join(str(q["no"]) for q in Q) + " |",
        "|" + "---|" * len(Q),
        "| " + " | ".join(q["harf"] for q in Q) + " |",
        "",
        "### Çözümler",
        "",
    ]
    for q in Q:
        m += [f"*{q['madde']}*", "", f"**{q['no']}-** {q['kok'][0]}", ""]
        m += [l + "  " for l in q["kok"][1:]] + ([""] if len(q["kok"]) > 1 else [])
        m += [f"{L[j]}) {o}  " for j, o in enumerate(q["opts"])]
        m += ["", f"**Doğru Cevap:** {q['harf']}  ", f"**Gerekçe:** {q['g']}", ""]
    m += (
        ["### Set Raporu", "", "| Ölçüt | Değer |", "|---|---|"]
        + [f"| {a} | {b} |" for a, b in profil(Q)]
        + [""]
    )
    if R.get("bulunamayan"):
        m += (
            ["Metinde karşılığı bulunamayan çıkmış soru noktaları:", ""]
            + [f"- {x}" for x in R["bulunamayan"]]
            + [""]
        )
    if R.get("giremeyen"):
        m += [f"Sete giremeyen alanlar: {R['giremeyen']}", ""]
    m += ["---", f"**{MARKA}**"]
    return "\n".join(m) + "\n"


def arg_al(ad, varsayilan=None):
    if ad in sys.argv:
        i = sys.argv.index(ad)
        return sys.argv[i + 1]
    return varsayilan


def main():
    cozumsuz = "--cozumsuz" in sys.argv
    cilt = arg_al("--cilt")
    if cilt not in CILTLER:
        raise SystemExit("--cilt mevzuat | tarife-hesap verilmeli")
    secim = arg_al("--bolum")
    secim = set(secim.split(",")) if secim else None
    deger_alan = {arg_al("--cilt"), arg_al("--bolum")}
    arg = [a for a in sys.argv[1:] if not a.startswith("--") and a not in deger_alan]
    metin, bolum_yolu, veri, ad = arg[:4]
    harita = json.load(open(arg[4])) if len(arg) > 4 else {}
    veri = pathlib.Path(veri)
    BASLIK = CILTLER[cilt]["baslik"]
    bolumler = [
        b for b in json.load(open(bolum_yolu, encoding="utf-8")) if b["cilt"] == cilt
    ]
    kitap = []
    for sira, b in enumerate(bolumler, 1):
        kod = b["kod"]
        if secim and kod not in secim:
            continue
        yol = veri / f"gm_{kod}.py"
        if not yol.exists():
            continue
        Q = yukle([str(yol)])
        hata = denetle(Q, metin)
        if hata:
            raise SystemExit(f"{kod}: {hata} soru denetimden geçmedi")
        rp = veri / f"gm_{kod}_rapor.json"
        R = json.load(open(rp, encoding="utf-8")) if rp.exists() else {}
        kitap.append((kod, b["baslik"], b["dosya"], bolum_hazirla(kod, sira, Q), R))
    if not kitap:
        raise SystemExit("Bu ciltte verisi olan bölüm yok")
    toplam = sum(len(b[3]) for b in kitap)
    if not cozumsuz:
        mdk = pathlib.Path(f"{ad}_md")
        mdk.mkdir(exist_ok=True)
        for kod, baslik, kaynak, Q, R in kitap:
            (mdk / f"Bolum_{kod}.md").write_text(
                md_bolum(kod, baslik, kaynak, Q, R), encoding="utf-8"
            )
    css = gmy.CSS.replace("'Ortak Mevzuat Soru Bankası'", css_str(BASLIK)) + CSS_EK
    b = [
        f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{BASLIK}</title><style>{css}\n'
        f"{sayfa_kurallari(kitap, cozumsuz)}</style></head><body>",
        filigran_html(),
        on_kapak(toplam, len(kitap), cozumsuz, cilt),
    ]
    tarife = cilt == "tarife-hesap"
    giris = (
        "Her bölüm Gümrük Müşavirliği sınavı konularından birinin kaynak metninden hazırlanmış bir testtir; "
        "test uzunluğu konunun sınavdaki ağırlığına ve kaynağın genişliğine göre değişir. "
    )
    if tarife:
        giris += (
            "Tarife bölümlerinde soruların çoğu eşyanın tarife pozisyonunu ya da faslını sorar; doğru cevap Bölüm ve "
            "Fasıl notlarına ve Armonize Sistem İzahnamesine dayanır, çeldiriciler komşu pozisyonlardan ve notla "
            "dışlanan pozisyonlardan gelir. Hesaplama bölümleri 2021–2025 sınavlarındaki hesap kurgusunu izler; "
            "her gerekçe hesabı adım adım verir ve her yanlış şıkkın hangi hatadan doğduğunu söyler. "
        )
    else:
        giris += (
            "Sorular 2021–2025 Gümrük Müşavirliği sınavlarının soru mantığıyla yazılmıştır: kilit cümle mevzuat "
            "metninden, çeldiriciler komşu hükümlerden. Soru tiplerinin dağılımı (olumsuz kök, klasik, önermeli, "
            "tanım, boşluk, eşleştirme, vaka) bu sınavlardaki mevzuat sorularına göre ayarlanmıştır. "
        )
    giris += "Çıkmış soruların metni ve kurgusu kopyalanmamıştır."
    b.append(
        '<section class="tanitim"><h1>Bu Kitap Hakkında</h1>'
        f'<p class="giris">{giris}</p>'
        f'<div class="rakam"><div><b>{toplam}</b>soru</div><div><b>{len(kitap)}</b>konu bölümü</div>'
        f'<div><b>{"1,5–2" if tarife else "1,5"}</b>dakika / soru</div>'
        + (
            f"<div><b>{len(kitap)}</b>cevap anahtarı</div></div>"
            if cozumsuz
            else "<div><b>%100</b>gerekçeli çözüm</div></div>"
        )
        + "<h2>Kitap Nasıl Kullanılır?</h2><ul>"
    )
    sure = (
        "soru başına 1,5 dakika ayırın; hesaplama bölümlerinde 2 dakika"
        if tarife
        else "soru başına 1,5 dakika ayırın"
    )
    if cozumsuz:
        b.append(
            f"<li>Her bölüm bir testtir. Test sayfaları sınav kitapçığı gibi çift sütunludur; {sure}.</li>"
            "<li>Cevaplarınızı Ek B'deki cevap formuna işaretleyin.</li>"
            "<li>Testi bitirince cevaplarınızı Ek A'daki cevap anahtarlarıyla kontrol edin. Anahtarlar, test sırasında göz ucuyla görülmesin diye kitabın sonunda toplanmıştır.</li>"
        )
    else:
        b.append(
            f"<li>Her bölüm bir testle başlar. Test sayfaları sınav kitapçığı gibi çift sütunludur; {sure}.</li>"
            "<li>Cevaplarınızı Ek B'deki cevap formuna işaretleyin, sonra bölümün cevap anahtarıyla kontrol edin.</li>"
            "<li>Çözümler testin hemen arkasındadır ve tek sütundur. Her çözümde doğru şık, dayanak ve gerekçe vardır. Gerekçe, "
            "en güçlü tuzağın kaynaktaki yerini de söyler: yanlış yaptığınız soruda neyi neyle karıştırdığınızı görürsünüz.</li>"
            "<li>Her bölümün set profili ve kaynakta karşılığı bulunamayan çıkmış soru noktaları Ek A'dadır.</li>"
        )
    b.append(
        f'<li>İçindekiler sayfasındaki satırlar tıklanabilir; PDF\'te ilgili teste{"" if cozumsuz else " ya da çözüme"} doğrudan gidilir.</li></ul>'
        f'<div class="imza">{MARKA}</div></section>'
    )

    def ic_sat(etiket, ad_, hedef, hucreler, ek=False):
        sf = "".join(
            (
                f'<span class="ic-sf"><a href="#{h}">{harita.get(k, "")}</a></span>'
                if h
                else '<span class="ic-sf"></span>'
            )
            for h, k in hucreler
        )
        return (
            f'<div class="ic-sat"><span class="ic-no{" ek" if ek else ""}">{etiket}</span>'
            f'<span class="ic-ad"><a href="#{hedef}">{e(ad_)}</a></span><span class="ic-nokta"></span>{sf}</div>'
        )

    b.append(
        '<section class="icindekiler"><h1>İçindekiler</h1><div class="ic-bas">'
        + ("<span>SAYFA</span>" if cozumsuz else "<span>TEST</span><span>ÇÖZÜM</span>")
        + "</div>"
    )
    for kod, baslik, kaynak, Q, R in kitap:
        hucre = [(f"b{kod}", kod)] + ([] if cozumsuz else [(f"c{kod}", f"c{kod}")])
        b.append(ic_sat(kod, kisa(baslik, 90), f"b{kod}", hucre))
    for ek, ek_ad in (
        ("A", "Cevap anahtarları" if cozumsuz else "Set raporları"),
        ("B", "Cevap formu"),
    ):
        hucre = ([] if cozumsuz else [("", "")]) + [(f"ek{ek}", f"Ek{ek}")]
        b.append(ic_sat(f"Ek {ek}", ek_ad, f"ek{ek}", hucre, ek=True))
    b.append("</section>")
    for kod, baslik, kaynak, Q, R in kitap:
        b.append(f'<section class="test" id="b{kod}" style="page: t{kod}">')
        b.append(
            f'<div class="bas"><b>BÖLÜM {kod} · {e(tr_upper(kisa(baslik, 70)))}</b>'
            f"<span>{len(Q)} soru · {dakika(kod, len(Q))} dakika</span></div>"
        )
        b += [test_soru(q) for q in Q]
        b.append(
            '<div class="bitti">TEST BİTTİ. CEVAPLARINIZI KONTROL EDİNİZ.</div></section>'
        )
        if cozumsuz:
            continue
        b.append(
            f'<section class="cozum" id="c{kod}" style="page: c{kod}"><h2 class="ust">Bölüm {kod} · {e(kisa(baslik, 90))} — Cevap Anahtarı ve Çözümler</h2>'
        )
        b.append(
            '<table class="anahtar"><tr>'
            + "".join(f'<th>{q["no"]}</th>' for q in Q)
            + "</tr><tr>"
            + "".join(f'<td>{q["harf"]}</td>' for q in Q)
            + "</tr></table>"
        )
        b += [cozum_soru(q) for q in Q]
        b.append("</section>")
    if cozumsuz:
        b.append(
            '<section id="ekA" style="page: ekA"><h1>Ek A — Cevap Anahtarları</h1>'
        )
        for kod, baslik, kaynak, Q, R in kitap:
            b.append(
                f'<div class="ekanahtar"><h3>Bölüm {kod} · {e(kisa(baslik, 90))}</h3>'
                '<table class="anahtar"><tr>'
                + "".join(f'<th>{q["no"]}</th>' for q in Q)
                + "</tr><tr>"
                + "".join(f'<td>{q["harf"]}</td>' for q in Q)
                + "</tr></table></div>"
            )
        b.append("</section>")
    else:
        b.append('<section id="ekA" style="page: ekA"><h1>Ek A — Set Raporları</h1>')
        for kod, baslik, kaynak, Q, R in kitap:
            b.append(
                f'<div class="ekrapor"><h3>Bölüm {kod} · {e(kisa(baslik, 90))}</h3><table class="rapor"><tbody>'
            )
            b.append(f"<tr><td>Kaynak</td><td>{e(baslik)}</td></tr>")
            b += [f"<tr><td>{e(a)}</td><td>{e(v)}</td></tr>" for a, v in profil(Q)]
            b.append("</tbody></table>")
            if R.get("bulunamayan"):
                b.append(
                    "<p><b>Metinde karşılığı bulunamayan çıkmış soru noktaları:</b></p><ul>"
                    + "".join(f"<li>{e(x)}</li>" for x in R["bulunamayan"])
                    + "</ul>"
                )
            if R.get("giremeyen"):
                b.append(f'<p><b>Sete giremeyen alanlar:</b> {e(R["giremeyen"])}</p>')
            b.append("</div>")
        b.append("</section>")
    # Ek B: cevap formu (en uzun teste göre satır sayısı; 4 sütun)
    en_uzun = max(len(b_[3]) for b_ in kitap)
    satir = math.ceil(max(en_uzun, 20) / 4)
    b.append(
        '<section id="ekB" style="page: ekB"><h1>Ek B — Cevap Formu</h1><p>Bu sayfayı çoğaltarak her test için kullanabilirsiniz. Bölüm: ______  '
        'Adı Soyadı: ____________________  Doğru sayısı: ______</p><div class="form-izgara">'
    )
    for kol in range(4):
        b.append("<div>")
        for i in range(kol * satir + 1, kol * satir + satir + 1):
            b.append(
                f'<div class="form-sat"><span class="n">{i}</span>'
                + "".join(f'<span class="b">{h}</span>' for h in L)
                + "</div>"
            )
        b.append("</div>")
    b.append("</div></section>")
    b.append(arka_kapak(cilt))
    b.append("</body></html>")
    pathlib.Path(f"{ad}.html").write_text("\n".join(b), encoding="utf-8")
    json.dump(
        [
            {"kod": kod, "baslik": baslik, "kaynak": kaynak, "sorular": Q, "rapor": R}
            for kod, baslik, kaynak, Q, R in kitap
        ],
        open(f"{ad}.json", "w", encoding="utf-8"),
        ensure_ascii=False,
        indent=0,
    )
    print(f"{BASLIK}: {len(kitap)} bölüm, {toplam} soru → {ad}.html")
    for kod, *_r, Q, R in [(k[0], k[3], k[4]) for k in kitap]:
        print(
            f'  {kod}: harfler {"".join(q["harf"] for q in Q)}  {dict(sorted(Counter(q["harf"] for q in Q).items()))}'
        )


if __name__ == "__main__":
    main()
