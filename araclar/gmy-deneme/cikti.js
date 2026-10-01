const fs = require('fs');
const { d, p, h1, h2, bullet, table, pb, doc, coverPage, runs } = require('./gk.js');
const { Paragraph, TextRun } = d;
const Q = JSON.parse(fs.readFileSync('set100.json')); const L = 'ABCDE';
const md = fs.readFileSync('GK_GMY2025_Deneme_S1_100soru.md', 'utf8');
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
const dg = s => s.replace(/GK /g, 'Gümrük Kanunu ').replace(/GY /g, 'Gümrük Yönetmeliği ');
// Set kartı tablosunu md'den al
const kart = md.split('## Set Kartı')[1].split('## Sorular')[0].trim().split('\n').slice(2).map(l => l.split('|').slice(1, -1).map(s => s.trim()));
add(h1('Set Kartı'), table(['Alan', 'Değer'], kart, [3, 7]));
add(p(''), p('**Açıklama:** Her sorunun yalnız bir doğru cevabı vardır. Soru kitapçığı 2025 Gümrük Müşavir Yardımcılığı sınavının konu dağılımı örnek alınarak özgün olarak hazırlanmıştır; sınav sorularının kopyası değildir.'));
add(pb(), h1('Bölüm 1 — Genel Kültür'));
for (const q of Q) {
  if (q.no === 21) add(pb(), h1('Bölüm 2 — Gümrük Mevzuatı'));
  add(new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: q.no + '. ', bold: true }), ...runs(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: { left: 360 }, spacing: { after: 40 }, children: runs(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: j < 4, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun({ text: L[j] + ')  ', bold: true }), ...runs(o)] })));
}
add(pb(), h1('Cevap Anahtarı'));
for (let s = 0; s < 100; s += 20) { const part = Q.slice(s, s + 20); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
add(pb(), h1('Çözümler'));
for (const q of Q) {
  add(h2(`${q.no}. soru`));
  add(bullet(`**Doğru cevap:** ${q.harf}`), bullet(`**Gerekçe:** ${q.g}`), bullet(`**Tuzak nokta şudur:** ${q.t}`), bullet(`**Yasal Dayanak:** ${dg(q.madde)}`));
}
add(pb(), h1('Dağılım Tabloları'));
const sec = md.split('## Dağılım Tabloları')[1].split('## Üretim Notu')[0];
for (const blk of sec.split('**').slice(1)) { }
const tabs = sec.trim().split(/\n\s*\n(?=\*\*)/);
for (const t of tabs) {
  const lines = t.trim().split('\n'); const title = lines[0].replace(/\*\*/g, '');
  const rows = lines.filter(l => l.startsWith('|') && !/^\|(-+\|)+$/.test(l)).map(l => l.split('|').slice(1, -1).map(s => s.trim()));
  if (rows.length > 1) add(h2(title), table(rows[0], rows.slice(1), rows[0].map(() => 1)), p(''));
  else if (!rows.length) add(p(t.trim()));
}
add(h1('Üretim Notu'));
md.split('## Üretim Notu')[1].split('## HAFIZA')[0].trim().split('\n').filter(l => l.startsWith('- ')).forEach(l => add(bullet(l.slice(2))));
add(pb(), h1('HAFIZA GÜNCELLEMESİ'));
md.split('## HAFIZA GÜNCELLEMESİ')[1].split('```')[1].trim().split('\n').forEach(l => add(new Paragraph({ spacing: { after: 10 }, children: [new TextRun({ text: l, font: 'Courier New', size: 14 })] })));
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('GMY DENEME SINAVI', '2025 Sınavı Modelinde · 100 Soru · 150 Dakika', 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('GK_GMY2025_Deneme_S1_100soru.docx', b); console.log('docx ok'); });
