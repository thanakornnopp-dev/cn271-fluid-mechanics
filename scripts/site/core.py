# -*- coding: utf-8 -*-
"""ข้อ 1-8 และโจทย์ 15 คะแนน A, B (เฉลยวิธีทำ + เฉลยละเอียด)"""
import re, pathlib
from common import *

FIG_Q3 = figure('''<svg viewBox="0 0 640 230" role="img" aria-label="ท่อสามขนาด">
<line x1="20" y1="190" x2="620" y2="190" style="stroke:var(--ink);stroke-dasharray:6 5"/>
<path d="M30 190H125C145 190 145 130 165 130H215" style="stroke:var(--navy);fill:none;stroke-width:6"/>
<path d="M215 130H265C285 130 285 170 305 170H345" style="stroke:var(--navy);fill:none;stroke-width:12"/>
<path d="M345 170H600" style="stroke:var(--navy);fill:none;stroke-width:18"/>
<text x="40" y="176" font-size="15" fill="var(--blue)">① D=10 cm</text><text x="40" y="214" font-size="15" fill="var(--blue)">P₁=100 kPa, z₁=0</text>
<text x="165" y="112" font-size="15" fill="var(--blue)">② D=20 cm</text><text x="165" y="96" font-size="15" fill="var(--blue)">P₂=50 kPa</text>
<text x="380" y="146" font-size="15" fill="var(--blue)">③ D=30 cm</text><text x="380" y="214" font-size="15" fill="var(--blue)">P₃=20 kPa</text>
<line x1="150" y1="190" x2="150" y2="134" stroke="var(--red)" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="100" y="168" font-size="15" fill="var(--red)">3 m</text>
<line x1="470" y1="190" x2="470" y2="174" stroke="var(--red)" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="478" y="186" font-size="15" fill="var(--red)">1 m</text>
</svg>''', 'รูปที่ 1 ท่อสามขนาดต่างระดับ (ไม่ตามมาตราส่วน)')

FIG_Q4 = figure(pipesvg(60, '2 m', 'K=0.5'), 'รูปที่ 1 ท่อยกสูง 2 m มีข้องอ 2 ตัว (ไม่ตามมาตราส่วน)')
FIG_Q5 = figure(pipesvg(130, '20 m', 'K=0.3'), 'รูปที่ 1 ท่อยกสูง 20 m มีข้องอ 90° 2 ตัว (ไม่ตามมาตราส่วน)')

FIG_EA = figure('''<svg viewBox="0 0 640 230" role="img" aria-label="ท่อสามท่อต่ออนุกรมเอียง 5 องศา">
<line x1="30" y1="200" x2="600" y2="200" style="stroke:var(--ink);stroke-dasharray:6 5"/>
<path d="M50 188L210 154" style="stroke:var(--navy);fill:none;stroke-width:8"/>
<path d="M210 154L400 112" style="stroke:var(--navy);fill:none;stroke-width:14"/>
<path d="M400 112L570 76" style="stroke:var(--navy);fill:none;stroke-width:5"/>
<circle cx="50" cy="188" r="13" style="fill:var(--bg);stroke:var(--ink)"/><text x="45" y="193" font-size="15" fill="var(--ink)">A</text>
<circle cx="570" cy="76" r="13" style="fill:var(--bg);stroke:var(--ink)"/><text x="565" y="81" font-size="15" fill="var(--ink)">B</text>
<text x="100" y="156" font-size="15" fill="var(--blue)">ท่อ 1</text><text x="290" y="110" font-size="15" fill="var(--blue)">ท่อ 2</text><text x="470" y="78" font-size="15" fill="var(--blue)">ท่อ 3</text>
<path d="M130 200A80 80 0 0 0 126 190" style="stroke:var(--red);fill:none"/><text x="140" y="196" font-size="15" fill="var(--red)">θ = 5°</text>
<line x1="598" y1="200" x2="598" y2="76" stroke="var(--red)" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="530" y="150" font-size="15" fill="var(--red)">z_B = 280 sin 5°</text>
<text x="60" y="224" font-size="15" fill="var(--green)">L₁=80 + L₂=120 + L₃=80 = 280 m</text>
</svg>''', 'รูปที่ 1 ท่อสามท่อต่ออนุกรม เอียงขึ้นจาก A ไป B (ไม่ตามมาตราส่วน)')

FIG_EB = figure('''<svg viewBox="0 0 640 200" role="img" aria-label="ท่อ 1 แยกเป็นท่อ 2 กับ 3 ขนานกัน แล้วรวมเป็นท่อ 4">
<path d="M20 100H160" style="stroke:var(--navy);fill:none;stroke-width:8"/>
<path d="M160 100C190 40 290 40 320 100" style="stroke:var(--navy);fill:none;stroke-width:4"/>
<path d="M160 100C190 160 290 160 320 100" style="stroke:var(--navy);fill:none;stroke-width:6"/>
<path d="M320 100H560" style="stroke:var(--navy);fill:none;stroke-width:4"/>
<text x="20" y="84" font-size="15" fill="var(--ink)">AA</text><text x="76" y="124" font-size="15" fill="var(--blue)">ท่อ 1</text>
<text x="226" y="52" font-size="15" fill="var(--blue)">ท่อ 2</text><text x="226" y="164" font-size="15" fill="var(--blue)">ท่อ 3</text>
<text x="420" y="124" font-size="15" fill="var(--blue)">ท่อ 4</text><text x="580" y="84" font-size="15" fill="var(--ink)">BB</text>
<circle cx="360" cy="100" r="12" style="fill:var(--bg);stroke:var(--ink)"/><text x="355" y="105" font-size="15" fill="var(--ink)">A</text>
<circle cx="480" cy="100" r="12" style="fill:var(--bg);stroke:var(--ink)"/><text x="475" y="105" font-size="15" fill="var(--ink)">B</text>
<text x="205" y="22" font-size="15" fill="var(--red)">h₂ = h₃ = 0.42 m</text><text x="352" y="62" font-size="15" fill="var(--green)">L_AB = 300 m, z_B − z_A = 10 m</text>
</svg>''', 'รูปที่ 1 โครงข่ายท่อ 4 เส้น (ไม่ตามมาตราส่วน)')

