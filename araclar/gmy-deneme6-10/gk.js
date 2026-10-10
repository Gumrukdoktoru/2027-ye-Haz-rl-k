const d = require('docx');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  AlignmentType, Header, Footer, PageNumber, PageBreak, LevelFormat, HeadingLevel, TableLayoutType } = d;
const NAVY = '1B3A5C', GOLD = 'B8860B', W = 11906 - 2 * 1134; // A4 content width
const runs = (text, o = {}) => text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(s =>
  s.startsWith('**') ? new TextRun({ text: s.slice(2, -2), bold: true, ...o }) : new TextRun({ text: s, ...o }));
const p = (text, o = {}) => new Paragraph({ children: runs(text, o.run || {}), spacing: { after: 120, line: 276 }, ...o.para });
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)], spacing: { before: 360, after: 180 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 4 } } });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)], spacing: { before: 240, after: 120 },
  border: { left: { style: BorderStyle.SINGLE, size: 36, color: GOLD, space: 8 } } });
const bullet = (t, lvl = 0) => new Paragraph({ numbering: { reference: 'bul', level: lvl }, children: runs(t), spacing: { after: 60 } });
const mono = t => new Paragraph({ children: [new TextRun({ text: t, font: 'Courier New', size: 18 })], spacing: { after: 0 } });
const cell = (content, w, o = {}) => new TableCell({ width: { size: w, type: WidthType.DXA },
  shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
  margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders: o.borders,
  children: (Array.isArray(content) ? content : [content]).map(c => typeof c === 'string'
    ? new Paragraph({ children: runs(c, { size: o.size || 20, color: o.color, bold: o.bold }), spacing: { after: 40 } }) : c) });
function table(head, rows, widths) {
  const tot = widths.reduce((a, b) => a + b, 0), ws = widths.map(x => Math.floor(x * W / tot));
  ws[ws.length - 1] += W - ws.reduce((a, b) => a + b, 0);
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: ws, layout: TableLayoutType.FIXED, rows: [
    new TableRow({ tableHeader: true, children: head.map((h, i) => cell(h, ws[i], { fill: NAVY, color: 'FFFFFF', bold: true })) }),
    ...rows.map((r, k) => new TableRow({ children: r.map((c, i) => cell(c, ws[i], { fill: k % 2 ? 'F4F1E8' : undefined })) }))] });
}
const box = (lines, kind) => {
  const gold = kind === 'star', b = { style: BorderStyle.SINGLE, size: gold ? 12 : 4, color: gold ? GOLD : NAVY };
  return [new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ children: [
    cell(lines.map(l => new Paragraph({ children: runs(l, { size: 21, color: gold ? undefined : 'FFFFFF' }), spacing: { after: 60 } })), W,
      { fill: gold ? 'FFF8E7' : NAVY, borders: { top: b, bottom: b, left: b, right: b } })] })] }),
    new Paragraph({ spacing: { after: 100 }, children: [] })];
};
const pb = () => new Paragraph({ children: [new PageBreak()] });
function doc({ header, footer, cover, body }) {
  return new d.Document({
    styles: { default: { document: { run: { font: 'Arial', size: 22 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: NAVY, font: 'Arial' }, paragraph: { outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: 'Arial' }, paragraph: { outlineLevel: 1 } }] },
    numbering: { config: [{ reference: 'bul', levels: [0, 1].map(l => ({ level: l, format: LevelFormat.BULLET, text: l ? '–' : '•',
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540 + l * 360, hanging: 270 } } } })) }] },
    sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } }, titlePage: true },
      headers: { first: new Header({ children: [] }), default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 2 } }, children: [new TextRun({ text: header, size: 18, color: NAVY, bold: true })] })] }) },
      footers: ['first', 'default'].reduce((o, k) => (o[k] = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: footer + ' | Sayfa ', size: 16, color: '555555' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '555555' }),
        new TextRun({ text: ' / ', size: 16, color: '555555' }), new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: '555555' })] })] }), o), {}),
      children: [...cover, pb(), ...body] }] });
}
function coverPage(title, sub1, sub2) {
  const sp = n => new Paragraph({ spacing: { before: n }, children: [] });
  return [sp(2400), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'GÜMRÜK KOÇU', bold: true, size: 28, color: GOLD })] }),
    sp(400), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: title, bold: true, size: 56, color: NAVY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } },
      children: [new TextRun({ text: sub1, size: 26, color: NAVY })] }),
    sp(300), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: sub2, size: 26, bold: true })] }),
    sp(3600), new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Gümrük Koçu - Ufuk Çetintaş', bold: true, size: 24, color: NAVY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: '@gumrukkocunuz', size: 20, color: GOLD })] })];
}
module.exports = { d, p, h1, h2, bullet, mono, table, box, pb, doc, coverPage, runs, NAVY, GOLD, W };
