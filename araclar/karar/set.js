const fs = require('fs');
const { d, p, h1, h2, bullet, table, box, pb, doc, coverPage, runs } = require('./gk.js');
const { Paragraph, TextRun } = d;
const Q = JSON.parse(fs.readFileSync('set.json')); const L = 'ABCDE';
const md = fs.readFileSync('GK_Karar_S1_15soru.md', 'utf8');
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
add(h1('Set Kartı'));
add(table(['Alan', 'Değer'], [['Set', 'S1'], ['Konu', 'GK/GY – Karar (Gümrük Mevzuatının Uygulanmasına İlişkin Kararlar)'], ['Sınıf', 'GM'], ['Soru sayısı', '15'],
  ['Zorluk', 'Zorlayıcı (0-10-30-40-20) → ÇK 0 · K 1 · O 5 · Z 6 · ÇZ 3'], ['Hafızadaki önceki soru (Karar)', '0'], ['Bu setle toplam', '15']], [3, 7]));
add(pb(), h1('Sorular'));
for (const q of Q) {
  add(new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: q.no + '. ', bold: true }), ...runs(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: { left: 360 }, spacing: { after: 40 }, children: runs(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: j < 4, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun({ text: L[j] + ')  ', bold: true }), ...runs(o)] })));
}
add(pb(), h1('Cevap Anahtarı'));
add(table(Q.map(q => String(q.no)), [Q.map(q => q.harf)], Q.map(() => 1)));
add(h1('Çözümler'));
for (const q of Q) {
  add(h2(`${q.no}. soru`));
  add(bullet(`**Doğru cevap:** ${q.harf}`), bullet(`**Gerekçe:** ${q.g}`), bullet(`**Tuzak nokta şudur:** ${q.t}`),
      bullet(`**Yasal Dayanak:** ${q.madde.replace(/GK/g, 'Gümrük Kanunu').replace(/GY/g, 'Gümrük Yönetmeliği')}`));
}
add(pb(), h1('Dağılım Tabloları'));
const cnt = (k, order) => order.map(o => String(Q.filter(q => q[k] === o).length));
const T = [['Tip', 'tip', ['DY', 'DĞ', 'ÇI', 'SÜ', 'MK', 'BD', 'EŞ', 'UK', 'UU']], ['Zorluk', 'z', ['ÇK', 'K', 'O', 'Z', 'ÇZ']], ['Doğru cevap harfi', 'harf', [...L]]];
for (const [t, k, o] of T) { add(h2(t), table(o, [cnt(k, o)], o.map(() => 1)), p('')); }
const tz = ['İdare/makam karıştırma', 'Rejim sınıflandırma', 'Tanım çiftleri', 'Belge eşleştirme', 'Süre kaydırma', 'Eşik/oran kaydırma', 'İstisna atlatma'];
add(h2('Tuzak kategorisi'), table(['Kategori', 'Soru sayısı', 'Sorular'], tz.map(t => [t, String(Q.filter(q => q.tuzak === t).length), Q.filter(q => q.tuzak === t).map(q => q.no).join(', ')]), [4, 2, 3]));
add(p(''), p('**Şık uzunluğu:** Protokol A 13 soru (ihlal 0) · Protokol B 2 soru (9, 14) = %13,3.'));
add(h1('Üretim Notu'));
md.split('## Üretim Notu')[1].split('## HAFIZA')[0].trim().split('\n').filter(l => l.startsWith('- ')).forEach(l => add(bullet(l.slice(2))));
add(h1('HAFIZA GÜNCELLEMESİ'));
md.split('```')[1].trim().split('\n').forEach(l => add(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: l, font: 'Courier New', size: 15 })] })));
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('KARAR', 'Akıllı Test · Set S1 · 15 Soru', 'GM / GMY Sınavlarına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('GK_Karar_S1_15soru.docx', b); console.log('ok'); });
