# -*- coding: utf-8 -*-

def get_section_ch3():
    return r'''
<section id="ch3">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์ (จลนศาสตร์ &amp; พลศาสตร์ของไหล)</p>
    <h1>บทที่ 3: จลนศาสตร์และสมการโมเมนตัม (Kinematics &amp; Momentum)</h1>
    <p class="sub">สนามความเร็วและความเร่ง (Velocity &amp; Acceleration Field) · สมการความต่อเนื่อง · สมการพลังงานเบอร์นูลลี · สมการโมเมนตัมเชิงเส้น · ลำน้ำพุ่งชนแผ่นโค้ง 180° · ท่อกาลักน้ำ (Siphon)</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 3</span>ข้อสอบเต็งหนึ่งจลนศาสตร์ สมการโมเมนตัม และพลังงาน</h2>
  <div class="stmt">
    <p>บทที่ 3 ครอบคลุมหัวใจสำคัญ 3 หัวข้อหลักที่ออกสอบข้อเขียนทุกปี: <b>(1) ความเร็วและความเร่งของอนุภาคของไหล (Velocity &amp; Acceleration Field)</b> ซึ่งแบ่งเป็น Convective และ Local Acceleration, <b>(2) แรงปะทะของลำน้ำบนแผ่นโค้ง (Jet on Vane)</b> เปรียบเทียบกรณีแผ่นอยู่นิ่งกับแผ่นเคลื่อนที่ตามลำน้ำ และ <b>(3) ท่อกาลักน้ำ (Siphon)</b> ที่ความดันที่จุดสูงสุดของท่อมีค่าติดลบ (ความดันสุญญากาศ)</p>
  </div>

  <div class="jump">
    <a href="#ch3-theory">ก. สูตรและหลักการ First Principles</a>
    <a href="#ch3-traps">ข. จุดดักคะแนนข้อสอบ</a>
    <a href="#ch3-accel">1. ความเร็วและความเร่งของอนุภาคของไหล (ตัวอย่างข้อ 1)</a>
    <a href="#ch3-jet">2. ลำน้ำพุ่งชนแผ่นโค้ง 180° (ข้อ 5 หน้า 21)</a>
    <a href="#ch3-siphon">3. ท่อกาลักน้ำ Siphon (ข้อ 9 หน้า 22)</a>
  </div>

  <h3 class="grp" id="ch3-theory">ก. สูตรและหลักการ First Principles (อธิบายแบบเข้าใจง่าย)</h3>
  <div class="plan">
    <p><b class="l">สนามความเร็ว 3 มิติ (Velocity Field):</b> ความเร็วของอนุภาคของไหลที่ตำแหน่ง \((x,y,z)\) ณ เวลา \(t\) ใดๆ เขียนในรูปเวกเตอร์ได้เป็น:
    $$\vec{V}(x,y,z,t) = u\vec{i} + v\vec{j} + w\vec{k}\tag{3.1}$$
    เมื่อ \(u = u(x,y,z,t)\), \(v = v(x,y,z,t)\) และ \(w = w(x,y,z,t)\) คือความเร็วในแนวแกน \(x, y, z\) ตามลำดับ</p>

    <p><b class="l">ความเร่งของอนุภาคของไหล (Material / Substantial Derivative):</b> ในกลศาสตร์ของไหล อนุภาคไม่ได้เร่งขึ้นเพราะเวลาเปลี่ยนเพียงอย่างเดียว (แบบฟิสิกส์มัธยม) แต่เร่งขึ้นเพราะ <i>อนุภาคไหลเคลื่อนที่ไปยังตำแหน่งอื่นที่มีความเร็วไม่เท่ากันด้วย</i> จึงเขียนในรูปอนุพันธ์รวม \(\dfrac{D\vec{V}}{Dt}\):
    $$\vec{a} = \frac{D\vec{V}}{Dt} = (\vec{V} \cdot \nabla)\vec{V} + \frac{\partial \vec{V}}{\partial t}\tag{3.2}$$</p>

    <p><b class="l">การแยกองค์ประกอบความเร่ง 3 แกน (Component Equations):</b>
    $$a_x = \underbrace{u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z}}_{\text{Convective Acceleration (ความเร่งพา)}} + \underbrace{\frac{\partial u}{\partial t}}_{\text{Local Acc. (ความเร่งเฉพาะที่)}}\tag{3.3}$$
    $$a_y = \underbrace{u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z}}_{\text{Convective Acceleration (ความเร่งพา)}} + \underbrace{\frac{\partial v}{\partial t}}_{\text{Local Acc. (ความเร่งเฉพาะที่)}}\tag{3.4}$$
    $$a_z = \underbrace{u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z}}_{\text{Convective Acceleration (ความเร่งพา)}} + \underbrace{\frac{\partial w}{\partial t}}_{\text{Local Acc. (ความเร่งเฉพาะที่)}}\tag{3.5}$$</p>

    <p><b class="l">ความหมายทางกายภาพ (Physical Intuition):</b><br>
    • <b>Convective Acceleration (ความเร่งพา):</b> เกิดจากอนุภาคไหลเปลี่ยนตำแหน่งในปริภูมิ เช่น ไหลผ่านท่อบีบคอคอด (Nozzle) น้ำจะพุ่งเร็วขึ้น แม้ว่าระบบจะปล่อยน้ำคงที่ตลอดเวลาก็ตาม<br>
    • <b>Local / Unsteady Acceleration (ความเร่งเฉพาะที่ / ความเร่งตามเวลา):</b> เกิดจากการเปลี่ยนแปลงความเร็วตามเวลา ณ ตำแหน่งเดิม เช่น ตอนเริ่มเปิดวาล์วหรือปิดวาล์ว หากเป็นการไหลแบบคงตัว (Steady Flow) พจน์นี้จะเป็นศูนย์ (\(\partial/\partial t = 0\))</p>

    <p><b class="l">สมการโมเมนตัมเชิงเส้น (Linear Momentum):</b>
    $$\sum F_x = \dot{m} (v_{2x} - v_{1x})\tag{3.6}$$
    เมื่อลำน้ำพุ่งชนแผ่นโค้งเคลื่อนที่ด้วยความเร็ว \(u\) ตามแนวลำน้ำ แรงที่กระทำต่อแผ่นคือ:
    $$R_x = \rho A (v - u)^2 (1 - \cos\theta)\tag{3.7}$$
    สำหรับแผ่นโค้งรูปตัวยู \(180^\circ\) (\(\cos 180^\circ = -1\)): \(R_x = 2 \rho A (v - u)^2\)</p>
  </div>

  <h3 class="grp" id="ch3-traps">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>จุดดักคะแนนที่ 1: ลืมคูณความเร็ว \(u, v, w\) ข้างหน้าพจน์ Convective</b>
    <div>
      ในสมการความเร่ง พจน์ความเร่งพาคือ \(u \dfrac{\partial u}{\partial x}\) (ต้องเอาค่าความเร็ว \(u\) มาคูณกับอนุพันธ์ย่อย \(\dfrac{\partial u}{\partial x}\))<br>
      นักศึกษาหลายคนชอบจำสับสนและเขียนแค่ \(\dfrac{\partial u}{\partial x}\) เฉยๆ โดยลืมคูณ \(u\) ทำให้หน่วยผิดและคำตอบผิดทั้งหมด
    </div>
  </div>

  <div class="bx trap">
    <b>จุดดักคะแนนที่ 2: ความผิดพลาดเรื่องเครื่องหมายลบคูณลบ</b>
    <div>
      ในแกน \(y\): \(v = -15xy\) เมื่อคำนวณ \(v\) ได้ค่าลบ (\(-30\text{ m/s}\)) และ \(\dfrac{\partial v}{\partial y} = -15x = -30\)<br>
      เมื่อนำมาคูณกัน: \(v \dfrac{\partial v}{\partial y} = (-30) \times (-30) = +900\text{ m/s}^2\) (เครื่องหมายต้องเป็นบวก!)
    </div>
  </div>

  <div class="bx trap">
    <b>จุดดักคะแนนที่ 3: ใช้ \(\dot{m}\) เดิมเมื่อแผ่นเคลื่อนที่</b>
    <div>
      เมื่อแผ่นโค้งเคลื่อนที่หนีลำน้ำด้วยความเร็ว \(u = 6\text{ m/s}\) อัตราการไหลมวลจริงที่ปะทะแผ่นคือ \(\dot{m}_{\text{rel}} = \rho A (v - u)\) ไม่ใช่ \(\rho A v\) ดั้งเดิม
    </div>
  </div>

  <hr>

  <!-- 1. FLUID ACCELERATION EX 1 -->
  <h3 id="ch3-accel" class="grp">1. ตัวอย่างข้อ 1: ความเร็วและความเร่งของอนุภาคของไหล (ลายมืออาจารย์)</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> ถ้าเวกเตอร์ความเร็วของของไหลหนึ่งเท่ากับ \(\vec{V}(x,y,z,t) = 10x^2\vec{i} - 15xy\vec{j} + 32t\vec{k}\) หน่วยความเร็วคือ \(\text{m/s}\) จงหาความเร็วและความเร่งของโมเลกุลของไหลนี้ที่ \(X = 2\text{ m},\ Y = 1\text{ m},\ Z = 3\text{ m}\) และ \(t = 0.5\text{ s}\)</p>
  </div>

  <figure>
    <svg viewBox="0 0 640 220" role="img" aria-label="แผนภาพเวกเตอร์ความเร็วและความเร่งของอนุภาคของไหล">
      <!-- Coordinate Axes -->
      <line x1="80" y1="170" x2="260" y2="170" stroke="var(--ink)" stroke-width="2" marker-end="url(#ar)"/>
      <text x="265" y="175" font-size="14" font-weight="700" fill="var(--ink)">X</text>
      <line x1="80" y1="170" x2="80" y2="30" stroke="var(--ink)" stroke-width="2" marker-end="url(#ar)"/>
      <text x="75" y="22" font-size="14" font-weight="700" fill="var(--ink)">Y</text>
      <line x1="80" y1="170" x2="30" y2="210" stroke="var(--ink)" stroke-width="2" marker-end="url(#ar)"/>
      <text x="20" y="215" font-size="14" font-weight="700" fill="var(--ink)">Z</text>

      <!-- Particle Point P -->
      <circle cx="180" cy="110" r="7" fill="var(--red)"/>
      <text x="195" y="105" font-size="14" font-weight="700" fill="var(--red)">P (x=2, y=1, z=3, t=0.5)</text>

      <!-- Velocity Vector V -->
      <line x1="180" y1="110" x2="280" y2="150" stroke="var(--blue)" stroke-width="3.5" marker-end="url(#ar)"/>
      <text x="285" y="145" font-size="14" font-weight="700" fill="var(--blue)">V = 40i - 30j + 16k (|V| = 52.5 m/s)</text>

      <!-- Acceleration Vector a -->
      <line x1="180" y1="110" x2="350" y2="60" stroke="var(--gold)" stroke-width="3.5" marker-end="url(#ar)"/>
      <text x="355" y="55" font-size="14" font-weight="700" fill="var(--gold)">a = 1600i + 300j + 32k (|a| = 1628.2 m/s²)</text>

      <!-- Acceleration Formula Notes -->
      <rect x="360" y="110" width="260" height="95" rx="6" fill="var(--hover)" stroke="var(--rule)" stroke-width="1.5"/>
      <text x="375" y="133" font-size="13" font-weight="700" fill="var(--navy)">ส่วนประกอบความเร่ง:</text>
      <text x="375" y="153" font-size="12" fill="var(--ink)">• ax = u(∂u/∂x) = 40×40 = 1600 m/s²</text>
      <text x="375" y="173" font-size="12" fill="var(--ink)">• ay = u(∂v/∂x) + v(∂v/∂y) = 300 m/s²</text>
      <text x="375" y="193" font-size="12" fill="var(--ink)">• az = ∂w/∂t = 32 m/s² (Local Acc.)</text>
    </svg>
    <figcaption>รูปที่ 3.1 การกระจายเวกเตอร์ความเร็วและความเร่งของอนุภาคของไหล (3D Velocity &amp; Acceleration)</figcaption>
  </figure>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับทีละสเต็ป)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & \vec{V}(x,y,z,t) = 10x^2\vec{i} - 15xy\vec{j} + 32t\vec{k}\ [\text{m/s}] \\ & \text{ตำแหน่ง: } X = 2\ \text{m},\quad Y = 1\ \text{m},\quad Z = 3\ \text{m} \\ & \text{เวลา: } t = 0.5\ \text{s} \end{aligned}$$</div>
    </div>

    <!-- Step 1: Velocity -->
    <div class="row">
      <div class="lab">Step 1: ความเร็ว (u, v, w)</div>
      <div>$$\begin{aligned} u &= 10x^2 = 10(2)^2 = 40\ \text{m/s} \\ v &= -15xy = -15(2)(1) = -30\ \text{m/s} \\ w &= 32t = 32(0.5) = 16\ \text{m/s} \end{aligned}$$
      <p style="margin-top:6px;color:var(--blue);font-weight:600;">Ans คำตอบเซตแรก (เวกเตอร์ความเร็วและขนาด):</p>
      $$\vec{V} = 40\vec{i} - 30\vec{j} + 16\vec{k}\ \text{m/s}$$
      $$|\vec{V}| = \sqrt{40^2 + (-30)^2 + 16^2} = \sqrt{1600 + 900 + 256} = \sqrt{2756} \approx 52.50\ \text{m/s}$$</div>
    </div>

    <!-- Step 2: Derivatives for ax -->
    <div class="row">
      <div class="lab">Step 2: อนุพันธ์ย่อยของ u</div>
      <div>$$\begin{aligned} \frac{\partial u}{\partial x} &= \frac{\partial}{\partial x}[10x^2] = 20x = 20(2) = 40\ \text{s}^{-1} \\ \frac{\partial u}{\partial y} &= \frac{\partial}{\partial y}[10x^2] = 0 \\ \frac{\partial u}{\partial z} &= \frac{\partial}{\partial z}[10x^2] = 0 \\ \frac{\partial u}{\partial t} &= \frac{\partial}{\partial t}[10x^2] = 0 \end{aligned}$$</div>
    </div>

    <div class="row">
      <div class="lab">คำนวณ \(a_x\)</div>
      <div>$$\begin{aligned} a_x &= u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} + \frac{\partial u}{\partial t} \\ &= [40 \times 40] + [-30 \times 0] + [16 \times 0] + 0 \\ &= 1600 + 0 + 0 + 0 = 1600\ \text{m/s}^2 \end{aligned}$$</div>
    </div>

    <!-- Step 3: Derivatives for ay -->
    <div class="row">
      <div class="lab">Step 3: อนุพันธ์ย่อยของ v</div>
      <div>$$\begin{aligned} \frac{\partial v}{\partial x} &= \frac{\partial}{\partial x}[-15xy] = -15y = -15(1) = -15\ \text{s}^{-1} \\ \frac{\partial v}{\partial y} &= \frac{\partial}{\partial y}[-15xy] = -15x = -15(2) = -30\ \text{s}^{-1} \\ \frac{\partial v}{\partial z} &= \frac{\partial}{\partial z}[-15xy] = 0 \\ \frac{\partial v}{\partial t} &= \frac{\partial}{\partial t}[-15xy] = 0 \end{aligned}$$</div>
    </div>

    <div class="row">
      <div class="lab">คำนวณ \(a_y\)</div>
      <div>$$\begin{aligned} a_y &= u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} + \frac{\partial v}{\partial t} \\ &= [(40)(-15)] + [(-30)(-30)] + [(16)(0)] + 0 \\ &= -600 + 900 + 0 + 0 = 300\ \text{m/s}^2 \end{aligned}$$</div>
    </div>

    <!-- Step 4: Derivatives for az -->
    <div class="row">
      <div class="lab">Step 4: อนุพันธ์ย่อยของ w</div>
      <div>$$\begin{aligned} \frac{\partial w}{\partial x} &= \frac{\partial}{\partial x}[32t] = 0 \\ \frac{\partial w}{\partial y} &= \frac{\partial}{\partial y}[32t] = 0 \\ \frac{\partial w}{\partial z} &= \frac{\partial}{\partial z}[32t] = 0 \\ \frac{\partial w}{\partial t} &= \frac{\partial}{\partial t}[32t] = 32\ \text{m/s}^2 \end{aligned}$$</div>
    </div>

    <div class="row">
      <div class="lab">คำนวณ \(a_z\)</div>
      <div>$$\begin{aligned} a_z &= u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} + \frac{\partial w}{\partial t} \\ &= [40 \times 0] + [-30 \times 0] + [16 \times 0] + 32 \\ &= 0 + 0 + 0 + 32 = 32\ \text{m/s}^2 \end{aligned}$$</div>
    </div>

    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(\begin{aligned} & \vec{V} = 40\vec{i} - 30\vec{j} + 16\vec{k}\ \text{m/s}\quad (|\vec{V}| \approx 52.50\ \text{m/s}) \\ & \vec{a} = 1600\vec{i} + 300\vec{j} + 32\vec{k}\ \text{m/s}^2\quad (|\vec{a}| \approx 1,628.20\ \text{m/s}^2) \end{aligned}\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 2. JET ON VANE EX 5 -->
  <h3 id="ch3-jet" class="grp">2. ตัวอย่างข้อ 5 (หน้า 21): ลำน้ำพุ่งชนแผ่นโค้ง 180°</h3>
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
    <figcaption>รูปที่ 3.2 ลำน้ำพุ่งชนแผ่นโค้งรูปตัวยู 180° (180° Jet Deflection)</figcaption>
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

  <!-- 3. SIPHON EX 9 -->
  <h3 id="ch3-siphon" class="grp">3. ตัวอย่างข้อ 9 (หน้า 22): ท่อกาลักน้ำ Siphon</h3>
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
