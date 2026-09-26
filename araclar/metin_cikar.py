import sys, zipfile, re, html, pathlib
from html.parser import HTMLParser
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
import xml.etree.ElementTree as ET

def docx_text(p):
    with zipfile.ZipFile(p) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    out = []
    body = root.find(W+'body')
    for el in body:
        if el.tag == W+'p':
            out.append(para(el))
        elif el.tag == W+'tbl':
            for tr in el.iter(W+'tr'):
                cells = []
                for tc in tr.findall(W+'tc'):
                    cells.append(' '.join(para(p) for p in tc.iter(W+'p')).strip())
                out.append(' | '.join(cells))
            out.append('')
    return '\n'.join(out)

def para(p):
    s = []
    for n in p.iter():
        if n.tag == W+'t' and n.text: s.append(n.text)
        elif n.tag == W+'tab': s.append('\t')
        elif n.tag in (W+'br', W+'cr'): s.append('\n')
    return ''.join(s)

class H(HTMLParser):
    BLOCK = {'p','div','br','li','tr','h1','h2','h3','h4','h5','h6','table'}
    def __init__(s): super().__init__(); s.buf=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style'): s.skip+=1
        if t in s.BLOCK: s.buf.append('\n')
        if t in ('td','th'): s.buf.append(' | ')
    def handle_endtag(s,t):
        if t in ('script','style'): s.skip-=1
        if t in s.BLOCK: s.buf.append('\n')
    def handle_data(s,d):
        if not s.skip: s.buf.append(d)

def html_text(p):
    h = H(); h.feed(pathlib.Path(p).read_text(encoding='utf-8', errors='replace'))
    return ''.join(h.buf)

for f in sorted(pathlib.Path('.').glob('*.doc*')):
    t = docx_text(f) if f.suffix == '.docx' else html_text(f)
    t = re.sub(r'[ \t\xa0]+\n', '\n', t.replace('\r',''))
    t = re.sub(r'\n{3,}', '\n\n', t).strip() + '\n'
    (pathlib.Path('metin') / (f.stem + '.txt')).write_text(t, encoding='utf-8')