# ---------------------------------------------------------------- Q1
Q1 = sec('q1', 'ข้อ 1', 'Laminar หรือ Turbulent? และความเร็วสูงสุดที่ยังเป็น Laminar',
r'''<p>น้ำไหลในท่อเส้นผ่านศูนย์กลาง 10 cm ด้วยความเร็ว 0.1 m/s ความหนืดสัมบูรณ์ \(\mu=10^{-3}\) N·s/m² จงหาว่าการไหลเป็นแบบ Laminar หรือ Turbulent ถ้าเป็น Turbulent ความเร็วสูงสุดที่ทำให้เป็น Laminar เท่าไร</p>''', '',
[row('ข้อมูล', r'''$$D=0.1\ \text{m},\quad v=0.1\ \text{m/s}$$$$\mu=10^{-3}\ \text{N}\!\cdot\!\text{s/m}^2,\quad \rho=1000\ \text{kg/m}^3$$''', 'given'),
 row('Reynolds number', r'''$$Re=\frac{\rho vD}{\mu}=\frac{(1000)(0.1)(0.1)}{10^{-3}}=10{,}000$$$$Re>4000\ \Rightarrow\ \text{Turbulent}$$'''),
 row('v สูงสุดของ Laminar<br>(ตั้ง Re = 2000)', r'''$$2000=\frac{(1000)\,v\,(0.1)}{10^{-3}}\ \Rightarrow\ v=\frac{2000}{10^{5}}=0.02\ \text{m/s}$$'''),
 fin(r'''Turbulent (\(Re=10{,}000\)),\ \(v_{max}=0.02\ \text{m/s}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> โจทย์ถามชนิดการไหล ซึ่งตัดสินด้วยเลขเรย์โนลด์ส \(Re\) เราจึงคิดย้อนว่าต้องรู้ \(Re\) แล้วเทียบกับเกณฑ์ ส่วนข้อถามที่สองคือแก้สมการ \(Re\) ย้อนกลับหา \(v\)</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> เขียนนิยามของ \(Re\) และเกณฑ์ตัดสินชนิดการไหล</p><p><b class="l">ขั้นที่ 2:</b> คำนวณ \(Re\) จากข้อมูลที่ให้ แล้วเทียบเกณฑ์</p><p><b class="l">ขั้นที่ 3:</b> ตั้ง \(Re=2000\) แล้วแก้หา \(v\) ที่ขอบของ Laminar</p></div>
<h4>ขั้นที่ 1: นิยามของ Reynolds number และเกณฑ์</h4>
<p>เลขเรย์โนลด์สเป็นอัตราส่วนของแรงเฉื่อยต่อแรงหนืด ไม่มีหน่วย</p>
$$Re=\frac{\rho vD}{\mu}\tag{1}$$
$$Re<2000:\ \text{Laminar},\qquad 2000\le Re\le4000:\ \text{Transitional},\qquad Re>4000:\ \text{Turbulent}\tag{2}$$
<h4>ขั้นที่ 2: คำนวณ Re จากข้อมูลโจทย์</h4>
<p>แทน \(\rho=1000\) kg/m³ (น้ำ), \(v=0.1\) m/s, \(D=0.1\) m และ \(\mu=10^{-3}\) N·s/m² ลงใน (1)</p>
$$Re=\frac{(1000)(0.1)(0.1)}{10^{-3}}=\frac{10}{10^{-3}}=10{,}000\tag{3}$$
<p>เนื่องจาก \(Re=10{,}000>4000\) การไหลเป็นแบบ <b>Turbulent</b></p>
<h4>ขั้นที่ 3: ความเร็วสูงสุดที่ยังเป็น Laminar</h4>
<p>ขอบบนของ Laminar คือ \(Re=2000\) ตั้ง (1) เท่ากับค่านี้แล้วแก้หา \(v\)</p>
$$2000=\frac{(1000)\,v\,(0.1)}{10^{-3}}=10^{5}\,v\tag{4}$$
$$v_{max}=\frac{2000}{10^{5}}=0.02\ \text{m/s}\tag{5}$$
<p><b>ตรวจสอบ:</b> แทน \(v=0.02\) m/s กลับใน (1) ได้ \(Re=2000\) พอดี และความเร็วจริง 0.1 m/s เป็น 5 เท่าของค่านี้ จึงเป็น Turbulent สอดคล้องกัน</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(Re=10{,}000\) (Turbulent) และ \(v_{max}=0.02\) m/s</p>''')

# ---------------------------------------------------------------- Q2
Q2 = sec('q2', 'ข้อ 2', 'ความดันลด ΔP ในท่อราบ: Laminar เทียบกับ Turbulent',
r'''<p>น้ำไหลในท่อเส้นผ่านศูนย์กลาง 8 cm ด้วยความเร็วเฉลี่ย 0.02 m/s (ก) จงหาว่าไหลแบบ Laminar หรือ Turbulent (ข) จงหาความดันที่ลดลงในระยะ 0.5 m (ค) ถ้าท่อเป็นพลาสติก (\(\varepsilon=0.12\) mm) จงหาความดันที่ลดลงในระยะ 0.1 m เมื่อความเร็วเพิ่มเป็น 1 m/s</p>''', '',
[row('ข้อมูล', r'''$$D=0.08\ \text{m},\quad \mu=10^{-3}\ \text{N}\!\cdot\!\text{s/m}^2,\quad \rho=1000\ \text{kg/m}^3$$''', 'given'),
 row('(ก) Re', r'''$$Re=\frac{\rho vD}{\mu}=\frac{(1000)(0.02)(0.08)}{10^{-3}}=1600<2000\ \Rightarrow\ \text{Laminar}$$'''),
 row('(ข) สมการพลังงาน<br>ท่อราบ ขนาดคงที่', r'''$$\frac{P_1}{\gamma}+\frac{v^2}{2g}+z=\frac{P_2}{\gamma}+\frac{v^2}{2g}+z+h_L\ \Rightarrow\ \frac{\Delta P}{\gamma}=f\frac{L}{D}\frac{v^2}{2g}$$$$\Delta P=f\,\frac{L}{D}\,\frac{\rho v^2}{2}$$'''),
 row('(ข) แทนค่า', r'''$$f=\frac{64}{Re}=\frac{64}{1600}=0.04$$$$\Delta P=(0.04)\frac{0.5}{0.08}\,\frac{(1000)(0.02)^2}{2}=0.05\ \text{Pa}$$'''),
 row('(ค) Re ใหม่, ε/D', r'''$$Re=\frac{(1000)(1)(0.08)}{10^{-3}}=8\times10^{4}\ (\text{Turbulent}),\qquad \frac{\varepsilon}{D}=\frac{0.12}{80}=0.0015$$'''),
 row('(ค) อ่านชาร์ต, แทนค่า', r'''$$f_{\text{Moody}}=0.024$$$$\Delta P=(0.024)\frac{0.1}{0.08}\,\frac{(1000)(1)^2}{2}=15\ \text{Pa}$$'''),
 fin(r'''(ก) Laminar,\ (ข) \(\Delta P=0.05\ \text{Pa}\),\ (ค) \(\Delta P\approx15\ \text{Pa}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ข้อ (ข), (ค) ถามความดันลด ซึ่งมาจากการสูญเสียพลังงานเสียดทานในท่อราบ ต้องรู้ \(f\) และ \(f\) ขึ้นกับชนิดการไหล จึงต้องเริ่มจาก \(Re\)</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> หา \(Re\) ของกรณี (ก) เพื่อระบุชนิดการไหล</p><p><b class="l">ขั้นที่ 2:</b> ตั้งสมการพลังงานของท่อราบ ได้ \(\Delta P\) ในรูปของ \(f\) แล้วแทน \(f=64/Re\) (Laminar)</p><p><b class="l">ขั้นที่ 3:</b> กรณี (ค) ความเร็วเพิ่ม เป็น Turbulent จึงอ่าน \(f\) จากชาร์ตตาม \(Re\) และ \(\varepsilon/D\)</p></div>
<h4>ขั้นที่ 1: ชนิดการไหลของกรณี (ก)</h4>
$$Re=\frac{\rho vD}{\mu}=\frac{(1000)(0.02)(0.08)}{10^{-3}}=1600\tag{1}$$
<p>\(Re=1600<2000\) จึงเป็น <b>Laminar</b></p>
<h4>ขั้นที่ 2: ความดันลดจากสมการพลังงาน (ข้อ ข)</h4>
<p>ท่อราบและขนาดคงที่ จึงมี \(z_1=z_2\) และ \(v_1=v_2\) พจน์ความสูงกับความเร็วตัดกันหมด</p>
$$\frac{P_1-P_2}{\gamma}=h_L=f\,\frac{L}{D}\,\frac{v^2}{2g}\tag{2}$$
<p>คูณ \(\gamma=\rho g\) ทั้งสองข้าง</p>
$$\Delta P=P_1-P_2=f\,\frac{L}{D}\,\frac{\rho v^2}{2}\tag{3}$$
<p>การไหลแบบ Laminar มี \(f\) ขึ้นกับ \(Re\) เท่านั้น ไม่ขึ้นกับความขรุขระ</p>
$$f=\frac{64}{Re}=\frac{64}{1600}=0.04\tag{4}$$
$$\Delta P=(0.04)\,\frac{0.5}{0.08}\,\frac{(1000)(0.02)^2}{2}=(0.04)(6.25)(0.2)=0.05\ \text{Pa}\tag{5}$$
<h4>ขั้นที่ 3: กรณีท่อพลาสติก ความเร็ว 1 m/s (ข้อ ค)</h4>
$$Re=\frac{(1000)(1)(0.08)}{10^{-3}}=8\times10^{4}\tag{6}$$
$$\frac{\varepsilon}{D}=\frac{0.12\ \text{mm}}{80\ \text{mm}}=0.0015\tag{7}$$
<p>\(Re>4000\) เป็น Turbulent จึงอ่าน \(f\) จากชาร์ตที่ \(Re=8\times10^4\) และ \(\varepsilon/D=0.0015\) ได้ \(f\approx0.024\) แล้วใช้ (3)</p>
$$\Delta P=(0.024)\,\frac{0.1}{0.08}\,\frac{(1000)(1)^2}{2}=(0.024)(1.25)(500)=15\ \text{Pa}\tag{8}$$
<p><b>ตรวจสอบ:</b> Colebrook-White ให้ \(f=0.0242\) และ \(\Delta P=15.1\) Pa ตรงกับที่อ่านชาร์ต</p>
<p class="ans">คำตอบที่ถูกต้องคือ: (ก) Laminar (ข) \(\Delta P=0.05\) Pa (ค) \(\Delta P\approx15\) Pa</p>''')

# ---------------------------------------------------------------- Q3
Q3 = sec('q3', 'ข้อ 3', 'ท่อ 3 ขนาดต่างระดับ: หา h_L ระหว่างจุด',
r'''<p>น้ำไหลแบบ Incompressible Steady State อัตราการไหลคงที่ \(Q=0.1\) m³/s จงหาการสูญเสียพลังงานระหว่างจุด 1 ถึงจุด 2 และระหว่างจุด 2 ถึงจุด 3 (ข้อมูลในรูป)</p>''', FIG_Q3,
[row('ข้อมูล', r'''$$Q=0.1\ \text{m}^3/\text{s},\quad D_1=0.1,\ D_2=0.2,\ D_3=0.3\ \text{m}$$$$P_1=100,\ P_2=50,\ P_3=20\ \text{kPa};\qquad z_1=0,\ z_2=3,\ z_3=1\ \text{m}$$''', 'given'),
 row('ความเร็ว v = Q/A', r'''$$v_1=\frac{0.1}{\pi(0.05)^2}=12.73,\quad v_2=\frac{0.1}{\pi(0.1)^2}=3.18,\quad v_3=\frac{0.1}{\pi(0.15)^2}=1.41\ \text{m/s}$$'''),
 row('สมการพลังงาน 1 → 2', r'''$$\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2+h_{L,12}$$$$\frac{100\times10^3}{9810}+\frac{12.73^2}{2g}+0=\frac{50\times10^3}{9810}+\frac{3.18^2}{2g}+3+h_{L,12}$$$$10.19+8.26=5.10+0.52+3+h_{L,12}\ \Rightarrow\ h_{L,12}=9.84\ \text{m}$$'''),
 row('สมการพลังงาน 2 → 3', r'''$$\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2=\frac{P_3}{\gamma}+\frac{v_3^2}{2g}+z_3+h_{L,23}$$$$5.10+0.52+3=\frac{20\times10^3}{9810}+\frac{1.41^2}{2g}+1+h_{L,23}$$$$8.61=2.04+0.10+1+h_{L,23}\ \Rightarrow\ h_{L,23}=5.47\ \text{m}$$'''),
 fin(r'''\(h_{L,1\to2}=9.84\ \text{m}\),\ \(h_{L,2\to3}=5.47\ \text{m}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> โจทย์ต้องการพลังงานที่หายไประหว่างจุด ซึ่งคือผลต่างของพลังงานรวมทั้งสองจุด จึงต้องรู้พลังงานรวม \(H=P/\gamma+v^2/2g+z\) ที่แต่ละจุด ซึ่งต้องรู้ความเร็วในแต่ละท่อก่อน</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> หาความเร็วในท่อแต่ละขนาดจาก \(Q=vA\)</p><p><b class="l">ขั้นที่ 2:</b> คำนวณพลังงานรวม \(H\) ที่จุด 1, 2, 3</p><p><b class="l">ขั้นที่ 3:</b> \(h_L\) คือผลต่างของ \(H\) ระหว่างจุดที่ไล่ตามทิศการไหล</p></div>
<h4>ขั้นที่ 1: ความเร็วในแต่ละท่อ (ความต่อเนื่อง)</h4>
<p>ท่อมี \(Q\) เท่ากันทุกหน้าตัด แต่หน้าตัดต่างกัน ความเร็วจึงต่างกัน</p>
$$v_1=\frac{Q}{A_1}=\frac{0.1}{\pi(0.05)^2}=12.73\ \text{m/s}\tag{1}$$
$$v_2=\frac{0.1}{\pi(0.1)^2}=3.18\ \text{m/s},\qquad v_3=\frac{0.1}{\pi(0.15)^2}=1.41\ \text{m/s}\tag{2}$$
<h4>ขั้นที่ 2: พลังงานรวมที่แต่ละจุด</h4>
<p>นิยามพลังงานรวมต่อหน่วยน้ำหนัก (หน่วยเมตร) แล้วแทนค่าที่จุด 1, 2, 3</p>
$$H=\frac{P}{\gamma}+\frac{v^2}{2g}+z\tag{3}$$
$$H_1=\frac{100\times10^3}{9810}+\frac{12.73^2}{2g}+0=10.19+8.26=18.46\ \text{m}\tag{4}$$
$$H_2=\frac{50\times10^3}{9810}+\frac{3.18^2}{2g}+3=5.10+0.52+3=8.61\ \text{m}\tag{5}$$
$$H_3=\frac{20\times10^3}{9810}+\frac{1.41^2}{2g}+1=2.04+0.10+1=3.14\ \text{m}\tag{6}$$
<h4>ขั้นที่ 3: การสูญเสียพลังงานระหว่างจุด</h4>
<p>จากสมการพลังงาน \(H_1=H_2+h_{L,12}\) ดังนั้น</p>
$$h_{L,1\to2}=H_1-H_2=18.46-8.61=9.84\ \text{m}\tag{7}$$
$$h_{L,2\to3}=H_2-H_3=8.61-3.14=5.47\ \text{m}\tag{8}$$
<p><b>ตรวจสอบ:</b> \(h_{L,1\to2}+h_{L,2\to3}=15.32\) m เท่ากับ \(H_1-H_3=18.46-3.14=15.32\) m และค่า \(h_L\) เป็นบวกทั้งสองช่วง (พลังงานต้องลดตามทิศการไหล)</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(h_{L,1\to2}=9.84\) m และ \(h_{L,2\to3}=5.47\) m</p>''')

# ---------------------------------------------------------------- Q4
Q4 = sec('q4', 'ข้อ 4', 'ท่อยาว 600 m มีข้องอ: หา major loss และ minor loss',
r'''<p>น้ำไหลในท่อด้วยอัตราการไหล \(Q=0.1\) m³/s เส้นผ่านศูนย์กลางคงที่ 20 cm ความยาวจากจุด 1 ถึงจุด 2 เท่ากับ 600 m ค่าสัมประสิทธิ์ความขรุขระ \(\varepsilon=0.4\) mm ความหนืดสัมบูรณ์ \(\mu=10^{-3}\) N·s/m² จงหาการสูญเสียพลังงานหลักและการสูญเสียพลังงานรองจากจุด 1 ถึงจุด 2 (ข้องอ \(K_L=0.5\) สองตัว)</p>''', FIG_Q4,
[row('ข้อมูล', r'''$$Q=0.1\ \text{m}^3/\text{s},\ D=0.2\ \text{m},\ L=600\ \text{m},\ \varepsilon=0.4\ \text{mm},\ \textstyle\sum K_L=0.5+0.5=1.0$$''', 'given'),
 row('ความเร็ว', r'''$$v=\frac{Q}{A}=\frac{0.1}{\pi(0.1)^2}=3.18\ \text{m/s},\qquad \frac{v^2}{2g}=0.516\ \text{m}$$'''),
 row('Re, ε/D', r'''$$Re=\frac{\rho vD}{\mu}=\frac{(1000)(3.18)(0.2)}{10^{-3}}=6.37\times10^{5},\qquad \frac{\varepsilon}{D}=\frac{0.4}{200}=0.002$$'''),
 row('อ่านชาร์ตหา f', r'''$$f_{\text{Moody}}\approx0.024$$'''),
 row('Major loss', r'''$$h_f=f\,\frac{L}{D}\,\frac{v^2}{2g}=(0.024)\,\frac{600}{0.2}\,(0.516)=37.2\ \text{m}$$'''),
 row('Minor loss', r'''$$h_m=\Big(\sum K_L\Big)\frac{v^2}{2g}=(1.0)(0.516)=0.52\ \text{m}$$'''),
 fin(r'''\(h_f\approx37\ \text{m}\),\ \(h_m=0.52\ \text{m}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการ \(h_f\) และ \(h_m\) ซึ่งทั้งคู่เป็นผลคูณของ \(v^2/2g\) กับค่าสัมประสิทธิ์ จึงต้องรู้ \(v\) ก่อน ส่วน \(h_f\) ต้องใช้ \(f\) ซึ่งหาได้ตรง ๆ เพราะรู้ \(Q\) จึงรู้ \(Re\) โดยไม่ต้องเดา</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> หา \(v\) และ \(v^2/2g\) จาก \(Q\) และ \(D\)</p><p><b class="l">ขั้นที่ 2:</b> หา \(Re\) กับ \(\varepsilon/D\) แล้วอ่าน \(f\)</p><p><b class="l">ขั้นที่ 3:</b> คำนวณ \(h_f\) (Darcy-Weisbach) และ \(h_m\)</p></div>
<h4>ขั้นที่ 1: ความเร็วและเฮดความเร็ว</h4>
$$v=\frac{Q}{A}=\frac{0.1}{\pi(0.1)^2}=3.18\ \text{m/s}\tag{1}$$
$$\frac{v^2}{2g}=\frac{(3.18)^2}{2(9.81)}=0.516\ \text{m}\tag{2}$$
<h4>ขั้นที่ 2: Re, ความขรุขระสัมพัทธ์ และ f</h4>
$$Re=\frac{\rho vD}{\mu}=\frac{(1000)(3.18)(0.2)}{10^{-3}}=6.37\times10^{5}\tag{3}$$
$$\frac{\varepsilon}{D}=\frac{0.4\ \text{mm}}{200\ \text{mm}}=0.002\tag{4}$$
<p>ที่ \(Re=6.4\times10^5\) และ \(\varepsilon/D=0.002\) อ่านจากชาร์ตได้ \(f\approx0.024\) (Colebrook-White ให้ \(0.0237\))</p>
<h4>ขั้นที่ 3: Major loss และ minor loss</h4>
$$h_f=f\,\frac{L}{D}\,\frac{v^2}{2g}=(0.024)\,\frac{600}{0.2}\,(0.516)=37.2\ \text{m}\tag{5}$$
$$h_m=\Big(\sum K_L\Big)\frac{v^2}{2g}=(0.5+0.5)(0.516)=0.52\ \text{m}\tag{6}$$
<p><b>ตรวจสอบ:</b> ใช้ \(f=0.0237\) จาก Colebrook จะได้ \(h_f=36.7\) m ต่างจากการอ่านชาร์ตเพียง 1% และ \(h_m\ll h_f\) ซึ่งสมเหตุสมผลสำหรับท่อยาว ส่วนความสูง 2 m ในรูปไม่เกี่ยวกับ \(h_f, h_m\) (ใช้ตอนหา \(\Delta P\) เท่านั้น)</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(h_f\approx37\) m (36.7–37.2 m ตามการอ่านชาร์ต) และ \(h_m=0.52\) m</p>''')

# ---------------------------------------------------------------- Q5
Q5 = sec('q5', 'ข้อ 5', 'ท่อขึ้นเนิน 20 m: ความดันน้อยที่สุดที่จุด 1',
r'''<p>น้ำไหลในท่อเส้นผ่านศูนย์กลาง 0.6 m ด้วยความเร็ว 2 m/s ถ้าความดันที่จุด 2 ต้องมากกว่า 10 kPa จงหาความดันที่น้อยที่สุดที่จุด 1 ให้คิดการสูญเสียพลังงานทั้งหมด จุด 1 และ 2 ห่างกัน 120 m ข้องอ 90° \(K_L=0.3\) (2 ตัวตามรูป) \(\varepsilon=3\) mm</p>''', FIG_Q5,
[row('ข้อมูล', r'''$$D=0.6\ \text{m},\ v=2\ \text{m/s},\ L=120\ \text{m},\ \varepsilon=3\ \text{mm},\ P_2=10\ \text{kPa}$$$$z_2-z_1=20\ \text{m},\qquad \textstyle\sum K_L=0.3+0.3=0.6$$''', 'given'),
 row('สมการพลังงาน 1 → 2', r'''$$\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2+h_L$$$$D_1=D_2\Rightarrow v_1=v_2\ \Rightarrow\ \frac{P_1}{\gamma}=\frac{P_2}{\gamma}+(z_2-z_1)+h_L$$'''),
 row('Re, ε/D, f', r'''$$Re=\frac{(2)(0.6)}{10^{-6}}=1.2\times10^{6},\qquad \frac{\varepsilon}{D}=\frac{3}{600}=0.005\ \Rightarrow\ f_{\text{Moody}}=0.0304$$'''),
 row('h_L', r'''$$\frac{v^2}{2g}=0.204\ \text{m}$$$$h_f=(0.0304)\frac{120}{0.6}(0.204)=1.24\ \text{m},\qquad h_m=(0.6)(0.204)=0.12\ \text{m}$$$$h_L=1.24+0.12=1.36\ \text{m}$$'''),
 row('แทนค่า', r'''$$\frac{P_1}{\gamma}=\frac{10\times10^3}{9810}+20+1.36=22.38\ \text{m}$$$$P_1=22.38\times9810=219{,}600\ \text{Pa}$$'''),
 fin(r'''\(P_{1,min}\approx219.6\ \text{kPa}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการ \(P_1\) ซึ่งหาได้จากสมการพลังงานเมื่อรู้ \(P_2\), ความสูง และ \(h_L\) จึงต้องรู้ \(h_L\) ซึ่งต้องรู้ \(f\) ก่อน และรู้ \(Re\) ได้เลยเพราะโจทย์ให้ \(v\)</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> หา \(f\) จาก \(Re\) และ \(\varepsilon/D\)</p><p><b class="l">ขั้นที่ 2:</b> คำนวณ \(h_L=h_f+h_m\)</p><p><b class="l">ขั้นที่ 3:</b> ตั้งสมการพลังงานจุด 1 → 2 แล้วแก้หา \(P_1\)</p></div>
<h4>ขั้นที่ 1: ค่า f</h4>
<p>ท่อขนาดคงที่ \(v=2\) m/s ตลอดแนว</p>
$$Re=\frac{vD}{\nu}=\frac{(2)(0.6)}{10^{-6}}=1.2\times10^{6}\tag{1}$$
$$\frac{\varepsilon}{D}=\frac{3\ \text{mm}}{600\ \text{mm}}=0.005\tag{2}$$
<p>ค่า \(\varepsilon/D=0.005\) อยู่ในโซน fully turbulent อ่านชาร์ตได้ \(f\approx0.030\) (Colebrook ให้ \(0.0304\))</p>
<h4>ขั้นที่ 2: การสูญเสียพลังงานรวม</h4>
$$\frac{v^2}{2g}=\frac{2^2}{2(9.81)}=0.204\ \text{m}\tag{3}$$
$$h_f=f\,\frac{L}{D}\,\frac{v^2}{2g}=(0.0304)\,\frac{120}{0.6}\,(0.204)=1.24\ \text{m}\tag{4}$$
$$h_m=\Big(\sum K_L\Big)\frac{v^2}{2g}=(0.3+0.3)(0.204)=0.12\ \text{m}\tag{5}$$
$$h_L=h_f+h_m=1.36\ \text{m}\tag{6}$$
<h4>ขั้นที่ 3: สมการพลังงานจุด 1 → 2</h4>
<p>ท่อขนาดเดียวกัน \(v_1=v_2\) พจน์ \(v^2/2g\) ตัดกัน และจุด 2 สูงกว่าจุด 1 อยู่ \(z_2-z_1=20\) m</p>
$$\frac{P_1}{\gamma}=\frac{P_2}{\gamma}+(z_2-z_1)+h_L\tag{7}$$
$$\frac{P_1}{\gamma}=\frac{10\times10^3}{9810}+20+1.36=1.02+20+1.36=22.38\ \text{m}\tag{8}$$
$$P_1=22.38\times9810=219{,}600\ \text{Pa}=219.6\ \text{kPa}\tag{9}$$
<p><b>ตรวจสอบ:</b> ส่วนใหญ่ (20 m จาก 22.38 m) ใช้ยกน้ำขึ้นเนิน ที่เหลือคือ \(P_2\) และการสูญเสีย จึงสมเหตุสมผล และ \(P_1>P_2\) ตามทิศการไหลขึ้นเนิน</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(P_{1,min}\approx219.6\) kPa (ประมาณ 220 kPa)</p>''')

# ---------------------------------------------------------------- Q6
Q6 = sec('q6', 'ข้อ 6', 'หาความเร็วจาก h_L ที่กำหนด (วิธีเดา f)',
r'''<p>ถ้าการสูญเสียพลังงานในท่อที่มีความยาว 700 m เท่ากับ 3 m ท่อมีเส้นผ่านศูนย์กลาง 15 cm ค่าสัมประสิทธิ์ความขรุขระ \(\varepsilon=0.12\) mm จงหาความเร็วของน้ำในท่อ (\(\nu=10^{-6}\) m²/s)</p>''', '',
[row('ข้อมูล', r'''$$L=700\ \text{m},\ h_L=3\ \text{m},\ D=0.15\ \text{m},\ \varepsilon=0.12\ \text{mm},\ \nu=10^{-6}\ \text{m}^2/\text{s}$$$$\frac{\varepsilon}{D}=\frac{0.12}{150}=0.0008$$''', 'given'),
 row('สมการ<br>(ไม่มี minor loss)', r'''$$h_L=f\,\frac{L}{D}\,\frac{v^2}{2g}\ \Rightarrow\ 3=f\,\frac{700}{0.15}\,\frac{v^2}{2g}\ \Rightarrow\ v=\sqrt{\frac{0.01261}{f}}\qquad\star$$'''),
 row('เดา f รอบที่ 1', r'''$$f=0.020\ \Rightarrow\ v=\sqrt{\frac{0.01261}{0.020}}=0.79\ \text{m/s}$$$$Re=\frac{vD}{\nu}=\frac{0.79(0.15)}{10^{-6}}=1.2\times10^{5}$$$$\frac{\varepsilon}{D}=0.0008\ \Rightarrow\ f_{\text{Moody}}=0.021\ \ \textcolor{#ff8178}{\neq0.020\ \ (\text{No})}$$'''),
 row('เดา f รอบที่ 2', r'''$$f=0.021\ \Rightarrow\ v=\sqrt{\frac{0.01261}{0.021}}=0.77\ \text{m/s}$$$$Re=\frac{0.77(0.15)}{10^{-6}}=1.2\times10^{5}\ \Rightarrow\ f_{\text{Moody}}=0.021\ \ \textcolor{#63d487}{=0.021\ \ (\text{OK})}$$'''),
 fin(r'''\(v\approx0.77\ \text{m/s}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการ \(v\) ซึ่งอยู่ในสมการ \(h_L=f\frac{L}{D}\frac{v^2}{2g}\) แต่ \(f\) ขึ้นกับ \(Re=vD/\nu\) ที่ต้องรู้ \(v\) จึงเกิดวงวน ต้องเดา \(f\) แล้วทำซ้ำ</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> จัดสมการให้ได้ \(v\) ในรูปของ \(f\)</p><p><b class="l">ขั้นที่ 2:</b> เดา \(f\) หา \(v\) แล้วคำนวณ \(Re\) กับ \(\varepsilon/D\) เพื่ออ่าน \(f\) ใหม่</p><p><b class="l">ขั้นที่ 3:</b> ทำซ้ำจน \(f\) ที่เดาตรงกับ \(f\) ที่อ่านได้</p></div>
<h4>ขั้นที่ 1: จัดสมการหา v ในรูปของ f</h4>
<p>โจทย์ไม่มี minor loss จึงเหลือเฉพาะ major loss แทน \(h_L=3\) m, \(L/D=700/0.15\)</p>
$$3=f\,\frac{700}{0.15}\,\frac{v^2}{2g}\tag{1}$$
$$v=\sqrt{\frac{3\,(0.15)\,2(9.81)}{700\,f}}=\sqrt{\frac{0.01261}{f}}\tag{2}$$
$$\frac{\varepsilon}{D}=\frac{0.12\ \text{mm}}{150\ \text{mm}}=0.0008\tag{3}$$
<h4>ขั้นที่ 2: เดา f รอบที่ 1</h4>
<p>เดา \(f=0.020\) แทนใน (2)</p>
$$v=\sqrt{\frac{0.01261}{0.020}}=0.79\ \text{m/s},\qquad Re=\frac{0.79\,(0.15)}{10^{-6}}=1.2\times10^{5}\tag{4}$$
<p>ที่ \(Re=1.2\times10^5\) และ \(\varepsilon/D=0.0008\) ชาร์ตให้ \(f=0.021\) ไม่เท่ากับที่เดา จึงทำรอบที่ 2</p>
<h4>ขั้นที่ 3: เดา f รอบที่ 2</h4>
$$v=\sqrt{\frac{0.01261}{0.021}}=0.77\ \text{m/s},\qquad Re=\frac{0.77\,(0.15)}{10^{-6}}=1.2\times10^{5}\tag{5}$$
<p>ชาร์ตให้ \(f=0.021\) เท่ากับที่เดา ค่าลู่เข้าแล้ว</p>
<div class="tw"><table><caption>ตารางที่ 1 ผลการวนซ้ำ</caption><thead><tr><th>รอบ</th><th>\(f\) ที่เดา</th><th>\(v\) (m/s)</th><th>\(Re\)</th><th>\(f\) จากชาร์ต</th><th>ผล</th></tr></thead><tbody><tr><td>1</td><td>0.020</td><td>0.79</td><td>\(1.2\times10^5\)</td><td>0.021</td><td>ไม่ตรง</td></tr><tr><td>2</td><td>0.021</td><td>0.77</td><td>\(1.2\times10^5\)</td><td>0.021</td><td>ตรง</td></tr></tbody></table></div>
<p><b>ตรวจสอบ:</b> Colebrook-White ให้ \(f=0.0212\) และ \(v=0.772\) m/s ตรงกับที่อ่านชาร์ต</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(v\approx0.77\) m/s (\(f=0.021\))</p>''')

# ---------------------------------------------------------------- Q7 (ส่วนที่เขียนไว้แล้ว เก็บเป็นไฟล์)
Q7 = (pathlib.Path(__file__).with_name('q7_section.html')).read_text(encoding='utf-8')

# ---------------------------------------------------------------- Q8
Q8 = sec('q8', 'ข้อ 8', 'หาเส้นผ่านศูนย์กลางท่อ (จัดรูป D⁵)',
r'''<p>น้ำไหลในท่อด้วยอัตราการไหล 0.5 m³/s โดยที่ \(\varepsilon=0.12\) mm ความยาวท่อ 200 m การสูญเสียพลังงานในท่อเท่ากับ 10 m จงหาเส้นผ่านศูนย์กลางของท่อนี้ (\(\nu=10^{-6}\) m²/s)</p>''', '',
[row('ข้อมูล', r'''$$Q=0.5\ \text{m}^3/\text{s},\ L=200\ \text{m},\ h_L=10\ \text{m},\ \varepsilon=0.12\ \text{mm},\ \nu=10^{-6}\ \text{m}^2/\text{s}$$''', 'given'),
 row('เขียน v ด้วย D', r'''$$Q=vA=v\,\frac{\pi D^2}{4}=0.5\ \Rightarrow\ v=\frac{2}{\pi D^2}$$'''),
 row('แทนใน Darcy-Weisbach', r'''$$10=f\,\frac{200}{D}\,\frac{1}{2g}\,\Big(\frac{2}{\pi D^2}\Big)^2\ \Rightarrow\ D^5=\frac{(200)(4)\,f}{10\,(2g)\,\pi^2}=0.413\,f\qquad\star$$'''),
 row('เดา f รอบที่ 1', r'''$$f=0.030\ \Rightarrow\ D=(0.413\times0.030)^{0.2}=0.42\ \text{m},\quad v=\frac{2}{\pi(0.42)^2}=3.61\ \text{m/s}$$$$Re=\frac{vD}{\nu}=1.5\times10^{6},\quad \frac{\varepsilon}{D}=\frac{0.12}{420}=0.00029\ \Rightarrow\ f_{\text{Moody}}=0.015\ \ \textcolor{#ff8178}{(\text{No})}$$'''),
 row('เดา f รอบที่ 2', r'''$$f=0.015\ \Rightarrow\ D=(0.413\times0.015)^{0.2}=0.36\ \text{m},\quad v=\frac{2}{\pi(0.36)^2}=4.91\ \text{m/s}$$$$Re=1.8\times10^{6},\quad \frac{\varepsilon}{D}=\frac{0.12}{360}=0.00033\ \Rightarrow\ f_{\text{Moody}}=0.0155\ \ \textcolor{#ff8178}{(\text{No})}$$'''),
 row('เดา f รอบที่ 3', r'''$$f=0.0155\ \Rightarrow\ D=(0.413\times0.0155)^{0.2}=0.36\ \text{m}\ \ \textcolor{#63d487}{(\text{OK},\ D\ \text{คงที่})}$$'''),
 fin(r'''\(D\approx0.36\ \text{m}\)\ (360 mm)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการ \(D\) แต่ \(D\) ปรากฏทั้งใน \(L/D\), ใน \(v\) (ผ่าน \(Q\)) และใน \(Re\), \(\varepsilon/D\) ที่กำหนด \(f\) จึงต้องเขียน \(h_L\) ให้อยู่ในรูป \(D^5\) แล้วเดา \(f\) ทำซ้ำ</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> เขียน \(v\) ด้วย \(Q\) และ \(D\) แล้วแทนใน Darcy-Weisbach ให้ได้ \(D^5\) ในรูปของ \(f\)</p><p><b class="l">ขั้นที่ 2:</b> เดา \(f\) หา \(D\) แล้วหา \(v, Re, \varepsilon/D\) เพื่ออ่าน \(f\) ใหม่</p><p><b class="l">ขั้นที่ 3:</b> ทำซ้ำจน \(D\) (และ \(f\)) คงที่</p></div>
<h4>ขั้นที่ 1: จัดสมการให้อยู่ในรูป D⁵</h4>
<p>จากความต่อเนื่อง \(Q=vA\) เขียน \(v\) และ \(v^2\) ด้วย \(D\)</p>
$$v=\frac{4Q}{\pi D^2}=\frac{2}{\pi D^2},\qquad v^2=\frac{4}{\pi^2D^4}\tag{1}$$
<p>แทนใน Darcy-Weisbach (ไม่มี minor loss) \(h_L=f\,\dfrac{L}{D}\,\dfrac{v^2}{2g}\)</p>
$$10=f\,\frac{200}{D}\,\frac{1}{2g}\,\frac{4}{\pi^2D^4}=\frac{f\,(200)(4)}{D^5\,(2g)\,\pi^2}\tag{2}$$
$$D^5=\frac{800\,f}{10\,(2)(9.81)\,\pi^2}=0.413\,f\tag{3}$$
<h4>ขั้นที่ 2: เดา f รอบที่ 1 และ 2</h4>
<p>เดา \(f=0.030\)</p>
$$D=(0.413\times0.030)^{0.2}=0.42\ \text{m},\qquad v=\frac{2}{\pi(0.42)^2}=3.61\ \text{m/s}\tag{4}$$
$$Re=\frac{3.61(0.42)}{10^{-6}}=1.5\times10^{6},\qquad \frac{\varepsilon}{D}=\frac{0.12}{420}=0.00029\ \Rightarrow\ f=0.015\tag{5}$$
<p>ไม่ตรงกับที่เดา ใช้ \(f=0.015\) ต่อ</p>
$$D=(0.413\times0.015)^{0.2}=0.36\ \text{m},\qquad v=4.91\ \text{m/s},\qquad Re=1.8\times10^{6}\tag{6}$$
$$\frac{\varepsilon}{D}=\frac{0.12}{360}=0.00033\ \Rightarrow\ f=0.0155\tag{7}$$
<h4>ขั้นที่ 3: รอบที่ 3 จนลู่เข้า</h4>
<p>ใช้ \(f=0.0155\) ใน (3) ได้ \(D\) เท่าเดิม</p>
$$D=(0.413\times0.0155)^{0.2}=0.36\ \text{m}\tag{8}$$
<div class="tw"><table><caption>ตารางที่ 1 ผลการวนซ้ำ</caption><thead><tr><th>รอบ</th><th>\(f\) ที่เดา</th><th>\(D\) (m)</th><th>\(v\) (m/s)</th><th>\(Re\)</th><th>\(f\) จากชาร์ต</th></tr></thead><tbody><tr><td>1</td><td>0.030</td><td>0.42</td><td>3.61</td><td>\(1.5\times10^6\)</td><td>0.015</td></tr><tr><td>2</td><td>0.015</td><td>0.36</td><td>4.91</td><td>\(1.8\times10^6\)</td><td>0.0155</td></tr><tr><td>3</td><td>0.0155</td><td>0.36</td><td>4.91</td><td>\(1.8\times10^6\)</td><td>0.0155</td></tr></tbody></table></div>
<p><b>ตรวจสอบ:</b> Colebrook-White ให้ \(D=0.365\) m, \(f=0.0156\) แทนกลับ \(h_f=0.0156\,(548)(1.166)=10.0\) m ตรงกับโจทย์</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(D\approx0.36\) m (360 mm)</p>''')

# ---------------------------------------------------------------- Exam A
QA = sec('ea', 'ข้อสอบ A', 'ท่อ 3 เส้นต่ออนุกรม วางเอียง 5°: หาความเร็วในแต่ละท่อ',
r'''<p>ท่อสามท่อต่อกันตามรูป มุมเอียง \(\theta=5^\circ\) ผลต่างความดันระหว่างจุด A และ B เท่ากับ 245.25 kPa จงประมาณความเร็วในแต่ละท่อ (\(\nu=10^{-6}\) m²/s)</p>
<div class="tw"><table><thead><tr><th>ท่อ</th><th>\(D\) (m)</th><th>\(L\) (m)</th><th>\(\varepsilon\) (mm)</th></tr></thead><tbody><tr><td>1</td><td>0.4</td><td>80</td><td>0.08</td></tr><tr><td>2</td><td>0.5</td><td>120</td><td>0.15</td></tr><tr><td>3</td><td>0.3</td><td>80</td><td>0.12</td></tr></tbody></table></div>''', FIG_EA,
[row('ข้อมูล', r'''$$\theta=5^\circ,\quad P_A-P_B=245.25\ \text{kPa},\quad z_A=0\ (\text{datum})$$$$z_B=(80+120+80)\sin5^\circ=24.40\ \text{m}$$''', 'given'),
 row('K จากชาร์ต', r'''$$\frac{A_1}{A_2}=0.64\ \Rightarrow\ K_{12}=0.15\ (\text{expansion},\ \times v_1^2/2g)$$$$\frac{A_3}{A_2}=0.36\ \Rightarrow\ K_{23}=0.35\ (\text{contraction},\ \times v_3^2/2g)$$'''),
 row('ความต่อเนื่อง<br>Q₁ = Q₂ = Q₃', r'''$$v_2=v_1\frac{A_1}{A_2}=0.64\,v_1,\qquad v_3=v_1\frac{A_1}{A_3}=\Big(\frac{0.4}{0.3}\Big)^2v_1=1.78\,v_1$$'''),
 row('สมการพลังงาน A → B<br>(v_A = v₁, v_B = v₃)', r'''$$\begin{aligned}&\frac{P_A}{\gamma}+\frac{v_1^2}{2g}+0=\frac{P_B}{\gamma}+\frac{v_3^2}{2g}+z_B\\&\quad+f_1\tfrac{80}{0.4}\tfrac{v_1^2}{2g}+f_2\tfrac{120}{0.5}\tfrac{v_2^2}{2g}+f_3\tfrac{80}{0.3}\tfrac{v_3^2}{2g}\\&\quad+0.15\tfrac{v_1^2}{2g}+0.35\tfrac{v_3^2}{2g}\end{aligned}$$'''),
 row('จัดรูป', r'''$$\frac{P_A-P_B}{\gamma}-z_B=25.00-24.40=0.60\ \text{m}$$$$\begin{aligned}0.60=\big[&(1.78^2-1)+0.15+0.35(1.78)^2\\&+200f_1+98.3f_2+844.9f_3\big]\frac{v_1^2}{2g}\end{aligned}$$$$0.60=\big[3.427+200f_1+98.3f_2+844.9f_3\big]\frac{v_1^2}{2g}\qquad\star$$'''),
 row('ε/D', r'''$$\Big(\tfrac{\varepsilon}{D}\Big)_1=\tfrac{0.08}{400}=0.0002,\quad \Big(\tfrac{\varepsilon}{D}\Big)_2=\tfrac{0.15}{500}=0.0003,\quad \Big(\tfrac{\varepsilon}{D}\Big)_3=\tfrac{0.12}{300}=0.0004$$'''),
 row('เดา f รอบที่ 1<br>(fully turbulent)', r'''$$f_1=0.014,\ f_2=0.015,\ f_3=0.016\ \Rightarrow\ [\ ]=21.22$$$$v_1=\sqrt{\frac{0.60\,(2g)}{21.22}}=0.745,\quad v_2=0.477,\quad v_3=1.326\ \text{m/s}$$$$Re_1=3.0\times10^5,\ Re_2=2.4\times10^5,\ Re_3=4.0\times10^5$$$$f_{\text{Moody}}=0.0163,\ 0.0175,\ 0.0173\ \ \textcolor{#ff8178}{(\text{No})}$$'''),
 row('เดา f รอบที่ 2', r'''$$f_1=0.0163,\ f_2=0.0175,\ f_3=0.0173\ \Rightarrow\ [\ ]=23.02$$$$v_1=\sqrt{\frac{0.60\,(2g)}{23.02}}=0.715,\quad v_2=0.458,\quad v_3=1.273\ \text{m/s}$$$$Re_1=2.9\times10^5,\ Re_2=2.3\times10^5,\ Re_3=3.8\times10^5$$$$f_{\text{Moody}}=0.0163,\ 0.0175,\ 0.0173\ \ \textcolor{#63d487}{(\text{OK})}$$'''),
 fin(r'''\(v_1\approx0.71,\ v_2\approx0.46,\ v_3\approx1.27\ \text{m/s}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการความเร็วทั้งสามท่อ แต่ท่ออนุกรมมี \(Q\) เท่ากัน จึงเขียนทุกความเร็วด้วย \(v_1\) ตัวเดียว แล้วใช้สมการพลังงานระหว่าง A กับ B ซึ่งมีผลต่างความดันและความสูงเป็นข้อมูลที่รู้ ส่วน \(f\) ของแต่ละท่อต้องเดาแล้วทำซ้ำ</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> หา \(z_B\), ค่า \(K\) ของ expansion/contraction และความสัมพันธ์ \(v_2, v_3\) กับ \(v_1\)</p><p><b class="l">ขั้นที่ 2:</b> ตั้งสมการพลังงาน A → B แล้วรวมเป็นก้อน × \(v_1^2/2g\)</p><p><b class="l">ขั้นที่ 3:</b> เดา \(f\) ทั้งสามท่อ หา \(v_1\) แล้วตรวจ \(f\) จากชาร์ต ทำซ้ำจนตรง</p></div>
<h4>ขั้นที่ 1: ความสูงของ B, ค่า K และความต่อเนื่อง</h4>
<p>กำหนดให้ A เป็น datum \(z_A=0\) ความยาวรวมตามแนวเอียง \(280\) m</p>
$$z_B=(L_1+L_2+L_3)\sin5^\circ=280\sin5^\circ=24.40\ \text{m}\tag{1}$$
<p>จุดต่อท่อ 1→2 เป็น sudden expansion และท่อ 2→3 เป็น sudden contraction อ่านค่า \(K\) จากชาร์ตของอาจารย์ที่อัตราส่วนพื้นที่</p>
$$\frac{A_1}{A_2}=\Big(\frac{0.4}{0.5}\Big)^2=0.64\ \Rightarrow\ K_{12}=0.15,\qquad \frac{A_3}{A_2}=\Big(\frac{0.3}{0.5}\Big)^2=0.36\ \Rightarrow\ K_{23}=0.35\tag{2}$$
<p>Expansion คูณกับ \(v_1^2/2g\) (ท่อเล็กก่อนขยาย) Contraction คูณกับ \(v_3^2/2g\) (ท่อเล็กหลังหด) ความต่อเนื่อง \(v_1A_1=v_2A_2=v_3A_3\) ให้</p>
$$v_2=v_1\frac{A_1}{A_2}=0.64\,v_1,\qquad v_3=v_1\frac{A_1}{A_3}=\Big(\frac{0.4}{0.3}\Big)^2v_1=1.78\,v_1\tag{3}$$
<h4>ขั้นที่ 2: สมการพลังงาน A → B</h4>
<p>จุด A อยู่ในท่อ 1 (\(v_A=v_1\)) และจุด B อยู่ในท่อ 3 (\(v_B=v_3\)) พจน์ความเร็วสองข้างจึงไม่ตัดกัน</p>
$$\frac{P_A}{\gamma}+\frac{v_1^2}{2g}=\frac{P_B}{\gamma}+\frac{v_3^2}{2g}+z_B+\sum_{i=1}^{3}f_i\frac{L_i}{D_i}\frac{v_i^2}{2g}+K_{12}\frac{v_1^2}{2g}+K_{23}\frac{v_3^2}{2g}\tag{4}$$
<p>ย้ายความดันและความสูงไปไว้ด้านซ้าย (\(z_B\) ย้ายข้างเป็นลบ) แล้วแทน \(v_2=0.64v_1,\ v_3=1.78v_1\)</p>
$$\frac{P_A-P_B}{\gamma}-z_B=\frac{245.25\times10^3}{9810}-24.40=0.60\ \text{m}\tag{5}$$
$$\begin{aligned}0.60=\Big[\,&(1.78^2-1)+0.15+0.35(1.78)^2\\&+200f_1+98.3f_2+844.9f_3\Big]\frac{v_1^2}{2g}\end{aligned}\tag{6}$$
<p>โดยที่ \(98.3=\frac{120}{0.5}(0.64)^2\) และ \(844.9=\frac{80}{0.3}(1.78)^2\) รวมค่าคงที่ได้ \(3.427\)</p>
$$0.60=\Big[\,3.427+200f_1+98.3f_2+844.9f_3\Big]\frac{v_1^2}{2g}\tag{7}$$
<h4>ขั้นที่ 3: เดา f และวนซ้ำ</h4>
$$\Big(\frac{\varepsilon}{D}\Big)_1=\frac{0.08}{400}=0.0002,\quad \Big(\frac{\varepsilon}{D}\Big)_2=\frac{0.15}{500}=0.0003,\quad \Big(\frac{\varepsilon}{D}\Big)_3=\frac{0.12}{300}=0.0004\tag{8}$$
<p><b>รอบที่ 1:</b> เดา \(f\) จากโซน fully turbulent ของแต่ละ \(\varepsilon/D\) คือ \(0.014, 0.015, 0.016\)</p>
$$[\ ]=3.427+2.80+1.47+13.52=21.22\ \Rightarrow\ v_1=\sqrt{\frac{0.60\,(2g)}{21.22}}=0.745\ \text{m/s}\tag{9}$$
$$v_2=0.477,\quad v_3=1.326\ \text{m/s}\ \Rightarrow\ Re_1=3.0\times10^5,\ Re_2=2.4\times10^5,\ Re_3=4.0\times10^5\tag{10}$$
<p>ชาร์ตให้ \(f=0.0163,\ 0.0175,\ 0.0173\) ไม่ตรงที่เดา</p>
<p><b>รอบที่ 2:</b> ใช้ \(f\) ที่อ่านได้</p>
$$[\ ]=3.427+3.26+1.72+14.62=23.02\ \Rightarrow\ v_1=\sqrt{\frac{0.60\,(2g)}{23.02}}=0.715\ \text{m/s}\tag{11}$$
$$v_2=0.458,\quad v_3=1.273\ \text{m/s}\ \Rightarrow\ Re_1=2.9\times10^5,\ Re_2=2.3\times10^5,\ Re_3=3.8\times10^5\tag{12}$$
<p>ชาร์ตให้ \(f\) เท่าเดิมทั้งสามท่อ ค่าลู่เข้าแล้ว</p>
<div class="tw"><table><caption>ตารางที่ 1 ผลการวนซ้ำ</caption><thead><tr><th>รอบ</th><th>\(f_1,f_2,f_3\) ที่เดา</th><th>\(v_1\)</th><th>\(v_2\)</th><th>\(v_3\)</th><th>\(f_1,f_2,f_3\) จากชาร์ต</th></tr></thead><tbody><tr><td>1</td><td>0.014, 0.015, 0.016</td><td>0.745</td><td>0.477</td><td>1.326</td><td>0.0163, 0.0175, 0.0173</td></tr><tr><td>2</td><td>0.0163, 0.0175, 0.0173</td><td>0.715</td><td>0.458</td><td>1.273</td><td>0.0163, 0.0175, 0.0173</td></tr></tbody></table></div>
<p><b>ตรวจสอบ:</b> วนด้วย Colebrook-White จนลู่เข้า ได้ \(v_1=0.713,\ v_2=0.457,\ v_3=1.268\) m/s (\(Q=0.0897\) m³/s) ต่างจากที่อ่านชาร์ตไม่ถึง 1%</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(v_1\approx0.71\) m/s, \(v_2\approx0.46\) m/s, \(v_3\approx1.27\) m/s</p>''')

# ---------------------------------------------------------------- Exam B
QB = sec('eb', 'ข้อสอบ B', 'โครงข่ายท่อ 4 เส้น (15 คะแนน): หา major loss จาก AA ถึง BB',
r'''<p>ท่อ 4 เส้นต่อกันตามรูป จงประมาณ major loss จาก AA ถึง BB จุด A ต่ำกว่าจุด B 10 m ท่อจาก A ถึง B ยาว 300 m major loss ในท่อ 3 เท่ากับ 0.42 m ความดันที่ A และ B เท่ากับ 910 และ 811.41 kPa ไม่ต้องคิด minor loss (\(\nu=10^{-6}\) m²/s)</p>
<div class="tw"><table><thead><tr><th>ท่อ</th><th>\(D\) (m)</th><th>\(L\) (m)</th><th>\(\varepsilon\) (mm)</th></tr></thead><tbody><tr><td>1</td><td>0.9</td><td>900</td><td>0.90</td></tr><tr><td>2</td><td>0.8</td><td>800</td><td>0.32</td></tr><tr><td>3</td><td>0.6</td><td>800</td><td>0.48</td></tr><tr><td>4</td><td>ไม่ทราบ</td><td>1000</td><td>0.96</td></tr></tbody></table></div>''', FIG_EB,
[row('ข้อมูล', r'''$$h_3=0.42\ \text{m},\quad P_A=910\ \text{kPa},\quad P_B=811.41\ \text{kPa},\quad z_B-z_A=10\ \text{m},\quad L_{AB}=300\ \text{m}$$''', 'given'),
 row('Major loss รวม<br>(ขนาน: h₂ = h₃)', r'''$$h_{AA\to BB}=h_1+h_2+h_4=h_1+0.42+h_4$$'''),
 row('สมการพลังงาน A → B<br>(ท่อ 4 ขนาดคงที่ v_A = v_B)', r'''$$\frac{P_A}{\gamma}=\frac{P_B}{\gamma}+z_B+h_{AB}\ \Rightarrow\ \frac{(910-811.41)\times10^3}{9810}=10+h_{AB}$$$$10.05=10+h_{AB}\ \Rightarrow\ h_{AB}=0.05\ \text{m}$$'''),
 row('h₄ ทั้งเส้น', r'''$$h_4=h_{AB}\,\frac{1000}{300}=0.05\times3.33=0.167\ \text{m}$$'''),
 row('ท่อ 3: หา v₃', r'''$$0.42=f_3\,\frac{800}{0.6}\,\frac{v_3^2}{2g}\ \Rightarrow\ v_3=\sqrt{\frac{0.00618}{f_3}},\qquad \frac{\varepsilon}{D}=\frac{0.48}{600}=0.0008$$$$f=0.02\Rightarrow v_3=0.556,\ Re=3.3\times10^5\ \Rightarrow\ f_{\text{Moody}}=0.0196\ \ \textcolor{#ff8178}{(\text{No})}$$$$f=0.0196\Rightarrow v_3=0.562\ \text{m/s},\ Re=3.4\times10^5\ \Rightarrow\ f_{\text{Moody}}=0.0196\ \ \textcolor{#63d487}{(\text{OK})}$$'''),
 row('ท่อ 2: หา v₂', r'''$$0.42=f_2\,\frac{800}{0.8}\,\frac{v_2^2}{2g}\ \Rightarrow\ v_2=\sqrt{\frac{0.00824}{f_2}},\qquad \frac{\varepsilon}{D}=\frac{0.32}{800}=0.0004$$$$f=0.017\Rightarrow v_2=0.696,\ Re=5.6\times10^5\ \Rightarrow\ f_{\text{Moody}}=0.0169\ \ \textcolor{#ff8178}{(\text{No})}$$$$f=0.0169\Rightarrow v_2=0.698\ \text{m/s},\ Re=5.6\times10^5\ \Rightarrow\ f_{\text{Moody}}=0.0169\ \ \textcolor{#63d487}{(\text{OK})}$$'''),
 row('อัตราการไหลรวม', r'''$$\begin{aligned}Q=Q_2+Q_3&=\frac{\pi(0.8)^2}{4}(0.698)+\frac{\pi(0.6)^2}{4}(0.562)\\&=0.351+0.159=0.510\ \text{m}^3/\text{s}\end{aligned}$$'''),
 row('ท่อ 1: หา h₁', r'''$$v_1=\frac{Q}{A_1}=\frac{0.510}{\pi(0.45)^2}=0.80\ \text{m/s},\quad Re=7.2\times10^5,\quad \frac{\varepsilon}{D}=\frac{0.90}{900}=0.001\ \Rightarrow\ f_1=0.0201$$$$h_1=f_1\,\frac{900}{0.9}\,\frac{v_1^2}{2g}=(0.0201)(1000)\frac{0.80^2}{2g}=0.656\ \text{m}$$'''),
 row('รวม', r'''$$h_{AA\to BB}=0.656+0.420+0.167=1.243\ \text{m}$$'''),
 fin(r'''\(h_{AA\to BB}\approx1.24\ \text{m}\)''')],
r'''<p><b>แนวคิดในการแก้ปัญหา:</b> ต้องการ major loss รวม ซึ่งคือผลบวกตามเส้นทางเดียว \(h_1+h_2+h_4\) โดยท่อขนานให้ \(h_2=h_3=0.42\) m ที่รู้อยู่แล้ว จึงเหลือหา \(h_1\) และ \(h_4\) ซึ่ง \(h_4\) หาได้จากสมการพลังงานช่วง A→B ส่วน \(h_1\) ต้องรู้ \(Q\) ซึ่งหาได้จากท่อ 2 และ 3</p>
<div class="plan"><p><b class="l">ขั้นที่ 1:</b> เขียน \(h_{AA\to BB}\) และหา \(h_4\) จากสมการพลังงานช่วง A→B</p><p><b class="l">ขั้นที่ 2:</b> หา \(v_2, v_3\) จาก \(h=0.42\) m (เดา \(f\)) แล้วรวมเป็น \(Q\)</p><p><b class="l">ขั้นที่ 3:</b> หา \(v_1\) จาก \(Q\) แล้วหา \(h_1\) และรวมทั้งหมด</p></div>
<h4>ขั้นที่ 1: โครงสร้าง h รวม และ h₄</h4>
<p>น้ำหนึ่งก้อนไหลผ่านท่อ 2 หรือท่อ 3 เส้นใดเส้นหนึ่งเท่านั้น และท่อขนานมีการสูญเสียเท่ากัน \(h_2=h_3\) จึงนับครั้งเดียว</p>
$$h_{AA\to BB}=h_1+h_2+h_4=h_1+0.42+h_4\tag{1}$$
<p>ช่วง A→B อยู่ในท่อ 4 ขนาดคงที่ \(v_A=v_B\) ตัดกัน</p>
$$\frac{P_A}{\gamma}=\frac{P_B}{\gamma}+z_B+h_{AB}\tag{2}$$
$$\frac{(910-811.41)\times10^3}{9810}=10.05=10+h_{AB}\ \Rightarrow\ h_{AB}=0.05\ \text{m}\tag{3}$$
<p>ท่อ 4 มี \(D_4, v_4, f_4\) เท่ากันตลอดเส้น จึง \(h\propto L\) ไม่ต้องรู้ \(D_4\)</p>
$$h_4=h_{AB}\,\frac{1000}{300}=0.167\ \text{m}\tag{4}$$
<h4>ขั้นที่ 2: ความเร็วในท่อ 2, 3 และอัตราการไหลรวม</h4>
<p>ท่อ 3: \(h_3=0.42\) m, \(L/D=800/0.6\), \(\varepsilon/D=0.48/600=0.0008\)</p>
$$v_3=\sqrt{\frac{2g(0.42)(0.6)}{f_3(800)}}=\sqrt{\frac{0.00618}{f_3}}\tag{5}$$
<p>เดา \(f=0.02\) ได้ \(v_3=0.556\) m/s, \(Re=3.3\times10^5\) ชาร์ตให้ \(0.0196\) ไม่ตรง ใช้ \(f=0.0196\) ได้ \(v_3=0.562\) m/s, \(Re=3.4\times10^5\) ชาร์ตให้ \(0.0196\) ตรงแล้ว</p>
<p>ท่อ 2: \(h_2=0.42\) m, \(L/D=800/0.8\), \(\varepsilon/D=0.32/800=0.0004\)</p>
$$v_2=\sqrt{\frac{2g(0.42)(0.8)}{f_2(800)}}=\sqrt{\frac{0.00824}{f_2}}\tag{6}$$
<p>เดา \(f=0.017\) ได้ \(v_2=0.696\) m/s, \(Re=5.6\times10^5\) ชาร์ตให้ \(0.0169\) ใช้ \(f=0.0169\) ได้ \(v_2=0.698\) m/s ตรงแล้ว ท่อขนานรวมอัตราการไหล</p>
$$\begin{aligned}Q=Q_2+Q_3&=\frac{\pi(0.8)^2}{4}(0.698)+\frac{\pi(0.6)^2}{4}(0.562)\\&=0.351+0.159=0.510\ \text{m}^3/\text{s}\end{aligned}\tag{7}$$
<h4>ขั้นที่ 3: ท่อ 1 และผลรวม</h4>
<p>ท่อ 1 รับน้ำทั้งหมด \(Q_1=Q\)</p>
$$v_1=\frac{Q}{A_1}=\frac{0.510}{\pi(0.45)^2}=0.80\ \text{m/s},\qquad Re=\frac{0.80(0.9)}{10^{-6}}=7.2\times10^{5}\tag{8}$$
$$\frac{\varepsilon}{D}=\frac{0.90}{900}=0.001\ \Rightarrow\ f_1=0.0201\tag{9}$$
$$h_1=f_1\,\frac{L_1}{D_1}\,\frac{v_1^2}{2g}=(0.0201)\,\frac{900}{0.9}\,\frac{0.80^2}{2g}=0.656\ \text{m}\tag{10}$$
<p>แทนใน (1)</p>
$$h_{AA\to BB}=0.656+0.420+0.167=1.243\ \text{m}\tag{11}$$
<p><b>ตรวจสอบ:</b> Colebrook-White ให้ \(Q=0.5096\) m³/s, \(h_1=0.656\) m, \(h_4=0.166\) m รวม \(1.243\) m ตรงกัน ท่อ 1 ใหญ่และยาวที่สุดจึงรับ \(h\) มากกว่าท่อขนานแต่ \(v_1\) ต่ำ</p>
<p class="ans">คำตอบที่ถูกต้องคือ: \(h_{AA\to BB}\approx1.24\) m</p>''')


SECS = [('q1','ข้อ 1',Q1),('q2','ข้อ 2',Q2),('q3','ข้อ 3',Q3),('q4','ข้อ 4',Q4),('q5','ข้อ 5',Q5),('q6','ข้อ 6',Q6),('q7','ข้อ 7',Q7),('q8','ข้อ 8',Q8),('ea','สอบ A',QA),('eb','สอบ B',QB)]
