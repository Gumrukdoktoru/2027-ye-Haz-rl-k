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
    1: ("KESİN DÖNÜŞ", "0–7 s", "cut", "<b>Kraft zemin:</b> solda üç koli üst üste oturur; sağda \"Kesin dönüş\" ve eğik kırmızı \"muaf mı?\"."),
    2: ("DÖRT KİŞİ", "7–26 s", "push-slide LEFT", "<b>Dört koli etiketi</b> seslendirmede sırayla yapışır: a) 24 ay, b) kamu görevlisi, c) vatandaşlığa geçen, ç) mirasçı."),
    3: ("AİLE ÜNİTESİ", "26–32 s", "crossfade", "<b>Etiketler yerinde;</b> a–c üstüne koyu kuşak \"aile ünitesi\", ç soluklaşır; altta vukuatlı nüfus kayıt örneği."),
    4: ("TAKVİM YILI", "32–46 s", "blur-crossfade", "<b>Karar ağacı:</b> kök \"≥ 24 ay\" → \"en çok 6 ay\"; takvimde 6 ay dolar, kırmızı sınır; \"≤ 45 gün = yurt dışı\"."),
    5: ("ON YILDA BEŞ", "46–55 s", "crossfade", "<b>Aynı ağaç;</b> altta \"10 yılda ≥ 5 yıl\" düğümü, kırmızı ok ve \"SÜRE ŞARTI ARANMAZ\" damgası; elektronik sistem çipi."),
    6: ("İKİNCİ KEZ", "55–62 s", "crossfade", "<b>Aynı ağaç;</b> kökün üstünde kırmızı döngü oku: \"tekrar için yeniden ≥ 24 ay\"."),
    7: ("İSTİSNALAR", "62–73 s", "push-slide LEFT", "<b>Üç etiket:</b> ikisine kırmızı \"YARARLANAMAZ\", çift uyrukluya tikli \"YARARLANIR\"."),
    8: ("GETİRME SÜRESİ", "73–87 s", "blur-crossfade", "<b>İki zaman çizgisi:</b> geliş (önce · beraber · sonra 6 ay) ve veraset ilamı → 24 ay; altta mücbir sebep notu."),
    9: ("ÜLKEDEN ÜLKEYE", "87–104 s", "push-slide LEFT", "<b>Akış:</b> kişi → (4 nüsha) kurum → (3 nüsha) gümrük; gümrük inceler; onaylı liste örneği geri kişiye."),
    10: ("MÜKERRER Mİ?", "104–114 s", "crossfade", "<b>BİLGE ekranı</b> kişi + aile ünitesini tarar; süre bandında üç parti koli; \"MÜKERRER DEĞİL\"."),
    11: ("ÜÇ SAYI", "114–122 s", "blur-crossfade", "<b>Kırmızı panel:</b> 24 · 6 · 6."),
    12: ("GÜMRÜK KOÇU", "122–127 s", "blur-crossfade", "<b>Beyaz zeminde logo</b> tek ve sakin hareketle oturur, altında @gumrukkocunuz."),
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
<title>Ev Eşyası Muafiyeti — Taslak {VERSION}</title>
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
.frame{{width:{CELL_W}px;height:{CELL_W * 9 / 16:.0f}px;position:relative;overflow:hidden;outline:1px solid #cfc8c2;background:#E6D5B8}}
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
<header><div><h1>Kullanılmış ev eşyası · <em>Taşınma</em> <span style="font-family:'Space Grotesk';font-weight:600;font-size:16px;letter-spacing:2px;color:#7a6f68">TASLAK {VERSION.upper()}</span></h1>
<p>Gümrük Koçu serisi 4. bölüm (Muafiyet Tebliği Seri No: 2, md. 10–16). Koli etiketleri, karar ağacı ve üç sayı: 24 · 6 · 6. Hareketsiz taslak — yerleşim, metin ve renkler; hareket bir sonraki adımda.</p></div>
<div class="tagline">1920×1080 · ~2:05 · 12 sahne · Cem (ElevenLabs v4)</div></header>
<main class="grid">
{"".join(cells)}
<section><div class="frame"><div class="seam">{seams}</div></div>
<div class="meta"><span>GEÇİŞ HARİTASI</span><span class="r">12 sahne</span></div>
<p class="note"><b>Ortak sahneler:</b> 2–3 aynı dört etiket, 4–6 aynı karar ağacı (yumuşak geçiş); konu değişirken sayfa sola kayar; karar ağacı, süreler ve kırmızı panel bulanık geçişle.</p></section>
</main></body></html>'''
    out = os.path.join(ROOT, "storyboard.html")
    open(out, "w").write(html)
    print("wrote", out)


if __name__ == "__main__":
    main()
