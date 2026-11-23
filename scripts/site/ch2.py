# -*- coding: utf-8 -*-
"""บทที่ 2 สถิตยศาสตร์ของไหลและบานประตู (Fluid Statics & Gates)"""
from common import row, fin, exam

CH2_HTML = '''<section id="ch2">
<header class="top"><p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
<h1>บทที่ 2 สถิตยศาสตร์ของไหลและบานประตู</h1>
<p class="sub">มาโนมิเตอร์ · แรงดันบนระนาบเรียบและจุดศูนย์กลางแรงกด · สมดุลบานพับ · แรงดันบนผิวโค้ง</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
</header>

<h2 class="prob"><span class="tag">บทที่ 2</span>สรุปสูตรและข้อสอบเต็งหนึ่งสถิตยศาสตร์ของไหล (39 ข้อ)</h2>
<div class="stmt">
<p>บทที่ 2 เป็นบทที่มีน้ำหนักคะแนนสูงมากในข้อสอบ มักออกข้อสอบ 2 ข้อใหญ่: <b>(1) ข้อสอบคำนวณมาโนมิเตอร์หลายของไหลท่อเอียง</b> และ <b>(2) แรงดันบนประตูระนาบเอียงหรือระนาบโค้งพร้อมเทคโมเมนต์รอบบานพับ</b></p>
</div>

<div class="jump">
<a href="#ch2-mano">1. มาโนมิเตอร์ (ข้อ 9)</a>
<a href="#ch2-plane">2. แรงดันบนผนังระนาบเรียบ (ข้อ 22)</a>
<a href="#ch2-hinge">3. บานประตูปิดน้ำเอียงสมดุลบานพับ (ข้อ 26)</a>
<a href="#ch2-curved">4. แรงดันบนผิวโค้งวงกลม (ข้อ 29)</a>
</div>

<hr>

<!-- 1. MANOMETER EX 9 -->
<h3 id="ch2-mano" class="part">1. ตัวอย่างข้อ 9 (หน้า 3): มาโนมิเตอร์ของเหลว 2 ชนิด</h3>
<div class="stmt">
<p><b>โจทย์:</b> จงหาความดันเกจที่จุด A, B, C, D, E ไม่ต้องคิดความดันบรรยากาศ กำหนด \(S.G._1 = 1.0\), \(S.G._2 = 0.8\), จุด B อยู่ที่ผิวน้ำเปิด, จุด A อยู่เหนือผิวน้ำ \(0.2\text{ m}\) ในท่อปิด, จุด C อยู่ต่ำกว่าผิวน้ำ \(0.2\text{ m}\), จุด D อยู่ระดับเดียวกับ C, จุด E อยู่ก้นถังต่ำลงไปอีก \(0.7\text{ m}\) ในของเหลว 2</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('จุด B', r'P_B = 0\text{ Pa (ผิวน้ำอิสระเปิดสู่อากาศ)}'),
    row('จุด A', r'P_A = P_B - \gamma_1 \Delta h_{BA} = 0 - (9,810\text{ N/m}^3 \times 0.2\text{ m}) = -1,962\text{ Pa}'),
    row('จุด C', r'P_C = P_B + \gamma_1 \Delta h_{BC} = 0 + (9,810\text{ N/m}^3 \times 0.2\text{ m}) = +1,962\text{ Pa}'),
    row('จุด D', r'P_D = P_C = +1,962\text{ Pa (ระดับเดียวกันในของเหลวชนิดเดียวกันต่อเนื่อง)}'),
    row('จุด E', r'P_E = P_D + \gamma_2 \Delta h_{DE} = 1,962 + (0.8 \times 9,810\text{ N/m}^3 \times 0.7\text{ m}) = 1,962 + 5,493.6 = +7,455.6\text{ Pa}'),
    fin(r'P_A = -1,962\text{ Pa}, \quad P_B = 0\text{ Pa}, \quad P_C = P_D = 1,962\text{ Pa}, \quad P_E = 7,455.6\text{ Pa}')
]) + '''

<hr>

