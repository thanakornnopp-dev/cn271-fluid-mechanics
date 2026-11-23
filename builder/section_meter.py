# -*- coding: utf-8 -*-

def get_section_meter():
    return r'''
<section id="meter">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
    <h1>การวัดอัตราการไหลและการเกิดโพรงไอ (Flow Measurement &amp; Cavitation)</h1>
    <p class="sub">ท่อเวนจูรี่ (Venturi Meter) · แผ่นออริฟิส (Orifice Plate) · ท่อปีโตต์ (Pitot Tube) · การป้องกัน Cavitation ในปั๊มน้ำ</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">เครื่องมือวัด</span>อุปกรณ์วัดอัตราการไหลในท่อและขีดจำกัดปั๊มน้ำ</h2>
  <div class="stmt">
    <p>ส่วนนี้ครอบคลุมการประยุกต์ใช้สมการเบอร์นูลลีเพื่อวัดอัตราการไหลจริงในท่อส่งน้ำด้วย <b>Venturi Meter</b> การหาสัมประสิทธิ์ปรับแก้เครื่อง (\(C_d\)) และการคำนวณหาความสูงสูงสุดในการติดตั้งเครื่องสูบน้ำเหนือผิวน้ำ (\(Z_{1,\max}\)) เพื่อป้องกันการระเหิดกลายเป็นไอและการเกิดฟองโพรงไอ <b>(Cavitation)</b></p>
  </div>

  <div class="jump">
    <a href="#meter-theory">ก. หลักการและสมการเครื่องมือวัด</a>
    <a href="#meter-traps">ข. จุดดักคะแนนข้อสอบ</a>
    <a href="#meter-venturi">ค. ตัวอย่างเรื่องการวัดอัตราการไหล Venturi Meter (หน้า 43)</a>
    <a href="#meter-cavitation">ง. ตัวอย่างข้อ 14 การป้องกัน Cavitation ในปั๊มน้ำ (หน้า 43)</a>
  </div>

  <h3 class="grp" id="meter-theory">ก. หลักการและสมการเครื่องมือวัด First Principles</h3>
  <div class="plan">
    <p><b class="l">สมการท่อเวนจูรี่ (Venturi Meter Equation):</b> จากสมการเบอร์นูลลีและสมการความต่อเนื่องระหว่างท่อหลัก (1) และคอคอด (2):
    $$Q_{\text{ideal}} = \frac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \Delta h} = \frac{A_2}{\sqrt{1 - (D_2/D_1)^4}} \sqrt{2g \left( \frac{P_1 - P_2}{\gamma} \right)}\tag{6.1}$$
    เมื่อนำความเสียดทานจริงมาคิด ต้องคูณสัมประสิทธิ์การปล่อย (\(C_d \approx 0.95 - 0.98\)):
    $$Q_{\text{actual}} = C_d \frac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \frac{\Delta P}{\gamma}}\tag{6.2}$$</p>
    <p><b class="l">ท่อปีโตต์ (Pitot Tube):</b> วัดความเร็วเฉพาะจุดจากผลต่างความดันหยุดนิ่ง (Stagnation Pressure, \(P_0\)) กับความดันสถิต (Static Pressure, \(P\)):
    $$v = \sqrt{\frac{2(P_0 - P)}{\rho}} = \sqrt{2g \Delta h}\tag{6.3}$$</p>
    <p><b class="l">เกณฑ์ป้องกัน Cavitation ของเครื่องสูบน้ำ:</b> เฮดดูดสุทธิที่มีอยู่จริง (NPSHA) ต้องมากกว่าหรือเท่ากับค่าเฮดดูดสุทธิขั้นต่ำที่เครื่องสูบต้องการ (NPSHR):
    $$\text{NPSHA} = \frac{P_{\text{atm}}}{\gamma} - Z_1 - h_L - \frac{P_v}{\gamma} \ge \text{NPSHR}\tag{6.4}$$
    ดังนั้น ระดับความสูงในการติดตั้งปั๊มเหนือผิวน้ำที่ปลอดภัยคือ:
    $$Z_{1,\max} = \frac{P_{\text{atm}} - P_v}{\gamma} - \text{NPSHR} - h_L - \frac{v^2}{2g}\tag{6.5}$$</p>
  </div>

  <h3 class="grp" id="meter-traps">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>ข้อผิดพลาดอันดับ 1 ในเรื่อง Cavitation:</b>
    <div>
      • <b>ความดันไอ (\(P_v\)):</b> ต้องใช้ความดันสัมบูรณ์ (Absolute Pressure) ทั้ง \(P_{\text{atm}}\) และ \(P_v\)<br>
      • <b>การลืมหักค่า Head Loss ท่อดูด:</b> การสูญเสียพลังงานในท่อดูด (\(h_L\)) จะดึงความดันหน้าใบพัดปั๊มให้ลดต่ำลง ทำให้เกิด Cavitation ได้ง่ายขึ้น จึงต้องนำ \(h_L\) และเฮดความเร็วไปหักออกจากความสูงในการติดตั้งเสมอ
    </div>
  </div>

  <hr>

  <!-- 1. VENTURI METER -->
  <h3 id="meter-venturi" class="grp">ค. ตัวอย่างเรื่องการวัดอัตราการไหล (หน้า 43): Venturi Meter</h3>
  <div class="stmt">
    <p><b>โจทย์:</b> ในการตรวจสอบท่อน้ำ ติดตั้ง Venturi Meter ที่มีค่าสัมประสิทธิ์ปรับแก้เครื่อง \(C_d = 0.85\) ข้อมูลจากมาโนมิเตอร์อ่านความดันได้ \(P_1 = 525\text{ Pa}\) และที่คอคอดอ่านได้ \(P_2 = 225\text{ Pa}\) จงเขียนสมการและคำนวณอัตราการไหลของน้ำในท่อ</p>
  </div>

  <figure>
    <svg viewBox="0 0 620 180" role="img" aria-label="แผนภาพ Venturi Meter และหลอดวัดความดัน">
      <!-- Pipe converging and diverging -->
      <path d="M40 50 H160 L240 75 H340 L420 50 H580" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
      <path d="M40 130 H160 L240 105 H340 L420 130 H580" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
      <path d="M40 52 H160 L240 77 H340 L420 52 H580 V128 H420 L340 103 H240 L160 128 H40 Z" fill="var(--water)" opacity="0.4"/>

      <!-- Manometer tubes -->
      <rect x="110" y="10" width="16" height="40" fill="var(--bg)" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="110" y1="25" x2="126" y2="25" stroke="var(--blue)" stroke-width="2"/>
      <text x="135" y="30" font-size="13" font-weight="700" fill="var(--navy)">P₁ = 525 Pa</text>

      <rect x="285" y="30" width="16" height="45" fill="var(--bg)" stroke="var(--ink)" stroke-width="1.5"/>
      <line x1="285" y1="52" x2="301" y2="52" stroke="var(--blue)" stroke-width="2"/>
      <text x="310" y="55" font-size="13" font-weight="700" fill="var(--navy)">P₂ = 225 Pa</text>

      <!-- Delta h -->
      <line x1="126" y1="25" x2="285" y2="25" stroke="var(--red)" stroke-dasharray="3 3"/>
      <line x1="200" y1="25" x2="200" y2="52" stroke="var(--red)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="210" y="42" font-size="13" font-weight="600" fill="var(--red)">Δh</text>
    </svg>
    <figcaption>รูปที่ 6.1 โครงสร้าง Venturi Meter แสดงท่อหลัก คอคอด และผลต่างเฮดความดัน</figcaption>
  </figure>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">สูตรคำนวณ Venturi</div>
      <div class="given">$$Q = C_d \frac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \left( \frac{P_1 - P_2}{\gamma} \right)}$$</div>
    </div>
    <div class="row">
      <div class="lab">ผลต่างความดัน \(\Delta P\)</div>
      <div>$$\Delta P = P_1 - P_2 = 525\ \text{Pa} - 225\ \text{Pa} = 300\ \text{Pa}\ (\text{N/m}^2)$$</div>
    </div>
    <div class="row">
      <div class="lab">ผลต่างเฮดความดัน \(\Delta h\)</div>
      <div>$$\Delta h = \frac{\Delta P}{\gamma} = \frac{300\ \text{N/m}^2}{9,810\ \text{N/m}^3} = 0.03058\ \text{m}$$</div>
    </div>
    <div class="row">
      <div class="lab">พจน์อัตราเร็ว \(\sqrt{2g \Delta h}\)</div>
      <div>$$\sqrt{2g \Delta h} = \sqrt{2 \times 9.81 \times 0.03058} = \sqrt{0.600} = 0.7746\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q = 0.85 \times \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \times 0.7746\ \text{m/s} = 0.6584 \left(\dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}}\right)\ \text{m}^3/\text{s}\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 2. CAVITATION EX 14 -->
  <h3 id="meter-cavitation" class="grp">ง. ตัวอย่างข้อ 14 (หน้า 43): การป้องกัน Cavitation ในปั๊มน้ำ</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 14:</b> ต้องการสูบน้ำจากถังน้ำโดยไม่ให้เกิด Cavitation จะต้องตั้งเครื่องสูบน้ำให้สูงกว่าระดับน้ำ (\(Z_1\)) ได้มากที่สุดกี่เมตร กำหนดให้อัตราสูบ \(Q = 0.015\text{ m}^3\text{/s}\), ขนาดท่อดูด \(D = 0.2\text{ m}\), \(P_{\text{atm}} = 101\text{ kPa}\), \(\text{NPSHR} = 4.6\text{ m}\), ความดันไอของน้ำ \(P_v = 5,950\text{ Pa}\) และคิดเฉพาะ Minor Loss โดยมีสัมประสิทธิ์รวม \(\sum K_L = 20\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ความเร็วในท่อดูด \(v\)</div>
      <div class="given">$$v = \frac{4 Q}{\pi D^2} = \frac{4 \times 0.015}{\pi \times (0.2)^2} = \frac{0.060}{0.12566} = 0.4775\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">เฮดความเร็ว \(\frac{v^2}{2g}\)</div>
      <div>$$\frac{v^2}{2g} = \frac{(0.4775)^2}{2 \times 9.81} = \frac{0.2280}{19.62} = 0.0116\ \text{m}$$</div>
    </div>
    <div class="row">
      <div class="lab">การสูญเสียในท่อดูด \(h_L\)</div>
      <div>$$h_L = \sum K_L \frac{v^2}{2g} = 20 \times 0.0116\ \text{m} = 0.232\ \text{m}$$</div>
    </div>
    <div class="row">
      <div class="lab">เฮดความดันบรรยากาศและเฮดความดันไอ</div>
      <div>$$\begin{aligned} & \frac{P_{\text{atm}}}{\gamma} = \frac{101,000\ \text{N/m}^2}{9,810\ \text{N/m}^3} = 10.2956\ \text{m} \\ & \frac{P_v}{\gamma} = \frac{5,950\ \text{N/m}^2}{9,810\ \text{N/m}^3} = 0.6065\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">สมการเงื่อนไข NPSHA \(\ge\) NPSHR</div>
      <div>$$\begin{aligned} & \text{NPSHA} = \frac{P_{\text{atm}}}{\gamma} - \frac{P_v}{\gamma} - Z_1 - h_L - \frac{v^2}{2g} \ge \text{NPSHR} \\ & 10.2956 - 0.6065 - Z_1 - 0.232 - 0.0116 \ge 4.60 \\ & 9.4455 - Z_1 \ge 4.60 \\ & Z_1 \le 9.4455 - 4.60 = 4.8455\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Z_{1,\max} \approx 4.85\ \text{m}\ (\text{ตั้งปั๊มน้ำได้สูงกว่าผิวน้ำไม่เกิน } 4.85\ \text{m})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#ch5">← บทที่ 5 ท่อส่งน้ำ &amp; วนลูป</a>
    <a href="#exam">คลังข้อสอบ &amp; เก็งข้อสอบ →</a>
  </div>
</section>
'''
