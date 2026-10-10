import sys,re,pymupdf,json
def anahtar(path):
    d=pymupdf.open(path); ans={}; q=None
    for pg in d:
        W=pg.rect.width
        lines=[]
        for b in pg.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                x0,y0=l['bbox'][0],l['bbox'][1]
                lines.append((0 if x0<W/2-10 else 1,round(y0,1),x0,l['spans']))
        lines.sort(key=lambda t:(t[0],t[1],t[2]))
        for col,y,x,spans in lines:
            txt=''.join(s['text'] for s in spans).strip()
            m=re.match(r'^(\d{1,3})\s*\.(\s|$)',txt)
            if m and int(m.group(1))<=100: q=int(m.group(1))
            red=[s for s in spans if s['color'] not in (0,) and s['text'].strip() and (s['color']>>16)>200 and ((s['color']>>8)&255)<80]
            if red and q:
                mm=re.match(r'^([A-E])\)',txt)
                if mm and q not in ans: ans[q]=mm.group(1)
    return ans
for p in sys.argv[1:]:
    a=anahtar(p); print(p.split('/')[-1][:40], len(a), ''.join(a.get(i,'?') for i in range(1,101)))
    json.dump(a,open(p.split('/')[-1][:4]+'_anahtar.json','w'))
