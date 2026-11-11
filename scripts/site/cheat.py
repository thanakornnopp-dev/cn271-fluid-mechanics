# -*- coding: utf-8 -*-
"""สรุปสูตร + แนวทางทำโจทย์แต่ละประเภท (หน้าแรกของ sample/all-solutions.html)"""


def row(lab, body, cls=''):
    return f'<div class="row"><div class="lab">{lab}</div><div class="{cls}">{body}</div></div>'


def card(title, rows):
    return f'<h4 class="cardt">{title}</h4><div class="exam">' + ''.join(rows) + '</div>'


def ty(title, given, steps, extra=''):
    lis = ''.join(f'<li>{s}</li>' for s in steps)
    return f'''<div class="ty"><div class="tyh">{title}</div><div class="tyb">
<p class="gq">{given}</p><ol class="st">{lis}</ol>{extra}</div></div>'''


def box(kind, title, body):
    return f'<div class="bx {kind}"><b>{title}</b><div>{body}</div></div>'


# ------------------------------------------------------------------ ส่วน ก
A = ''

A += '''<div class="tw"><table><caption>ตารางที่ ก1 ค่าคงที่ของน้ำ (ประมาณ 20°C) และการแปลงหน่วย</caption>
<thead><tr><th>ค่า</th><th>ใช้</th><th>หมายเหตุ</th></tr></thead><tbody>
<tr><td>\\(\\gamma\\)</td><td>9810 N/m³</td><td>\\(\\gamma=\\rho g\\)</td></tr>
<tr><td>\\(\\rho\\)</td><td>1000 kg/m³</td><td></td></tr>
<tr><td>\\(g\\)</td><td>9.81 m/s²</td><td>\\(2g=19.62\\)</td></tr>
<tr><td>\\(\\mu\\)</td><td>\\(10^{-3}\\) N\\(\\!\\cdot\\!\\)s/m²</td><td>1 N\\(\\!\\cdot\\!\\)s/m² = 1 Pa\\(\\!\\cdot\\!\\)s</td></tr>
<tr><td>\\(\\nu\\)</td><td>\\(10^{-6}\\) m²/s</td><td>\\(\\nu=\\mu/\\rho\\)</td></tr>
<tr><td>แปลงหน่วย</td><td colspan="2">1 kPa = 1000 Pa = 1000 N/m² · 1 mm = \\(10^{-3}\\) m · 1 cm = \\(10^{-2}\\) m · 1 L/s = \\(10^{-3}\\) m³/s · 1 atm = 101.3 kPa · 1 hp = 745.7 W</td></tr>
</tbody></table></div>'''

A += card('ปริมาณพื้นฐาน', [
    row('ความต่อเนื่อง', r'''$$Q=vA,\qquad A=\frac{\pi D^2}{4}\ \Rightarrow\ v=\frac{4Q}{\pi D^2}$$$$Q_1=Q_2\ \Rightarrow\ v_2=v_1\Big(\frac{D_1}{D_2}\Big)^2$$'''),
    row('Reynolds number', r'''$$Re=\frac{\rho vD}{\mu}=\frac{vD}{\nu}$$$$\begin{aligned}Re&<2000&&\text{Laminar}\\2000\le Re&\le4000&&\text{Transitional}\\Re&>4000&&\text{Turbulent}\end{aligned}$$'''),
])

A += card('สมการพลังงานและการสูญเสีย', [
    row('สมการพลังงาน<br>จุด 1 → จุด 2', r'''$$\begin{aligned}\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1+h_p&=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2\\&\quad+h_t+h_L\end{aligned}$$<p class="nt">\(h_p\) = เฮดที่ปั๊มเพิ่ม, \(h_t\) = เฮดที่เทอร์ไบน์ดึงออก (ไม่มี = 0) ท่อ fully developed ใช้ \(\alpha_1=\alpha_2\) จึงไม่ต้องเขียน \(\alpha\) ใช้ \(P\) แบบเกจทั้งสองจุด</p>'''),
    row('เฮดรวมที่จุดหนึ่ง', r'''$$H=\frac{P}{\gamma}+\frac{v^2}{2g}+z$$$$h_L=H_1-H_2$$<p class="nt">ใช้ \(h_L=H_1-H_2\) เมื่อไม่มีปั๊มและเทอร์ไบน์</p>'''),
    row('การสูญเสียรวม', r'''$$h_L=h_f+h_m$$$$h_f=f\,\frac{L}{D}\,\frac{v^2}{2g}$$$$h_m=\sum K_L\,\frac{v^2}{2g}$$$$h_f=\frac{8fLQ^2}{\pi^2 g\,D^5}$$<p class="nt">\(h_f\) คือสมการ Darcy-Weisbach สูตรล่างคือ \(h_f\) ที่เขียนด้วย \(Q\)</p>'''),
    row('ความดันลด', r'''$$\Delta P=\gamma\,h_L=\rho g\,h_L$$$$\Delta P=f\,\frac{L}{D}\,\frac{\rho v^2}{2}$$<p class="nt">สูตรล่างใช้กับท่อราบ ขนาดคงที่ ไม่มี minor loss</p>'''),
])

