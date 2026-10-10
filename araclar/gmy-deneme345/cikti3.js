const fs = require('fs');
const { d, p, h1, h2, bullet, table, pb, doc, coverPage, runs } = require('./gk.js');
const { Paragraph, TextRun } = d;
const S = process.argv[2]; const Q = JSON.parse(fs.readFileSync('set' + S + '.json')); const L = 'ABCDE';
const md = fs.readFileSync('GK_GMY_Deneme' + S + '_100soru.md', 'utf8');
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
const soru = (q) => {
  add(new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: q.no + '- ', bold: true }), ...runs(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: { left: 360 }, spacing: { after: 40 }, children: runs(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: j < 4, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun(L[j] + ') '), ...runs(o)] })));
};
const kart = md.split('## GMY Deneme Sınavı ' + S)[1].split('# BÖLÜM A')[0].trim().split('\n').slice(2).map(l => l.split('|').slice(1, -1).map(s => s.trim()));
add(h1('Sınav Bilgileri'), table(['Alan', 'Değer'], kart, [3, 7]));
add(p(''), p('Her sorunun yalnız bir doğru cevabı vardır. Sorular 2024 ve 2025 GMY sınavlarında (resmî cevap anahtarlarıyla) ölçülen bilgi alanları ve kurum soru dili esas alınarak özgün olarak hazırlanmıştır; çıkmış soruların kopyası değildir.'));
add(pb(), h1('BÖLÜM A — SORU KİTAPÇIĞI'), h2('Genel Kültür (1–20)'));
for (const q of Q) { if (q.no === 21) add(pb(), h2('Gümrük Mevzuatı (21–100)')); soru(q); }
add(pb(), h1('Cevap Anahtarı'));
for (let s = 0; s < 100; s += 20) { const part = Q.slice(s, s + 20); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
add(pb(), h1('BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR'));
for (const q of Q) {
  add(new Paragraph({ keepNext: true, spacing: { before: 280, after: 40 }, children: [new TextRun({ text: q.madde, italics: true, color: 'B8860B', size: 20 })] }));
  soru(q);
  add(new Paragraph({ keepNext: true, spacing: { before: 80, after: 40 }, children: [new TextRun({ text: 'Doğru Cevap: ', bold: true }), new TextRun({ text: q.harf, bold: true, color: '1B3A5C' })] }));
  add(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: 'Gerekçe: ', bold: true }), ...runs(q.g)] }));
}
add(pb(), h1('Dağılım'));
const sec = md.split('## Dağılım')[1].split('## Üretim Notu')[0];
for (const t of sec.trim().split(/\n\s*\n(?=\*\*)/)) {
  const lines = t.trim().split('\n'); const title = lines[0].replace(/\*\*/g, '');
  const rows = lines.filter(l => l.startsWith('|') && !/^\|(-+\|)+$/.test(l)).map(l => l.split('|').slice(1, -1).map(s => s.trim()));
  if (rows.length > 1) add(h2(title), table(rows[0], rows.slice(1), rows[0].map(() => 1)), p(''));
}
add(h1('Üretim Notu'));
md.split('## Üretim Notu')[1].split('## HAFIZA')[0].trim().split('\n').filter(l => l.startsWith('- ')).forEach(l => add(bullet(l.slice(2))));
add(pb(), h1('HAFIZA GÜNCELLEMESİ'));
md.split('## HAFIZA GÜNCELLEMESİ')[1].split('```')[1].trim().split('\n').forEach(l => add(new Paragraph({ spacing: { after: 10 }, children: [new TextRun({ text: l, font: 'Courier New', size: 14 })] })));
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('GMY DENEME SINAVI ' + S, '100 Soru · 150 Dakika · 2024–2025 Sınavları Esas', 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('GK_GMY_Deneme' + S + '_100soru.docx', b); console.log('docx ok'); });
