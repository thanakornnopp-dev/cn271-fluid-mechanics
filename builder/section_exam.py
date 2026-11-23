# -*- coding: utf-8 -*-

def get_section_exam():
    return r'''
<section id="exam">
  <header class="top">
    <p class="kick">คลังข้อสอบและแนวทางเก็งข้อสอบอัตนัยตามระเบียบอาจารย์</p>
    <h1>คลังข้อสอบและศูนย์เก็งข้อสอบ (Mock Exam &amp; Forecast Center)</h1>
    <p class="sub">เจาะลึก 4 โซนข้อสอบเต็งหนึ่ง · 5 จุดดักคะแนนตาย · ข้อสอบอัตนัยเสมือนจริง 6 ข้อใหญ่พร้อมเฉลยละเอียด</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <!-- Exam Mode Switcher -->
  <div class="quiz-controls">
    <div class="quiz-tabs">
      <button type="button" id="btn-tab-forecast" class="quiz-tab-btn active" onclick="switchExamTab('forecast')">
        🎯 1. แผนเก็งข้อสอบ &amp; 4 โซนคะแนนทอง
      </button>
      <button type="button" id="btn-tab-step" class="quiz-tab-btn" onclick="switchExamTab('step')">
        📝 2. ข้อสอบอัตนัยเสมือนจริง 6 ข้อใหญ่ (Step-by-Step)
      </button>
    </div>
  </div>

  <!-- TAB 1: HIGH-YIELD EXAM FORECAST -->
  <div id="exam-tab-forecast">
    <h2 class="prob"><span class="tag">เก็งข้อสอบ</span>วิเคราะห์ 4 โซนคะแนนทอง &amp; 5 จุดดักคะแนนตาย</h2>
    <div class="stmt">
      <p>สรุปจากการวิเคราะห์เอกสารตัวอย่างโจทย์จริงปี 2569–2570 ของอาจารย์ผู้สอน ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์ โดยคัดกรองหัวข้อที่ออกสอบบ่อยที่สุดและมีน้ำหนักคะแนนสูงสุดในข้อสอบอัตนัย</p>
    </div>

    <h3 class="grp">🎯 4 โซนข้อสอบอัตนัยเต็งหนึ่งที่ต้องซ้อมมือให้คล่อง 100%</h3>
    <div class="formula-grid">
      <div class="f-card">
        <h4>1. สถิตยศาสตร์ &amp; ประตูน้ำ (95%)</h4>
        <p>• <b>มาโนมิเตอร์หลายของไหล:</b> กฎการเดินท่อ \(P_{\text{end}} = P_{\text{start}} \pm \sum \gamma \Delta h\)<br>
        • <b>บานประตูปิดน้ำระนาบเอียง:</b> หาแรงลัพธ์ \(F_R = \gamma h_c A\) ตำแหน่ง \(y_{cp} = y_c + I_c/(y_c A)\) และเทคโมเมนต์รอบบานพับ \(\sum M = 0\)<br>
        • <b>แรงดันบนผิวโค้ง:</b> แยก \(F_H\) และ \(F_V = \gamma \times \text{Vol}\)</p>
      </div>

      <div class="f-card">
        <h4>2. จลนศาสตร์ &amp; โมเมนตัม (95%)</h4>
        <p>• <b>ความเร่งของไหล (Acceleration Field):</b><br>
        - \(a_i = u\frac{\partial v_i}{\partial x} + v\frac{\partial v_i}{\partial y} + w\frac{\partial v_i}{\partial z} + \frac{\partial v_i}{\partial t}\) (Convective + Local)<br>
        • <b>ลำน้ำพุ่งชนแผ่นโค้ง 180°:</b><br>
        - แผ่นอยู่นิ่ง: \(F_x = 2\rho A v^2\)<br>
        - แผ่นเคลื่อนที่ตามน้ำ \(u\): ใช้ความเร็วสัมพัทธ์ \(v_r = v - u\) ได้ \(F_x = 2\rho A (v - u)^2\)<br>
        • <b>ท่อกาลักน้ำ:</b> ความดันยอดท่อติดลบ</p>
      </div>

      <div class="f-card">
        <h4>3. วิเคราะห์มิติ &amp; สเกล (95%)</h4>
        <p>• <b>Buckingham \(\Pi\) Theorem:</b> บังคับแสดงครบ 8 ลำดับขั้นตามเกณฑ์ตรวจ ห้ามข้ามขั้นตอนเลขชี้กำลัง<br>
        • <b>Froude Similitude (ผิวน้ำอิสระ):</b> \(\lambda_v = \sqrt{\lambda_L},\quad \lambda_Q = \lambda_L^{2.5}\)<br>
        • <b>Reynolds Similitude (ท่อปิด):</b> \(\lambda_v = 1/\lambda_L\) เมื่อของไหลชนิดเดียวกัน</p>
      </div>

      <div class="f-card">
        <h4>4. ท่อส่งน้ำ &amp; วนลูป (98%)</h4>
        <p>• <b>Type II (หาอัตราไหล / ความเร็ว):</b> สมมุติ \(f\) คำนวณ \(v\) ตรวจสอบ \(Re\) ลู่เข้าใน 2–3 รอบ (ข้อ 7 ถังน้ำ)<br>
        • <b>Type III (ออกแบบขนาดท่อ D):</b> สมมุติ \(f\) คำนวณ \(D\) ลู่เข้าใน 3 รอบ (ข้อ 8)<br>
        • <b>ท่ออนุกรม &amp; ขนาน:</b> ข้อสอบ A (ท่อเอียง 5°) และข้อสอบ B (ท่อขนาน 4 เส้น)</p>
      </div>
    </div>

    <h3 class="grp" style="margin-top:30px;">⚠️ 5 จุดดักคะแนนตายในห้องสอบ (Deadly Traps)</h3>
    <div class="bx trap">
      <b>จุดดักที่ 1: ลืมแปลงหน่วยมิลลิเมตร เซนติเมตร เป็นเมตร</b>
      <div>ระยะห่างแผ่น \(h = 8\text{ mm}\), ขนาดท่อ \(D = 15\text{ cm}\), ค่าความขรุขระ \(\varepsilon = 0.15\text{ mm}\) ต้องแปลงเป็นเมตร (\(\text{m}\)) ทันทีก่อนแทนในสูตร</div>
    </div>

    <div class="bx trap">
      <b>จุดดักที่ 2: ใช้สูตรโมเมนต์ความเฉื่อยผิดรูปทรง</b>
      <div>สำหรับประตูสี่เหลี่ยมผืนผ้ารอบจุดเซนทรอยด์ ต้องใช้ \(I_c = \dfrac{b h^3}{12}\) เสมอ (ห้ามใช้ \(\dfrac{b h^3}{3}\) เด็ดขาด) และตัวยกกำลัง 3 คือมิติที่ขนานกับแนวเอียงของประตู</div>
    </div>

    <div class="bx trap">
      <b>จุดดักที่ 3: ลืมปรับอัตราการไหลเชิงมวลเมื่อแผ่นเบนลำน้ำเคลื่อนที่</b>
      <div>เมื่อแผ่นเคลื่อนที่หนีน้ำด้วยความเร็ว \(u\) อัตราการไหลมวลจริงที่ปะทะแผ่นคือ \(\dot{m}_{\text{rel}} = \rho A (v - u)\) ไม่ใช่ \(\rho A v\) ดั้งเดิม</div>
    </div>

    <div class="bx trap">
      <b>จุดดักที่ 4: ลัดขั้นตอนใน Buckingham \(\Pi\) Theorem</b>
      <div>ห้ามใส่กลุ่มสำเร็จรูปลงไปโดยไม่แสดงสมการเลขชี้กำลัง \(M, L, T\) อาจารย์ตรวจให้คะแนนแยกทีละมิติ ละเลยแกนใดแกนหนึ่งจะโดนตัดคะแนนทันที</div>
    </div>

    <div class="bx trap">
      <b>จุดดักที่ 5: ลืมรวม Minor Losses ในการคำนวณท่อส่งน้ำ</b>
      <div>ทางเข้าท่อ (\(K_{\text{ent}} = 0.5\)), ข้องอ 90° (\(K_{\text{elbow}} = 0.9\)), วาล์ว และทางออก (\(K_{\text{exit}} = 1.0\)) ต้องรวมในวงเล็บของ \(\dfrac{v^2}{2g}\) ให้ครบถ้วน</div>
    </div>
  </div>

  <!-- TAB 2: STEP-BY-STEP EXAM PRACTICE -->
  <div id="exam-tab-step" style="display:none;">
    <h2 class="prob"><span class="tag">อัตนัย</span>ชุดข้อสอบอัตนัยเสมือนจริง 6 ข้อใหญ่ตามลายมืออาจารย์</h2>
    <div class="stmt">
      <p>รวบรวมโจทย์ข้อสอบอัตนัยเสมือนจริงครอบคลุมครบทุกบท แนะนำให้กดปุ่ม <b>"ฝึก"</b> ที่แถบเมนูด้านบนขวาเพื่อซ่อนเฉลย แล้วลองเขียนลงในกระดาษทดด้วยตนเองก่อนแตะตรวจดูทีละขั้นตอน</p>
    </div>

    <!-- Exam Q1 -->
    <h3 class="grp" id="meq1">ข้อ 1: คุณสมบัติของไหลและการแปลงหน่วยความเค้นเฉือน (บทที่ 1)</h3>
    <div class="stmt">
      <p>แผ่นเรียบขนาด \(0.5\text{ m} \times 0.8\text{ m}\) เคลื่อนที่ด้วยความเร็ว \(2.5\text{ m/s}\) เหนือแผ่นเรียบคงที่ โดยมีน้ำมันหล่อลื่นหนา \(5\text{ mm}\) คั่นกลาง กำหนดความหนืดคิเนมาติก \(\nu = 2.0 \times 10^{-4}\text{ m}^2/\text{s}\) และความถ่วงจำเพาะ \(SG = 0.88\) จงหาแรงเฉือนที่ต้องใช้ดึงแผ่นเรียบ</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">ข้อมูลที่กำหนด</div>
        <div class="given">$$\begin{aligned} & A = 0.5 \times 0.8 = 0.40\ \text{m}^2,\quad V = 2.5\ \text{m/s},\quad h = 5\ \text{mm} = 0.005\ \text{m} \\ & \rho = 0.88 \times 1,000 = 880\ \text{kg/m}^3,\quad \mu = \rho \nu = 880 \times 2.0 \times 10^{-4} = 0.176\ \text{Pa}\cdot\text{s} \end{aligned}$$</div>
      </div>
      <div class="row">
        <div class="lab">ความเค้นเฉือน \(\tau\)</div>
        <div>$$\tau = \mu \frac{V}{h} = (0.176\ \text{Pa}\cdot\text{s}) \times \left( \frac{2.5\ \text{m/s}}{0.005\ \text{m}} \right) = 0.176 \times 500 = 88.0\ \text{N/m}^2\ (\text{Pa})$$</div>
      </div>
      <div class="row">
        <div class="lab">แรงเฉือน \(F\)</div>
        <div>$$F = \tau \times A = 88.0\ \text{N/m}^2 \times 0.40\ \text{m}^2 = 35.2\ \text{N}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(F = 35.2\ \text{N}\)</span></div>
      </div>
    </div>

    <!-- Exam Q2 -->
    <h3 class="grp" id="meq2" style="margin-top:30px;">ข้อ 2: มาโนมิเตอร์หลายของไหลและท่อเอียง (บทที่ 2)</h3>
    <div class="stmt">
      <p>ท่อส่งน้ำเชื่อมต่อกับมาโนมิเตอร์หลอดแก้วเอียงทำมุม \(30^\circ\) กับแนวนอน ของเหลวในมาโนมิเตอร์คือปรอท (\(SG = 13.6\)) โดยระยะตามแนวเอียงของปรอทอ่านได้ \(L = 0.40\text{ m}\) เหนือระดับรอยต่อในท่อ จงหาความดันน้ำในท่อ</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">ระยะความสูงแนวดิ่ง \(\Delta h\)</div>
        <div class="given">$$\Delta h = L \sin 30^\circ = 0.40\ \text{m} \times 0.50 = 0.20\ \text{m}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำนวณความดันปรอท</div>
        <div>$$P = \gamma_{\text{Hg}} \Delta h = (13.6 \times 9,810\ \text{N/m}^3) \times 0.20\ \text{m} = 133,416 \times 0.20 = 26,683\ \text{Pa}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(P = 26.68\ \text{kPa}\)</span></div>
      </div>
    </div>

    <!-- Exam Q3 -->
    <h3 class="grp" id="meq3" style="margin-top:30px;">ข้อ 3: แรงดันบนประตูระนาบเอียงและสมดุลบานพับ (บทที่ 2)</h3>
    <div class="stmt">
      <p>บานประตูกั้นน้ำเอียง \(4:3:5\) บานพับติดที่ขอบบน ประตูยาว \(4\text{ m}\) กว้าง \(2\text{ m}\) ระดับน้ำอยู่ที่ขอบบนพอดี จงหาน้ำหนักถ่วง \(W\) ที่ปลายล่างเพื่อให้ประตูปิดสนิท</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">แรงดันน้ำลัพธ์ \(F_R\)</div>
        <div class="given">$$h_c = 2.0 \times 0.8 = 1.6\ \text{m},\quad F_R = (9,810)(1.6)(8) = 125.57\ \text{kN}$$</div>
      </div>
      <div class="row">
        <div class="lab">จุดศูนย์กลางแรงกด \(y_{cp}\)</div>
        <div>$$y_{cp} = 2.0 + \frac{10.667}{16} = 2.667\ \text{m}\ (\text{วัดจากบานพับ})$$</div>
      </div>
      <div class="row">
        <div class="lab">สมดุลโมเมนต์รอบบานพับ</div>
        <div>$$F_R \times y_{cp} = (W \cos\theta) \times 4.0 \implies W = \frac{125.57 \times 2.667}{0.6 \times 4.0} = 180.5\ \text{kN}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(W = 180.5\ \text{kN}\)</span></div>
      </div>
    </div>

    <!-- Exam Q4: Acceleration -->
    <h3 class="grp" id="meq4" style="margin-top:30px;">ข้อ 4: ความเร็วและความเร่งของอนุภาคของไหล (Kinematics &amp; Acceleration Field)</h3>
    <div class="stmt">
      <p>เวกเตอร์ความเร็วของไหล \(\vec{V}(x,y,z,t) = 10x^2\vec{i} - 15xy\vec{j} + 32t\vec{k}\ \text{[m/s]}\) จงหาความเร็วและความเร่งของโมเลกุลของไหลที่ \(X = 2\text{ m},\ Y = 1\text{ m},\ Z = 3\text{ m}\) และ \(t = 0.5\text{ s}\)</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">Step 1: ความเร็ว (u, v, w)</div>
        <div class="given">$$\begin{aligned} & u = 10(2)^2 = 40\ \text{m/s},\quad v = -15(2)(1) = -30\ \text{m/s},\quad w = 32(0.5) = 16\ \text{m/s} \\ & \vec{V} = 40\vec{i} - 30\vec{j} + 16\vec{k}\ \text{m/s},\quad |\vec{V}| = \sqrt{40^2 + (-30)^2 + 16^2} = 52.50\ \text{m/s} \end{aligned}$$</div>
      </div>
      <div class="row">
        <div class="lab">Step 2: ความเร่ง \(a_x\)</div>
        <div>$$a_x = u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} + \frac{\partial u}{\partial t} = 40(20 \times 2) + 0 + 0 + 0 = 40(40) = 1600\ \text{m/s}^2$$</div>
      </div>
      <div class="row">
        <div class="lab">Step 3: ความเร่ง \(a_y\)</div>
        <div>$$a_y = u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} + \frac{\partial v}{\partial t} = 40(-15 \times 1) + (-30)(-15 \times 2) + 0 = -600 + 900 = 300\ \text{m/s}^2$$</div>
      </div>
      <div class="row">
        <div class="lab">Step 4: ความเร่ง \(a_z\)</div>
        <div>$$a_z = u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} + \frac{\partial w}{\partial t} = 0 + 0 + 0 + 32 = 32\ \text{m/s}^2$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(\vec{V} = 40\vec{i} - 30\vec{j} + 16\vec{k}\ \text{m/s},\quad \vec{a} = 1600\vec{i} + 300\vec{j} + 32\vec{k}\ \text{m/s}^2\ (|\vec{a}| \approx 1,628.20\ \text{m/s}^2)\)</span></div>
      </div>
    </div>

    <!-- Exam Q5 -->
    <h3 class="grp" id="meq5" style="margin-top:30px;">ข้อ 5: แรงกระแทกของลำน้ำพุ่งชนแผ่นโค้ง 180° (บทที่ 3)</h3>
    <div class="stmt">
      <p>น้ำพุ่งด้วยความเร็ว \(v = 24\text{ m/s}\) พื้นที่ \(A = 0.010\text{ m}^2\) ชนแผ่นโค้ง \(180^\circ\) จงหาแรง \(R_x\) เมื่อ (ก) แผ่นอยู่นิ่ง และ (ข) แผ่นเคลื่อนที่ตามน้ำด้วย \(u = 6\text{ m/s}\)</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">(ก) แผ่นอยู่นิ่ง (u = 0)</div>
        <div class="given">$$R_x = 2 \rho A v^2 = 2(1,000)(0.010)(24)^2 = 20 \times 576 = 11,520\ \text{N} = 11.52\ \text{kN}$$</div>
      </div>
      <div class="row">
        <div class="lab">(ข) แผ่นเคลื่อนที่ตามน้ำ (u = 6 m/s)</div>
        <div>$$v_r = 24 - 6 = 18\ \text{m/s},\quad R_x = 2 \rho A (v - u)^2 = 20 \times (18)^2 = 20 \times 324 = 6,480\ \text{N} = 6.48\ \text{kN}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(R_{x,\text{fixed}} = 11.52\ \text{kN},\quad R_{x,\text{moving}} = 6.48\ \text{kN}\)</span></div>
      </div>
    </div>

    <!-- Exam Q6 -->
    <h3 class="grp" id="meq6" style="margin-top:30px;">ข้อ 6: การวิเคราะห์มิติและแบบจำลอง Froude Similitude (บทที่ 4)</h3>
    <div class="stmt">
      <p>แบบจำลองแม่น้ำสเกล \(\lambda_L = 1:80\) วัดความเร็วในแบบจำลองได้ \(v_m = 18\text{ m/s}\) จงหาความเร็วในแม่น้ำจริงตามกฎความคล้ายคลึงของ Froude</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">อัตราส่วนความเร็ว Froude</div>
        <div class="given">$$\lambda_v = \sqrt{\lambda_L} = \sqrt{\frac{1}{80}} \implies v_p = v_m \sqrt{80}$$</div>
      </div>
      <div class="row">
        <div class="lab">แทนค่าคำนวณ</div>
        <div>$$v_p = 18\ \text{m/s} \times 8.9443 = 161.00\ \text{m/s}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(v_p = 161.00\ \text{m/s}\)</span></div>
      </div>
    </div>

    <!-- Exam Q7 -->
    <h3 class="grp" id="meq7" style="margin-top:30px;">ข้อ 7: การไหลในท่อวนรอบ Type II (บทที่ 5)</h3>
    <div class="stmt">
      <p>ปล่อยน้ำจากถังเปิดผ่านท่อเหล็กยาว \(L = 150\text{ m}\), \(D = 0.15\text{ m}\), ความขรุขระ \(\varepsilon = 0.15\text{ mm}\) ต่างระดับ \(H = 20\text{ m}\) อุปกรณ์มี \(\sum K_L = 1.5\) จงหาอัตราการไหล \(Q\) โดยวิธีวนรอบ</p>
    </div>
    <div class="exam">
      <div class="row">
        <div class="lab">สมการความเร็ว</div>
        <div class="given">$$v = \sqrt{\frac{2 g H}{1 + \sum K_L + f \frac{L}{D}}} = \sqrt{\frac{2(9.81)(20)}{2.5 + f \frac{150}{0.15}}} = \sqrt{\frac{392.4}{2.5 + 1,000 f}}$$</div>
      </div>
      <div class="row">
        <div class="lab">รอบที่ 1: สมมุติ f = 0.020</div>
        <div>$$v = \sqrt{\frac{392.4}{2.5 + 20}} = \sqrt{\frac{392.4}{22.5}} = 4.176\ \text{m/s} \implies Re = 6.26 \times 10^5 \implies f_{\text{new}} \approx 0.0202$$</div>
      </div>
      <div class="row">
        <div class="lab">รอบที่ 2: ใช้ f = 0.0202 (ลู่เข้า)</div>
        <div>$$v \approx 4.15\ \text{m/s},\quad Q = A v = \frac{\pi (0.15)^2}{4} \times 4.15 = 0.0733\ \text{m}^3/\text{s} = 73.3\ \text{L/s}$$</div>
      </div>
      <div class="row">
        <div class="lab">คำตอบสุดท้าย</div>
        <div><span class="fin">\(v \approx 4.15\ \text{m/s},\quad Q \approx 73.3\ \text{L/s}\)</span></div>
      </div>
    </div>
  </div>

  <div class="pn" style="margin-top:40px;">
    <a href="#meter">← เครื่องมือวัด &amp; Cavitation</a>
    <a href="#calc">เครื่องคิดเลขคำนวณสด →</a>
  </div>
</section>
'''