<!-- 2. PLANE GATE EX 22 -->
<h3 id="ch2-plane" class="part">2. ตัวอย่างข้อ 22 (หน้า 8): ผนังระนาบเรียบและจุดศูนย์กลางแรงกด</h3>
<div class="stmt">
<p><b>โจทย์:</b> จงหาแรงที่กระทำกับผนังแนวดิ่งที่มีความกว้าง (เข้าไปในกระดาษ) \(b = 5\text{ m}\) สูง \(h = 6\text{ m}\) โดยมีระดับน้ำอยู่ที่ขอบบนของผนังพอดี และหาตำแหน่งที่แรงกระทำ (\(y_{cp}\))</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('พื้นที่', r'A = b \times h = 5\text{ m} \times 6\text{ m} = 30\text{ m}^2'),
    row('เซนทรอยด์', r'h_{cg} = \dfrac{h}{2} = \dfrac{6}{2} = 3.0\text{ m}'),
    row('แรงลัพธ์', r'F_R = \gamma h_{cg} A = 9,810\text{ N/m}^3 \times 3.0\text{ m} \times 30\text{ m}^2 = 882,900\text{ N} = 882.9\text{ kN}'),
    row('ความเฉื่อย', r'I_{xx,c} = \dfrac{b h^3}{12} = \dfrac{5 \times 6^3}{12} = 90\text{ m}^4'),
    row('จุดศูนย์กลาง', r'y_{cp} = y_{cg} + \dfrac{I_{xx,c}}{y_{cg} A} = 3.0 + \dfrac{90}{3.0 \times 30} = 3.0 + 1.0 = 4.0\text{ m}'),
    fin(r'F_R = 882.9\text{ kN}, \quad y_{cp} = 4.0\text{ m}\text{ จากผิวน้ำ (หรือ } 2.0\text{ m จากก้นบาน)}')
]) + '''

<hr>

<!-- 3. TILTED GATE HINGE EX 26 -->
<h3 id="ch2-hinge" class="part">3. ตัวอย่างข้อ 26 (หน้า 9): บานประตูปิดน้ำเอียงสมดุลรอบบานพับ (ข้อสอบอัตนัยปราบเซียน)</h3>
<div class="stmt">
<p><b>โจทย์:</b> ประตู CD กว้าง \(1.8\text{ m}\) ยาว \(2.0\text{ m}\) สมมติวัสดุเนื้อเดียวกัน ไม่คิดแรงเสียดทานที่จุดหมุนบานพับ C บานประตูเอียงลาดชัน \(4:3:5\) (\(\sin\theta = 0.8, \cos\theta = 0.6\)) จงหาน้ำหนักประตู \(W\) ที่จะทำให้ประตูปิดพอดี เมื่อระดับน้ำในอ่างสูง \(2.0\text{ m}\) เหนือจุด C</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('เรขาคณิต', r'A = 1.8 \times 2.0 = 3.6\text{ m}^2, \quad y_C = \dfrac{2.0}{\sin\theta} = \dfrac{2.0}{0.8} = 2.5\text{ m}'),
    row('เซนทรอยด์', r'y_{cg} = y_C + \dfrac{L}{2} = 2.5 + 1.0 = 3.5\text{ m}, \quad h_{cg} = y_{cg} \sin\theta = 3.5 \times 0.8 = 2.8\text{ m}'),
    row('แรงดันน้ำ', r'F_R = \gamma h_{cg} A = 9,810 \times 2.8 \times 3.6 = 98,884.8\text{ N} = 98.88\text{ kN}'),
    row('จุดกดแรง', r'I_{xx,c} = \dfrac{1.8 \times 2^3}{12} = 1.2\text{ m}^4 \implies y_{cp} = 3.5 + \dfrac{1.2}{3.5 \times 3.6} = 3.5952\text{ m}'),
    row('แขนแรง F', r'd_F = y_{cp} - y_C = 3.5952 - 2.5 = 1.0952\text{ m}'),
    row('แขนน้ำหนัก W', r'd_W = \left(\dfrac{L}{2}\right) \cos\theta = 1.0 \times 0.6 = 0.6\text{ m}'),
    row('สมดุลโมเมนต์', r'\sum M_C = 0 \implies F_R \cdot d_F = W \cdot d_W \implies 98,884.8 \times 1.0952 = W \times 0.6'),
    row('แก้หา W', r'W = \dfrac{108,298.6}{0.6} = 180,498\text{ N} = 180.5\text{ kN}'),
    fin(r'W = 180.5\text{ kN}')
]) + '''

<hr>

<!-- 4. CURVED SURFACE EX 29 -->
<h3 id="ch2-curved" class="part">4. ตัวอย่างข้อ 29 (หน้า 10): แรงดันบนผิวโค้งวงกลม</h3>
<div class="stmt">
<p><b>โจทย์:</b> จงหาแรงที่กระทำต่อส่วนโค้ง AB และตำแหน่งที่แรงกระทำ ส่วนโค้งเป็น \(1/4\) ของวงกลมรัศมี \(R = 6\text{ m}\) ความกว้าง \(b = 2\text{ m}\) ผิวน้ำอยู่ที่ระดับขอบบน A พอดี</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('แรงแนวราบ', r'F_H = \gamma h_{cg,\text{proj}} A_{\text{proj}} = 9,810 \times \left(\dfrac{6}{2}\right) \times (6 \times 2) = 353,160\text{ N} = 353.16\text{ kN}'),
    row('ตำแหน่ง FH', r'y_{cp} = \dfrac{2}{3}(6) = 4.0\text{ m}\text{ จากผิวน้ำ}'),
    row('ปริมาตรน้ำ', r'\text{Vol} = \left(\dfrac{\pi R^2}{4}\right) b = \left(\dfrac{\pi \times 6^2}{4}\right) \times 2 = 18\pi = 56.55\text{ m}^3'),
    row('แรงแนวดิ่ง', r'F_V = \gamma \times \text{Vol} = 9,810 \times 56.55 = 554,742\text{ N} = 554.74\text{ kN}'),
    row('ตำแหน่ง FV', r'x_{cg} = \dfrac{4R}{3\pi} = \dfrac{4(6)}{3\pi} = 2.546\text{ m}\text{ จากผนังดิ่ง}'),
    row('แรงลัพธ์ FR', r'F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{353.16^2 + 554.74^2} = 657.6\text{ kN}'),
    row('มุมทิศทาง', r'\theta = \tan^{-1}\left(\dfrac{F_V}{F_H}\right) = \tan^{-1}\left(\dfrac{554.74}{353.16}\right) = 57.52^\circ\text{ กับแนวราบ}'),
    fin(r'F_R = 657.6\text{ kN}, \quad \theta = 57.52^\circ\text{ (แนวแรงพุ่งผ่านจุดศูนย์กลางความโค้ง } O\text{)}')
]) + '''
</section>'''
