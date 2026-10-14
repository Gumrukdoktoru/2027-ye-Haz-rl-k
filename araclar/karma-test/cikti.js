// test1..3.json → sorular/GK_Karma_Test_<t>_50soru.docx (../karar/gk.js tasarımı)
const fs = require('fs'), path = require('path');
const { d, p, h1, h2, table, pb, doc, coverPage, runs } = require('../karar/gk.js');
const { Paragraph, TextRun } = d;
const L = 'ABCDE';
const SIN = { 'ÇOK': 'çok çıkan', 'ORTA': 'orta çıkan', 'AZ': 'az çıkan', 'HİÇ': 'hiç çıkmayan' };
const say = (xs, f) => xs.reduce((m, x) => (m[f(x)] = (m[f(x)] || 0) + 1, m), {});
for (const t of [1, 2, 3]) {
  const Q = JSON.parse(fs.readFileSync(path.join(__dirname, `test${t}.json`)));
  const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
  const soru = (q) => {
    add(new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: q.no + '- ', bold: true }), ...runs(q.kok[0])] }));
    q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, indent: { left: 360 }, spacing: { after: 40 }, children: runs(l) })));
    q.opts.forEach((o, j) => add(new Paragraph({ keepNext: j < 4, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun(L[j] + ') '), ...runs(o)] })));
  };
  const s = say(Q, q => q.sinif);
  add(h1('Test Bilgileri'), table(['Alan', 'Değer'], [
    ['Set', `Karma Test ${t} (KT${t})`], ['Kapsam', 'Gümrük mevzuatı; 2021–2025 GMY sınavlarında çok çıkan konular ağırlıklı'],
    ['Konu dağılımı', `Çok çıkan ${s['ÇOK'] || 0} · orta çıkan ${s['ORTA'] || 0} · az çıkan ${s['AZ'] || 0} · hiç çıkmayan ${s['HİÇ'] || 0}`],
    ['İçerik', `Çıkmış bilgi alanı ${Q.filter(q => q.tur === 'cikmis_alani').length} · sorulmamış hüküm ${Q.filter(q => q.tur !== 'cikmis_alani').length}`],
    ['Süre önerisi', '75 dakika']], [3, 7]));
  add(p(''), p('Sorular 2021–2025 GMY sınavlarının konu sıklığına göre kurgulandı. Çıkmış soruların bilgi alanları yeni kurguyla ölçüldü; kitapçık soruları kopyalanmadı. Her sorunun yalnız bir doğru cevabı vardır.'));
  add(pb(), h1('BÖLÜM A — SORU KİTAPÇIĞI'));
  Q.forEach(soru);
  add(pb(), h1('Cevap Anahtarı'));
  for (let a = 0; a < 50; a += 25) { const part = Q.slice(a, a + 25); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
  add(pb(), h1('BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR'));
  for (const q of Q) {
    add(new Paragraph({ keepNext: true, spacing: { before: 280, after: 40 }, children: [new TextRun({ text: q.madde, italics: true, color: 'B8860B', size: 20 })] }));
    soru(q);
    add(new Paragraph({ keepNext: true, spacing: { before: 80, after: 40 }, children: [new TextRun({ text: 'Doğru Cevap: ', bold: true }), new TextRun({ text: q.harf, bold: true, color: '1B3A5C' })] }));
    add(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: 'Gerekçe: ', bold: true }), ...runs(q.gerekce)] }));
    add(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: `${q.konu} · ${SIN[q.sinif]} · ${q.alt_tip}${q.cikmis ? ' · Çıkmış: ' + q.cikmis : ''}`, size: 16, color: '777777' })] }));
  }
  add(pb(), h1('Dağılım'));
  const tb = (baslik, m, sira) => add(h2(baslik), table(sira, [sira.map(k => String(m[k] || 0))], sira.map(() => 1)), p(''));
  tb('Doğru cevap harfi', say(Q, q => q.harf), [...L]);
  tb('Konu sınıfı', say(Q, q => q.sinif), ['ÇOK', 'ORTA', 'AZ', 'HİÇ']);
  const at = say(Q, q => q.alt_tip); tb('Alt tip', at, Object.keys(at).sort((a, b) => at[b] - at[a]));
  const kon = say(Q, q => q.konu);
  add(h2('Konu'), table(['Konu', 'Sınıf', 'Soru'], Object.keys(kon).sort((a, b) => kon[b] - kon[a]).map(k => [k, Q.find(q => q.konu === k).sinif, String(kon[k])]), [6, 2, 1]));
  const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
    cover: coverPage(`GMY KARMA TEST ${t}`, '50 Soru · Çok Çıkan Konular Ağırlıklı · 2021–2025 Sınavlarına Göre', 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B });
  d.Packer.toBuffer(out).then(b => { fs.writeFileSync(path.join(__dirname, `../../sorular/GK_Karma_Test_${t}_50soru.docx`), b); console.log('docx ok', t); });
}