A += card('ค่า friction factor f', [
    row('Laminar<br>(Re &lt; 2000)', r'''$$f=\frac{64}{Re}$$$$\Delta P=\frac{32\,\mu L v}{D^2}$$<p class="nt">\(f\) ของ Laminar ไม่ขึ้นกับ \(\varepsilon\)</p>'''),
    row('Turbulent<br>Colebrook', r'''$$\frac{1}{\sqrt f}=-2\log_{10}\!\Big(\frac{\varepsilon/D}{3.7}+\frac{2.51}{Re\sqrt f}\Big)$$<p class="nt">ในห้องสอบใช้อ่านจากชาร์ต Moody ที่ \(Re\) และ \(\varepsilon/D\) (ต้องหารหน่วยเดียวกัน)</p>'''),
    row('fully rough<br>(Re สูงมาก)', r'''$$\frac{1}{\sqrt f}=-2\log_{10}\frac{\varepsilon/D}{3.7}$$<p class="nt">\(f\) ขึ้นกับ \(\varepsilon/D\) อย่างเดียว ใช้เป็นค่าเดารอบแรก (ตารางที่ ค3)</p>'''),
    row('Swamee-Jain<br>(เสริม)', r'''$$f=\frac{0.25}{\Big[\log_{10}\!\Big(\dfrac{\varepsilon/D}{3.7}+\dfrac{5.74}{Re^{0.9}}\Big)\Big]^{2}}$$<p class="nt">หา \(f\) ได้ตรงโดยไม่ต้องวนซ้ำ ใกล้ Colebrook ภายใน ~1% ในโจทย์ทั่วไป (คลาดสูงสุด ~3% ที่ขอบช่วง ใช้ได้ \(5000&lt;Re&lt;10^8\), \(10^{-6}&lt;\varepsilon/D&lt;10^{-2}\)) ไม่อยู่ในสไลด์ ใช้ตรวจคำตอบด้วยเครื่องคิดเลข</p>'''),
])

A += card('สมการที่จัดรูปไว้แล้ว (ประหยัดเวลา)', [
    row('หา v<br>ท่อเดี่ยว', r'''$$v=\sqrt{\frac{2g\,D\,h_f}{f\,L}},\qquad Q=vA$$<p class="nt">เมื่อโจทย์ให้ \(h_f\) (ไม่มี minor loss)</p>'''),
    row('หา v<br>ถัง → ปลายท่อ', r'''$$z_1-z_2=\Big[\,1+\sum K_L+f\,\frac{L}{D}\,\Big]\frac{v^2}{2g}$$$$v=\sqrt{\frac{2g\,(z_1-z_2)}{1+\sum K_L+f\,L/D}}$$<p class="nt">เมื่อ \(P_1=P_2=0\) และ \(v_1\approx0\) เลข 1 คือ \(v_2^2/2g\) ที่ปลายท่อปล่อยสู่อากาศ (ถ้าท่อไหลลงถัง \(v_2\approx0\) แต่มี \(K_{exit}=1\) ได้เลข 1 เท่ากัน) \(\sum K_L\) รวมปากท่อ ข้องอ วาล์ว แต่ไม่รวมทางออก ถ้า \(P_1\ne P_2\) ใช้ \(\dfrac{P_1-P_2}{\gamma}+(z_1-z_2)\) แทน \(z_1-z_2\)</p>'''),
    row('หา D', r'''$$D=\Big(\frac{8fLQ^2}{\pi^2 g\,h_f}\Big)^{1/5}$$<p class="nt">มาจากสูตรการสูญเสีย เมื่อไม่มี minor loss ผิดที่ \(f\) 10% ทำให้ \(D\) ผิดเพียง ~2%</p>'''),
    row('ท่อเอียง', r'''$$z_B-z_A=L\sin\theta\qquad(L=\textstyle\sum L_i)$$'''),
])

A += card('ท่อหลายเส้น', [
    row('อนุกรม', r'''$$Q_1=Q_2=Q_3=Q$$$$h_T=h_1+h_2+h_3$$$$v_i=\frac{4Q}{\pi D_i^2}$$$$h_i=\Big(f_i\frac{L_i}{D_i}+\sum K_i\Big)\frac{v_i^2}{2g}$$'''),
    row('ขนาน', r'''$$Q_T=Q_2+Q_3,\qquad h_2=h_3=h_{AB}$$<p class="nt">\(h\) ของวงขนานนับครั้งเดียว ไม่บวก \(h_2+h_3\)</p>'''),
    row('Q ของท่อขนาน<br>แต่ละเส้น', r'''$$Q_i=\frac{\pi}{4}D_i^2\sqrt{\frac{2g\,D_i\,h}{f_i\,L_i}}$$<p class="nt">รู้ \(h\) ร่วมของวงขนานแล้วหา \(Q_i\) ทีละเส้น (เดา \(f_i\) ของแต่ละเส้น) แล้วบวกกัน</p>'''),
    row('อ่างน้ำ 3 แห่ง', r'''$$\sum Q_{\text{เข้า}}=\sum Q_{\text{ออก}}\ \ (\text{ที่จุดต่อ})$$<p class="nt">สไลด์ระบุหัวข้อ Three-Reservoir System แต่ไม่มีตัวอย่างในไฟล์ที่ได้รับ: เดาเฮดที่จุดต่อ \(H_J\) หา \(Q\) ทุกท่อ (สูตร Q ของท่อขนานแต่ละเส้น) แล้วปรับ \(H_J\) จน \(\sum Q=0\)</p>'''),
])

A += card('ปั๊มและเทอร์ไบน์ (อยู่ในสไลด์ ch5 แต่ข้อ 1–8 ไม่ใช้)', [
    row('กำลังปั๊ม', r'''$$P=\rho g\,Q\,h_p=\gamma Q h_p$$<p class="nt">หน่วย W (1 hp = 745.7 W)</p>'''),
    row('เฮดที่ได้จริง', r'''$$\begin{aligned}H=h_p-h_L&=\frac{P_d-P_s}{\gamma}+(z_d-z_s)\\&\quad+\frac{v_d^2-v_s^2}{2g}\end{aligned}$$$$P_w=\gamma QH=Q\,\Delta P$$<p class="nt">\(s\) = ด้านดูด, \(d\) = ด้านส่ง ถ้าท่อสองด้านขนาดเท่ากัน พจน์ \(v\) ตัดกัน</p>'''),
    row('NPSH', r'''$$NPSH_A=\frac{P_{atm}}{\gamma}-z_1-h_{L,s}-\frac{P_v}{\gamma}$$$$NPSH_A\ge NPSH_R$$<p class="nt">\(z_1\) = ปั๊มสูงกว่าผิวน้ำด้านดูด ถ้า \(NPSH_A&lt;NPSH_R\) เกิด cavitation</p>'''),
    row('ปั๊มหลายตัว', r'''<p>ต่ออนุกรม: \(Q\) เท่าเดิม \(H\) บวกกัน &nbsp; ต่อขนาน: \(H\) เท่าเดิม \(Q\) บวกกัน จุดทำงาน (operating point) = จุดตัดของ pump curve กับ system curve</p>'''),
])

