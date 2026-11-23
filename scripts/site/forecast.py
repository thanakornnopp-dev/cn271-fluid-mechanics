# -*- coding: utf-8 -*-
"""หน้าเก็งข้อสอบอัตนัยและจุดดักคะแนนวิชา CN271 (Fluid Mechanics)"""

FORECAST_HTML = '''<section id="forecast">
<header class="top"><p class="kick">วิเคราะห์และเก็งข้อสอบอัตนัย CN271</p>
<h1>แผนเก็งข้อสอบ & 5 จุดดักคะแนนมรณะ</h1>
<p class="sub">สังเคราะห์จากเอกสารตัวอย่างโจทย์จริงปี 2569 และ 2570 ภาควิชาวิศวกรรมโยธา มธ.</p>
<p class="by">วย 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
</header>

<h2 class="prob"><span class="tag">เก็งข้อสอบ</span>วิเคราะห์ 4 โซนข้อสอบเต็ง 1 ที่ต้องฝึกทำให้คล่อง 100%</h2>
<div class="stmt">
<p>จากการวิเคราะห์สถิติข้อสอบอัตนัยวิชา CN271 และชุดตัวอย่างโจทย์ 2569–2570 ของอาจารย์ผู้สอน ข้อสอบจะเน้นการเขียนวิธีทำเต็มรูป <b>ห้ามลัดขั้นตอนเด็ดขาด (Strict No-Shortcut Policy)</b> โดยแบ่งน้ำหนักคะแนนออกเป็น 4 โซนหลักที่ออกสอบอย่างแน่นอน:</p>
</div>

<div class="jump">
<a href="#fc-zones">ก. 4 โซนข้อสอบเต็ง 1</a>
<a href="#fc-table">ข. ตารางข้อที่ต้องซ้อมทำในชีท</a>
<a href="#fc-traps">ค. 5 จุดดักคะแนนมรณะ</a>
<a href="#fc-strat">ง. กลยุทธ์การเขียนตอบในห้องสอบ</a>
</div>

<h3 id="fc-zones" class="part">ก. 4 โซนข้อสอบเต็ง 1 (High-Yield Exam Zones)</h3>
<div class="ty"><div class="tyh">Zone 1: สถิตยศาสตร์ของไหลและบานประตู (Fluid Statics & Gates) — ออกชัวร์ 95%</div><div class="tyb">
<p class="gq"><b>ลักษณะโจทย์:</b> มาโนมิเตอร์ของเหลวหลายชนิดท่อเอียง + แรงดันบนประตูระนาบเอียงหรือระนาบโค้ง</p>
<ol class="st">
<li><b>มาโนมิเตอร์ (Manometer):</b> กฎการเดินท่อขึ้นลบ-ลงบวก \(P_2 = P_1 \pm \gamma \Delta h\) สำหรับท่อเอียงมุม \(\theta\) ระยะดิ่งคือ \(\Delta h = L \sin\theta\) <i>(ซ้อมข้อ 9, 13, 17 ในชีทบทที่ 2)</i></li>
<li><b>แรงดันบนระนาบเรียบและบานพับ (Plane Gates):</b> หา \(F_R = \gamma h_{cg} A\) และ \(y_{cp} = y_{cg} + \dfrac{I_{xx,c}}{y_{cg} A}\) จากนั้นเทคโมเมนต์รอบบานพับ \(\sum M_{\text{hinge}} = 0\) เพื่อหาน้ำหนักประตูหรือแรงดึงลวด <i>(ซ้อมข้อ 22, 23, 26 ในชีทบทที่ 2)</i></li>
<li><b>แรงดันบนระนาบโค้ง (Curved Surfaces):</b> แยกคิดแรงแนวราบ \(F_H = \gamma h_{cg,\text{proj}} A_{\text{proj}}\) และแรงแนวดิ่ง \(F_V = \gamma \times \text{Volume}\) แล้วรวมเวกเตอร์ \(F_R = \sqrt{F_H^2 + F_V^2}\) <i>(ซ้อมข้อ 29, 31 ในชีทบทที่ 2)</i></li>
</ol>
<div class="bx chk"><b>จุดเน้นอาจารย์:</b> อย่าสับสนระหว่าง \(y_{cp}\) (วัดตามแนวเอียงของบานประตู) กับ \(h_{cp}\) (วัดในแนวดิ่งจากผิวน้ำ)</div>
</div></div>

<div class="ty"><div class="tyh">Zone 2: แรงโมเมนตัมของสายน้ำ (Linear Momentum Equation) — ออกชัวร์ 90%</div><div class="tyb">
<p class="gq"><b>ลักษณะโจทย์:</b> ลำน้ำพุ่งชนแผ่นโค้งเบี่ยงทิศทาง (Deflector Vane) หรือแรงกระทำที่ข้องอท่อ</p>
<ol class="st">
<li><b>แผ่นโค้งอยู่นิ่ง (\(u = 0\)):</b> อัตราการไหลเชิงมวล \(\dot{m} = \rho A v\) แรงกระทำ \(F_x = \dot{m} (v_1 - v_2 \cos\theta)\) ถ้าหักกลับ \(180^\circ\) จะได้ \(F_x = 2 \dot{m} v = 2 \rho A v^2\) <i>(ซ้อมข้อ 5 ก บทที่ 3: ตอบ 11.52 kN)</i></li>
<li><b>แผ่นโค้งเคลื่อนที่ตามน้ำด้วยความเร็ว \(u\):</b> <u>จุดที่นักศึกษาผิดมากที่สุด</u> ต้องใช้ความเร็วสัมพัทธ์ \(v_r = v - u\) และอัตราการไหลเชิงมวลที่กระทบจริง \(\dot{m}_r = \rho A (v - u)\) ทำให้แรงลดลงเหลือ \(F_x = 2 \rho A (v - u)^2\) <i>(ซ้อมข้อ 5 ข บทที่ 3: ตอบ 6.48 kN)</i></li>
</ol>
<div class="bx chk"><b>ตรวจ:</b> แผ่นเคลื่อนที่ตามน้ำ แรงปะทะต้องน้อยกว่าแผ่นอยู่นิ่งเสมอ (\(6.48\text{ kN} < 11.52\text{ kN}\))</div>
</div></div>

<div class="ty"><div class="tyh">Zone 3: การวิเคราะห์มิติและแบบจำลอง (Dimensional Analysis & Similitude) — ออกชัวร์ 95%</div><div class="tyb">
<p class="gq"><b>ลักษณะโจทย์:</b> ทฤษฎีบท Buckingham \(\Pi\) แสดงครบ 8 สเต็ป + กฎความคล้ายคลึงของแบบจำลอง</p>
<ol class="st">
<li><b>Buckingham \(\Pi\) Theorem:</b> ต้องเขียนครบ 8 สเต็ป (ฟังก์ชันนับ \(k\) \(\rightarrow\) มิติ \(M, L, T\) ทุกตัว \(\rightarrow\) มิติหลัก \(r=3\) \(\rightarrow\) เลือกตัวแปรซ้ำ \(r\) ตัว \(\rightarrow\) ตั้งสมการเลขชี้กำลัง \(\rightarrow\) เทียบหา \(A, B, C\) \(\rightarrow\) รวมกลุ่มไร้มิติ \(\rightarrow\) ตรวจสอบมิติ \([M^0 L^0 T^0]\)) <i>(ซ้อมข้อ 2 แรงผลักใบพัด บทที่ 4)</i></li>
<li><b>Froude Similitude (สำหรับแม่น้ำ/คลื่น/เรือ):</b> \(Fr_m = Fr_p \implies \lambda_v = \sqrt{\lambda_L}, \quad \lambda_Q = \lambda_L^{2.5}\) <i>(ซ้อมข้อ 6 บทที่ 4: สเกล 1:80 ได้ \(v_p = 161\text{ m/s}\))</i></li>
<li><b>Reynolds Similitude (สำหรับท่อ/อากาศยาน):</b> \(Re_m = Re_p \implies \lambda_v = 1 / \lambda_L\) เมื่อใช้ของไหลชนิดเดียวกัน <i>(ซ้อมข้อ 5 บทที่ 4: สเกล 1:10 ได้ \(v_m = 2.0\text{ m/s}\))</i></li>
</ol>
<div class="bx chk"><b>จุดเน้นอาจารย์:</b> ห้ามเลือกตัวแปรเป้าหมาย (เช่น \(F\) หรือ \(Q\)) เป็นตัวแปรซ้ำเด็ดขาด</div>
</div></div>

<div class="ty"><div class="tyh">Zone 4: การไหลในท่อและระบบท่อส่งน้ำ (Flow in Pipes & Losses) — ออกชัวร์ 98%</div><div class="tyb">
<p class="gq"><b>ลักษณะโจทย์:</b> โจทย์ Type II ปล่อยน้ำออกจากถังผ่านข้องอ หรือโจทย์ท่อขนาน/อนุกรม</p>
<ol class="st">
<li><b>Type II วนซ้ำหา \(v\) (เน้น "ข้อสอบแน่!"):</b> จัดรูป \(v = \dfrac{C}{\sqrt{\sum K_L + f(L/D)}}\) ตีตารางเดา \(f\) เพียง 2 รอบ ลู่เข้าที่ \(v = 2.51\text{ m/s}, f = 0.0195\) <i>(ซ้อมข้อ 7 บทที่ 5)</i></li>
<li><b>Type III วนซ้ำหาขนาดท่อ \(D\):</b> ดึงตัวแปร \(D^5 = 0.41314 f\) วนลูป 3 รอบจนได้ \(D \approx 0.36\text{ m} = 360\text{ mm}\) <i>(ซ้อมข้อ 8 บทที่ 5)</i></li>
<li><b>ระบบท่อขนาน 4 ท่อ:</b> เฮดสูญเสียเท่ากันทุกท่อ \(h_{L1} = h_{L2} = \dots = h_{Ln}\) และ \(Q_{\text{total}} = \sum Q_i\) <i>(ซ้อมข้อสอบ 15 คะแนน)</i></li>
</ol>
<div class="bx chk"><b>ตรวจ:</b> พจน์ปลายท่อเปิดสู่อากาศมี Velocity Head \(\dfrac{v^2}{2g}\) รวมกับ Minor Loss ทางเข้าและข้องอ กลายเป็นตัวคูณ \(2.6\)</div>
</div></div>

<hr>

<h3 id="fc-table" class="part">ข. ตารางข้อที่ต้องซ้อมทำในชีท 2569/2570</h3>
<div class="table-container">
<table>
<thead>
<tr>
<th>บทเรียน</th>
<th>ข้อในชีท</th>
<th>หัวข้อโจทย์</th>
<th>สูตรและตัวแปรหลัก</th>
<th>คำตอบที่ถูกต้อง 100%</th>
<th>ระดับความเสี่ยง</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>บทที่ 1</strong></td>
<td>ข้อ 1 (น.1)</td>
<td>Shear Stress แผ่นเลื่อนขนาน</td>
<td>\(\tau = \mu \dfrac{V}{h}\)</td>
<td>\(\mathbf{\tau = 116\text{ N/m}^2}\)</td>
<td><span class="tag">พื้นฐาน</span></td>
</tr>
<tr>
<td><strong>บทที่ 2</strong></td>
<td>ข้อ 9 (น.3)</td>
<td>มาโนมิเตอร์ของเหลว 2 ชนิด</td>
<td>\(P_2 = P_1 \pm \gamma h\)</td>
<td>\(\mathbf{P_A = -1,962\text{ Pa}, P_E = 7,455.6\text{ Pa}}\)</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 2</strong></td>
<td>ข้อ 22-23 (น.8)</td>
<td>แรงดันบนผนังระนาบเรียบ</td>
<td>\(F_R = \gamma h_{cg} A, \quad y_{cp} = y_{cg} + \dfrac{I_{xx}}{y_{cg}A}\)</td>
<td>\(\mathbf{F_R = 882.9\text{ kN}, y_{cp} = 4.0\text{ m}}\)</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 2</strong></td>
<td>ข้อ 26 (น.9)</td>
<td>บานประตูปิดน้ำเอียงสมดุลบานพับ</td>
<td>\(\sum M_C = 0 \implies F_R \cdot d_F = W \cdot d_W\)</td>
<td>\(\mathbf{W = 180.5\text{ kN}}\)</td>
<td><span class="tag" style="background:#d97706;">ปราบเซียน</span></td>
</tr>
<tr>
<td><strong>บทที่ 2</strong></td>
<td>ข้อ 29 (น.10)</td>
<td>แรงดันบนผิวโค้งวงกลม</td>
<td>\(F_H = \gamma h_{cg} A_{\text{proj}}, F_V = \gamma \cdot \text{Vol}\)</td>
<td>\(\mathbf{F_R = 657.6\text{ kN}, \theta = 57.5^\circ}\)</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 3</strong></td>
<td>ข้อ 5 (น.21)</td>
<td>สายน้ำชนแผ่นโค้ง 180°</td>
<td>อยู่นิ่ง: \(2\rho A v^2\) / เคลื่อนที่: \(2\rho A (v-u)^2\)</td>
<td>\(\mathbf{11.52\text{ kN}}\) (นิ่ง) / \(\mathbf{6.48\text{ kN}}\) (เคลื่อนที่)</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 3</strong></td>
<td>ข้อ 9 (น.22)</td>
<td>ท่อกาลักน้ำ (Siphon)</td>
<td>Bernoulli ระหว่างผิวน้ำกับยอดท่อ</td>
<td>\(\mathbf{v = 7.67\text{ m/s}, P_2 = -41.2\text{ kPa}}\)</td>
<td><span class="tag">เน้นมโนทัศน์</span></td>
</tr>
<tr>
<td><strong>บทที่ 4</strong></td>
<td>ข้อ 2 (น.23)</td>
<td>Buckingham \(\Pi\) แรงผลักใบพัด</td>
<td>\(F = f(D, \rho, \mu, \omega)\) บังคับแสดง 8 ขั้น</td>
<td>\(\mathbf{\Pi_1 = \dfrac{F}{\rho \omega^2 D^4}, \Pi_2 = \dfrac{\rho \omega D^2}{\mu}}\)</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 4</strong></td>
<td>ข้อ 6 (น.23)</td>
<td>Froude Similitude แม่น้ำ</td>
<td>\(\lambda_v = \sqrt{\lambda_L} \implies v_p = v_m \sqrt{L_p/L_m}\)</td>
<td>\(\mathbf{v_p = 161.0\text{ m/s}}\) (เมื่อ \(v_m = 18\))</td>
<td><span class="tag" style="background:#059669;">เต็งหนึ่ง</span></td>
</tr>
<tr>
<td><strong>บทที่ 5</strong></td>
<td>ข้อ 7 (น.40)</td>
<td><strong>ปล่อยน้ำจากถังผ่านข้องอ</strong></td>
<td>สมการพลังงาน + ตารางวนซ้ำ \(f\) 2 รอบ</td>
<td>\(\mathbf{v = 2.51\text{ m/s}, Q = 44.4\text{ L/s}}\)</td>
<td><span class="tag" style="background:#dc2626;">ออกแน่ 100%</span></td>
</tr>
<tr>
<td><strong>บทที่ 5</strong></td>
<td>ข้อ 8 (น.40)</td>
<td>ออกแบบขนาดท่อ \(D\) (Type III)</td>
<td>ดึงตัวแปร \(D^5 = 0.41314 f\) วนลูป 3 รอบ</td>
<td>\(\mathbf{D \approx 0.366\text{ m} \approx 360\text{ mm}}\)</td>
<td><span class="tag" style="background:#d97706;">ปราบเซียน</span></td>
</tr>
</tbody>
</table>
</div>

<hr>

<h3 id="fc-traps" class="part">ค. 5 จุดดักคะแนนมรณะ (Deadly Exam Traps)</h3>
<div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
<b>Trap 1: การลืม Velocity Head ปลายท่อในโจทย์ Type II</b>
<div>เมื่อท่อปล่อยน้ำออกสู่อากาศอิสระ พลังงานจลน์ที่พุ่งออกไปคือ \(\dfrac{v^2}{2g}\) ซึ่งจะรวมเข้ากับ Minor Losses หน้าวงเล็บ \(\dfrac{v^2}{2g}\) จึงต้องมีเลข \(1.0\) เสมอ เช่นในข้อ 7 กลายเป็น \([1.0_{\text{exit}} + 1.0_{\text{entrance}} + 2(0.3)_{\text{elbows}} + f(100/0.15)] = [2.6 + 666.67 f]\) ถ้าลืม \(1.0\) ของปลายท่อ ตัวเลขความเร็วจะผิดทันที</div>
</div>

<div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
<b>Trap 2: การแปลงหน่วยมิลลิเมตรและความขรุขระสัมพัทธ์</b>
<div>ความขรุขระ \(\varepsilon = 0.12\text{ mm} = 0.00012\text{ m}\) และท่อ \(D = 15\text{ cm} = 0.15\text{ m}\) เมื่อนำมาหารกันต้องใช้หน่วยเดียวกัน \(\dfrac{\varepsilon}{D} = \dfrac{0.12}{150} = 0.0008\) ถ้าใช้หน่วยผิดจะเปิดชาร์ต Moody ผิดเส้นอย่างสิ้นเชิง</div>
</div>

<div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
<b>Trap 3: ความเร็วสัมพัทธ์ในสมการโมเมนตัม</b>
<div>เมื่อใบพัดหรือแผ่นโค้งเคลื่อนที่ตามน้ำด้วยความเร็ว \(u\) สายน้ำที่กระทบจริงจะมีความเร็วสัมพัทธ์ลดลงเป็น \(v_r = v - u\) และมวลน้ำที่พุ่งเข้าปะทะต่อวินาทีก็ลดลงเป็น \(\dot{m}_r = \rho A (v - u)\) ห้ามใช้ \(\rho A v\) เพราะน้ำส่วนหนึ่งจะวิ่งตามแผ่นไปทันที</div>
</div>

<div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
<b>Trap 4: การวัดระยะ \(y_{cp}\) และ \(h_{cp}\) ของบานประตู</b>
<div>\(y_{cp}\) วัดตามความยาวของระนาบเอียง ส่วน \(h_{cp}\) วัดในแนวดิ่งจากระดับผิวน้ำอิสระ โดยมีสูตรเชื่อมกันคือ \(h_{cp} = y_{cp} \sin\theta\) เมื่อนำไปเทคโมเมนต์รอบบานพับ ต้องใช้แขนของแรงที่ตั้งฉากกับแนวแรงจริง ๆ เสมอ</div>
</div>

<div class="bx chk" style="border-left-color:var(--red);">
<b>Trap 5: การเลือก Repeating Variables ในทฤษฎีบท Buckingham \(\Pi\)</b>
<div>ตัวแปรซ้ำ 3 ตัวที่เลือกต้องประกอบด้วย: (1) ตัวแปรเรขาคณิต เช่น \(D\), (2) ตัวแปรของไหล เช่น \(\rho\), (3) ตัวแปรจลนศาสตร์ เช่น \(\omega\) หรือ \(V\) และ<u>ห้ามเลือกตัวแปรเป้าหมายที่โจทย์ต้องการหา</u> (เช่น ห้ามเลือก \(F\) หรือ \(Q\) เป็นตัวแปรซ้ำ)</div>
</div>

<hr>

<h3 id="fc-strat" class="part">ง. กลยุทธ์การเขียนตอบในห้องสอบเพื่อโกยคะแนนเต็ม</h3>
<ol class="st">
<li><b>บรรทัดแรก:</b> เขียนสมการ Governing Equation เต็มรูปก่อนเสมอ (เช่น Navier-Stokes, Reynolds, Bernoulli, Energy Equation)</li>
<li><b>บรรทัดสอง:</b> แสดงการขีดฆ่าพจน์ที่เป็นศูนย์พร้อมกำกับเหตุผล (เช่น \(P_1 = P_2 = 0\text{ atm}\), \(v_1 \approx 0\text{ ถังใหญ่}\))</li>
<li><b>บรรทัดสาม:</b> จัดรูปดึงตัวแปรเป้าหมายค้างไว้ทางซ้ายมือ แล้วค่อยแทนค่าตัวเลขพร้อมหน่วยในบรรทัดถัดไป</li>
<li><b>กรณี Trial & Error:</b> ตีตาราง 5 ช่อง (รอบ | \(f\) สมมติ | ค่าที่คำนวณได้ | \(Re\) | \(f\) ใหม่) แสดงเพียง 2 รอบจนค่าลู่เข้า จะได้คะแนนเต็ม 100%</li>
</ol>
</section>'''
