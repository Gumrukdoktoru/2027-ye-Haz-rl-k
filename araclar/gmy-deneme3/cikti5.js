// Deneme 3 Word çıktısı. Kullanım: node cikti5.js set3.json notlar3.json CIKTI.docx
const fs = require('fs');
const path = require('path');
const { d, p, h1, h2, bullet, table, pb, doc, runs, NAVY, GOLD } = require(path.join(__dirname, '../karar/gk.js'));
const { Paragraph, TextRun, AlignmentType, BorderStyle } = d;

const [, , setYol, notYol, cikti] = process.argv;
const Q = JSON.parse(fs.readFileSync(setYol, 'utf8'));
const N = JSON.parse(fs.readFileSync(notYol, 'utf8'));
const L = 'ABCDE';
const MARKA = 'Gümrük Koçu - Ufuk Çetintaş';
const B = [];
const add = (...x) => x.flat().forEach(e => B.push(e));
const onerme = l => /^(I|II|III|IV|V)\.\s/.test(l.trim());

const soru = (q, cevapli) => {
  if (cevapli) add(new Paragraph({ keepNext: true, spacing: { before: 240, after: 40 }, children: [new TextRun({ text: q.madde, italics: true, color: GOLD, size: 19 })] }));
  add(new Paragraph({ keepNext: true, spacing: { before: cevapli ? 40 : 200, after: 80 }, children: [new TextRun({ text: q.no + '- ', bold: true, color: NAVY }), ...runs(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: onerme(l) ? { left: 360 } : undefined, spacing: { after: 40 }, children: runs(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: cevapli || j < 4, indent: { left: 720, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun(L[j] + ') '), ...runs(o)] })));
  if (cevapli) {
    add(new Paragraph({ keepNext: true, spacing: { before: 80, after: 40 }, children: [new TextRun({ text: 'Doğru Cevap: ', bold: true }), new TextRun({ text: q.harf, bold: true, color: NAVY })] }));
    add(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: 'Gerekçe: ', bold: true }), ...runs(q.g)] }));
  }
};

const C = arr => arr.reduce((o, k) => (o[k] = (o[k] || 0) + 1, o), {});
const n = Q.length;
const yk = C(Q.map(q => q.yakinlik));
const on = Q.filter(q => q.kalip === 'ÖNERMELİ');
const tz = Object.entries(C(Q.flatMap(q => q.tuzak))).sort((a, b) => b[1] - a[1]);
const hf = C(Q.map(q => q.harf));
const yuzde = x => `${x} (%${Math.round(100 * x / n)})`;
const profil = [
  ['Kilit cümlesi madde metninden birebir', yuzde(yk['BİREBİR'] || 0)],
  ['Parafraz', yuzde(yk['PARAFRAZ'] || 0)],
  ['Çıkarım (tek adımlı)', yuzde(yk['ÇIKARIM'] || 0)],
  ['Olumsuz kök', yuzde(Q.filter(q => q.olumsuz).length)],
  ['Önermeli', `${on.length}; doğru kombinasyonlar: ${on.map(q => q.d).join(', ')}; en kapsamlı şık doğru: ${on.filter(q => q.kapsamli).length}; yanlıştır köklü: ${on.filter(q => q.olumsuz).length}`],
  ['Vaka, uygulama, hesap', String(Q.filter(q => q.vaka).length)],
  ['Tanımdan ad / addan tanım', String(Q.filter(q => ['TANIM', 'KAVRAM'].includes(q.kalip)).length)],
  ['Boşluk doldurma ve eşleştirme', String(Q.filter(q => ['BOŞLUK', 'EŞLEŞTİRME'].includes(q.kalip)).length)],
  ['Süre sorularında başlangıç anı ölçülen', String(Q.filter(q => q.baslangic).length)],
  ['Tuzak dağılımı', tz.map(([k, v]) => `${k} ${v}`).join(', ')],
  ['Güncellik soruları', Q.filter(q => q.guncellik).map(q => `${q.no}. soru (${q.guncellik})`).join('; ')],
  ['Cevap harfi dağılımı', [...L].map(h => `${h} ${hf[h] || 0}`).join(' · ') + ' (art arda aynı harf yok)'],
];

// Kapak
const sp = k => new Paragraph({ spacing: { before: k }, children: [] });
const cover = [sp(2200),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'GMY SINAVI · GÜMRÜK MEVZUATI', bold: true, size: 24, color: GOLD })] }),
  sp(300), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: N.baslik, bold: true, size: 52, color: NAVY })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } },
    children: [new TextRun({ text: `${n} soru · ${Math.round(n * 1.5)} dakika · karışık konu · cevaplı ve gerekçeli`, size: 26, color: NAVY })] }),
  sp(3800), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: MARKA, bold: true, size: 26, color: NAVY })] })];

add(h1('Sınav Bilgileri'), table(['Alan', 'Değer'], [
  ['Soru sayısı', `${n} (gümrük mevzuatı, karışık konu)`],
  ['Süre', `${Math.round(n * 1.5)} dakika`],
  ['Hazırlama kuralı', 'GMY Sınavı Mevzuat Sorusu Hazırlama Promptu (Prompt 5)'],
  ['Çıkmış soru bilgi alanını karşılayan', `${Q.filter(q => q.cikmis).length} soru (çıkmış soruların metni ve kurgusu kopyalanmadı)`],
], [3, 7]));
add(p(''), p("Önce Bölüm A'yı süre tutarak çözün; sonra cevap anahtarı ve Bölüm B'deki gerekçelerle kontrol edin. Her sorunun yalnız bir doğru cevabı vardır."));

add(pb(), h1('BÖLÜM A — SORU KİTAPÇIĞI'));
let g = null;
for (const q of Q) { if (q.grup !== g) { g = q.grup; add(h2(g)); } soru(q, false); }
add(pb(), h1('Cevap Anahtarı'));
for (let s = 0; s < n; s += 10) { const part = Q.slice(s, s + 10); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
add(pb(), h1('BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR'));
g = null;
for (const q of Q) { if (q.grup !== g) { g = q.grup; add(h2(g)); } soru(q, true); }
add(pb(), h1('SET RAPORU'), h2('Set profili'), table(['Ölçüt', 'Değer'], profil, [4, 6]));
add(h2('Kapsanan çıkmış soru noktaları'));
Q.filter(q => q.cikmis).forEach(q => add(bullet(`${q.no}. soru (${q.konu}): ${q.cikmis}`)));
add(h2('Metinde karşılığı bulunamayan çıkmış soru noktaları'));
N.bulunamayan.forEach(x => add(bullet(x)));
add(h2('Sete giremeyen önemli soru alanları'), p(N.giremeyen));
add(h2('Üretim notu'));
N.uretim.forEach(x => add(bullet(x)));

const out = doc({ header: MARKA, footer: MARKA, cover, body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync(cikti, b); console.log('docx yazıldı:', cikti); });
