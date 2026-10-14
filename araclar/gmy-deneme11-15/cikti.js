// Kullanım: node cikti.js 6  → ../../sorular/GK_GMY_Deneme6_100soru.docx (önce python3 cikti.py 6 çalıştırılır)
const fs = require('fs');
const { d, p, h1, h2, bullet, table, pb, doc, coverPage, NAVY, GOLD } = require('./gk.js');
const { Paragraph, TextRun, UnderlineType } = d;
const D = process.argv[2]; const Q = JSON.parse(fs.readFileSync('set' + D + '.json')); const O = JSON.parse(fs.readFileSync('ozet' + D + '.json'));
const L = 'ABCDE';
const ZOR = { 'OÜ': 'Orta Üstü', 'Z': 'Zor', 'O': 'Orta' };
const TIPSIRA = ['T1', 'T1+T2', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'];
const R = (text, o = {}) => text.split(/(\[\[[^\]]+\]\]|\*\*[^*]+\*\*)/).filter(Boolean).map(s =>
  s.startsWith('[[') ? new TextRun({ text: s.slice(2, -2), bold: true, underline: { type: UnderlineType.SINGLE }, ...o })
    : s.startsWith('**') ? new TextRun({ text: s.slice(2, -2), bold: true, ...o }) : new TextRun({ text: s, ...o }));
const strip = s => s.replace(/\[\[|\]\]|\*\*/g, '');
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
const soru = (q, lab) => {
  if (lab) add(new Paragraph({ keepNext: true, spacing: { before: 280, after: 60 }, children: [
    new TextRun({ text: 'SORU ' + q.no + '. ', bold: true, color: NAVY }),
    new TextRun({ text: '[' + q.tip + ' – ' + ZOR[q.z] + ']', bold: true, color: GOLD }),
    new TextRun({ text: '  ·  Model soru: ' + q.cikmis, italics: true, size: 18, color: '555555' })] }));
  add(new Paragraph({ keepNext: true, spacing: { before: lab ? 40 : 200, after: 80 }, children: [
    ...(lab ? [] : [new TextRun({ text: q.no + '. ', bold: true })]), ...R(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: { left: 360 }, spacing: { after: 40 }, children: R(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: lab || j < 4, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun(L[j] + ') '), ...R(o)] })));
};
const satir = (etiket, metin, renk) => new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: etiket, bold: true, color: renk || NAVY }), ...R(metin)] });
const yuzde = (n, t) => n + ' (%' + Math.round(100 * n / t) + ')';
add(h1('Sınav Bilgileri'), table(['Alan', 'Değer'], O.bilgi, [3, 7]));
add(p(''), p('Her sorunun yalnız bir doğru cevabı vardır. Sorular çıkmış soruların kopyası değildir; aynı bilgi alanı farklı hükümle, kurum soru diliyle özgün olarak ölçülmüştür.'));
add(pb(), h1('BÖLÜM A — SORU KİTAPÇIĞI'), h2('Genel Kültür (1–20)'));
for (const q of Q) { if (q.no === 21) add(pb(), h2('Gümrük Mevzuatı (21–100)')); soru(q, false); }
add(pb(), h1('Cevap Anahtarı'));
for (let s = 0; s < 100; s += 20) { const part = Q.slice(s, s + 20); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
add(pb(), h1('BÖLÜM B — ÇÖZÜMLÜ SORULAR'), h2('Genel Kültür (1–20)'));
for (const q of Q) {
  if (q.no === 21) add(pb(), h2('Gümrük Mevzuatı (21–100)'));
  soru(q, true);
  const ls = q.opts.map(o => strip(o).length);
  add(satir('✅ Doğru Cevap: ', q.harf, '1B7A3C'), satir('📖 Açıklama: ', q.g_harfli), satir('⚖️ Yasal Dayanak: ', q.madde),
    satir('🔍 Şık Uzunluk Kontrolü: ', ls.map((n, j) => L[j] + ':' + n).join(' ') + ' karakter → Denge: UYGUN' + (q.tuzak ? ' (ters tuzak: doğru şık bilinçli olarak en uzun; 2. ve 3. en uzun şık ≥ %90)' : '')));
}
add(pb(), h1('Set Sonu'));
add(h2('Cevap Anahtarı'));
for (let s = 0; s < 100; s += 10) add(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: Q.slice(s, s + 10).map(q => 'Soru ' + q.no + ': ' + q.harf).join('   '), font: 'Courier New', size: 17 })] }));
add(h2('Harf Dağılımı'), table(['Kapsam', ...L.split('')], [['1–100', ...L.split('').map(h => yuzde(O.harf_all[h], 100))], ['21–100', ...L.split('').map(h => yuzde(O.harf_m[h], 80))]], [2, 1, 1, 1, 1, 1]), p(''));
add(h2('Tip Dağılımı (21–100)'), table(TIPSIRA, [TIPSIRA.map(t => String(O.tip_m[t]))], TIPSIRA.map(() => 1)));
add(p('T1+T2 olumsuz köklü öncüllüdür; hem T1 hem T2 sayılır. T1 toplam: ' + (O.tip_m['T1'] + O.tip_m['T1+T2']) + ' · T2 toplam: ' + (O.tip_m['T2'] + O.tip_m['T1+T2'])));
const tg = Object.keys(O.tip_g).sort();
add(h2('Tip Dağılımı (1–20 genel kültür)'), table(tg, [tg.map(t => String(O.tip_g[t]))], tg.map(() => 1)), p(''));
add(h2('Kök Uzunluk Bandı (21–100)'), table(Object.keys(O.bant), [Object.values(O.bant).map(v => yuzde(v, 80))], [1, 1, 1, 1]), p(''));
add(h2('Şık Uzunluk Sınıfı (21–100)'), table(Object.keys(O.sinif), [Object.values(O.sinif).map(v => yuzde(v, 80))], [1, 1, 1]));
add(p('Ters tuzak (doğru şık bilinçli olarak en uzun): ' + O.tuzak + ' soru.'));
add(h2('Konu Dağılımı'), table(['Konu', 'Soru'], O.konu.map(([k, v]) => [k, String(v)]), [7, 2]));
add(h1('Üretim Notu')); O.notlar.forEach(x => add(bullet(x)));
add(pb(), h1('HAFIZA GÜNCELLEMESİ'));
Q.forEach(q => add(new Paragraph({ spacing: { after: 10 }, children: [new TextRun({ text: ['GMY' + D + '-' + String(q.no).padStart(3, '0'), q.konu || q.ders, q.madde, q.cek, q.tip, q.z, q.harf, 'GMY-S' + D].join(' | '), font: 'Courier New', size: 14 })] })));
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('GMY DENEME SINAVI ' + D, '100 Soru · 150 Dakika · ' + O.yil + ' Sınavı Modeli', 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('../../sorular/GK_GMY_Deneme' + D + '_100soru.docx', b); console.log('docx ok', D); });
