# -*- coding: utf-8 -*-
"""สร้าง index.html จากเนื้อหาใน scripts/site/*.py

รัน:  python3 scripts/site/build.py
แก้เนื้อหาที่ core.py (ข้อ 1-8, สอบ A/B), extra.py (ข้อ 9-13), cheat.py (หน้าสรุป), tools.py
หน้าตาที่ assets/style.css  แล้วรัน build ใหม่ ตามด้วย python3 -m unittest discover -s scripts
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from common import wrap_math, wrap_exam  # noqa: E402
import core  # noqa: E402
import extra  # noqa: E402
import cheat  # noqa: E402
import tools  # noqa: E402

HEADER = '''<header class="top"><p class="kick">แนวการแก้ปัญหากลศาสตร์ของไหล</p>
<h1>บทที่ 5 การไหลในท่อ</h1>
<p class="sub">สรุปสูตร · ขั้นตอนแต่ละประเภทโจทย์ · เฉลยวิธีทำ · เฉลยละเอียด</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
<p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p></header>'''

PAGES = ([('sum', 'สรุปสูตร', cheat.CHEAT.replace('<section id="sum">', '<section id="sum">' + HEADER, 1))]
         + core.SECS + extra.SECS
         + [('calc', 'คิดเลข', tools.CALC), ('ref', 'อ้างอิง', tools.REF)])
GROUP_START = {'q1', 'q9', 'calc'}  # เส้นแบ่งกลุ่มใน nav

DETAIL = '<hr>\n<h3 class="part">เฉลยละเอียด</h3>'


def finish(i, pid, label, html):
    if DETAIL in html:
        html = html.replace(DETAIL, '<div class="detail">' + DETAIL, 1)
        html = html[:html.rindex('</section>')] + '</div>' + html[html.rindex('</section>'):]
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i + 1 < len(PAGES) else None
    pn = '<div class="pn">'
    pn += f'<a href="#{prev[0]}">← {prev[1]}</a>' if prev else '<span></span>'
    pn += f'<a href="#{nxt[0]}">{nxt[1]} →</a>' if nxt else '<span></span>'
    pn += '</div>'
    return html[:html.rindex('</section>')] + pn + html[html.rindex('</section>'):]


def build():
    def link(pid, label):
        cls = ' class="gap"' if pid in GROUP_START else ''
        return '<a href="#%s"%s>%s</a>' % (pid, cls, label)
    nav = ''.join(link(pid, label) for pid, label, _ in PAGES)
    icon_sun = '<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
    icon_moon = '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg>'
    icon_pen = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13.5 6.5l4 4"/></svg>'
    tools_html = (f'<span class="tools"><button class="th" id="practice" type="button" aria-pressed="false" aria-label="โหมดฝึก ซ่อนวิธีทำ">{icon_pen}<span class="lbl">ฝึก</span></button>'
                  f'<button class="th" id="theme" type="button" aria-label="สลับโหมดสว่าง/มืด">{icon_sun}{icon_moon}<span class="lbl" id="thl"></span></button></span>')
    body = '\n'.join(finish(i, pid, label, html) for i, (pid, label, html) in enumerate(PAGES))
    foot = ('<p class="foot">ผู้จัดทำเดิม Thanaporn Nopparat · ปรับปรุงโดยเพื่อนร่วมวิชา<br>'
            'ตัวเลขทุกข้อคำนวณซ้ำด้วย Colebrook-White (scripts/pipeflow.py) ค่า f ที่อ่านจากชาร์ตอาจต่างได้ไม่เกิน ~2%</p>')
    page = f'''<!doctype html>
<html lang="th" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>บทที่ 5 การไหลในท่อ · วย 271</title>
<meta name="description" content="สรุปสูตร ขั้นตอนทำโจทย์ และเฉลยบทที่ 5 การไหลในท่อ วิชากลศาสตร์ของไหลสำหรับวิศวกรโยธา">
<link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<link rel="stylesheet" href="assets/style.css">
<script>(function(){{var t=null;try{{t=localStorage.getItem('theme')}}catch(e){{}}if(t!=='light'&&t!=='dark')t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t)}})()</script>
</head><body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs></svg>
<nav class="toc" aria-label="สารบัญ">{nav}<span class="sp"></span>{tools_html}</nav>
<main>
<noscript><p>เว็บนี้ใช้ JavaScript แสดงสูตรและสลับหน้า กรุณาเปิด JavaScript</p></noscript>
{body}
{foot}
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js" defer></script>
<script src="assets/calc.js" defer></script>
<script src="assets/app.js" defer></script>
</body></html>
'''
    page = wrap_exam(page, 24)
    page = wrap_math(page)
    page = page.replace('\\textcolor{#ff8178}{', '\\htmlClass{no}{').replace('\\textcolor{#63d487}{', '\\htmlClass{ok}{')
    (ROOT / 'index.html').write_text(page, encoding='utf-8')
    print(f'index.html: {len(page.encode("utf-8")) // 1024} KB, {len(PAGES)} หน้า')


if __name__ == '__main__':
    build()