# ------------------------------------------------------------------ ส่วน ข
B = ''

B += '''<div class="tw"><table><caption>ตารางที่ ข1 ดูโจทย์แล้วจัดเป็นประเภทไหน</caption>
<thead><tr><th>โจทย์ให้</th><th>ถาม</th><th>ประเภท</th><th>เดา \\(f\\)?</th><th>ตัวอย่าง</th></tr></thead><tbody>
<tr><td>\\(v\\) หรือ \\(Q\\), \\(D\\), \\(\\rho\\), \\(\\mu\\)</td><td>Laminar/Turbulent, \\(v\\) สูงสุดของ Laminar</td><td>ชนิดการไหล (B1)</td><td>ไม่</td><td><a href="#q1">1</a> <a href="#q2">2ก</a></td></tr>
<tr><td>\\(v\\) หรือ \\(Q\\), \\(D\\), \\(L\\), \\(\\varepsilon\\) (+ \\(K\\))</td><td>\\(h_L\\), \\(\\Delta P\\), \\(P_1\\)</td><td>Type 1 / Case A (B2)</td><td>ไม่</td><td><a href="#q2">2ข-ค</a> <a href="#q3">3</a> <a href="#q4">4</a> <a href="#q5">5</a></td></tr>
<tr><td>\\(h_L\\) หรือ \\(\\Delta z\\), \\(D\\), \\(L\\), \\(\\varepsilon\\) (+ \\(K\\))</td><td>\\(v\\) หรือ \\(Q\\)</td><td>Type 2 / Case B (B3)</td><td><b>เดา</b></td><td><a href="#q6">6</a> <a href="#q7">7</a></td></tr>
<tr><td>\\(Q\\), \\(h_f\\), \\(L\\), \\(\\varepsilon\\)</td><td>\\(D\\)</td><td>Type 3 / Case C (B4)</td><td><b>เดา</b></td><td><a href="#q8">8</a></td></tr>
<tr><td>ท่อหลายขนาดต่อเรียงกัน</td><td>\\(v\\) ทุกท่อ หรือ \\(h\\) รวม</td><td>อนุกรม (B5)</td><td><b>เดาทุกท่อ</b></td><td><a href="#ea">สอบ A</a></td></tr>
<tr><td>ท่อแยกแล้วรวม</td><td>\\(h\\) รวม, \\(Q\\) รวม</td><td>ขนาน/โครงข่าย (B6)</td><td><b>เดาทุกท่อ</b></td><td><a href="#eb">สอบ B</a></td></tr>
<tr><td>มีปั๊มหรือเทอร์ไบน์</td><td>\\(h_p\\), กำลัง</td><td>พลังงาน + สูตรกำลังปั๊ม (B7)</td><td>ถ้ารู้ \\(Q\\) ไม่เดา</td><td></td></tr>
</tbody></table></div>'''

B += '''<h4 class="cardt">วงวนเดา f (ใช้ในประเภท 2, 3, อนุกรม, ขนาน)</h4>
<figure><svg viewBox="0 0 640 176" role="img" aria-label="วงวนการเดา f">
<defs><marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>
<g style="fill:var(--bg);stroke:var(--navy);stroke-width:1.8">
<rect x="6" y="34" width="112" height="62"/><rect x="134" y="34" width="112" height="62"/><rect x="262" y="34" width="112" height="62"/><rect x="390" y="34" width="112" height="62"/><rect x="518" y="34" width="112" height="62" style="stroke:var(--red)"/></g>
<g font-size="15" text-anchor="middle" style="fill:var(--ink)">
<text x="62" y="60">① เดา f</text><text x="62" y="82" font-size="13" fill="var(--gray)">ตาราง ค3 / 0.02</text>
<text x="190" y="60">② หา v (หรือ D)</text><text x="190" y="82" font-size="13" fill="var(--gray)">จากสูตรหา v / D</text>
<text x="318" y="60">③ คำนวณ Re</text><text x="318" y="82" font-size="13" fill="var(--gray)">และ ε/D</text>
<text x="446" y="60">④ อ่าน f ใหม่</text><text x="446" y="82" font-size="13" fill="var(--gray)">Moody / Colebrook</text>
<text x="574" y="60">⑤ เทียบ f</text><text x="574" y="82" font-size="13" fill="var(--gray)">ต่างเกิน 2% ?</text></g>
<g style="stroke:var(--navy);stroke-width:1.8;fill:none" marker-end="url(#ar2)">
<path d="M118 65H132"/><path d="M246 65H260"/><path d="M374 65H388"/><path d="M502 65H516"/></g>
<path d="M574 96V138H62V98" style="stroke:var(--red);stroke-width:1.8;fill:none" marker-end="url(#ar2)"/>
<text x="318" y="158" font-size="15" text-anchor="middle" style="fill:var(--red)">ไม่ตรง: ใช้ f ที่อ่านได้เป็นค่าเดารอบถัดไป</text>
<text x="574" y="22" font-size="15" text-anchor="middle" style="fill:var(--green)">ตรง: จบ ตอบข้อ</text>
</svg><figcaption>รูปที่ ข1 วงวนเดา \\(f\\) มักลู่เข้าใน 2–3 รอบ</figcaption></figure>'''

