// sorular/GK_GMY_Soru_Tipi_Katalogu.md → .docx (../karar/gk.js tasarımı). Kullanım: NODE_PATH=$(npm root -g) node katalog_docx.js
const fs = require('fs'), path = require('path');
const { d, p, h1, h2, bullet, table, box, pb, doc, coverPage, runs, NAVY, GOLD } = require('../karar/gk.js');
const { Paragraph, TextRun, BorderStyle } = d;
const MD = path.join(__dirname, '../../sorular/GK_GMY_Soru_Tipi_Katalogu.md');
const lines = fs.readFileSync(MD, 'utf8').split('\n');
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
const h3 = t => new Paragraph({ keepNext: true, spacing: { before: 220, after: 100 }, children: [new TextRun({ text: t, bold: true, size: 24, color: NAVY })] });
const h4 = t => new Paragraph({ keepNext: true, spacing: { before: 200, after: 80 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD, space: 2 } }, children: [new TextRun({ text: t, bold: true, size: 22, color: NAVY })] });
const ital = t => t.replace(/(^|[^*])\*([^*]+)\*(?!\*)/g, '$1$2');
const cells = l => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(s => ital(s.trim()));
let i = 0, ilkH1 = true;
while (i < lines.length) {
  const l = lines[i];
  if (/^```/.test(l)) {                                   // kod bloğu
    const blk = []; i++;
    while (i < lines.length && !/^```/.test(lines[i])) blk.push(lines[i++]);
    i++; add(box(blk, 'star')); continue;
  }
  if (/^\|/.test(l)) {                                    // tablo
    const rows = [];
    while (i < lines.length && /^\|/.test(lines[i])) { if (!/^\|\s*:?-{2,}/.test(lines[i])) rows.push(cells(lines[i])); i++; }
    const n = Math.max(...rows.map(r => r.length)); rows.forEach(r => { while (r.length < n) r.push(''); });
    const w = Array.from({ length: n }, (_, k) => Math.min(40, Math.max(4, ...rows.map(r => (r[k] || '').length))));
    add(table(rows[0], rows.slice(1), w), p(''));
    continue;
  }
  if (/^>/.test(l)) {                                     // alıntı (gerçek örnek)
    const blk = [];
    while (i < lines.length && /^>/.test(lines[i])) { const t = lines[i].replace(/^>\s?/, ''); if (t.trim()) blk.push(ital(t)); i++; }
    add(box(blk, 'star')); continue;
  }
  if (/^# /.test(l)) { if (!ilkH1) add(pb()); ilkH1 = false; add(h1(l.slice(2).trim())); }
  else if (/^## /.test(l)) add(h1(l.slice(3).trim()));
  else if (/^### /.test(l)) add(h2(l.slice(4).trim()));
  else if (/^#### /.test(l)) add(h4(l.slice(5).trim()));
  else if (/^##### /.test(l)) add(h3(l.slice(6).trim()));
  else if (/^\s*[-*] /.test(l)) add(bullet(ital(l.replace(/^\s*[-*] /, '')), /^\s{2,}/.test(l) ? 1 : 0));
  else if (/^\d+\.\s/.test(l)) add(new Paragraph({ indent: { left: 360, hanging: 360 }, spacing: { after: 80 }, children: runs(ital(l)) }));
  else if (/^---\s*$/.test(l)) add(p(''));
  else if (/^<!--/.test(l)) {}
  else if (l.trim()) add(p(ital(l)));
  i++;
}
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('SORU TİPİ KATALOĞU', 'GMY 2021–2025 · 500 Sorunun Alt Tip Haritası', 'Gümrük Müşavir Yardımcılığı Sınavına Hazırlık'), body: B.slice(1) });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync(MD.replace(/\.md$/, '.docx'), b); console.log('docx ok'); });
