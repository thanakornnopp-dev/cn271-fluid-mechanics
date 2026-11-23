# -*- coding: utf-8 -*-
"""เครื่องมือวัดอัตราการไหลและการเกิดโพรงไอ (Flow Measurement & Cavitation)"""
from common import row, fin, exam

METERS_HTML = '''<section id="meter">
<header class="top"><p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
<h1>การวัดอัตราการไหลและการเกิดโพรงไอ</h1>
<p class="sub">Venturi Meter · Orifice Plate · Pitot Tube · Net Positive Suction Head (NPSH)</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
</header>

<h2 class="prob"><span class="tag">เครื่องมือวัด</span>การวัดอัตราการไหลและข้อจำกัดของเครื่องสูบน้ำ</h2>
<div class="stmt">
<p>ครอบคลุมการประยุกต์ใช้สมการเบอร์นูลลีเพื่อวัดอัตราการไหลในท่อจริงด้วย <b>Venturi Meter</b> และการคำนวณหาระยะความสูงปลอดภัยในการตั้งเครื่องสูบน้ำเพื่อป้องกัน <b>Cavitation</b></p>
</div>

<div class="jump">
<a href="#meter-venturi">1. Venturi Meter (ตัวอย่างเรื่องการวัดอัตราการไหล)</a>
<a href="#meter-cavitation">2. การป้องกัน Cavitation ในเครื่องสูบน้ำ (ข้อ 14 หน้า 43)</a>
</div>

<hr>

<!-- 1. VENTURI METER -->
<h3 id="meter-venturi" class="part">1. ตัวอย่างเรื่องการวัดอัตราการไหล (หน้า 43): Venturi Meter</h3>
<div class="stmt">
<p><b>โจทย์:</b> ในการตรวจสอบท่อน้ำเก่า ติดตั้ง Venturi Meter ที่มีค่าสัมประสิทธิ์ปรับแก้เครื่อง \(C_d = 0.85\) ข้อมูลจากมาโนมิเตอร์อ่านความดันได้ \(P_1 = 525\text{ Pa}\) และ \(P_2 = 225\text{ Pa}\) จงหาอัตราการไหลของน้ำในท่อ</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('สมการ Venturi', r'Q = C_d \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \left( \dfrac{P_1 - P_2}{\gamma} \right)}'),
    row('ความดันลด', r'\Delta P = P_1 - P_2 = 525\text{ Pa} - 225\text{ Pa} = 300\text{ Pa}'),
    row('ความต่างเฮด', r'\Delta h = \dfrac{\Delta P}{\gamma} = \dfrac{300\text{ N/m}^2}{9,810\text{ N/m}^3} = 0.03058\text{ m}'),
    row('อัตราการไหล', r'Q = 0.85 \times \left( \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \right) \sqrt{2(9.81)(0.03058)} = 0.85 \times \left( \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \right) \times 0.7746\text{ m/s}'),
    fin(r'Q = 0.85 \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \dfrac{\Delta P}{\gamma}}')
]) + '''

<hr>

<!-- 2. CAVITATION EX 14 -->
<h3 id="meter-cavitation" class="part">2. ตัวอย่างข้อ 14 (หน้า 43): การป้องกัน Cavitation ในปั๊มน้ำ</h3>
<div class="stmt">
<p><b>โจทย์:</b> ต้องการสูบน้ำจากถังน้ำโดยไม่ให้เกิด Cavitation จะต้องตั้งเครื่องสูบน้ำให้สูงกว่าระดับน้ำ (\(Z_1\)) ได้มากที่สุดกี่เมตร กำหนดให้อัตราสูบ \(Q = 0.015\text{ m}^3\text{/s}\), \(D = 0.2\text{ m}\), \(P_{\text{atm}} = 101\text{ kPa}\), \(\text{NPSHR} = 4.6\text{ m}\), \(P_v = 5,950\text{ Pa}\) และคิดเฉพาะ Minor loss โดยมีสัมประสิทธิ์รวม \(\sum K_L = 20\)</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('ความเร็วท่อดูด', r'v = \dfrac{4 Q}{\pi D^2} = \dfrac{4(0.015)}{\pi (0.2)^2} = \dfrac{0.060}{0.12566} = 0.4775\text{ m/s}'),
    row('เฮดความเร็ว', r'\dfrac{v^2}{2g} = \dfrac{0.4775^2}{2(9.81)} = \dfrac{0.2280}{19.62} = 0.0116\text{ m}'),
    row('เฮดสูญเสียท่อดูด', r'h_L = \sum K_L \dfrac{v^2}{2g} = 20 \times 0.0116\text{ m} = 0.232\text{ m}'),
    row('เงื่อนไข NPSHA', r'\text{NPSHA} = \dfrac{P_{\text{atm}} - P_v}{\gamma} - Z_1 - h_L \ge \text{NPSHR}'),
    row('แทนค่าตัวเลข', r'\dfrac{101,000 - 5,950}{9,810} - Z_1 - 0.232 \ge 4.6'),
    row('คำนวณ Z1 max', r'\dfrac{95,050}{9,810} - Z_1 - 0.232 = 9.689 - Z_1 - 0.232 \ge 4.6 \implies Z_1 \le 9.689 - 0.232 - 4.6 = 4.857\text{ m}'),
    fin(r'Z_{1,\max} \approx 4.86\text{ m}\text{ (ตั้งปั๊มสูงกว่าระดับน้ำได้ไม่เกิน } 4.86\text{ เมตร)}')
]) + '''
</section>'''