B += ty('B1 ชนิดการไหล และ Laminar (ข้อ 1, ข้อ 2 ก-ข)',
        '<b>ให้</b> \\(v\\) (หรือ \\(Q\\)), \\(D\\), ของไหล &nbsp;<b>ถาม</b> ชนิดการไหล / \\(v\\) สูงสุดที่ยัง Laminar / \\(\\Delta P\\)',
        [r'เขียนข้อมูล แปลงหน่วย ถ้าโจทย์ให้ \(\mu\) ใช้ \(\rho=1000\) (หรือ \(\nu=\mu/\rho\))',
         r'คำนวณ \(Re=\rho vD/\mu\) แล้วเทียบเกณฑ์ 2000 / 4000 เขียนผลว่า Laminar, Transitional หรือ Turbulent',
         r'ถามความเร็วสูงสุดที่ยังเป็น Laminar: ตั้ง \(Re=2000\) แล้วแก้ \(v_{max}=2000\,\mu/(\rho D)\)',
         r'ถามความดันลดและเป็น Laminar: \(f=64/Re\) แล้ว \(\Delta P=f\dfrac{L}{D}\dfrac{\rho v^2}{2}\) หรือ \(\Delta P=32\mu Lv/D^2\)',
         r'ถ้าเป็น Turbulent: หา \(\varepsilon/D\) แล้วอ่าน \(f\) จากชาร์ตก่อนใช้สูตร ΔP'],
        box('chk', 'ตรวจ', r'Laminar ให้ \(\Delta P\) น้อยมาก (ข้อ 2: 0.05 Pa) เทียบกับ Turbulent ที่ความเร็วสูงขึ้น (15 Pa) ตัวเลขห่างกันหลายเท่าเป็นเรื่องปกติ'))

B += ty('B2 Type 1 / Case A: รู้ Q หรือ v แล้วหา h<sub>L</sub>, ΔP, P (ไม่ต้องเดา) (ข้อ 2 ค, 3, 4, 5)',
        '<b>ให้</b> \\(Q\\) หรือ \\(v\\), \\(D\\), \\(L\\), \\(\\varepsilon\\), \\(K_L\\), ความสูง &nbsp;<b>ถาม</b> \\(h_L\\), \\(h_f\\), \\(h_m\\), \\(\\Delta P\\) หรือ \\(P_1\\)',
        [r'วาดรูปสั้น ๆ ตั้งจุด 1 (ต้นทาง) → จุด 2 (ปลายทาง) ตามทิศการไหล เลือก datum ผ่านจุดต่ำสุด (\(z=0\))',
         r'เขียนข้อมูล แปลงหน่วย: \(D\) เป็น m, \(P\) เป็น Pa, \(\varepsilon\) เป็น mm คู่กับ \(D\) เป็น mm เมื่อหา \(\varepsilon/D\)',
         r'หาความเร็วทุกท่อ \(v=4Q/\pi D^2\) และเฮดความเร็ว \(v^2/2g\) ของแต่ละท่อ',
         r'คำนวณ \(Re\) และ \(\varepsilon/D\) แล้วอ่าน \(f\) จาก Moody (ตรง ๆ ไม่ต้องเดา เพราะรู้ \(v\) แล้ว)',
         r'\(h_f=f\dfrac{L}{D}\dfrac{v^2}{2g}\) และ \(h_m=\sum K_L\dfrac{v^2}{2g}\) แล้วรวม \(h_L=h_f+h_m\)',
         r'เขียนสมการพลังงาน ขีดฆ่าพจน์ที่เป็นศูนย์หรือตัดกัน (ตาราง ง1) แล้วแทนค่าแก้หาตัวที่ถาม',
         r'ท่อเดียวกันตลอด (\(v_1=v_2\)): \(\dfrac{P_1}{\gamma}=\dfrac{P_2}{\gamma}+(z_2-z_1)+h_L\)  ท่อเปลี่ยนขนาด: เก็บพจน์ \(v^2/2g\) ของทั้งสองจุดไว้'],
        box('chk', 'ตรวจ', r'ไหลขึ้นเนินต้องได้ \(P_1>P_2\) และ \(h_L>0\) เสมอ ท่อยาวมาก \(h_f\gg h_m\) (ข้อ 4: 36.7 m เทียบ 0.52 m)'))

B += ty('B3 Type 2 / Case B: รู้ h แล้วหา v หรือ Q (ต้องเดา f) (ข้อ 6, 7)',
        '<b>ให้</b> \\(h_f\\) หรือ \\(\\Delta z\\), \\(D\\), \\(L\\), \\(\\varepsilon\\), \\(K_L\\) &nbsp;<b>ถาม</b> \\(v\\) หรือ \\(Q\\)',
        [r'เขียนข้อมูล แปลงหน่วย หา \(\varepsilon/D\) ก่อน (ค่านี้ไม่เปลี่ยนระหว่างวน)',
         r'<b>ท่อเดี่ยวไม่มี minor</b> (ข้อ 6): ใช้สูตรหา v ท่อเดี่ยว \(v=\sqrt{2gDh_f/fL}\)',
         r'<b>ระบบถังปล่อยสู่อากาศ</b> (ข้อ 7): เขียนสมการพลังงานผิวน้ำ → ปลายท่อ ตัด \(P_1=P_2=0\), \(v_1\approx0\) แล้วจัดเป็น \(z_1-z_2=[1+\sum K_L+fL/D]\,v^2/2g\) (เลข 1 คือ \(v_2^2/2g\))',
         r'เดา \(f_1\) จากตาราง ค3 (หรือ 0.02) แล้วหา \(v_1\)',
         r'คำนวณ \(Re=vD/\nu\) → อ่าน \(f\) จาก Moody ที่ \(\varepsilon/D\) เดิม',
         r'ถ้า \(f\) ที่อ่านไม่เท่า \(f\) ที่เดา (ต่างเกิน ~2%) ให้ใช้ \(f\) ที่อ่านเป็นค่าเดารอบใหม่ เขียนเป็นตาราง เดา → \(v\) → \(Re\) → \(f_{\text{Moody}}\) → ตรง/ไม่ตรง',
         r'เมื่อตรงกันแล้วจึงตอบ \(v\) (ถ้าถาม \(Q\) คูณ \(A\) ด้วย)'],
        box('trap', 'จุดดัก', r'\(\Delta z=z_1-z_2\) คือผิวน้ำเหนือ<b>ปลายท่อ</b> ไม่ใช่ความสูงถัง (ข้อ 7: 15 − 10 = 5 m) และเลข 1 ของปลายท่อห้ามลืม'))

