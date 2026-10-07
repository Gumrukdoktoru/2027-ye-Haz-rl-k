"""Deneme 3 birleştirme: blok dosyalarını konu sırasına dizer, cevap harflerini dağıtır, gerekçeye harfi yazar.

Kullanım: python3 birlestir5.py METIN_KLASORU CIKTI.json batch_A.py batch_B.py ...

Harf kuralları (Prompt 5, bölüm 13):
- sirali=True sorularda harf, doğru şıkkın verilen sıradaki yeridir (sayısal şıklarda B/C/D).
- Diğer sorularda harf; art arda aynı harf olmayacak ve her harf eşit sayıda (50 soruda 10) kullanılacak biçimde dağıtılır.
"""
import json
import random
import re
import sys
from collections import Counter

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from kontrol5 import denetle, profil, yukle  # noqa: E402

L = 'ABCDE'

# Kitapçık konu sırası (Bakanlık A kitapçığı gibi bloklar hâlinde)
SIRA = ['Gümrük Kıymeti ve Vergiler', 'Gümrük Kanunu Cezaları', 'Menşe, Ticaret Politikası ve Bağlayıcı Bilgi',
        'Serbest Dolaşım, İhracat ve Geri Gelen Eşya', 'Temel Tanımlar, Beyan ve Sonradan Kontrol',
        'Ekonomik Etkili Rejimler', 'Geçici İthalat', 'Transit ve TIR',
        'Antrepo, Geçici Depolama, Serbest Bölge ve Gümrüksüz Satış', 'Kabotaj ve Sınır Ticareti',
        'Muafiyetler, Yolcu ve Posta', 'Kaçakçılık', 'Tahsilat, Teminat, Geri Verme ve İtiraz',
        'Yetkilendirilmiş Yükümlü ve Onaylanmış Kişi', 'Gümrük Müşavirliği, Temsil ve Disiplin']
# Eşleme önceliği (özelden genele); konu alanı küçük harfle aranır
ESLE = [
    (r'kaçakçılık|5607', 11), (r'yetkilendirilmiş yükümlü|\byys\b|onaylanmış kişi|oksb', 13),
    (r'müşavir|temsil|disiplin|\bygm\b', 14), (r'kabotaj|sınır ticareti', 9),
    (r'geçici ithalat', 6), (r'transit|\btır\b|\btir\b', 7),
    (r'dahilde|hariçte|gkaır|gkair|kontrol altında işleme|şartlı muafiyet|ekonomik etkili', 5),
    (r'antrepo|geçici depolama|serbest bölge|gümrüksüz|depolama', 8),
    (r'muafiyet|yolcu|posta|kargo|kumanya', 10),
    (r'menşe|ticaret politikası|ithalat rejimi|bağlayıcı|\bbtb\b|\bbmb\b|tarife', 2),
    (r'kıymet|gümrük vergileri|gümrüklenmiş', 0),
    (r'ceza|usulsüzlük|vergi kaybı', 1),
    (r'serbest dolaşım|nihai kullanım|fikri|ihracat|geri gelen', 3),
    (r'tahsil|tebliğ|teminat|faiz|geri verme|kaldırma|itiraz|uzlaşma|yükümlülük|tasfiye|ödeme|zamanaşımı', 12),
    (r'tanım|beyan|sonradan kontrol|muayene', 4),
]


def grup(q):
    k = q['konu'].replace('İ', 'i').replace('I', 'ı').lower()
    for pat, i in ESLE:
        if re.search(pat, k):
            return i
    return len(SIRA)


