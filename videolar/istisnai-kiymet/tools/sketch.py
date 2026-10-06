#!/usr/bin/env python3
"""storyboard.html — hareketsiz taslak sayfası (tools/scenes.py yerleşimlerinden)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import ROOT, W, H, BG, RED, DARK, LIGHT, FONT_FACES, css_common, frame_specs  # noqa: E402

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
CELL_W = 544
SCALE = CELL_W / W

META = {  # id: (name, time window, seam, note)
    1: ("KIYMET BELLİ DEĞİL", "0–7 s", "cut", "<b>Önce soru:</b> beyanname kâğıdı gelir, KIYMET hücresi kırmızı çerçevelenir ve dev \"?\" eğik iner; solda \"Kıymet / belli değil.\""),
    2: ("İSTİSNAİ KIYMETLE BEYAN", "7–17 s", "blur-crossfade", "<b>Kavram damgalanır;</b> \"talep\" sözünde ilk kutu, \"basitleştirilmiş usul\"de ok ve ikinci kutu; sağ üstte yöntem etiketi."),
    3: ("BEŞ EŞYA", "17–36 s", "push-slide LEFT", "<b>Beş kart</b> seslendirmede adı geçtikçe soldan sağa sırayla oturur; her kartın çizimi kendi sözünde belirir."),
    4: ("KOŞULLAR · SÖZLEŞME", "36–50 s", "crossfade", "<b>Kartlar yerinde kalır;</b> üstte iki satır (aranmaz / verilmez), a ve d söner, b-c-ç'ye damga basılır."),
    5: ("TESCİL", "50–57 s", "push-slide LEFT", "<b>Zaman çizgisi soldan çizilir;</b> TESCİL halkası kırmızıya döner, altına \"vergi = mevcut belgelerdeki kıymet\"."),
    6: ("26'SI AKŞAMI", "57–70 s", "crossfade", "<b>1. ay işareti</b>, sonra 2. ay günleri; 26 halkası çizilir, bayrak direği yükselir: tamamlayıcı beyan + ödeme."),
    7: ("YÜKSEK / DÜŞÜK", "70–86 s", "crossfade", "<b>Sağ üstte</b> \"yüksek → ek tahakkuk\"; altta \"düşük →\" ve üç adım, en son GK md. 211 damgası."),
    8: ("ZAMANAŞIMI", "86–92 s", "crossfade", "<b>Tescil söner;</b> 26'dan sağa kırmızı ok uzar: zamanaşımı buradan başlar."),
    9: ("MUHASEBE KAYDI", "92–114 s", "crossfade", "<b>1. ay etiketi ikiye ayrılır</b> (tahakkuk · muhasebe kaydı); (5) ve (6) kartları sırayla, 26 halkası yeniden yanar."),
    10: ("GECİKME FAİZİ", "114–129 s", "crossfade", "<b>\"Süre geçti\"</b> etiketi, sonra kırmızı ok 26'dan geriye, TESCİL'e uzanır; GK md. 241/1 damgası."),
    11: ("KISACASI", "129–138 s", "blur-crossfade", "<b>Kırmızı panel:</b> iki durak ve aradaki çizgi; altta iki kural satırı."),
    12: ("GÜMRÜK KOÇU", "138–141 s", "blur-crossfade", "<b>Logo</b> tek ve sakin hareketle oturur, altında @gumrukkocunuz."),
}


def main():
    specs = frame_specs()
    cells = []
    for n in range(1, 13):
        s = specs[n]
        p = f"f{n:02d}"
        ground = s.get("ground", BG)
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
<title>İstisnai Kıymet — Taslak {VERSION}</title>
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
.frame{{width:{CELL_W}px;height:{CELL_W * 9 / 16:.0f}px;position:relative;overflow:hidden;outline:1px solid #cfc8c2;background:{BG}}}
.stage{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform:scale({SCALE:.5f});transform-origin:0 0;overflow:hidden}}
.meta{{display:flex;justify-content:space-between;font-family:'Space Grotesk';font-weight:600;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;margin-top:10px}}
.meta .r{{color:#7a6f68}}
.note{{font-size:13px;line-height:1.6;margin-top:6px}}
.chip{{display:inline-block;margin-top:8px;font-family:'Space Grotesk';font-weight:600;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:{RED};border:1.5px solid {RED};padding:3px 8px}}
.seam{{position:absolute;inset:0;display:flex;flex-wrap:wrap;gap:6px;padding:18px;align-content:center}}
.sm{{flex:1 1 70px;border:2px solid {DARK};padding:6px 4px;text-align:center;background:{BG}}}
.smn{{font-family:'Shrikhand';font-size:20px;color:{RED}}}
.sms{{font-family:'Space Grotesk';font-weight:600;font-size:9px;text-transform:uppercase;letter-spacing:1px}}
</style></head><body>
<header><div><h1>İstisnai kıymet · <em>İki tarih arası</em> <span style="font-family:'Space Grotesk';font-weight:600;font-size:16px;letter-spacing:2px;color:#7a6f68">TASLAK {VERSION.upper()}</span></h1>
<p>Gümrük Koçu serisi 2. bölüm. Açılışta beş eşya, sonra tescilden tamamlayıcı beyana tek zaman çizgisi. Hareketsiz taslak — yerleşim, metin ve renkler; hareket bir sonraki adımda.</p></div>
<div class="tagline">1920×1080 · ~2:20 · 12 sahne · Cem (ElevenLabs v4)</div></header>
<main class="grid">
{"".join(cells)}
<section><div class="frame"><div class="seam">{seams}</div></div>
<div class="meta"><span>GEÇİŞ HARİTASI</span><span class="r">12 sahne</span></div>
<p class="note"><b>İki sahne grubu:</b> 3–4 aynı kartlar, 5–10 aynı zaman çizgisi (yumuşak geçiş); grup değişirken sayfa sola kayar; kırmızı panele giriş-çıkış bulanık geçişle.</p></section>
</main></body></html>'''
    out = os.path.join(ROOT, "storyboard.html")
    open(out, "w").write(html)
    print("wrote", out)


if __name__ == "__main__":
    main()