B += ty('B4 Type 3 / Case C: รู้ Q แล้วหา D (ต้องเดา f) (ข้อ 8)',
        '<b>ให้</b> \\(Q\\), \\(h_f\\), \\(L\\), \\(\\varepsilon\\) &nbsp;<b>ถาม</b> \\(D\\)',
        [r'เขียนข้อมูล แปลงหน่วย จัดสมการเป็น \(D=(8fLQ^2/\pi^2 g h_f)^{1/5}\)',
         r'เดา \(f_1\) แล้วหา \(D_1\)',
         r'ใช้ \(D_1\) คำนวณ \(v=4Q/\pi D_1^2\), \(Re=vD_1/\nu\) และ \(\varepsilon/D_1\) (<b>ต้องคำนวณใหม่ทุกรอบเพราะ \(D\) เปลี่ยน</b>) แล้วอ่าน \(f\) ใหม่',
         r'วนจน \(f\) ตรงกัน แล้วตอบ \(D\) (ปัดตามที่โจทย์ต้องการ เช่น 0.365 ≈ 0.36 m หรือปัดขึ้นเป็นขนาดท่อที่มี)'],
        box('chk', 'ตรวจ', r'\(D\) ไวต่อ \(f\) น้อย (ยกกำลัง 1/5) จึงลู่เข้าเร็ว ปัดขึ้นปลอดภัยกว่าปัดลงเพราะ \(h_f\) ลดลงเมื่อ \(D\) โตขึ้น'))

B += ty('B5 ท่ออนุกรมหลายขนาด (ข้อสอบ A)',
        '<b>ให้</b> ท่อหลายเส้นต่อเรียงกัน แต่ละเส้นมี \\(D_i\\), \\(L_i\\), \\(\\varepsilon_i\\) &nbsp;<b>ถาม</b> \\(v\\) ในแต่ละท่อ หรือ \\(h\\) รวม',
        [r'ท่ออนุกรมมี \(Q\) เท่ากันทุกเส้น จึงเขียน \(v_2=v_1(D_1/D_2)^2\), \(v_3=v_1(D_1/D_3)^2\) ให้ทุกอย่างอยู่ในรูป \(v_1\) ตัวเดียว',
         r'ทำตารางข้อมูล: \(D_i\), \(L_i\), \(\varepsilon_i/D_i\) ของทุกท่อ',
         r'สมการพลังงาน A → B: \(z_B-z_A=L\sin\theta\) (ท่อเอียง) และ \(h_L=\sum f_i\dfrac{L_i}{D_i}\dfrac{v_i^2}{2g}\)',
         r'เดา \(f_1,f_2,f_3\) พร้อมกัน แก้หา \(v_1\) แล้วหา \(v_2,v_3\)',
         r'คำนวณ \(Re_i\) และอ่าน \(f_i\) <b>ของทั้งสามท่อ</b> เทียบกับที่เดา วนซ้ำจนทั้งสามตรง',
         r'ตอบ \(v_i\) (และ \(Q=v_1A_1\) ถ้าถาม)'],
        box('trap', 'จุดดัก', r'ท่อแต่ละเส้นมี \(\varepsilon/D\) คนละค่า จึงต้องอ่านชาร์ตแยกเส้น และห้ามใช้ \(v_1\) กับท่อ 2, 3'))

B += ty('B6 ท่อขนานและโครงข่าย (ข้อสอบ B)',
        '<b>ให้</b> ท่อแยกเป็นหลายเส้นแล้วรวมกลับ พร้อม \\(D_i\\), \\(L_i\\), \\(\\varepsilon_i\\) และค่าใดค่าหนึ่ง เช่น \\(h\\) ของท่อขนาน &nbsp;<b>ถาม</b> \\(h\\) รวม หรือ \\(Q\\) รวม',
        [r'วาดผังว่าเส้นไหน<b>อนุกรม</b> (ท่อ 1, 4) เส้นไหน<b>ขนาน</b> (ท่อ 2, 3)',
         r'วงขนานมี \(h_2=h_3=h\) ร่วมกัน ใช้ \(h\) ที่โจทย์ให้ หา \(Q_2\) และ \(Q_3\) แยกกันด้วยสูตร Q ของท่อขนาน (เดา \(f_2\), \(f_3\) ของแต่ละเส้น)',
         r'\(Q_T=Q_2+Q_3\) แล้วท่ออนุกรม \(Q_1=Q_4=Q_T\) หา \(v=Q/A\) → \(Re\) → \(f\) → \(h_1,h_4\)',
         r'\(h_{\text{รวม}}=h_1+h_2+h_4\) (นับวงขนานครั้งเดียว)',
         r'ตรวจ \(Q_2+Q_3=Q_1=Q_4\) ว่าสมดุล'],
        box('trap', 'จุดดัก', r'ห้ามบวก \(h_3\) ซ้ำ ท่อขนานแบ่ง \(Q\) ไม่แบ่ง \(h\) และท่อที่ใหญ่กว่า สั้นกว่า รับ \(Q\) มากกว่า'))

