# -*- coding: utf-8 -*-

def get_section_ch3():
    return r'''
<section id="ch3">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
    <h1>บทที่ 3: จลนศาสตร์และสมการโมเมนตัม (Kinematics &amp; Momentum)</h1>
    <p class="sub">สมการความต่อเนื่อง · สมการพลังงานเบอร์นูลลี · สมการโมเมนตัมเชิงเส้น · ลำน้ำพุ่งชนแผ่นโค้ง 180° · ท่อกาลักน้ำ (Siphon)</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 3</span>ข้อสอบเต็งหนึ่งสมการโมเมนตัมและพลังงาน (10 ข้อ)</h2>
  <div class="stmt">
    <p>บทที่ 3 เน้นโจทย์ 2 รูปแบบที่ออกสอบอัตนัยบ่อยที่สุด: <b>(1) แรงปะทะของลำน้ำบนแผ่นโค้ง (Jet on Vane)</b> เปรียบเทียบกรณีแผ่นอยู่นิ่งกับแผ่นเคลื่อนที่ตามลำน้ำ และ <b>(2) ท่อกาลักน้ำ (Siphon)</b> ที่ความดันที่จุดสูงสุดของท่อมีค่าติดลบ (ความดันสุญญากาศ)</p>
  </div>

  <div class="jump">
    <a href="#ch3-theory">ก. สูตรและหลักการโมเมนตัม</a>
    <a href="#ch3-traps">ข. จุดดักคะแนนข้อสอบ</a>
    <a href="#ch3-jet">ค. ตัวอย่างข้อ 5 ลำน้ำพุ่งชนแผ่นโค้ง 180° (หน้า 21)</a>
    <a href="#ch3-siphon">ง. ตัวอย่างข้อ 9 ท่อกาลักน้ำ Siphon (หน้า 22)</a>
  </div>

  <h3 class="grp" id="ch3-theory">ก. สูตรและหลักการโมเมนตัม First Principles</h3>
  <div class="plan">
    <p><b class="l">สมการความต่อเนื่อง (Continuity Equation):</b> สำหรับของไหลที่อัดตัวไม่ได้:
    $$Q = A_1 v_1 = A_2 v_2 = \text{คงที่}\tag{3.1}$$</p>
    <p><b class="l">สมการโมเมนตัมเชิงเส้น (Linear Momentum):</b>
    $$\sum F_x = \dot{m} (v_{2x} - v_{1x})\tag{3.2}$$
    แรงที่ของไหลกระทำต่อแผ่นเบนลำน้ำ (\(R_x\)):
    $$R_x = \dot{m} (v_{1x} - v_{2x})\tag{3.3}$$</p>
    <p><b class="l">แผ่นโค้งเคลื่อนที่ด้วยความเร็ว \(u\):</b> ความเร็วสัมพัทธ์ที่ไหลเข้าและออกจากแผ่นคือ \(v_r = v - u\) และอัตราการไหลเชิงมวลที่ปะทะแผ่นคือ \(\dot{m}_{\text{rel}} = \rho A (v - u)\):
    $$R_x = \rho A (v - u)^2 (1 - \cos\theta)\tag{3.4}$$
    สำหรับแผ่นโค้งรูปตัวยู \(180^\circ\) (\(\cos 180^\circ = -1\)):
    $$R_x = 2 \rho A (v - u)^2\tag{3.5}$$</p>
  </div>

  <h3 class="grp" id="ch3-traps">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>ข้อผิดพลาดอันดับ 1: ใช้ \(\dot{m}\) เดิมเมื่อแผ่นเคลื่อนที่</b>
    <div>
      เมื่อแผ่นโค้งเคลื่อนที่หนีลำน้ำด้วยความเร็ว \(u = 6\text{ m/s}\):<br>
      • น้ำที่กระทบแผ่นใน 1 วินาทีจะมีปริมาตรลดลง อัตราการไหลมวลจริงที่ปะทะแผ่นคือ \(\dot{m}_{\text{rel}} = \rho A (v - u)\) ไม่ใช่ \(\rho A v\)<br>
      • หากใช้ \(\dot{m} = \rho A v\) ค่าแรงจะผิดทันทีเป็น \(8.64\text{ kN}\) (คำตอบที่ถูกต้องคือ \(6.48\text{ kN}\))
    </div>
  </div>

  <hr>

  <!-- 1. JET ON VANE EX 5 -->
  <h3 id="ch3-jet" class="grp">ค. ตัวอย่างข้อ 5 (หน้า 21): ลำน้ำพุ่งชนแผ่นโค้ง 180°</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 5:</b> น้ำพุ่งชนแผ่นโค้งตามรูป น้ำมีความเร็ว \(v = 24\text{ m/s}\) พื้นที่ของสายน้ำ \(A = 0.010\text{ m}^2\) แผ่นโค้งมีผิวเรียบ น้ำมีความเร็วคงที่<br>
    (ก) จงหาแรงกระทำสุทธิต่อแผ่นโค้ง เมื่อแผ่นโค้งอยู่นิ่ง (\(u = 0\))<br>
    (ข) จงหาแรงกระทำสุทธิต่อแผ่นโค้ง เมื่อแผ่นโค้งเคลื่อนที่ไปในทิศทางเดียวกับน้ำด้วยความเร็ว \(u = 6\text{ m/s}\)</p>
  </div>

  <figure>
    <svg viewBox="0 0 620 200" role="img" aria-label="ลำน้ำพุ่งชนแผ่นโค้ง 180 องศา">
      <!-- Curved Vane -->
      <path d="M380 40 A70 70 0 0 1 380 160" fill="none" stroke="var(--ink)" stroke-width="12"/>
      <path d="M380 40 A70 70 0 0 1 380 160" fill="none" stroke="var(--hover)" stroke-width="8"/>

      <!-- Incoming jet -->
      <rect x="60" y="92" width="310" height="16" fill="var(--water)" opacity="0.8"/>
      <path d="M60 100 H360" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
      <text x="180" y="80" font-size="14" font-weight="700" fill="var(--blue)">ลำน้ำเข้า: v₁ = 24 m/s (A = 0.010 m²)</text>

      <!-- Deflected upper jet -->
      <path d="M375 42 H220" stroke="var(--blue)" stroke-width="2.5" marker-end="url(#ar)"/>
      <text x="210" y="32" font-size="13" font-weight="600" fill="var(--navy)">ลำน้ำออกด้านบน: v₂x = -v</text>

      <!-- Deflected lower jet -->
      <path d="M375 158 H220" stroke="var(--blue)" stroke-width="2.5" marker-end="url(#ar)"/>
      <text x="210" y="180" font-size="13" font-weight="600" fill="var(--navy)">ลำน้ำออกด้านล่าง: v₂x = -v</text>

      <!-- Force Rx on vane -->
      <path d="M410 100 H490" stroke="var(--red)" stroke-width="3.5" marker-end="url(#ar)"/>
      <text x="495" y="105" font-size="15" font-weight="700" fill="var(--red)">Rx</text>
    </svg>
    <figcaption>รูปที่ 3.1 ลำน้ำพุ่งชนแผ่นโค้งรูปตัวยู 180° (180° Jet Deflection)</figcaption>
  </figure>

  <h4 class="cardt">เฉลยวิธีทำ: (ก) กรณีแผ่นโค้งอยู่นิ่ง (u = 0)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">อัตราการไหลเชิงมวล \(\dot{m}\)</div>
      <div class="given">$$\dot{m} = \rho A v = (1,000\ \text{kg/m}^3) \times (0.010\ \text{m}^2) \times (24\ \text{m/s}) = 240\ \text{kg/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">ความเร็วตามแนวแกน x</div>
      <div>$$v_{1x} = +24\ \text{m/s},\quad v_{2x} = -24\ \text{m/s}\ (\text{เลี้ยวกลับทิศ } 180^\circ)$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงกระทำต่อแผ่น \(R_x\)</div>
      <div>$$R_x = \dot{m} (v_{1x} - v_{2x}) = (240\ \text{kg/s}) \times [24 - (-24)]\ \text{m/s} = 240 \times 48 = 11,520\ \text{N}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบส่วนที่ (ก)</div>
      <div><span class="fin">\(R_x = 11,520\ \text{N} = 11.52\ \text{kN}\ (\text{ทิศไปทางขวา})\)</span></div>
    </div>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ: (ข) กรณีแผ่นโค้งเคลื่อนที่ตามน้ำด้วย u = 6 m/s</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ความเร็วสัมพัทธ์ \(v_r\)</div>
      <div class="given">$$v_r = v - u = 24 - 6 = 18\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">มวลน้ำปะทะแผ่นต่อวินาที \(\dot{m}_{\text{rel}}\)</div>
      <div>$$\dot{m}_{\text{rel}} = \rho A (v - u) = 1,000 \times 0.010 \times 18 = 180\ \text{kg/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">การเปลี่ยนความเร็วสัมพัทธ์</div>
      <div>$$\Delta v_{rx} = v_{r1x} - v_{r2x} = 18 - (-18) = 36\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงกระทำต่อแผ่น \(R_x\)</div>
      <div>$$R_x = \dot{m}_{\text{rel}} \Delta v_{rx} = 180\ \text{kg/s} \times 36\ \text{m/s} = 6,480\ \text{N} = 6.48\ \text{kN}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบส่วนที่ (ข)</div>
      <div><span class="fin">\(R_x = 6,480\ \text{N} = 6.48\ \text{kN}\ (\text{ทิศไปทางขวา})\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 2. SIPHON EX 9 -->
  <h3 id="ch3-siphon" class="grp">ง. ตัวอย่างข้อ 9 (หน้า 22): ท่อกาลักน้ำ Siphon</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 9:</b> ท่อกาลักน้ำเส้นผ่านศูนย์กลางสม่ำเสมอดึงน้ำออกจากถังเปิด ปลายท่อระบายออกสู่อากาศที่จุด 3 ต่ำกว่าระดับน้ำในถัง (จุด 1) เป็นระยะ \(H = 3.0\text{ m}\) และจุดยอดสูงสุดของท่อ (จุด 2) อยู่สูงกว่าระดับน้ำในถัง \(1.2\text{ m}\) จงหา (ก) ความเร็วของน้ำที่พุ่งออกจากปลายท่อ \(v_3\) และ (ข) ความดันเกจที่จุดยอดของท่อ \(P_2\) (ไม่คิดการสูญเสียพลังงาน)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">สมการพลังงาน จุด 1 ไปจุด 3</div>
      <div class="given">$$\frac{P_1}{\gamma} + z_1 + \frac{v_1^2}{2g} = \frac{P_3}{\gamma} + z_3 + \frac{v_3^2}{2g}$$</div>
    </div>
    <div class="row">
      <div class="lab">เงื่อนไขขอบเขต</div>
      <div>$$P_1 = P_3 = 0\ (\text{เกจ}),\quad v_1 \approx 0\ (\text{ถังใหญ่}),\quad z_1 - z_3 = 3.0\ \text{m}$$</div>
    </div>
    <div class="row">
      <div class="lab">หาความเร็วปลายท่อ \(v_3\)</div>
      <div>$$v_3 = \sqrt{2 g (z_1 - z_3)} = \sqrt{2 \times 9.81 \times 3.0} = \sqrt{58.86} = 7.672\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">สมการพลังงาน จุด 1 ไปจุด 2</div>
      <div>$$\frac{P_1}{\gamma} + z_1 + \frac{v_1^2}{2g} = \frac{P_2}{\gamma} + z_2 + \frac{v_2^2}{2g}$$</div>
    </div>
    <div class="row">
      <div class="lab">แทนค่าหาความดันจุดยอด \(P_2\)</div>
      <div>$$\begin{aligned} & 0 + 0 + 0 = \frac{P_2}{\gamma} + 1.2\ \text{m} + \frac{7.672^2}{2(9.81)}\ \text{m} \\ & 0 = \frac{P_2}{\gamma} + 1.2 + 3.0 \\ & \frac{P_2}{\gamma} = -4.2\ \text{m} \\ & P_2 = -4.2\ \text{m} \times 9,810\ \text{N/m}^3 = -41,202\ \text{Pa} = -41.2\ \text{kPa} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(v_3 = 7.67\ \text{m/s},\quad P_2 = -41.2\ \text{kPa (Gage)}\ (\text{ความดันสุญญากาศ } 41.2\ \text{kPa})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#ch2">← บทที่ 2 สถิตยศาสตร์ &amp; ประตูน้ำ</a>
    <a href="#ch4">บทที่ 4 วิเคราะห์มิติ &amp; สเกล →</a>
  </div>
</section>
'''
