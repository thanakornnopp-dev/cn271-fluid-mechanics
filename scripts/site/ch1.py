# -*- coding: utf-8 -*-
"""บทที่ 1 คุณสมบัติของไหล (Fluid Properties)"""
from common import row, fin, exam

CH1_HTML = '''<section id="ch1">
<header class="top"><p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
<h1>บทที่ 1 คุณสมบัติของไหล</h1>
<p class="sub">ความหนืด (Viscosity) · ความเค้นเฉือน (Shear Stress) · กฎของนิวตัน</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
</header>

<h2 class="prob"><span class="tag">บทที่ 1</span>ตัวอย่างข้อ 1 (หน้า 1): แผ่นเลื่อนขนานและความเค้นเฉือน</h2>
<div class="stmt">
<p><b>โจทย์:</b> ของไหล A อยู่ระหว่างแผ่นเรียบดังรูป ถ้า Dynamic viscosity (\(\mu\)) ของของไหล A เท่ากับ \(0.29\text{ kg}\cdot\text{m}^{-1}\text{s}^{-1}\) จงหาค่า Shear stress (\(\tau\)) ที่ต้องการ เพื่อให้แผ่นด้านบนเคลื่อนที่ด้วยความเร็ว \(V = 3.2\text{ m/s}\) โดยมีระยะห่างระหว่างแผ่น \(h = 8\text{ mm}\)</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('ข้อมูล', r'\mu = 0.29\text{ kg}\cdot\text{m}^{-1}\text{s}^{-1} = 0.29\text{ Pa}\cdot\text{s}, \quad V = 3.2\text{ m/s}, \quad h = 8\text{ mm} = 0.008\text{ m}'),
    row('สูตร', r'\tau = \mu \dfrac{dv}{dy} \approx \mu \dfrac{V}{h}'),
    row('แทนค่า', r'\tau = 0.29\text{ Pa}\cdot\text{s} \times \left( \dfrac{3.2\text{ m/s}}{0.008\text{ m}} \right) = 0.29 \times 400\text{ s}^{-1}'),
    row('ผลลัพธ์', r'\tau = 116\text{ N/m}^2'),
    fin(r'\tau = 116\text{ N/m}^2\text{ (Pa)}')
]) + '''
<hr>
<h3 class="part">เฉลยละเอียด</h3>
<div class="detail">
<p><b>1. กฎความหนืดของนิวตัน (Newton's Law of Viscosity):</b><br>
สำหรับของไหลนิวโทเนียน (Newtonian Fluid) ความเค้นเฉือนแปรผันตรงกับอัตราการเปลี่ยนรูปหรือความลาดความเร็ว (Velocity Gradient) เมื่อระยะห่างระหว่างแผ่น \(h\) มีค่าน้อย การกระจายความเร็วระหว่างแผ่นจะถือเป็นเส้นตรง (Linear Velocity Profile):
$$\dfrac{dv}{dy} = \dfrac{V - 0}{h - 0} = \dfrac{V}{h} = \dfrac{3.2}{0.008} = 400\text{ s}^{-1}$$</p>

<p><b>2. การตรวจสอบหน่วย:</b><br>
$$[\tau] = [\mu] \times \left[\dfrac{V}{h}\right] = (\text{kg}\cdot\text{m}^{-1}\text{s}^{-1}) \times (\text{s}^{-1}) = \text{kg}\cdot\text{m}^{-1}\text{s}^{-2} = \text{N/m}^2 = \text{Pa}$$</p>
<div class="bx chk"><b>จุดที่คนมักผิด:</b> ลืมแปลง \(h = 8\text{ mm}\) เป็น \(0.008\text{ m}\) หากลืมแปลง ค่าจะผิดไป 1,000 เท่า</div>
</div>
</section>'''