B += ty('B7 ระบบที่มีปั๊มหรือเทอร์ไบน์ (ถ้าเจอ)',
        '<b>ให้</b> ระบบท่อพร้อมปั๊ม &nbsp;<b>ถาม</b> เฮดของปั๊ม \\(h_p\\) หรือกำลัง',
        [r'ทำเหมือน Type 1 จนได้ \(h_L\) (รู้ \(Q\) จึงไม่ต้องเดา)',
         r'เขียนสมการพลังงานมีพจน์ \(h_p\) ฝั่งจุดต้นทาง แล้วแก้หา \(h_p\)',
         r'กำลัง \(P=\gamma Q h_p\) แปลงเป็น hp ด้วย 745.7 ถ้าโจทย์ถามเป็นแรงม้า',
         r'ถามเรื่อง cavitation: คำนวณ \(NPSH_A\) เทียบกับ \(NPSH_R\) ที่โจทย์ให้'],
        '')

# ------------------------------------------------------------------ ส่วน ค
C = ''

C += '''<div class="tw"><table><caption>ตารางที่ ค1 ค่า \\(K_L\\) ของจุดเปลี่ยน (ตามสไลด์ ch5) &nbsp;\\(h_m=K_L\\,v^2/2g\\)</caption>
<thead><tr><th>จุดที่เกิด</th><th>\\(K_L\\)</th><th>ใช้ \\(v\\) ของท่อ</th></tr></thead><tbody>
<tr><td>ปากท่อจากอ่าง: Reentrant</td><td>0.8</td><td>ท่อที่ต่อจากอ่าง</td></tr>
<tr><td>ปากท่อ: Sharp-edged (ขอบคม)</td><td>0.5</td><td>ท่อที่ต่อจากอ่าง</td></tr>
<tr><td>ปากท่อ: Slightly rounded</td><td>0.2</td><td>ท่อที่ต่อจากอ่าง</td></tr>
<tr><td>ปากท่อ: Well-rounded</td><td>0.04</td><td>ท่อที่ต่อจากอ่าง</td></tr>
<tr><td>ท่อไหลลงอ่าง (ทุกแบบ)</td><td>1.0</td><td>ท่อที่ไหลออก</td></tr>
<tr><td>Sudden expansion</td><td>\\((1-A_1/A_2)^2\\) หรืออ่านกราฟ</td><td><b>ท่อเล็ก</b> (\\(v_1\\) ก่อนขยาย)</td></tr>
<tr><td>Sudden contraction</td><td>อ่านกราฟตาม \\(A_2/A_1\\) (ตารางที่ ค2)</td><td><b>ท่อเล็ก</b> (\\(v_2\\) หลังหด)</td></tr>
<tr><td>Elbow 90° Regular: flanged / threaded</td><td>0.3 / 1.5</td><td>ท่อนั้น</td></tr>
<tr><td>Elbow 90° Long radius: flanged / threaded</td><td>0.2 / 0.7</td><td>ท่อนั้น</td></tr>
<tr><td>Elbow 45°: Long radius flanged / Regular flanged</td><td>0.2 / 0.4</td><td>ท่อนั้น</td></tr>
<tr><td>180° return bend: flanged / threaded</td><td>0.2 / 1.5</td><td>ท่อนั้น</td></tr>
<tr><td>Tee line flow: flanged / threaded</td><td>0.2 / 0.9</td><td>ท่อนั้น</td></tr>
<tr><td>Tee branch flow: flanged / threaded</td><td>1.0 / 2.0</td><td>ท่อนั้น</td></tr>
<tr><td>Union, threaded</td><td>0.08</td><td>ท่อนั้น</td></tr>
</tbody></table></div>
<div class="tw"><table><caption>ตารางที่ ค2 กราฟ Sudden contraction (อ่านจากสไลด์ ±0.03) และ Sudden expansion</caption>
<thead><tr><th>อัตราส่วนพื้นที่</th><th>0</th><th>0.2</th><th>0.4</th><th>0.6</th><th>0.8</th><th>1.0</th></tr></thead><tbody>
<tr><td>contraction \\(K_L\\) ที่ \\(A_2/A_1\\)</td><td>0.50</td><td>0.45</td><td>0.34</td><td>0.18</td><td>0.06</td><td>0</td></tr>
<tr><td>expansion \\(K_L=(1-A_1/A_2)^2\\)</td><td>1.00</td><td>0.64</td><td>0.36</td><td>0.16</td><td>0.04</td><td>0</td></tr>
</tbody></table></div>
<div class="tw"><table><caption>ตารางที่ ค2ก วาล์ว (ตามสไลด์ ch5)</caption>
<thead><tr><th colspan="5">Gate valve: เปิดอยู่ \\(w/D\\) (0 = เปิดเต็ม)</th></tr>
<tr><th>\\(w/D\\)</th><th>0</th><th>0.25</th><th>0.50</th><th>0.75</th></tr></thead><tbody>
<tr><td>\\(K\\)</td><td>0.2</td><td>0.9</td><td>4.5</td><td>24.0</td></tr></tbody>
<thead><tr><th colspan="9">Butterfly valve (สไลด์ตั้งชื่อ Test Tap) มุม \\(\\alpha\\)</th></tr>
<tr><th>\\(\\alpha\\)</th><th>5°</th><th>10°</th><th>20°</th><th>30°</th><th>40°</th><th>50°</th><th>60°</th><th>70°</th></tr></thead><tbody>
<tr><td>\\(K\\)</td><td>0.05</td><td>0.29</td><td>1.56</td><td>5.47</td><td>17.3</td><td>52.6</td><td>206</td><td>486</td></tr></tbody></table></div>'''

