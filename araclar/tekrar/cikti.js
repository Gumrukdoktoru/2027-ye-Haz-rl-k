// Kullanım: node araclar/tekrar/cikti.js 01  → tekrar/Tekrar_01_<Konu>.md ve .docx
const fs = require('fs'), path = require('path');
const { d, p, h1, h2, table, box, doc, coverPage } = require('../karar/gk.js');
const no = process.argv[2];
const v = require(`./veri_${no}.js`);
const kok = path.join(__dirname, '..', '..', 'tekrar');
const slug = v.konu.replace(/[çÇğĞıİöÖşŞüÜ]/g, c => ({ ç: 'c', Ç: 'C', ğ: 'g', Ğ: 'G', ı: 'i', İ: 'I', ö: 'o', Ö: 'O', ş: 's', Ş: 'S', ü: 'u', Ü: 'U' })[c]).replace(/\s+/g, '_');
const ad = path.join(kok, `Tekrar_${v.no}_${slug}`);
const yildiz = k => k ? ` ★ ${k}` : '';
const toplam = v.bolumler.reduce((a, b) => a + b.sorular.length, 0);

// Markdown
let n = 0;
const md = [`# Hızlı Tekrar ${v.no} — ${v.konu}`, '', `**Gümrük Koçu - Ufuk Çetintaş** · Kısa soru-cevap · ${toplam} soru`, '',
  `Kaynak: ${v.kaynak}. ★ işaretli sorular 2021–2025 GMY sınavlarında sorulmuş bilgilerdir.`, ''];
for (const b of v.bolumler) {
  md.push(`## ${b.baslik}`, '');
  for (const [s, c, dy, k] of b.sorular) md.push(`**${++n}. ${s}**${yildiz(k)}  `, `→ ${c} *(${dy})*`, '');
}
md.push('## Sık Karıştırılanlar', '', ...v.tuzaklar.map(t => `- ${t}`), '');
fs.writeFileSync(ad + '.md', md.join('\n'));

// Word
n = 0;
const body = [h1(`Hızlı Tekrar ${v.no} — ${v.konu}`),
  p(`Kaynak: ${v.kaynak}. ★ işaretli sorular 2021–2025 GMY sınavlarında sorulmuş bilgilerdir. Cevap sütununu kapatarak kendinizi sınayın.`)];
for (const b of v.bolumler) {
  body.push(h2(b.baslik));
  body.push(table(['#', 'Soru', 'Cevap'], b.sorular.map(([s, c, dy, k]) => [String(++n), `**${s}**${yildiz(k)}`, `${c} (${dy})`]), [6, 40, 54]));
}
body.push(h2('Sık Karıştırılanlar'), ...box(v.tuzaklar, 'star'));
const D = doc({ header: `Gümrük Koçu | Hızlı Tekrar ${v.no} — ${v.konu}`, footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('HIZLI TEKRAR', `${v.no}. Konu — ${v.konu}`, `Kısa Soru-Cevap · ${toplam} soru`), body });
d.Packer.toBuffer(D).then(buf => { fs.writeFileSync(ad + '.docx', buf); console.log(ad, toplam, 'soru'); });
