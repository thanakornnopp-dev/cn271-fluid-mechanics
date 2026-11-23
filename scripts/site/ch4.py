# -*- coding: utf-8 -*-
"""บทที่ 4 การวิเคราะห์มิติและแบบจำลอง (Dimensional Analysis & Similitude)"""
from common import row, fin, exam

CH4_HTML = '''<section id="ch4">
<header class="top"><p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
<h1>บทที่ 4 การวิเคราะห์มิติและแบบจำลอง</h1>
<p class="sub">ทฤษฎีบท Buckingham Pi 8 ขั้นตอน · กฎความคล้ายคลึงของแบบจำลอง Froude & Reynolds</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
</header>

<h2 class="prob"><span class="tag">บทที่ 4</span>ข้อสอบเต็งหนึ่งการวิเคราะห์มิติและแบบจำลอง (9 ข้อ)</h2>
<div class="stmt">
<p>บทที่ 4 ออกข้อสอบอัตนัยแน่นอน 1 ข้อใหญ่ โดยมี 2 ส่วน: <b>(1) ทฤษฎีบท Buckingham \(\Pi\)</b> บังคับแสดงครบ 8 ลำดับขั้นตามระเบียบอาจารย์ และ <b>(2) กฎการสเกลแบบจำลอง (Similitude)</b></p>
</div>

<div class="jump">
<a href="#ch4-bpi">1. Buckingham Pi 8 ขั้นตอน (ข้อ 2 แรงผลักใบพัด)</a>
<a href="#ch4-froude">2. Froude Similitude แบบจำลองแม่น้ำ (ข้อ 6)</a>
<a href="#ch4-reynolds">3. Reynolds Similitude แบบจำลองท่อ (ข้อ 5)</a>
</div>

<hr>

<!-- 1. BUCKINGHAM PI EX 2 -->
<h3 id="ch4-bpi" class="part">1. ตัวอย่างข้อ 2 (หน้า 23): Buckingham \(\Pi\) Theorem 8 ขั้นตอน (แรงผลักใบพัด)</h3>
<div class="stmt">
<p><b>โจทย์:</b> แรงผลัก \(F\) ที่เกิดจากใบพัดเครื่องจักร ขึ้นอยู่กับ เส้นผ่านศูนย์กลาง \(D\), ความหนาแน่นของของไหล \(\rho\), ความหนืดสัมบูรณ์ \(\mu\), และความเร็วเชิงมุม \(\omega\) จงหากลุ่มตัวแปรที่ไม่มีมิติที่เกี่ยวข้อง</p>
</div>

<h3 class="part">เฉลยวิธีทำ 8 ลำดับขั้นมาตรฐานอาจารย์ (ห้ามลัดขั้นตอน)</h3>
''' + exam([
    row('ขั้น 1: ฟังก์ชัน', r'F = f(D, \rho, \mu, \omega) \implies \text{จำนวนตัวแปรทั้งหมด } k = 5'),
    row('ขั้น 2: มิติพื้นฐาน', r'[F] = M L T^{-2}, \quad [D] = L, \quad [\rho] = M L^{-3}, \quad [\mu] = M L^{-1} T^{-1}, \quad [\omega] = T^{-1}'),
    row('ขั้น 3: มิติหลัก', r'r = 3\text{ มิติ } (M, L, T) \implies \text{จำนวนกลุ่มไร้มิติ } \Pi = k - r = 5 - 3 = 2\text{ กลุ่ม } (\Pi_1, \Pi_2)'),
    row('ขั้น 4: ตัวแปรซ้ำ', r'\text{เลือก } r=3\text{ ตัวแปร: } D\text{ (เรขาคณิต)}, \quad \rho\text{ (ของไหล)}, \quad \omega\text{ (จลนศาสตร์)}'),
    row('ขั้น 5: ตั้งกลุ่ม Pi 1', r'\Pi_1 = F \cdot D^a \rho^b \omega^c \implies [M^0 L^0 T^0] = (M L T^{-2}) \cdot (L)^a \cdot (M L^{-3})^b \cdot (T^{-1})^c'),
    row('ขั้น 6: แก้หากลุ่ม 1', r'M: 1 + b = 0 \implies b = -1; \quad T: -2 - c = 0 \implies c = -2; \quad L: 1 + a - 3b = 0 \implies a = -4'),
    row('ผลลัพธ์ Pi 1', r'\mathbf{\Pi_1 = \dfrac{F}{\rho \omega^2 D^4}\text{ (Thrust Coefficient)}}'),
    row('ตั้งกลุ่ม Pi 2', r'\Pi_2 = \mu \cdot D^d \rho^e \omega^f \implies [M^0 L^0 T^0] = (M L^{-1} T^{-1}) \cdot (L)^d \cdot (M L^{-3})^e \cdot (T^{-1})^f'),
    row('แก้หากลุ่ม 2', r'M: 1 + e = 0 \implies e = -1; \quad T: -1 - f = 0 \implies f = -1; \quad L: -1 + d - 3e = 0 \implies d = -2'),
    row('ผลลัพธ์ Pi 2', r'\Pi_2 = \dfrac{\mu}{\rho \omega D^2} \implies \text{กลับเศษเป็นส่วนเป็น } \mathbf{\Pi_2 = \dfrac{\rho \omega D^2}{\mu}\text{ (Rotational Reynolds Number)}}'),
    row('ขั้น 7: รูปฟังก์ชัน', r'\mathbf{\dfrac{F}{\rho \omega^2 D^4} = \phi\left( \dfrac{\rho \omega D^2}{\mu} \right)}'),
    row('ขั้น 8: ตรวจมิติ', r'\left[ \dfrac{M L T^{-2}}{(M L^{-3})(T^{-2})(L^4)} \right] = \left[ \dfrac{M L T^{-2}}{M L T^{-2}} \right] = [M^0 L^0 T^0] \quad \checkmark'),
    fin(r'\dfrac{F}{\rho \omega^2 D^4} = \phi\left( \dfrac{\rho \omega D^2}{\mu} \right)')
]) + '''

<hr>

<!-- 2. FROUDE SIMILITUDE EX 6 -->
<h3 id="ch4-froude" class="part">2. ตัวอย่างข้อ 6 (หน้า 23): แบบจำลองแม่น้ำด้วย Froude Similitude</h3>
<div class="stmt">
<p><b>โจทย์:</b> แบบจำลองแม่น้ำสายหนึ่งสร้างมาในอัตราส่วน \(1:80\) (\(\lambda_L = \frac{1}{80}\)) จงหาความเร็วในแม่น้ำของ Prototype (\(v_p\)) เมื่อความเร็วของแบบจำลองเท่ากับ \(v_m = 18\text{ m/s}\)</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('เกณฑ์ความคล้าย', r'Fr_m = Fr_p \implies \dfrac{v_m}{\sqrt{g L_m}} = \dfrac{v_p}{\sqrt{g L_p}}'),
    row('อัตราส่วนความเร็ว', r'\lambda_v = \dfrac{v_m}{v_p} = \sqrt{\dfrac{L_m}{L_p}} = \sqrt{\lambda_L} = \sqrt{\dfrac{1}{80}} = \dfrac{1}{\sqrt{80}}'),
    row('คำนวณ vp', r'v_p = v_m \sqrt{\dfrac{L_p}{L_m}} = 18\text{ m/s} \times \sqrt{80} = 18 \times 8.94427 = 161.00\text{ m/s}'),
    fin(r'v_p = 161.00\text{ m/s}')
]) + '''