C += '''<div class="tw"><table><caption>ตารางที่ ค3 ค่า \\(f\\) ที่ควรเดารอบแรก (fully rough จากสูตร fully rough; ค่าจริงจะต่ำกว่าเล็กน้อยถ้า \\(Re\\) ไม่สูงมาก)</caption>
<thead><tr><th>\\(\\varepsilon/D\\)</th><th>0.0002</th><th>0.0003</th><th>0.0005</th><th>0.0008</th><th>0.001</th><th>0.0015</th><th>0.002</th><th>0.003</th><th>0.005</th><th>0.01</th><th>0.02</th></tr></thead><tbody>
<tr><td>\\(f\\)</td><td>0.0137</td><td>0.0149</td><td>0.0167</td><td>0.0186</td><td>0.0196</td><td>0.0217</td><td>0.0234</td><td>0.0262</td><td>0.0304</td><td>0.0379</td><td>0.0486</td></tr>
</tbody></table></div>'''

C += '''<div class="tw"><table><caption>ตารางที่ ค4 ค่า \\(\\varepsilon\\) ของวัสดุทั่วไป (ใช้เมื่อโจทย์ไม่ให้ ค่าที่โจทย์ให้มาก่อนเสมอ)</caption>
<thead><tr><th>วัสดุท่อ</th><th>\\(\\varepsilon\\) (mm)</th></tr></thead><tbody>
<tr><td>Drawn tubing, พลาสติก/แก้ว (เรียบมาก)</td><td>0.0015 (หรือ ≈ 0)</td></tr>
<tr><td>Commercial steel / Wrought iron</td><td>0.045</td></tr>
<tr><td>Asphalted cast iron</td><td>0.12</td></tr>
<tr><td>Galvanized iron</td><td>0.15</td></tr>
<tr><td>Cast iron</td><td>0.26</td></tr>
<tr><td>Wood stave</td><td>0.18–0.9</td></tr>
<tr><td>Concrete</td><td>0.3–3</td></tr>
<tr><td>Riveted steel</td><td>0.9–9</td></tr>
</tbody></table></div>'''

# ------------------------------------------------------------------ ส่วน ง
D = ''

D += card('ตารางขีดฆ่าพจน์ในสมการพลังงาน (ตาราง ง1)', [
    row('ผิวน้ำถังใหญ่', r'''\(v\approx0\) และ \(P=0\) (เกจ) ถ้าผิวเปิดสู่อากาศ'''),
    row('ปลายท่อปล่อยสู่อากาศ', r'''\(P_2=0\) แต่ \(v_2\ne0\): ต้องเก็บ \(v_2^2/2g\) ไว้ (ห้ามขีดฆ่า)'''),
    row('ปลายท่อจมน้ำ / ไหลลงถัง', r'''\(v_2\approx0\) แต่เพิ่ม \(K_{exit}=1\) ที่ \(v\) ของท่อ'''),
    row('ท่อขนาดเท่ากันตลอด', r'''\(v_1=v_2\) จึงตัด \(v^2/2g\) ของสองจุดได้ (ถ้า \(D\) ต่างกัน ห้ามตัด)'''),
    row('ท่อราบ', r'''\(z_1=z_2\) ตัดพจน์ความสูง'''),
    row('ไม่มีเครื่องกล', r'''\(h_p=h_t=0\)'''),
    row('เลือก datum', r'''ให้ผ่านจุดต่ำสุด เพื่อให้ \(z\) เป็นบวกหมดและแทนค่าง่าย'''),
])

D += '''<h4 class="cardt">ลำดับที่เขียนในห้องสอบ</h4>
<ol class="st wr">
<li>เขียน<b>ข้อมูล</b>ที่ให้ พร้อมแปลงหน่วย (mm → m, cm → m, kPa → Pa) และค่าคงที่ที่ใช้ (\\(\\gamma\\), \\(\\nu\\))</li>
<li>เขียน<b>สมการพลังงาน</b>จุด 1 → 2 ในรูปทั่วไปก่อนแทนค่า</li>
<li><b>ขีดฆ่า</b>พจน์ที่เป็นศูนย์ พร้อมเหตุผลสั้น ๆ (ตาราง ง1)</li>
<li>เขียนสมการ \\(h_L=h_f+h_m\\) และรวม \\(\\sum K_L\\) เป็นก้อนเดียว</li>
<li>คำนวณ \\(\\varepsilon/D\\) แล้วเขียนสมการที่ต้องแก้ ถ้าต้องเดา ให้จัดรูปเป็น \\(v=\\ldots f\\)</li>
<li>ทำตารางเดา: <b>1<sup>st</sup> guess</b> → \\(v\\) → \\(Re\\) → \\(f_{\\text{Moody}}\\) → เขียน <span class="no">No</span> หรือ <span class="ok">OK</span></li>
<li>ตอบพร้อม<b>หน่วย</b> กรอบหรือขีดเส้นใต้ ตรวจว่า \\(Re\\) กับ \\(f\\) รอบสุดท้ายตรงกันจริง</li>
</ol>'''

D += '''<h4 class="cardt">จุดดักที่ทำให้เสียคะแนนบ่อย</h4>''' + ''.join([
    box('trap', 'แปลงหน่วย', r'\(\varepsilon\) เป็น mm แต่ \(D\) เป็น m ต้องหารหน่วยเดียวกัน \(0.12\ \text{mm}/150\ \text{mm}=0.0008\) ความดัน kPa × 1000 ก่อนหารด้วย \(\gamma\)'),
    box('trap', 'ท่อเปลี่ยนขนาด ต้องหา v ทุกท่อน', r'\(v_2=v_1(D_1/D_2)^2\) ห้ามใช้ \(v_1\) กับท่อ 2 และ \(v^2/2g\) ของสองจุดไม่ตัดกันเมื่อ \(D\) ต่างกัน'),
    box('trap', 'ปล่อยสู่อากาศ ต้องมี v²/2g ที่ปลายท่อ', r'\(P_2=0\) แต่ \(v_2\ne0\) เป็นเลข 1 ในวงเล็บของสูตรหา v จากถัง แยกจาก \(\sum K_L\)'),
    box('trap', 'เครื่องหมายของ z', r'ไหลขึ้นเนิน \(z_2>z_1\) ย้ายข้างแล้วต้องเป็นลบ \(\dfrac{P_1-P_2}{\gamma}-(z_2-z_1)=h_L\) หรือจัดเป็น \(\dfrac{P_1}{\gamma}=\dfrac{P_2}{\gamma}+(z_2-z_1)+h_L\)'),
    box('trap', 'K ใช้ v ของท่อไหน', r'ขยาย/หดฉับพลันใช้ \(v\) ของ<b>ท่อเล็ก</b> ปากท่อเข้า/ข้องอใช้ \(v\) ของท่อนั้น'),
    box('trap', 'ท่อขนาน อย่าบวก h', r'\(h_{\text{รวม}}=h_1+h_2+h_4\) ไม่ใช่ \(h_2+h_3\)'),
    box('trap', 'ตรวจ f รอบสุดท้าย', r'\(f\) ที่เดาต้องตรงกับ \(f\) จากชาร์ตที่ \(Re\) รอบสุดท้าย ถ้าต่างเกิน ~2% ทำอีกรอบ และตรวจก่อนว่าเป็น Laminar หรือ Turbulent เพราะใช้ \(f\) คนละสูตร'),
])

