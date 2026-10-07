// HTML'i A4 PDF'e basar. Kullanım: NODE_PATH=<playwright klasörü> node pdf5.mjs GIRDI.html CIKTI.pdf
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

const { chromium } = createRequire(import.meta.url)('playwright');
const [, , girdi, cikti] = process.argv;
const tarayici = await chromium.launch();
const sayfa = await tarayici.newPage();
await sayfa.setContent(readFileSync(girdi, 'utf-8'), { waitUntil: 'load' });
await sayfa.pdf({ path: cikti, printBackground: true, preferCSSPageSize: true });
await tarayici.close();
console.log('PDF yazıldı:', cikti);