<hr>

<!-- 3. REYNOLDS SIMILITUDE EX 5 -->
<h3 id="ch4-reynolds" class="part">3. ตัวอย่างข้อ 5 (หน้า 23): แบบจำลองท่อด้วย Reynolds Similitude</h3>
<div class="stmt">
<p><b>โจทย์:</b> ท่อยาว \(200\text{ m}\) เส้นผ่านศูนย์กลาง \(0.5\text{ m}\) น้ำไหลด้วยความเร็ว \(0.2\text{ m/s}\) ถ้าต้องการสร้างแบบจำลองท่อนี้สัดส่วน \(1:10\) โดยใช้น้ำทดสอบ จงหาความเร็วของน้ำในท่อแบบจำลอง (\(v_m\))</p>
</div>

<h3 class="part">เฉลยวิธีทำ (เขียนส่งในห้องสอบ ตามลำดับ)</h3>
''' + exam([
    row('เกณฑ์ความคล้าย', r'Re_m = Re_p \implies \dfrac{v_m D_m}{\nu_m} = \dfrac{v_p D_p}{\nu_p}'),
    row('ของไหลชนิดเดียวกัน', r'\nu_m = \nu_p \implies v_m D_m = v_p D_p \implies v_m = v_p \left( \dfrac{D_p}{D_m} \right)'),
    row('แทนค่าสัดส่วน', r'v_m = 0.2\text{ m/s} \times \left( \dfrac{10}{1} \right) = 2.0\text{ m/s}'),
    fin(r'v_m = 2.0\text{ m/s}')
]) + '''
</section>'''
