# -*- coding: utf-8 -*-

def get_section_ch1():
    return r'''
<section id="ch1">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
    <h1>บทที่ 1: คุณสมบัติของไหล (Fluid Properties)</h1>
    <p class="sub">ความหนืด (Viscosity) · ความเค้นเฉือน (Shear Stress) · กฎของนิวตัน · การแปลงหน่วย</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 1</span>คุณสมบัติพื้นฐานและกฎความหนืดของนิวตัน</h2>
  <div class="stmt">
    <p>บทที่ 1 ปูพื้นฐานคุณสมบัติทางกายภาพของของเหลวและก๊าซ หัวใจสำคัญที่สุดของการสอบคือ <b>กฎความหนืดของนิวตัน (Newton's Law of Viscosity)</b> ความสัมพันธ์ระหว่างแรงเฉือน ความหนืดสัมบูรณ์ และความลาดความเร็ว รวมถึงการแปลงหน่วยในระบบ SI ให้ถูกต้องแม่นยำ 100%</p>
  </div>

  <div class="jump">
    <a href="#ch1-theory">ก. หลักการและสูตรสำคัญ</a>
    <a href="#ch1-traps">ข. จุดดักคะแนนข้อสอบ</a>
    <a href="#ch1-ex1">ค. ตัวอย่างข้อ 1 แผ่นเลื่อนขนาน (หน้า 1)</a>
  </div>

  <h3 class="grp" id="ch1-theory">ก. หลักการและสูตรสำคัญ First Principles</h3>
  <div class="plan">
    <p><b class="l">ความหนาแน่นและน้ำหนักจำเพาะ:</b> \(\rho = \dfrac{m}{V}\ \text{[kg/m}^3\text{]},\quad \gamma = \rho g\ \text{[N/m}^3\text{]},\quad SG = \dfrac{\rho}{\rho_{\text{water}}} = \dfrac{\gamma}{\gamma_{\text{water}}}\)</p>
    <p><b class="l">กฎความหนืดของนิวตัน:</b> สำหรับของไหลนิวโทเนียน (Newtonian Fluid) ความเค้นเฉือนแปรผันตรงกับอัตราการเปลี่ยนรูปหรือความลาดความเร็ว:
    $$\tau = \mu \frac{dv}{dy} \approx \mu \frac{V}{h}\tag{1.1}$$
    เมื่อ \(h\) คือระยะห่างระหว่างแผ่นเรียบที่มีค่าน้อยมาก ทำให้การกระจายความเร็วเป็นเส้นตรง (Linear Velocity Profile)</p>
    <p><b class="l">ความหนืดคิเนมาติก:</b> อัตราส่วนความหนืดสัมบูรณ์ต่อความหนาแน่น \(\nu = \dfrac{\mu}{\rho}\ \text{[m}^2/\text{s]}\)</p>
  </div>

  <h3 class="grp" id="ch1-traps">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>ข้อผิดพลาดอันดับ 1: ลืมแปลงหน่วยมิลลิเมตรเป็นเมตร</b>
    <div>
      โจทย์มักให้ระยะห่างระหว่างแผ่น \(h\) ในหน่วยมิลลิเมตร (mm) เช่น \(h = 8\text{ mm}\)<br>
      • ต้องแปลงเป็นหน่วยเมตรเสมอ: \(h = 8 \times 10^{-3}\text{ m} = 0.008\text{ m}\)<br>
      • หากลืมแปลง ค่าความเค้นเฉือน \(\tau\) จะผิดไป 1,000 เท่าทันที
    </div>
  </div>

  <div class="bx chk">
    <b>การตรวจสอบหน่วยความหนืดในระบบ SI:</b>
    <div>
      \(1\text{ Pa}\cdot\text{s} = 1\text{ N}\cdot\text{s/m}^2 = 1\text{ kg}/(\text{m}\cdot\text{s})\)<br>
      ในหน่วย cgs: \(1\text{ Poise (P)} = 0.1\text{ Pa}\cdot\text{s}\) และ \(1\text{ Centipoise (cP)} = 10^{-3}\text{ Pa}\cdot\text{s}\)
    </div>
  </div>

  <h3 class="grp" id="ch1-ex1">ค. ตัวอย่างข้อ 1 (หน้า 1): แผ่นเลื่อนขนานและความเค้นเฉือน</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 1:</b> ของไหล A อยู่ระหว่างแผ่นเรียบดังรูป ถ้า Dynamic Viscosity (\(\mu\)) ของของไหล A เท่ากับ \(0.29\text{ kg}\cdot\text{m}^{-1}\text{s}^{-1}\) จงหาค่า Shear Stress (\(\tau\)) ที่ต้องการ เพื่อให้แผ่นด้านบนเคลื่อนที่ด้วยความเร็ว \(V = 3.2\text{ m/s}\) โดยมีระยะห่างระหว่างแผ่น \(h = 8\text{ mm}\)</p>
  </div>

  <figure>
    <svg viewBox="0 0 620 180" role="img" aria-label="แผ่นเลื่อนขนานและเส้นการกระจายความเร็ว">
      <!-- Fixed bottom plate -->
      <rect x="80" y="140" width="460" height="16" fill="var(--hover)" stroke="var(--ink)" stroke-width="2"/>
      <line x1="80" y1="156" x2="540" y2="156" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="4 4"/>
      <text x="310" y="172" font-size="13" font-weight="600" text-anchor="middle" fill="var(--gray)">แผ่นเรียบด้านล่างอยู่นิ่ง (Fixed Plate, v = 0)</text>

      <!-- Moving top plate -->
      <rect x="80" y="40" width="460" height="16" fill="var(--hover)" stroke="var(--navy)" stroke-width="2"/>
      <path d="M500 48 H580" fill="none" stroke="var(--red)" stroke-width="3" marker-end="url(#ar)"/>
      <text x="540" y="38" font-size="14" font-weight="700" fill="var(--red)">V = 3.2 m/s</text>

      <!-- Fluid layer -->
      <rect x="80" y="56" width="460" height="84" fill="var(--water)" opacity="0.5"/>
      <text x="180" y="105" font-size="14" font-weight="600" fill="var(--navy)">ของไหล A (μ = 0.29 Pa·s)</text>

      <!-- Velocity Profile -->
      <line x1="380" y1="56" x2="380" y2="140" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="3 3"/>
      <line x1="380" y1="140" x2="460" y2="56" stroke="var(--blue)" stroke-width="2.5"/>
      <path d="M380 75 H442" stroke="var(--blue)" stroke-width="1.2" marker-end="url(#ar)"/>
      <path d="M380 95 H423" stroke="var(--blue)" stroke-width="1.2" marker-end="url(#ar)"/>
      <path d="M380 115 H404" stroke="var(--blue)" stroke-width="1.2" marker-end="url(#ar)"/>

      <!-- Height h -->
      <line x1="120" y1="56" x2="120" y2="140" stroke="var(--ink)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="135" y="103" font-size="14" font-weight="600" fill="var(--ink)">h = 8 mm</text>
    </svg>
    <figcaption>รูปที่ 1.1 การกระจายความเร็วเชิงเส้นระหว่างแผ่นเลื่อนขนาน (Linear Velocity Gradient)</figcaption>
  </figure>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & \mu = 0.29\ \text{kg}\cdot\text{m}^{-1}\text{s}^{-1} = 0.29\ \text{Pa}\cdot\text{s} \\ & V = 3.2\ \text{m/s},\quad h = 8\ \text{mm} = 0.008\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">สูตรคำนวณ</div>
      <div>$$\tau = \mu \frac{dv}{dy} \approx \mu \frac{V}{h}$$</div>
    </div>
    <div class="row">
      <div class="lab">แทนค่าตัวเลข</div>
      <div>$$\tau = (0.29\ \text{Pa}\cdot\text{s}) \times \left( \frac{3.2\ \text{m/s}}{0.008\ \text{m}} \right) = 0.29 \times 400\ \text{s}^{-1}$$</div>
    </div>
    <div class="row">
      <div class="lab">ผลลัพธ์ที่ได้</div>
      <div>$$\tau = 116\ \text{N/m}^2\ (\text{Pa})$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(\tau = 116\ \text{N/m}^2\ (\text{Pa})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#sum">← สรุปภาพรวม</a>
    <a href="#ch2">บทที่ 2 สถิตยศาสตร์ &amp; ประตูน้ำ →</a>
  </div>
</section>
'''
