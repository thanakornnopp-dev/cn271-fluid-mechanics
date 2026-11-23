# -*- coding: utf-8 -*-

def get_section_sum():
    return r'''
<section id="sum" class="on">
  <header class="top">
    <p class="kick">แนวทางการเตรียมสอบกลศาสตร์ของไหลสำหรับวิศวกรโยธา</p>
    <h1>CN 271 กลศาสตร์ของไหล</h1>
    <p class="sub">สรุปเนื้อหา · สมการควบคุม · เฉลยวิธีทำ 4 สเต็ป · จุดดักคะแนน ครบทุกบท</p>
    <p class="by">ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์<br>อ้างอิงชุดตัวอย่างโจทย์ 2569–2570 · จัดทำโดย ธนภรณ์ นพรัตน์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">ภาพรวม</span>สรุปมโนทัศน์สำคัญและการสอบอัตนัย</h2>
  <div class="stmt">
    <p>คู่มือนี้รวบรวมและสังเคราะห์เนื้อหากลศาสตร์ของไหล (CN 271) ครบทั้ง 5 บทหลัก พร้อมหัวข้อเครื่องมือวัดอัตราการไหลและ Cavitation จากชุดโจทย์จริง 74 ข้อของภาควิชา (ปี 2569 และ 2570) ออกแบบตามระเบียบ <b>Strict No-Shortcut Policy (ห้ามลัดขั้นตอน)</b> เพื่อให้นักศึกษาได้ฝึกเขียนขั้นตอนการคำนวณที่ถูกต้อง พร้อมทั้งวิเคราะห์จุดหลอกและเก็งข้อสอบเต็ง 1 ที่ต้องซ้อมมือก่อนเข้าสอบจริง</p>
  </div>

  <div class="jump">
    <a href="#sum-a">ตารางสรุปสมการ 5 บท</a>
    <a href="#sum-b">การ์ดสรุปสูตรสำคัญ</a>
    <a href="#sum-c">5 จุดดักคะแนนมรณะ</a>
    <a href="#ch1">บท 1 คุณสมบัติของไหล</a>
    <a href="#ch2">บท 2 สถิตยศาสตร์ &amp; ประตูน้ำ</a>
    <a href="#ch3">บท 3 จลนศาสตร์ &amp; โมเมนตัม</a>
    <a href="#ch4">บท 4 วิเคราะห์มิติ &amp; สเกล</a>
    <a href="#ch5">บท 5 ท่อส่งน้ำ &amp; วนลูป</a>
    <a href="#meter">เครื่องมือวัด &amp; Cavitation</a>
    <a href="#exam">คลังข้อสอบ &amp; เก็งข้อสอบ</a>
    <a href="#calc">คิดเลข</a>
    <a href="#ref">ตารางอ้างอิง</a>
  </div>

  <h3 class="grp" id="sum-a">ก. สรุปสมการควบคุมหลักครบทุกบท (Governing Formulas Matrix)</h3>
  <div class="tw">
    <table>
      <caption>ตารางสรุปสมการและแก่นการคำนวณ ครบทุกบท (เลื่อนแนวนอนเพื่อดูคอลัมน์เต็ม)</caption>
      <thead>
        <tr>
          <th class="td-num">บทที่</th>
          <th class="td-name">ชื่อบท / มโนทัศน์</th>
          <th class="td-eq">สมการสำคัญ</th>
          <th class="td-vars">ตัวแปรหลักที่ต้องหา</th>
          <th class="td-tools">ข้อสอบเต็ง 1 ในชีท</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="td-num"><b>1</b></td>
          <td class="td-name">คุณสมบัติของไหล<small>Fluid Properties</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\tau = \mu \dfrac{dv}{dy} \approx \mu \dfrac{V}{h}\)</div>
              <div class="eq-subnote">\(\tau\ [\text{N/m}^2],\quad \mu\ [\text{Pa}\cdot\text{s}],\quad h\ [\text{m}]\)</div>
            </div>
          </td>
          <td class="td-vars">ความเค้นเฉือน \(\tau\), ความหนืดพลวัต \(\mu\)</td>
          <td class="td-tools">ข้อ 1 (น.1): แผ่นขนาน \(\tau = 116\text{ N/m}^2\)</td>
        </tr>
        <tr>
          <td class="td-num"><b>2</b></td>
          <td class="td-name">สถิตยศาสตร์ &amp; ประตูน้ำ<small>Fluid Statics &amp; Gates</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(P_2 = P_1 \pm \gamma \Delta h,\quad F_R = \gamma h_{cg} A\)</div>
              <div class="eq-pill">\(y_{cp} = y_{cg} + \dfrac{I_{xx,c}}{y_{cg} A},\quad \sum M_{\text{hinge}} = 0\)</div>
              <div class="eq-subnote">ผิวโค้ง: \(F_H = \gamma h_{cg,\text{proj}} A_{\text{proj}},\quad F_V = \gamma \cdot \text{Vol}\)</div>
            </div>
          </td>
          <td class="td-vars">ความดัน \(P\), แรงลัพธ์ \(F_R\), จุดกด \(y_{cp}\), โมเมนต์รอบบานพับ</td>
          <td class="td-tools">ข้อ 9 (มาโนมิเตอร์), ข้อ 26 (บานพับเอียง \(W=180.5\text{ kN}\)), ข้อ 29 (ผิวโค้ง)</td>
        </tr>
        <tr>
          <td class="td-num"><b>3</b></td>
          <td class="td-name">จลนศาสตร์ &amp; โมเมนตัม<small>Kinematics &amp; Momentum</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(F_x = \dot{m}(v_{1x} - v_{2x}) = 2\rho A v^2\) (นิ่ง)</div>
              <div class="eq-pill">\(F_x = 2\rho A (v - u)^2\) (เคลื่อนที่ตามน้ำ \(u\))</div>
              <div class="eq-subnote">Siphon: \(\dfrac{P_1}{\gamma} + z_1 + \dfrac{v_1^2}{2g} = \dfrac{P_2}{\gamma} + z_2 + \dfrac{v_2^2}{2g}\)</div>
            </div>
          </td>
          <td class="td-vars">แรงกระทำต่อใบพัด \(F_x\), ความดันสุญญากาศที่ยอดท่อ \(P_2\)</td>
          <td class="td-tools">ข้อ 5 (สายน้ำชนแผ่นโค้ง 180°), ข้อ 9 (กาลักน้ำ Siphon)</td>
        </tr>
        <tr>
          <td class="td-num"><b>4</b></td>
          <td class="td-name">การวิเคราะห์มิติ &amp; สเกล<small>Dimensional Analysis</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(\Pi = k - r\quad (8\text{ สเต็ปเต็มรูป})\)</div>
              <div class="eq-pill">Froude: \(\lambda_v = \sqrt{\lambda_L},\quad \lambda_Q = \lambda_L^{2.5}\)</div>
              <div class="eq-subnote">Reynolds: \(\lambda_v = 1/\lambda_L\) (ของไหลชนิดเดียวกัน)</div>
            </div>
          </td>
          <td class="td-vars">กลุ่มไร้มิติ \(\Pi_1, \Pi_2\), ความเร็วต้นแบบ \(v_p\)</td>
          <td class="td-tools">ข้อ 2 (แรงผลักใบพัด 8 ขั้น), ข้อ 6 (สเกลแม่น้ำ \(v_p = 161\text{ m/s}\))</td>
        </tr>
        <tr>
          <td class="td-num"><b>5</b></td>
          <td class="td-name">การไหลในท่อ &amp; การสูญเสีย<small>Flow in Pipes &amp; Losses</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(h_f = f \dfrac{L}{D}\dfrac{v^2}{2g},\quad h_m = \sum K_L \dfrac{v^2}{2g}\)</div>
              <div class="eq-pill">Type II: \(v = \sqrt{\dfrac{2g \Delta z}{\sum K_L + f(L/D)}}\)</div>
              <div class="eq-subnote">Type III: \(D^5 = \dfrac{f L 16 Q^2}{2g \pi^2 h_L} \implies \text{เดา } f \rightarrow D\)</div>
            </div>
          </td>
          <td class="td-vars">ความเร็ว \(v\), อัตราไหล \(Q\), ขนาดท่อ \(D\), แฟกเตอร์ \(f\)</td>
          <td class="td-tools">ข้อ 7 (ปล่อยน้ำจากถัง "ข้อสอบแน่!"), ข้อ 8 (ขนาดท่อ D)</td>
        </tr>
        <tr>
          <td class="td-num"><b>-</b></td>
          <td class="td-name">เครื่องมือวัด &amp; Cavitation<small>Flow Meters &amp; NPSH</small></td>
          <td class="td-eq">
            <div class="eq-row">
              <div class="eq-pill">\(Q = C_d \dfrac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g \dfrac{\Delta P}{\gamma}}\)</div>
              <div class="eq-subnote">\(\text{NPSHA} = \dfrac{P_{\text{atm}} - P_v}{\gamma} - Z_1 - h_L \ge \text{NPSHR}\)</div>
            </div>
          </td>
          <td class="td-vars">อัตราการไหล \(Q\), ความสูงปั๊มปลอดภัยสูงสุด \(Z_{1,\max}\)</td>
          <td class="td-tools">ข้อ 1 (Venturi Meter), ข้อ 14 (ป้องกัน Cavitation ปั๊ม)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="sum-b">ข. การ์ดสรุปสูตรและแนวทางพิจารณาโจทย์ (Formula Study Cards)</h3>
  <div class="formula-grid">
    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">1. กฎการเดินท่อมาโนมิเตอร์</span>
        <span class="badge-sm">บทที่ 2</span>
      </div>
      <div>$$P_{\text{end}} = P_{\text{start}} + \sum (\gamma \Delta h)_{\text{down}} - \sum (\gamma \Delta h)_{\text{up}}$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">เดินลงบวก เดินขึ้นลบ ท่อเอียงคูณ \(\sin\theta\) และจำไว้ว่า \(\gamma = S.G. \times 9,810\text{ N/m}^3\)</p>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">2. แรงดันบานประตูและจุดศูนย์กลางแรงกด</span>
        <span class="badge-sm">บทที่ 2</span>
      </div>
      <div>$$F_R = \gamma h_{cg} A,\quad y_{cp} = y_{cg} + \frac{I_{xx,c}}{y_{cg} A}$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">สี่เหลี่ยม \(I_{xx} = \frac{bh^3}{12}\) เสมอ และเทคโมเมนต์บานพับ \(\sum M_C = 0\) แขนแรงต้องตั้งฉาก</p>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">3. ลำน้ำพุ่งชนแผ่นโค้ง 180°</span>
        <span class="badge-sm">บทที่ 3</span>
      </div>
      <div>$$F_x = 2 \rho A v^2\ \text{(นิ่ง)},\quad F_x = 2 \rho A (v - u)^2\ \text{(วิ่งตามน้ำ)}$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">ถ้าแผ่นเคลื่อนที่ตามน้ำ ความเร็วสัมพัทธ์ลดเหลือ \(v - u\) และมวลน้ำกระทบลดลงด้วย</p>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">4. ทฤษฎีบท Buckingham Pi 8 สเต็ป</span>
        <span class="badge-sm">บทที่ 4</span>
      </div>
      <div>$$\Pi = k - r,\quad \Pi_1 = q \cdot q_a^A q_b^B q_c^C \implies [M^0 L^0 T^0]$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">เลือกตัวแปรซ้ำ 3 ตัว ห้ามเลือกตัวแปรเป้าหมาย และต้องครอบคลุมมิติ \(M, L, T\)</p>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">5. วงวนเดาค่า f ในโจทย์ Type II</span>
        <span class="badge-sm">บทที่ 5</span>
      </div>
      <div>$$v = \sqrt{\frac{2g \Delta z}{\sum K_L + f(L/D)}} \implies Re \implies \text{Moody } f_{\text{new}}$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">เดารอบ 1 (\(f=0.020\)) \(\rightarrow\) ได้ \(f_{\text{new}}\) \(\rightarrow\) นำไปเดารอบ 2 ค่าจะลู่เข้าคงที่ 100%</p>
    </div>

    <div class="formula-card">
      <div class="formula-card-head">
        <span class="formula-card-title">6. การออกแบบขนาดท่อ Type III</span>
        <span class="badge-sm">บทที่ 5</span>
      </div>
      <div>$$D^5 = \frac{f \cdot L \cdot 16 Q^2}{2g \pi^2 h_L} \implies D = (C \cdot f)^{0.2}$$</div>
      <p style="font-size:13.5px;color:var(--gray);margin:0;">ดึงตัวแปร \(D^5\) ค้างไว้ แล้วทำ Trial &amp; Error 2–3 รอบ จนขนาดท่อ \(D\) ลู่เข้า</p>
    </div>
  </div>

  <h3 class="grp" id="sum-c">ค. 5 จุดดักคะแนนมรณะที่คนมักตกม้าตาย (Deadly Exam Traps)</h3>
  <div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
    <b>Trap 1: การลืม Velocity Head ที่ปลายท่อในโจทย์ Type II</b>
    <div>เมื่อท่อปล่อยน้ำออกสู่บรรยากาศ ปลายท่อมี \(\dfrac{v^2}{2g}\) เสมอ เมื่อรวมกับ Minor Loss อื่น ๆ ตัวคูณหน้า \(\dfrac{v^2}{2g}\) จะมี \(1.0_{\text{exit}}\) บวกอยู่ เช่น ข้อ 7 ได้ตัวคูณ \(2.6\) ถ้าลืมเลข \(1.0\) ความเร็วจะเพี้ยนทั้งข้อ</div>
  </div>

  <div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
    <b>Trap 2: การแปลงหน่วยมิลลิเมตรและความขรุขระสัมพัทธ์ \(\varepsilon/D\)</b>
    <div>\(\varepsilon = 0.12\text{ mm} = 0.00012\text{ m}\) และ \(D = 15\text{ cm} = 0.15\text{ m}\) เมื่อจับหารกันต้องใช้หน่วยเดียวกัน \(\dfrac{0.12}{150} = 0.0008\) ถ้าลืมแปลงจะเปิดชาร์ต Moody ผิดเส้น</div>
  </div>

  <div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
    <b>Trap 3: ความเร็วสัมพัทธ์ในสมการโมเมนตัม</b>
    <div>เมื่อแผ่นเคลื่อนที่ตามน้ำด้วยความเร็ว \(u\) สายน้ำที่กระทบจริงจะมีความเร็วสัมพัทธ์ลดลงเหลือ \(v_r = v - u\) และมวลน้ำที่ปะทะต่อวินาทีลดลงเป็น \(\dot{m}_r = \rho A (v - u)\) ห้ามใช้ \(\rho A v\) เด็ดขาด</div>
  </div>

  <div class="bx chk" style="border-left-color:var(--red);margin-bottom:14px;">
    <b>Trap 4: ระยะ \(y_{cp}\) และ \(h_{cp}\) ของบานประตู</b>
    <div>\(y_{cp}\) วัดตามแนวเอียงของบานประตู ส่วน \(h_{cp} = y_{cp} \sin\theta\) วัดในแนวดิ่งจากระดับผิวน้ำอิสระ เมื่อนำไปเทคโมเมนต์รอบบานพับ ต้องใช้แขนของแรงที่ตั้งฉากกับแนวแรงจริง ๆ เสมอ</div>
  </div>

  <div class="bx chk" style="border-left-color:var(--red);">
    <b>Trap 5: การเลือก Repeating Variables ใน Buckingham \(\Pi\)</b>
    <div>ตัวแปรซ้ำ 3 ตัวที่เลือกต้องครอบคลุม: (1) เรขาคณิต เช่น \(D\), (2) ของไหล เช่น \(\rho\), (3) จลนศาสตร์ เช่น \(\omega\) หรือ \(V\) และห้ามเลือกตัวแปรเป้าหมายที่โจทย์ถามหาเป็นตัวแปรซ้ำเด็ดขาด</div>
  </div>
</section>
'''
