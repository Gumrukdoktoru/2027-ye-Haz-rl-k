# 2021–2025 GMY gümrük sorularını (400) konuya göre sayar; çok / orta / az / hiç sınıflarını
# ve 3 × 50 soruluk karma testin konu kotalarını üretir → siniflar.json
import json, math, pathlib, collections
HERE = pathlib.Path(__file__).parent; ROOT = HERE.parent.parent
C = collections.Counter
env = [l.split('\t') for l in (ROOT / 'araclar/gmy-deneme2/cikmis_envanter.tsv').read_text(encoding='utf-8').splitlines()[1:] if l.strip()]
DUZ = {('2021', '32'): 'Geri Gelen Eşya'}          # envanterde "Taşıtlar" yazıyor, hüküm GK 168 (geri gelen eşya)
rows = [dict(yil=int(r[0]), no=int(r[1]), konu=DUZ.get((r[0], r[1]), r[2]), olculen=r[3], kaynak=r[5]) for r in env]
HIC = [  # 5 yılda hiç sorulmayan konular (sorulmayan konular analizi, kaynak dosya düzeyinde 0 soru)
    ('Uzlaşma', '50-uzlaşma.txt', 'GK 244 ve Gümrük Uzlaşma Yönetmeliği'),
    ('Taşıtların Giriş-Çıkışı ve Fazla Çalışma', '13-TAŞITLAR.txt', 'GK 33–35, GY 72–72/T, 560; 2009/15481 Karar 121–125; Seri No 74'),
    ('Sonradan Kontrol', '5-SONRADAN KONTROL.txt', 'Sonradan Kontrol ve Riskli İşlemlerin Kontrolü Yönetmeliği'),
    ('Transit Basitleştirmeleri ve İzinli Gönderici', '24-SERİ NO 5.txt|25-SERİ NO 6.txt|26-seri no 8.txt|27-seri no 14.txt', 'Transit Tebliğleri Seri No 5, 6, 8, 14'),
    ('Akaryakıt Transiti', '22-SERİ NO 3.txt', 'Transit Tebliği Seri No 3'),
    ('Kabotaj Tebliği', '14-KABOTAJ.txt', 'Kabotaj Tebliği (2013)'),
    ('Silah-Mühimmat Tahsisi', 'milli_savunma_veya_ic_guvenlik_hizmetleriyle_dogrudan_ilgili_silah_muhimmat_arac_ve_gerec_ile_sarf_malzem.txt', 'Tahsis Yönetmeliği'),
]
say = C(r['konu'] for r in rows); son = C(r['konu'] for r in rows if r['yil'] >= 2024)
yil = {k: [sum(1 for r in rows if r['konu'] == k and r['yil'] == y) for y in range(2021, 2026)] for k in say}
def sinif(n): return 'ÇOK' if n >= 10 else 'ORTA' if n >= 5 else 'AZ'
kon = [{'konu': k, 'n': n, 'yil': yil[k], 'son2': son.get(k, 0), 'sinif': sinif(n)} for k, n in say.most_common()]
kon += [{'konu': a, 'n': 0, 'yil': [0] * 5, 'son2': 0, 'sinif': 'HİÇ', 'kaynak': b, 'mevzuat': c} for a, b, c in HIC]
def dagit(pay, toplam):
    ham = {k: toplam * v for k, v in pay.items()}; tam = {k: math.floor(x) for k, x in ham.items()}
    for k in sorted(ham, key=lambda k: -(ham[k] - tam[k]))[:toplam - sum(tam.values())]: tam[k] += 1
    return tam
KOTA = {'ÇOK': 32, 'ORTA': 12, 'AZ': 5, 'HİÇ': 1}      # test başına
kota = {}
for s, t in KOTA.items():
    ks = [k for k in kon if k['sinif'] == s]
    if s == 'HİÇ':
        sec = ['Uzlaşma', 'Taşıtların Giriş-Çıkışı ve Fazla Çalışma', 'Sonradan Kontrol']; kota.update({k: 1 for k in sec}); continue
    if s == 'AZ':
        ks = sorted(ks, key=lambda k: (-k['n'], -k['son2']))[:15]; kota.update({k['konu']: 1 for k in ks}); continue
    n5 = sum(k['n'] for k in ks); n2 = sum(k['son2'] for k in ks) or 1
    w = {k['konu']: 0.4 * k['n'] / n5 + 0.6 * k['son2'] / n2 for k in ks}
    kota.update(dagit(w, 3 * t))
# Elle düzeltme: Menşe sorularının bir kısmı (EUR.1, Form A, GTS) kaynakta yok → 13 yerine 10;
# kaynağı depoda olmayan az çıkan konular (Dış Ticaret Belgeleri, İlave Gümrük Vergisi) yerine kaynaklı olanlar
kota['Menşe'] -= 3; kota['Gümrük Kıymeti'] += 1; kota['Kaçakçılık'] += 1; kota['Temel Tanımlar'] += 1
for eski, yeni in (('Dış Ticaret Belgeleri', 'Sınır Ticareti'), ('İlave Gümrük Vergisi', 'Gümrüksüz Satış')):
    kota.pop(eski, None); kota[yeni] = 1
# Test dağıtımı: her sınıfta konu birimleri sırayla 1-2-3 testlerine dağıtılır (her test 32/12/5/1)
test = {1: {}, 2: {}, 3: {}}
for s in ('ÇOK', 'ORTA', 'AZ', 'HİÇ'):
    birim = [k['konu'] for k in kon if k['sinif'] == s for _ in range(kota.get(k['konu'], 0))]
    for i, ko in enumerate(birim):
        t = i % 3 + 1; test[t][ko] = test[t].get(ko, 0) + 1
for k in kon: k['kota_3test'] = kota.get(k['konu'], 0); k['test'] = [test[t].get(k['konu'], 0) for t in (1, 2, 3)]
json.dump({'konular': kon, 'kota': kota, 'test_basina': KOTA, 'test': test}, open(HERE / 'siniflar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for s in ('ÇOK', 'ORTA', 'AZ', 'HİÇ'):
    ks = [k for k in kon if k['sinif'] == s]
    print(s, len(ks), 'konu', sum(k['n'] for k in ks), 'soru | 3 testte', sum(k['kota_3test'] for k in ks))
    for k in ks: print(f"   {k['konu']:<42} {k['n']:>3} 24-25:{k['son2']:>2}  kota:{k['kota_3test']} {k['test']}")
print({t: sum(v.values()) for t, v in test.items()})
