# -*- coding: utf-8 -*-
"""ตัวช่วยสร้างหน้าเฉลย: แถววิธีทำ กล่องคำตอบ รูป และตัวตัดบรรทัดสมการยาว"""
import re
import re as _re
def _vis(piece):
    t=_re.sub(r'\\(dfrac|frac|tfrac)\{','{',piece)
    t=_re.sub(r'\\text\{([^}]*)\}',lambda m:m.group(1),t)
    t=_re.sub(r'\\[a-zA-Z]+','x',t)
    return len(_re.sub(r'[{}^_\\ &]','',t))

def _split_top(body):
    """split at top-level \\qquad, \\quad and before \\ \\Rightarrow"""
    out=[]; cur=''; depth=0; i=0
    while i < len(body):
        c=body[i]
        if c=='{': depth+=1
        elif c=='}': depth-=1
        if depth==0 and body.startswith('\\left',i): depth+=1
        if body.startswith('\\right',i): depth-=1
        if depth==0:
            m=_re.match(r'\\(qquad|quad)(?![a-zA-Z])',body[i:])
            if m:
                out.append(cur); cur=''; i+=m.end(); continue
            m=_re.match(r',(\\ |\\quad)',body[i:])
            if m:
                cur+=','; out.append(cur); cur=''; i+=m.end(); continue
            m=_re.match(r'(\\ )?\\Rightarrow',body[i:])
            if m and cur.strip():
                out.append(cur); cur=''
        cur+=c; i+=1
    out.append(cur)
    return [p.strip().rstrip(',').strip() for p in out if p.strip()]

def wrap_math(html, limit=40):
    def fix(m):
        inner=m.group(1)
        if '\\begin' in inner or '\\underbrace' in inner: return m.group(0)
        tag=''
        t=_re.search(r'\\tag\{[^}]*\}\s*$',inner)
        if t: tag=t.group(0); inner=inner[:t.start()]
        if _vis(inner) <= limit: return m.group(0)
        # fix unbalanced \left..\right splitting: only split pieces whose braces balance
        parts=_split_top(inner)
        if len(parts)<2: return m.group(0)
        lines=[]; cur=''
        for p in parts:
            cand=(cur+(r'\quad ' if cur and not p.startswith(r'\ \Rightarrow') and not p.startswith(r'\Rightarrow') else ' ')+p) if cur else p
            if cur and _vis(cand)>limit:
                lines.append(cur); cur=p
            else:
                cur=cand
        lines.append(cur)
        if len(lines)<2: return m.group(0)
        if any(l.count('\\left')!=l.count('\\right') or l.count('{')!=l.count('}') for l in lines): return m.group(0)
        body=r'\begin{aligned}'+r' \\ '.join('& '+l for l in lines)+r'\end{aligned}'
        return '$$'+body+tag+'$$'
    return _re.sub(r'\$\$(.*?)\$\$',fix,html,flags=_re.S)

def row(lab, body, cls=''):
    return f'<div class="row"><div class="lab">{lab}</div><div class="{cls}">{body}</div></div>'

def exam(rows):
    return '<div class="exam">' + ''.join(rows) + '</div>'

def fin(s):
    parts = re.split(r'(\\\(.*?\\\))', s)
    s = ''.join(p if p.startswith('\\(') else p.replace('\\ ', ' ') for p in parts)
    return row('ตอบ', f'<span class="fin">{s}</span>')

def sec(id, tag, title, statement, fig, ex, detail):
    return f'''<section id="{id}">
<h2 class="prob"><span class="tag">{tag}</span>{title}</h2>
<div class="stmt">{statement}</div>
{fig}
<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
{exam(ex)}
<hr>
<h3 class="part">เฉลยละเอียด</h3>
{detail}
</section>'''

def figure(svg, cap):
    return f'<figure>{svg}<figcaption>{cap}</figcaption></figure>'

S = 'stroke:var(--navy);fill:none'
def pipesvg(rise_px, rise_lab, k_lab):
    y0, x1, x2 = 190, 300, 520
    ytop = y0 - rise_px
    return f'''<svg viewBox="0 0 640 230" role="img" aria-label="ท่อยกสูง {rise_lab}">
<line x1="20" y1="{y0}" x2="600" y2="{y0}" style="stroke:var(--ink);stroke-dasharray:6 5"/>
<path d="M40 {y0}H{x1}Q{x1+16} {y0} {x1+16} {y0-16}V{ytop+16}Q{x1+16} {ytop} {x1+32} {ytop}H{x2}" style="{S};stroke-width:6"/>
<circle cx="58" cy="{y0-16}" r="11" style="fill:var(--bg);stroke:var(--ink)"/><text x="53.5" y="{y0-11}" font-size="14" fill="var(--ink)">1</text>
<circle cx="{x2}" cy="{ytop-16}" r="11" style="fill:var(--bg);stroke:var(--ink)"/><text x="{x2-4.5}" y="{ytop-11}" font-size="14" fill="var(--ink)">2</text>
<line x1="{x2+40}" y1="{ytop+3}" x2="{x2+40}" y2="{y0-3}" stroke="var(--red)" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/>
<text x="{x2+48}" y="{(ytop+y0)//2+5}" font-size="16" fill="var(--red)">{rise_lab}</text>
<text x="{x1-90}" y="{y0-10}" font-size="15" fill="var(--green)">{k_lab}</text>
<text x="{x1+34}" y="{ytop-8}" font-size="15" fill="var(--green)">{k_lab}</text>
</svg>'''


def wrap_exam(html, limit=30):
    """ในกล่องเฉลยวิธีทำ ตัดบรรทัดสมการให้สั้นลง (อ่านบนมือถือได้โดยไม่ต้องเลื่อนซ้ายขวา)"""
    out, pos, tag = [], 0, '<div class="exam">'
    while True:
        i = html.find(tag, pos)
        if i < 0:
            out.append(html[pos:])
            break
        out.append(html[pos:i])
        depth, j = 0, i
        for m in re.finditer(r'<div\b|</div>', html[i:]):
            depth += 1 if m.group(0) != '</div>' else -1
            if depth == 0:
                j = i + m.end()
                break
        out.append(wrap_math(html[i:j], limit))
        pos = j
    return ''.join(out)