def harf_plan(Q, tohum):
    """Sabit harfleri koruyarak serbest sorulara harf dağıtır; olmazsa None."""
    r = random.Random(tohum)
    n = len(Q)
    sabit = {i: q['siklar'].index(q['d']) for i, q in enumerate(Q) if q.get('sirali')}
    sab_say = Counter(L[k] for k in sabit.values())
    hedef = {h: n // 5 + (1 if i < n % 5 else 0) for i, h in enumerate(L)}
    # sabit harfler hedefi aşıyorsa hedefi büyüt, fazlayı sabiti en az olan harflerden düş
    for h in L:
        while sab_say[h] > hedef[h]:
            hedef[h] += 1
            dus = min((x for x in L if hedef[x] > sab_say[x]), key=lambda x: (sab_say[x], -hedef[x]))
            hedef[dus] -= 1
    kalan = {h: hedef[h] - sab_say[h] for h in L}
    s = []
    for i in range(n):
        if i in sabit:
            h = L[sabit[i]]
            if s and s[-1] == h:
                return None
            s.append(h)
            continue
        yasak = {s[-1]} if s else set()
        if i + 1 in sabit:
            yasak.add(L[sabit[i + 1]])
        aday = [h for h in L if kalan[h] > 0 and h not in yasak]
        if not aday:
            return None
        m = max(kalan[h] for h in aday)
        aday = [h for h in aday if kalan[h] >= m - 1]
        h = r.choice(aday)
        s.append(h)
        kalan[h] -= 1
    return s


def harfle(q):
    """Gerekçedeki "doğru cevap '<metin>' seçeneğidir" ifadesini harfe çevirir."""
    g = q['g']
    for v in (q['d'], q['d'].rstrip('.')):
        for tirnak in ("'", '"'):
            kal = f"doğru cevap {tirnak}{v}{tirnak} seçeneğidir"
            if kal in g:
                return g.replace(kal, f"doğru cevap {q['harf']} seçeneğidir")
    raise ValueError(f"{q['no']}: gerekçede doğru cevap alıntısı bulunamadı")


def main():
    metin, cikti, *yollar = sys.argv[1:]
    Q = yukle(yollar)
    hata = denetle(Q, metin)
    if hata:
        sys.exit(f'Denetimden geçmeyen {hata} soru var; birleştirme durduruldu.')
    # konu sırasına diz (aynı grupta blok içi sıra korunur)
    Q = [q for _, q in sorted(enumerate(Q), key=lambda x: (grup(x[1]), x[0]))]
    plan = None
    for tohum in range(1, 5000):
        plan = harf_plan(Q, tohum)
        if plan:
            break
        # bitişik sabit harf çakışmasında aynı gruptaki bir sonraki serbest soruyla yer değiştir
        for i in range(len(Q) - 1):
            a, b = Q[i], Q[i + 1]
            if a.get('sirali') and b.get('sirali') and a['siklar'].index(a['d']) == b['siklar'].index(b['d']):
                for j in range(i + 2, len(Q)):
                    if not Q[j].get('sirali') and grup(Q[j]) == grup(b):
                        Q[i + 1], Q[j] = Q[j], Q[i + 1]
                        break
    if not plan:
        sys.exit('Harf planı kurulamadı.')
    for i, (q, h) in enumerate(zip(Q, plan), 1):
        q['no'], q['harf'], q['id'] = i, h, f'GMY3-{i:03d}'
        q['grup'] = SIRA[grup(q)] if grup(q) < len(SIRA) else 'Diğer'
        if q.get('sirali'):
            q['opts'] = list(q['siklar'])
        else:
            k = L.index(h)
            dist = list(q['c'])
            q['opts'] = [q['d'] if j == k else dist.pop(0) for j in range(5)]
        assert q['opts'][L.index(h)] == q['d']
        q['g'] = harfle(q)
    harfler = ''.join(q['harf'] for q in Q)
    assert all(harfler[i] != harfler[i + 1] for i in range(len(harfler) - 1)), 'art arda aynı harf'
    en_uzun = sum(len(q['d']) > max(len(x) for x in q['opts'] if x != q['d']) for q in Q)
    en_kisa = sum(len(q['d']) < min(len(x) for x in q['opts'] if x != q['d']) for q in Q)
    for q in Q:
        q.pop('_dosya', None)
    json.dump(Q, open(cikti, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    profil(Q)
    print('\nHarf dizisi:', harfler)
    print('Harf dağılımı:', dict(sorted(Counter(harfler).items())))
    print(f'Doğru şık tek başına en uzun: {en_uzun} | en kısa: {en_kisa} (her biri ≤ {len(Q) // 4})')
    print('Gruplar:', [(g, c) for g, c in Counter(q['grup'] for q in Q).items()])


if __name__ == '__main__':
    main()
