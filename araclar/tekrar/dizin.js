// Kullanım: node araclar/tekrar/dizin.js → tekrar/README.md (konu listesi) ve tekrar/Tekrar_00_Tum_Konular.pdf (birleşik)
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const kok = path.join(__dirname, '..', '..', 'tekrar');
const veriler = fs.readdirSync(__dirname).filter(f => /^veri_\d+\.js$/.test(f)).sort().map(f => require(`./${f}`));
const pdfler = fs.readdirSync(kok).filter(f => /^Tekrar_\d\d_.*\.pdf$/.test(f) && !f.startsWith('Tekrar_00')).sort();
let top = 0, topY = 0;
const satir = veriler.map(v => {
  const s = v.bolumler.flatMap(b => b.sorular), y = s.filter(q => q[3]).length;
  top += s.length; topY += y;
  const pdf = pdfler.find(f => f.startsWith(`Tekrar_${v.no}_`));
  return `| ${v.no} | ${v.konu} | ${s.length} | ${y} | [PDF](${pdf}) |`;
});
fs.writeFileSync(path.join(kok, 'README.md'), [
  '# Hızlı Tekrar — Kısa Soru-Cevap Setleri', '',
  '**Gümrük Koçu - Ufuk Çetintaş** · Kaynak: depo kökündeki numaralı mevzuat dosyaları (11-STALAR BOŞ dosyası boş olduğu için set yok).', '',
  `Toplam **${veriler.length} konu, ${top} soru**; ★ (2021–2025 GMY sınavlarında sorulmuş bilgi) işaretli **${topY} soru**. Tüm konular tek dosyada: [Tekrar_00_Tum_Konular.pdf](Tekrar_00_Tum_Konular.pdf).`, '',
  '| No | Konu | Soru | ★ | Dosya |', '|---|---|---|---|---|', ...satir, ''].join('\n'));
execFileSync('pdfunite', [...pdfler.map(f => path.join(kok, f)), path.join(kok, 'Tekrar_00_Tum_Konular.pdf')]);
console.log(veriler.length, 'konu,', top, 'soru,', topY, '★');
