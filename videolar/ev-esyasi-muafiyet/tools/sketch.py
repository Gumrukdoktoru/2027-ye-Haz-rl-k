#!/usr/bin/env python3
"""storyboard.html — hareketsiz taslak sayfası (tools/scenes.py yerleşimlerinden)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import ROOT, W, H, RED, DARK, GROUND, FONT_FACES, css_common, frame_specs  # noqa: E402

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
CELL_W = 544
SCALE = CELL_W / W

META = {  # id: (name, time window, seam, note)
    1: ("İKİ LİSTE", "0–11 s", "cut", "<b>Liman gecesi:</b> gemi yanaşır, sağda iki kâğıt liste iner; solda \"İki liste tutmazsa…\", altta md. 237."),
    2: ("EKSİK Mİ, FAZLA MI?", "11–20 s", "crossfade", "<b>Listeler yerinde kalır;</b> kap 03 özet beyanda var listede yok → kırmızı EKSİK; kap 06 listede var özet beyanda yok → kehribar FAZLA."),
    3: ("NE KANITLANMALI?", "20–33 s", "push-slide LEFT", "<b>Boş kap yuvası;</b> dört sebep kartı seslendirmede sırayla; kum saati \"idarece belirlenecek süre\"; altta küçük TIR notu."),
    4: ("CEZA MERDİVENİ", "33–52 s", "crossfade", "<b>Yuva yerinde kalır;</b> üç basamak sırayla iner: pozisyon → fasıl en yüksek → her kap için 241/1."),
    5: ("FAZLA KAP", "52–65 s", "push-slide LEFT", "<b>Kehribar kap;</b> sağdaki şerit sırayla dolar: el konur → kamuya geçer → tasfiye → kırmızı CIF cezası."),
    6: ("DÖKME EŞYA", "65–80 s", "blur-crossfade", "<b>Yığın ve iki gösterge:</b> %3'e kadar açık bant (takibat yok), doğalgaz ürünlerinde %6; altta GY 75/7 notu."),
    7: ("KAP TAMAM", "80–87 s", "crossfade", "<b>Beş kap tiklenir,</b> \"5 = 5\"; ölçü farklı; \"TAKİBAT YOK\" damgası."),
    8: ("BELGEDEKİ MİKTAR", "87–102 s", "push-slide LEFT", "<b>Rejim beyanı kâğıdı</b> → fark özet beyan aykırılığı; md. 234'ün üstü çizilir, md. 237 kalır."),
    9: ("ÖZET BEYANSIZ EŞYA", "102–114 s", "crossfade", "<b>Listesiz kap</b> ve iki tetik; 5. sahnedeki şerit aynı yerde yeniden dolar."),
    10: ("CEZA KİMDEN?", "114–127 s", "push-slide LEFT", "<b>İki adres kartı;</b> sağdakinin altından kesik çizgiyle \"tespit edilemezse → eşyayı getiren\"."),
    11: ("KISACASI", "127–138 s", "blur-crossfade", "<b>Kırmızı panel:</b> üç satır — noksan, fazla, dökme."),
    12: ("GÜMRÜK KOÇU", "138–142 s", "blur-crossfade", "<b>Beyaz zeminde logo</b> tek ve sakin hareketle oturur, altında @gumrukkocunuz."),
}


def main():
    specs = frame_specs()
    cells = []
    for n in range(1, 13):
        s = specs[n]
        p = f"f{n:02d}"
        ground = s.get("ground", GROUND)
        prog = s.get("prog", RED)
        name, t, seam, note = META[n]
        style = (f"<style>{css_common(p, ground).replace('#root', '#' + p + '-stage').replace(FONT_FACES, '')}\n"
                 f".{p}-prog {{ background:{prog}; }}\n{s['css']}</style>")
        stage = (f'<div class="stage" id="{p}-stage"><div id="{p}-bg"></div>{s["html"]}'
                 f'<div class="{p}-prog" style="transform:scaleX({n / 12:.3f})"></div></div>')
        cells.append(f'''<section>
{style}
<div class="frame" id="frame-{n:02d}">{stage}</div>
<div class="meta"><span>{n:02d} · {name}</span><span class="r">frame-{n:02d} · {t}</span></div>
<p class="note">{note}</p>
<span class="chip">{seam}</span>
</section>''')
    seams = "".join(f'<div class="sm"><div class="smn">{n:02d}</div><div class="sms">{META[n][2]}</div></div>' for n in range(1, 13))
    html = f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Özet Beyan 237 — Taslak {VERSION}</title>
<style>
{FONT_FACES}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#ECE8E4;color:{DARK};font-family:'Libre Baskerville',Georgia,serif;padding:40px 36px 60px}}
header{{width:{3 * CELL_W + 2 * 26}px;margin:0 auto 28px;display:flex;align-items:flex-end;justify-content:space-between;gap:24px;border-bottom:3px solid {DARK};padding-bottom:16px}}
header h1{{font-family:'Shrikhand';font-weight:400;font-size:44px;line-height:1}}
header h1 em{{font-style:normal;color:{RED};display:inline-block;transform:rotate(-4deg)}}
header p{{font-size:15px;margin-top:8px;max-width:760px;line-height:1.6}}
.tagline{{font-family:'Space Grotesk';font-weight:600;font-size:12px;letter-spacing:2px;text-transform:uppercase;border:2px solid {DARK};padding:6px 10px;white-space:nowrap}}
.grid{{width:{3 * CELL_W + 2 * 26}px;margin:0 auto;display:grid;grid-template-columns:repeat(3,{CELL_W}px);gap:34px 26px}}
.frame{{width:{CELL_W}px;height:{CELL_W * 9 / 16:.0f}px;position:relative;overflow:hidden;outline:1px solid #cfc8c2;background:#0E2640}}
.stage{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform:scale({SCALE:.5f});transform-origin:0 0;overflow:hidden}}
.meta{{display:flex;justify-content:space-between;font-family:'Space Grotesk';font-weight:600;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;margin-top:10px}}
.meta .r{{color:#7a6f68}}
.note{{font-size:13px;line-height:1.6;margin-top:6px}}
.chip{{display:inline-block;margin-top:8px;font-family:'Space Grotesk';font-weight:600;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{RED};border:1.5px solid {RED};padding:3px 8px}}
.seam{{position:absolute;inset:0;display:flex;flex-wrap:wrap;gap:6px;padding:18px;align-content:center}}
.sm{{flex:1 1 70px;border:2px solid {DARK};padding:6px 4px;text-align:center;background:#fff}}
.smn{{font-family:'Shrikhand';font-size:20px;color:{RED}}}
.sms{{font-family:'Space Grotesk';font-weight:600;font-size:9px;text-transform:uppercase;letter-spacing:1px}}
</style></head><body>
<header><div><h1>Özet beyanda aykırılıklar · <em>Liman</em> <span style="font-family:'Space Grotesk';font-weight:600;font-size:16px;letter-spacing:2px;color:#7a6f68">TASLAK {VERSION.upper()}</span></h1>
<p>Gümrük Koçu serisi 3. bölüm (GK md. 237). Gece limanı: iki liste karşılaştırılır; eksik kırmızı, fazla kehribar yanar. Hareketsiz taslak — yerleşim, metin ve renkler; hareket bir sonraki adımda.</p></div>
<div class="tagline">1920×1080 · ~2:15 · 12 sahne · Cem (ElevenLabs v4)</div></header>
<main class="grid">
{"".join(cells)}
<section><div class="frame"><div class="seam">{seams}</div></div>
<div class="meta"><span>GEÇİŞ HARİTASI</span><span class="r">12 sahne</span></div>
<p class="note"><b>Ortak sahneler:</b> 1–2 aynı iki liste, 3–4 aynı boş kap yuvası, 5 ve 9 aynı sonuç şeridi (yumuşak geçiş); konu değişirken sayfa sola kayar; dökme eşya ve kırmızı panel bulanık geçişle.</p></section>
</main></body></html>'''
    out = os.path.join(ROOT, "storyboard.html")
    open(out, "w").write(html)
    print("wrote", out)


if __name__ == "__main__":
    main()
