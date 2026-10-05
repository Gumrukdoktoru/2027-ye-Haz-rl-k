// sc.json → sorular/GK_Sorulmayan_Konular_SoruCevap.docx (özet karşılaştırma + soru–cevap)
const fs = require('fs'), path = require('path');
const { d, p, h1, h2, bullet, table, pb, doc, coverPage, runs, NAVY, GOLD } = require('../karar/gk.js');
const { Paragraph, TextRun } = d;
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'sc.json')));
const notlar = JSON.parse(fs.readFileSync(path.join(__dirname, 'notlar.json')));
const YIL = ['2021', '2022', '2023', '2024', '2025'];
const TOP = D.reduce((a, x) => a + x.soru_cevap.length, 0);
const st = (x, k) => x.st[k] || 0;
const B = []; const add = (...e) => e.flat().forEach(z => B.push(z));

add(h1('Karşılaştırma Özeti'));
notlar.yontem.forEach(n => add(bullet(n)));
add(p(''), h2('Konu bazında çıkmış soru sayısı ve sorulmayan hükümler'));
add(table(['#', 'Konu', ...YIL.map(y => y.slice(2)), 'Top.', 'Sorulan / Kısmen / Sorulmayan alt konu', 'S–C'],
  D.map((x, i) => { const yc = {}; x.refs.forEach(r => yc[r.slice(0, 4)] = (yc[r.slice(0, 4)] || 0) + 1);
    return [String(i + 1), x.konu, ...YIL.map(y => String(yc[y] || 0)), `**${x.refs.length}**`,
      `${st(x, 'SORULDU')} / ${st(x, 'KISMEN')} / ${st(x, 'SORULMADI')}`, String(x.soru_cevap.length)]; }),
  [3, 22, 3, 3, 3, 3, 3, 4, 9, 4]));
add(p('Top.: o kaynak dosyadaki hükümlere dayanan çıkmış soru sayısı (bir soru iki dosyayı ölçüyorsa ikisinde de sayılır). Ayrıntılı alt konu listesi GK_Cikmis_vs_Sorulmayan_Analiz dosyasındadır.', { run: { size: 18, italics: true } }));
add(h2('Beş yılda hiç sorulmayan konular'));
D.filter(x => !x.refs.length).forEach(x => add(bullet(`**${x.konu}** (${x.mevzuat}) — ${x.soru_cevap.length} soru–cevap`)));
add(h2('Az sorulan konular (1–3 soru)'));
D.filter(x => x.refs.length >= 1 && x.refs.length <= 3).forEach(x => add(bullet(`**${x.konu}** — ${x.refs.length} soru (${x.refs.join(', ')})`)));
(notlar.gozlem || []).forEach(n => add(bullet(n)));

add(pb(), h1('Sorulmayan Konular — Soru–Cevap'));
add(p('Sorular açık uçludur; cevabı kapatıp kendinizi deneyin. Her cevabın sonunda dayanak madde yer alır. Çıkmış sorularda ölçülen bilgi noktaları bu bölümde tekrar edilmemiştir.'));
D.forEach((x, i) => {
  if (!x.soru_cevap.length) return;
  add(h1(`${i + 1}. ${x.konu}`));
  add(new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: `${x.mevzuat} · Beş yılda ${x.refs.length} soru · ${x.soru_cevap.length} soru–cevap`, italics: true, color: GOLD, size: 19 })] }));
  let son = null;
  x.soru_cevap.forEach(q => {
    if (q.alt_konu !== son) { add(h2(q.alt_konu)); son = q.alt_konu; }
    add(new Paragraph({ keepNext: true, spacing: { before: 140, after: 40 }, children: [new TextRun({ text: `S${q.no}. `, bold: true, color: NAVY }), ...runs(q.soru)] }));
    add(new Paragraph({ indent: { left: 360 }, spacing: { after: 100 }, children: [new TextRun({ text: 'Cevap: ', bold: true }), ...runs(q.cevap.trim() + ' '),
      new TextRun({ text: `(${q.dayanak})`, italics: true, color: '555555' })] }));
  });
});
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('SORULMAYAN KONULAR', `2021–2025 GMY Çıkmış Sorularında Ölçülmeyen Hükümler · ${TOP} Soru–Cevap`, 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync(path.join(__dirname, '../../sorular/GK_Sorulmayan_Konular_SoruCevap.docx'), b); console.log('docx ok'); });