D += '''<h4 class="cardt">ตรวจความสมเหตุสมผลก่อนส่ง</h4>
<div class="tw"><table>
<thead><tr><th>ตัวเลข</th><th>ช่วงปกติ</th><th>ถ้าหลุดช่วง</th></tr></thead><tbody>
<tr><td>\\(f\\) (Turbulent)</td><td>0.01 – 0.05 (ท่อขรุขระมากถึง ~0.07)</td><td>อ่านชาร์ตผิดแถว หรือ \\(\\varepsilon/D\\) ผิดหน่วย</td></tr>
<tr><td>\\(v\\) น้ำในท่อ</td><td>ประมาณ 0.5 – 5 m/s</td><td>เช็ค \\(D\\) (cm/m) และ \\(Q\\)</td></tr>
<tr><td>\\(Re\\)</td><td>\\(10^4\\) – \\(10^7\\) ในโจทย์ส่วนใหญ่</td><td>เช็ค \\(\\nu\\) หรือ \\(\\mu\\)</td></tr>
<tr><td>\\(h_L\\), \\(h_f\\), \\(h_m\\)</td><td>เป็นบวกเสมอ \\(h_m\\ll h_f\\) เมื่อท่อยาว</td><td>เช็คเครื่องหมายสมการพลังงาน</td></tr>
<tr><td>\\(P\\) ต้นทางเทียบปลายทาง</td><td>ต้นทาง \\(>\\) ปลายทาง เมื่อไหลขึ้นเนิน</td><td>เช็ค \\(z\\) และเครื่องหมาย</td></tr>
</tbody></table></div>'''

# ------------------------------------------------------------------ รวม
CHEAT = f'''<section id="sum">
<h2 class="prob"><span class="tag">สรุป</span>สรุปสูตรและแนวทางทำโจทย์การไหลในท่อ</h2>
<div class="stmt"><p>หน้านี้รวมสูตรทั้งหมดของบทที่ 5 และขั้นตอนทำโจทย์แต่ละประเภท อ้างอิงสไลด์ ch5 ของอาจารย์ เริ่มจากสูตร แล้วตามด้วยขั้นตอนทำโจทย์แต่ละประเภท ตาราง และจุดดัก ก่อนถึงเฉลยข้อ 1–8 ด้านล่าง</p></div>
<div class="jump"><a href="#sum-a">ก. สรุปสูตร</a><a href="#sum-b">ข. ขั้นตอนแต่ละประเภท</a><a href="#sum-c">ค. ตารางค่าอ้างอิง</a><a href="#sum-d">ง. ห้องสอบและจุดดัก</a></div>
<h3 class="grp" id="sum-a">ก. สรุปสูตร</h3>
{A}
<h3 class="grp" id="sum-b">ข. ขั้นตอนทำโจทย์แต่ละประเภท</h3>
{B}
<h3 class="grp" id="sum-c">ค. ตารางค่าอ้างอิง</h3>
{C}
<h3 class="grp" id="sum-d">ง. วิธีเขียนในห้องสอบ และจุดดัก</h3>
{D}
</section>'''

CHEAT_CSS = '''
.jump{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
.jump a{border:1.5px solid var(--navy);color:var(--navy);padding:2px 14px;text-decoration:none;font-weight:500}
.jump a:hover{background:var(--hover)}
h3.grp{font-size:22px;margin:42px 0 6px;padding-top:8px;border-top:3px double var(--ink);color:var(--navy);scroll-margin-top:52px}
h4.cardt{font-size:18.5px;margin:26px 0 6px;color:var(--ink)}
.exam .nt{font-size:16px;color:var(--gray);margin:2px 0 8px;line-height:1.7}
.ty{border:1.5px solid var(--ink);margin:16px 0 22px}
.tyh{background:var(--hover);padding:6px 16px;border-bottom:1.5px solid var(--ink);font-weight:700;color:var(--navy)}
.tyb{padding:8px 18px 14px}
.tyb .gq{color:var(--blue);margin:4px 0 8px}
ol.st{padding-left:1.7em;margin:6px 0 10px}ol.st li{margin:0 0 7px;padding-left:4px}
.bx{border-left:4px solid var(--gold);padding:2px 14px;margin:10px 0;background:var(--hover)}
.bx>b{display:inline-block;margin-right:.5em}.bx>div{display:inline}
.bx.trap{border-left-color:var(--red)}.bx.chk{border-left-color:var(--green)}
.tyb .bx{margin:8px 0 0}
.katex{position:relative}
@media(max-width:520px){main{padding-left:14px;padding-right:14px}.exam{padding:4px 12px 14px}.exam .katex{font-size:1.02em}.tyb{padding:6px 12px 12px}ol.st{padding-left:1.4em}.bx{padding:2px 10px}}
'''
