# -*- coding: utf-8 -*-

def get_section_ch2():
    return r'''
<section id="ch2">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
    <h1>บทที่ 2: สถิตยศาสตร์ของไหลและบานประตู (Fluid Statics)</h1>
    <p class="sub">มาโนมิเตอร์หลายของไหล · แรงดันบนผนังระนาบ · จุดศูนย์กลางแรงกด (Center of Pressure) · สมดุลบานพับ · แรงดันบนผิวโค้ง</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 2</span>สรุปสูตรและข้อสอบเต็งหนึ่งสถิตยศาสตร์ของไหล (39 ข้อ)</h2>
  <div class="stmt">
    <p>บทที่ 2 เป็นบทที่มีน้ำหนักคะแนนสูงมากในข้อสอบ มักออก 2 ข้อใหญ่เสมอ: <b>(1) ข้อสอบคำนวณมาโนมิเตอร์หลายของไหล (Manometer Walking)</b> และ <b>(2) แรงดันบนประตูระนาบเอียงหรือระนาบโค้งพร้อมเทคโมเมนต์รอบบานพับ (Hinge Equilibrium)</b></p>
  </div>

  <div class="jump">
    <a href="#ch2-mano">1. มาโนมิเตอร์ของเหลว 2 ชนิด (ข้อ 9)</a>
    <a href="#ch2-plane">2. แรงดันบนผนังระนาบเรียบ (ข้อ 22)</a>
    <a href="#ch2-hinge">3. บานประตูปิดน้ำเอียงสมดุลบานพับ (ข้อ 26)</a>
    <a href="#ch2-curved">4. แรงดันบนผิวโค้งวงกลม (ข้อ 29)</a>
  </div>

  <h3 class="grp">หลักการพื้นฐานสถิตยศาสตร์ของไหล (Governing Principles)</h3>
  <div class="plan">
    <p><b class="l">กฎการเดินความดัน (Manometer Walking):</b> เดินลงบวก (\(+\gamma \Delta h\)) เดินขึ้นลบ (\(-\gamma \Delta h\)) ระดับเดียวกันในของไหลชนิดเดียวกันที่เชื่อมต่อถึงกัน ความดันเท่ากัน (\(P_{\text{left}} = P_{\text{right}}\))</p>
    <p><b class="l">แรงดันบนระนาบเรียบ:</b> \(F_R = \gamma h_c A = P_c A\)</p>
    <p><b class="l">ตำแหน่งจุดศูนย์กลางแรงกด (Center of Pressure):</b>
    $$y_{cp} = y_c + \frac{I_c}{y_c A}\tag{2.1}$$
    สำหรับรูปสี่เหลี่ยมผืนผ้ากว้าง \(b\) สูง \(h\): \(I_c = \dfrac{b h^3}{12}\) เสมอ (ห้ามใช้ \(I_x = \dfrac{b h^3}{3}\) เด็ดขาด)</p>
    <p><b class="l">แรงดันบนผิวโค้ง:</b> แยกคิด 2 แกนอิสระ:
    $$F_H = \gamma h_c A_{\text{proj}},\quad F_V = \gamma \times \text{Volume},\quad F_R = \sqrt{F_H^2 + F_V^2},\quad \theta = \arctan\left(\frac{F_V}{F_H}\right)\tag{2.2}$$
    แนวแรงลัพธ์ \(F_R\) จะพุ่งผ่านจุดศูนย์กลางความโค้งของวงกลมเสมอ</p>
  </div>

  <div class="bx trap">
    <b>จุดดักคะแนนอันดับ 1 ของบทที่ 2:</b>
    <div>
      • <b>ความดันติดลบ (Suction):</b> จุดที่อยู่สูงกว่าระดับผิวน้ำอิสระในระบบปิด ความดันเกจต้องติดลบ (\(P < 0\))<br>
      • <b>แกนของ \(y_c\) กับ \(h_c\):</b> ในระนาบเอียงทำมุม \(\theta\) กับแนวนอน \(h_c = y_c \sin\theta\) และระยะ \(y_{cp}\) ต้องวัดตามแนวเอียงของระนาบประตู ไม่ใช่วัดในแนวดิ่ง
    </div>
  </div>

  <hr>

  <!-- 1. MANOMETER EX 9 -->
  <h3 id="ch2-mano" class="grp">1. ตัวอย่างข้อ 9 (หน้า 3): มาโนมิเตอร์ของเหลว 2 ชนิด</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> จงหาความดันเกจที่จุด A, B, C, D, E ไม่ต้องคิดความดันบรรยากาศ กำหนด \(SG_1 = 1.0\), \(SG_2 = 0.8\), จุด B อยู่ที่ผิวน้ำเปิด, จุด A อยู่เหนือผิวน้ำ \(0.2\text{ m}\) ในท่อปิด, จุด C อยู่ต่ำกว่าผิวน้ำ \(0.2\text{ m}\), จุด D อยู่ระดับเดียวกับ C ในท่อรูปตัว U, จุด E อยู่ก้นถังต่ำลงไปอีก \(0.7\text{ m}\) ในของเหลว 2</p>
  </div>

  <figure>
    <svg viewBox="0 0 620 220" role="img" aria-label="ผังมาโนมิเตอร์ของเหลวสองชนิด">
      <!-- Tank with liquid 1 -->
      <rect x="60" y="70" width="160" height="130" fill="var(--water)" opacity="0.6" stroke="var(--ink)" stroke-width="2"/>
      <line x1="60" y1="70" x2="220" y2="70" stroke="var(--navy)" stroke-width="2.5"/>
      <text x="140" y="60" font-size="13" font-weight="700" text-anchor="middle" fill="var(--navy)">จุด B (ผิวน้ำอิสระเปิด)</text>
      <circle cx="140" cy="70" r="5" fill="var(--navy)"/>

      <!-- Tube upward to point A -->
      <rect x="80" y="20" width="30" height="50" fill="var(--hover)" stroke="var(--ink)" stroke-width="1.5"/>
      <circle cx="95" cy="30" r="5" fill="var(--red)"/>
      <text x="95" y="15" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">จุด A (ปิด, เหนือน้ำ 0.2 m)</text>

      <!-- Point C -->
      <circle cx="140" cy="110" r="5" fill="var(--blue)"/>
      <text x="175" y="115" font-size="13" font-weight="600" fill="var(--blue)">จุด C (ลึก 0.2 m)</text>

      <!-- U-tube connecting to right -->
      <path d="M140 160 H280 V110 H360 V200 H460 V110" fill="none" stroke="var(--ink)" stroke-width="18"/>
      <path d="M140 160 H280 V110 H360 V200 H460 V110" fill="none" stroke="var(--water)" stroke-width="14" opacity="0.6"/>
      <!-- Liquid 2 in U-tube bottom -->
      <path d="M360 140 V200 H460 V140" fill="none" stroke="var(--gold)" stroke-width="14" opacity="0.8"/>

      <!-- Point D -->
      <circle cx="360" cy="110" r="5" fill="var(--blue)"/>
      <text x="375" y="105" font-size="13" font-weight="600" fill="var(--blue)">จุด D (ระดับเดียวกับ C)</text>

      <!-- Point E -->
      <circle cx="410" cy="200" r="5" fill="var(--red)"/>
      <text x="410" y="218" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">จุด E (ก้นท่อ ลึก 0.7 m ใน SG=0.8)</text>
    </svg>
    <figcaption>รูปที่ 2.1 แผนภาพการเดินความดันมาโนมิเตอร์ (Manometer Walking Path)</figcaption>
  </figure>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">จุด B (ผิวน้ำอิสระ)</div>
      <div class="given">$$P_B = 0\ \text{Pa}\ (\text{ความดันเกจที่ผิวน้ำเปิดสู่อากาศ})$$</div>
    </div>
    <div class="row">
      <div class="lab">จุด A (เดินขึ้น 0.2 m)</div>
      <div>$$P_A = P_B - \gamma_1 \Delta h_{BA} = 0 - (9,810\ \text{N/m}^3 \times 0.2\ \text{m}) = -1,962\ \text{Pa}$$</div>
    </div>
    <div class="row">
      <div class="lab">จุด C (เดินลง 0.2 m)</div>
      <div>$$P_C = P_B + \gamma_1 \Delta h_{BC} = 0 + (9,810\ \text{N/m}^3 \times 0.2\ \text{m}) = +1,962\ \text{Pa}$$</div>
    </div>
    <div class="row">
      <div class="lab">จุด D (ระดับเดียวกับ C)</div>
      <div>$$P_D = P_C = +1,962\ \text{Pa}\ (\text{ของไหลชนิดเดียวกัน เชื่อมต่อถึงกันที่ระดับเดียวกัน})$$</div>
    </div>
    <div class="row">
      <div class="lab">จุด E (เดินลง 0.7 m ในของเหลว 2)</div>
      <div>$$\begin{aligned} P_E &= P_D + \gamma_2 \Delta h_{DE} = 1,962 + (0.8 \times 9,810\ \text{N/m}^3 \times 0.7\ \text{m}) \\ &= 1,962 + 5,493.6 = +7,455.6\ \text{Pa} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(P_A = -1,962\ \text{Pa},\quad P_B = 0\ \text{Pa},\quad P_C = P_D = 1,962\ \text{Pa},\quad P_E = 7,455.6\ \text{Pa}\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 2. PLANE GATE EX 22 -->
  <h3 id="ch2-plane" class="grp">2. ตัวอย่างข้อ 22 (หน้า 8): ผนังระนาบเรียบและจุดศูนย์กลางแรงกด</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> จงหาแรงที่กระทำกับผนังแนวดิ่งที่มีความกว้าง (ลึกเข้าไปในกระดาษ) \(b = 5\text{ m}\) สูง \(h = 6\text{ m}\) โดยมีระดับน้ำอยู่ที่ขอบบนของผนังพอดี และหาตำแหน่งที่แรงกระทำ (\(y_{cp}\)) วัดจากผิวน้ำ</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & b = 5\ \text{m},\quad h = 6\ \text{m},\quad A = b \times h = 5 \times 6 = 30\ \text{m}^2 \\ & h_c = y_c = \frac{h}{2} = \frac{6}{2} = 3.0\ \text{m},\quad \gamma = 9,810\ \text{N/m}^3 \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงลัพธ์ \(F_R\)</div>
      <div>$$F_R = \gamma h_c A = (9,810\ \text{N/m}^3) \times (3.0\ \text{m}) \times (30\ \text{m}^2) = 882,900\ \text{N} = 882.9\ \text{kN}$$</div>
    </div>
    <div class="row">
      <div class="lab">โมเมนต์ความเฉื่อย \(I_c\)</div>
      <div>$$I_c = \frac{b h^3}{12} = \frac{5 \times 6^3}{12} = \frac{5 \times 216}{12} = 90.0\ \text{m}^4$$</div>
    </div>
    <div class="row">
      <div class="lab">ตำแหน่งจุดศูนย์กลางแรงกด \(y_{cp}\)</div>
      <div>$$y_{cp} = y_c + \frac{I_c}{y_c A} = 3.0 + \frac{90.0}{3.0 \times 30} = 3.0 + 1.0 = 4.0\ \text{m}\ (\text{วัดจากผิวน้ำ})$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(F_R = 882.9\ \text{kN},\quad y_{cp} = 4.0\ \text{m}\ (\text{หรืออยู่สูงจากก้นผนัง } 2.0\ \text{m})\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 3. HINGED GATE EX 26 -->
  <h3 id="ch2-hinge" class="grp">3. ตัวอย่างข้อ 26 (หน้า 9): บานประตูปิดน้ำเอียงสมดุลบานพับ</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> บานประตูกั้นน้ำเอียงทำมุมด้วยอัตราส่วนดิ่ง:ราบ:เฉียง เท่ากับ \(4:3:5\) บานประตูยาวตามแนวเอียง \(L = 4\text{ m}\) กว้าง \(b = 2\text{ m}\) ยึดด้วยบานพับ (Hinge) ที่ขอบบน ระดับน้ำอยู่ที่ขอบบนของบานประตูพอดี จงหาน้ำหนัก \(W\) ที่ต้องถ่วงไว้ที่ปลายล่างของบานประตูเพื่อให้บานประตูปิดสนิทพอดี</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลเรขาคณิต</div>
      <div class="given">$$\begin{aligned} & L = 4\ \text{m},\quad b = 2\ \text{m},\quad A = 4 \times 2 = 8\ \text{m}^2 \\ & \sin\theta = \frac{4}{5} = 0.8,\quad y_c = \frac{L}{2} = 2.0\ \text{m},\quad h_c = y_c \sin\theta = 2.0 \times 0.8 = 1.6\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงดันน้ำลัพธ์ \(F_R\)</div>
      <div>$$F_R = \gamma h_c A = (9,810\ \text{N/m}^3) \times (1.6\ \text{m}) \times (8\ \text{m}^2) = 125,568\ \text{N} = 125.57\ \text{kN}$$</div>
    </div>
    <div class="row">
      <div class="lab">ระยะแรงกระทำจากบานพับ</div>
      <div>$$y_{cp} = y_c + \frac{I_c}{y_c A} = 2.0 + \frac{\frac{2 \times 4^3}{12}}{2.0 \times 8} = 2.0 + \frac{10.667}{16} = 2.0 + 0.667 = 2.667\ \text{m} = \frac{2}{3} L$$</div>
    </div>
    <div class="row">
      <div class="lab">สมดุลโมเมนต์รอบบานพับ \(\sum M_{\text{hinge}} = 0\)</div>
      <div>$$\begin{aligned} & F_R \times y_{cp} - W_x \times L = 0 \\ & 125.568\ \text{kN} \times 2.667\ \text{m} - (W \cos\theta) \times 4.0\ \text{m} = 0 \\ & 334.85\ \text{kN}\cdot\text{m} - W \times (0.6) \times 4.0 = 0 \\ & W = \frac{334.85}{2.4} = 180.5\ \text{kN} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(W = 180.5\ \text{kN}\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 4. CURVED GATE EX 29 -->
  <h3 id="ch2-curved" class="grp">4. ตัวอย่างข้อ 29 (หน้า 11): แรงดันบนผิวโค้งวงกลม</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> บานประตูกั้นน้ำผิวโค้งรูปหนึ่งในสี่ของวงกลม (Quarter Circle) มีรัศมี \(R = 6\text{ m}\) กว้างเข้าไปในกระดาษ \(b = 2\text{ m}\) โดยน้ำอยู่ด้านบนของผิวโค้งระดับน้ำสูงถึงขอบบนของประตู จงหาขนาดและทิศทางของแรงดันสุทธิที่กระทำต่อบานประตูโค้ง</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">แรงในแนวนอน \(F_H\)</div>
      <div>$$\begin{aligned} & A_{\text{proj}} = R \times b = 6 \times 2 = 12\ \text{m}^2,\quad h_c = \frac{R}{2} = 3.0\ \text{m} \\ & F_H = \gamma h_c A_{\text{proj}} = (9,810\ \text{N/m}^3) \times (3.0\ \text{m}) \times (12\ \text{m}^2) = 353,160\ \text{N} = 353.16\ \text{kN} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงในแนวดิ่ง \(F_V\)</div>
      <div>$$\begin{aligned} & \text{Volume} = \left(\frac{\pi R^2}{4}\right) \times b = \left(\frac{\pi \times 6^2}{4}\right) \times 2 = 18\pi = 56.549\ \text{m}^3 \\ & F_V = \gamma \times \text{Volume} = (9,810\ \text{N/m}^3) \times (56.549\ \text{m}^3) = 554,743\ \text{N} = 554.74\ \text{kN} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">แรงลัพธ์สุทธิ \(F_R\)</div>
      <div>$$F_R = \sqrt{F_H^2 + F_V^2} = \sqrt{(353.16)^2 + (554.74)^2} = \sqrt{124,722 + 307,737} = 657.60\ \text{kN}$$</div>
    </div>
    <div class="row">
      <div class="lab">มุมทิศทางของแรงลัพธ์ \(\theta\)</div>
      <div>$$\theta = \arctan\left(\frac{F_V}{F_H}\right) = \arctan\left(\frac{554.74}{353.16}\right) = \arctan(1.5708) = 57.52^\circ\ (\text{ทำมุมกับแนวนอน})$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(F_H = 353.16\ \text{kN},\quad F_V = 554.74\ \text{kN},\quad F_R = 657.6\ \text{kN},\quad \theta = 57.52^\circ\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#ch1">← บทที่ 1 คุณสมบัติของไหล</a>
    <a href="#ch3">บทที่ 3 จลนศาสตร์ &amp; โมเมนตัม →</a>
  </div>
</section>
'''
