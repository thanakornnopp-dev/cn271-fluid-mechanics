# -*- coding: utf-8 -*-

def get_section_ch4():
    return r'''
<section id="ch4">
  <header class="top">
    <p class="kick">เนื้อหาและเฉลยละเอียดตามระเบียบอาจารย์</p>
    <h1>บทที่ 4: การวิเคราะห์มิติและแบบจำลอง (Dimensional Analysis &amp; Similitude)</h1>
    <p class="sub">ทฤษฎีบท Buckingham Pi 8 ขั้นตอน · กฎความคล้ายคลึงของแบบจำลอง Froude &amp; Reynolds Similitude · อัตราส่วนสเกล</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 4</span>ข้อสอบเต็งหนึ่งการวิเคราะห์มิติและแบบจำลอง (9 ข้อ)</h2>
  <div class="stmt">
    <p>บทที่ 4 ออกข้อสอบอัตนัยแน่นอน 1 ข้อใหญ่ โดยมี 2 ส่วนหลัก: <b>(1) ทฤษฎีบท Buckingham \(\Pi\)</b> บังคับแสดงครบ 8 ลำดับขั้นตามระเบียบอาจารย์ และ <b>(2) กฎการสเกลแบบจำลองทางชลศาสตร์ (Similitude)</b> ระหว่างผิวน้ำอิสระ (Froude) กับท่อปิด (Reynolds)</p>
  </div>

  <div class="jump">
    <a href="#ch4-theory">ก. 8 ขั้นตอน Buckingham Pi</a>
    <a href="#ch4-traps">ข. จุดดักคะแนนข้อสอบ</a>
    <a href="#ch4-bpi">ค. ตัวอย่างข้อ 2 Buckingham Pi แรงผลักใบพัด (หน้า 23)</a>
    <a href="#ch4-froude">ง. ตัวอย่างข้อ 6 แบบจำลองแม่น้ำ Froude (หน้า 25)</a>
    <a href="#ch4-reynolds">จ. ตัวอย่างข้อ 5 แบบจำลองท่อ Reynolds (หน้า 24)</a>
  </div>

  <h3 class="grp" id="ch4-theory">ก. 8 ขั้นตอนมาตรฐาน Buckingham \(\Pi\) Theorem</h3>
  <div class="plan">
    <p><b class="l">ขั้น 1:</b> เขียนฟังก์ชันความสัมพันธ์และนับจำนวนตัวแปรทั้งหมด \(k\)</p>
    <p><b class="l">ขั้น 2:</b> เขียนมิติพื้นฐานของตัวแปรทุกตัวในระบบ \(M, L, T\)</p>
    <p><b class="l">ขั้น 3:</b> กำหนดจำนวนมิติหลัก \(r\) และคำนวณจำนวนกลุ่มไร้มิติ \(\Pi = k - r\)</p>
    <p><b class="l">ขั้น 4:</b> เลือกตัวแปรซ้ำ (Repeating Variables) จำนวน \(r\) ตัว (เรขาคณิต, ของไหล, จลนศาสตร์ ห้ามเลือกตัวแปรที่รวมกันเป็นกลุ่มไร้มิติเองได้)</p>
    <p><b class="l">ขั้น 5:</b> ตั้งสมการกลุ่ม \(\Pi_i\) ร่วมกับตัวแปรซ้ำยกกำลัง \(a, b, c, \dots\)</p>
    <p><b class="l">ขั้น 6:</b> ตั้งสมการเลขชี้กำลัง \(M, L, T\) และแก้หาระบบตัวแปร</p>
    <p><b class="l">ขั้น 7:</b> เขียนความสัมพันธ์ในรูปฟังก์ชัน \(\Pi_1 = \phi(\Pi_2, \Pi_3, \dots)\)</p>
    <p><b class="l">ขั้น 8:</b> ตรวจสอบมิติ (Dimensional Check) ของทุกกลุ่มว่าเป็น \([M^0 L^0 T^0]\) จริง</p>
  </div>

  <h3 class="grp" id="ch4-traps">ข. จุดดักคะแนนและข้อควรระวังในห้องสอบ</h3>
  <div class="bx trap">
    <b>จุดดักคะแนนของบทที่ 4:</b>
    <div>
      • <b>ห้ามลัดขั้นตอน:</b> คะแนนกว่า 80% อยู่ที่การตั้งสมการเลขชี้กำลัง \(M, L, T\) และแก้ทีละแกน การกระโดดใส่กลุ่มสำเร็จรูปจะได้คะแนนไม่เกิน 2/10<br>
      • <b>การเลือกระหว่าง Froude กับ Reynolds:</b> ผิวน้ำเปิด, คลื่น, ทางน้ำล้น, เขื่อน ใช้ <b>Froude Model</b> (\(Fr_m = Fr_p\)) ส่วนการไหลเต็มท่อปิด, อากาศยาน, การทดสอบใต้น้ำลึก ใช้ <b>Reynolds Model</b> (\(Re_m = Re_p\))
    </div>
  </div>

  <hr>

  <!-- 1. BUCKINGHAM PI EX 2 -->
  <h3 id="ch4-bpi" class="grp">ค. ตัวอย่างข้อ 2 (หน้า 23): Buckingham \(\Pi\) Theorem (แรงผลักใบพัด)</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 2:</b> แรงผลัก \(F\) ที่เกิดจากใบพัดเครื่องจักร ขึ้นอยู่กับ เส้นผ่านศูนย์กลาง \(D\), ความหนาแน่นของของไหล \(\rho\), ความหนืดสัมบูรณ์ \(\mu\), และความเร็วเชิงมุม \(\omega\) จงหากลุ่มตัวแปรที่ไม่มีมิติที่เกี่ยวข้อง</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ 8 ลำดับขั้นมาตรฐานอาจารย์</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ขั้น 1: ฟังก์ชัน</div>
      <div class="given">$$F = f(D, \rho, \mu, \omega) \implies \text{จำนวนตัวแปรทั้งหมด } k = 5$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 2: มิติพื้นฐาน</div>
      <div>$$[F] = M L T^{-2},\quad [D] = L,\quad [\rho] = M L^{-3},\quad [\mu] = M L^{-1} T^{-1},\quad [\omega] = T^{-1}$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 3: มิติหลัก &amp; จำนวนกลุ่ม</div>
      <div>$$r = 3\ (M, L, T) \implies \text{จำนวนกลุ่มไร้มิติ } \Pi = k - r = 5 - 3 = 2\ \text{กลุ่ม}\ (\Pi_1, \Pi_2)$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 4: เลือกตัวแปรซ้ำ</div>
      <div>$$\text{เลือก } r=3\ \text{ตัวแปร: } D\ \text{(ขนาด)}, \quad \rho\ \text{(คุณสมบัติของไหล)}, \quad \omega\ \text{(การเคลื่อนที่)}$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 5: ตั้งกลุ่ม \(\Pi_1\)</div>
      <div>$$\Pi_1 = F \cdot D^a \rho^b \omega^c \implies [M^0 L^0 T^0] = (M L T^{-2}) \cdot (L)^a \cdot (M L^{-3})^b \cdot (T^{-1})^c$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 6: แก้หากลุ่ม \(\Pi_1\)</div>
      <div>$$\begin{aligned} & M:\ 1 + b = 0 \implies b = -1 \\ & T:\ -2 - c = 0 \implies c = -2 \\ & L:\ 1 + a - 3b = 0 \implies 1 + a - 3(-1) = 0 \implies a = -4 \\ & \mathbf{\Pi_1 = \frac{F}{\rho \omega^2 D^4}\ (\text{Thrust Coefficient})} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">ตั้งกลุ่ม \(\Pi_2\)</div>
      <div>$$\Pi_2 = \mu \cdot D^d \rho^e \omega^f \implies [M^0 L^0 T^0] = (M L^{-1} T^{-1}) \cdot (L)^d \cdot (M L^{-3})^e \cdot (T^{-1})^f$$</div>
    </div>
    <div class="row">
      <div class="lab">แก้หากลุ่ม \(\Pi_2\)</div>
      <div>$$\begin{aligned} & M:\ 1 + e = 0 \implies e = -1 \\ & T:\ -1 - f = 0 \implies f = -1 \\ & L:\ -1 + d - 3e = 0 \implies -1 + d - 3(-1) = 0 \implies d = -2 \\ & \Pi_2 = \frac{\mu}{\rho \omega D^2} \implies \text{กลับเศษเป็นส่วน: } \mathbf{\Pi_2 = \frac{\rho \omega D^2}{\mu}\ (\text{Rotational Reynolds Number})} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 7: รูปฟังก์ชัน</div>
      <div>$$\frac{F}{\rho \omega^2 D^4} = \phi\left( \frac{\rho \omega D^2}{\mu} \right)$$</div>
    </div>
    <div class="row">
      <div class="lab">ขั้น 8: ตรวจมิติ</div>
      <div>$$\left[ \frac{M L T^{-2}}{(M L^{-3})(T^{-2})(L^4)} \right] = \left[ \frac{M L T^{-2}}{M L T^{-2}} \right] = [M^0 L^0 T^0] \quad \checkmark$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(\dfrac{F}{\rho \omega^2 D^4} = \phi\left( \dfrac{\rho \omega D^2}{\mu} \right)\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 2. FROUDE EX 6 -->
  <h3 id="ch4-froude" class="grp">ง. ตัวอย่างข้อ 6 (หน้า 25): Froude Similitude แบบจำลองแม่น้ำ</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 6:</b> ในการสร้างแบบจำลองแม่น้ำเพื่อศึกษาการไหลแบบผิวน้ำอิสระ ใช้สเกลอัตราส่วนความยาว \(\lambda_L = L_m / L_p = 1:80\) หากวัดความเร็วในแบบจำลองได้ \(v_m = 18\text{ m/s}\) จงหาความเร็วที่เกิดขึ้นในแม่น้ำจริง (\(v_p\))</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">กฎความคล้ายคลึงของ Froude</div>
      <div class="given">$$Fr_m = Fr_p \implies \frac{v_m}{\sqrt{g L_m}} = \frac{v_p}{\sqrt{g L_p}}$$</div>
    </div>
    <div class="row">
      <div class="lab">อัตราส่วนความเร็ว \(\lambda_v\)</div>
      <div>$$\lambda_v = \frac{v_m}{v_p} = \sqrt{\frac{L_m}{L_p}} = \sqrt{\lambda_L} = \sqrt{\frac{1}{80}} = \frac{1}{\sqrt{80}} = \frac{1}{8.9443}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำนวณหาความเร็วจริง \(v_p\)</div>
      <div>$$v_p = v_m \times \sqrt{80} = 18\ \text{m/s} \times 8.9443 = 161.00\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(v_p = 161.00\ \text{m/s}\)</span></div>
    </div>
  </div>

  <hr>

  <!-- 3. REYNOLDS EX 5 -->
  <h3 id="ch4-reynolds" class="grp">จ. ตัวอย่างข้อ 5 (หน้า 24): Reynolds Similitude แบบจำลองท่อ</h3>
  <div class="stmt">
    <p><b>โจทย์ข้อ 5:</b> แบบจำลองท่อสร้างด้วยอัตราส่วนขนาด \(1:10\) (\(D_m / D_p = 0.1\)) ทดสอบด้วยของไหลชนิดเดียวกัน หากในท่อจริงมีความเร็วของการไหล \(v_p = 0.2\text{ m/s}\) จงหาความเร็วที่ต้องใช้ในการทดสอบแบบจำลอง (\(v_m\))</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">กฎความคล้ายคลึงของ Reynolds</div>
      <div class="given">$$Re_m = Re_p \implies \frac{v_m D_m}{\nu_m} = \frac{v_p D_p}{\nu_p}$$</div>
    </div>
    <div class="row">
      <div class="lab">ของไหลชนิดเดียวกัน (\(\nu_m = \nu_p\))</div>
      <div>$$v_m D_m = v_p D_p \implies v_m = v_p \left( \frac{D_p}{D_m} \right)$$</div>
    </div>
    <div class="row">
      <div class="lab">แทนค่าตัวเลข</div>
      <div>$$v_m = 0.2\ \text{m/s} \times \left( \frac{10}{1} \right) = 2.0\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(v_m = 2.0\ \text{m/s}\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#ch3">← บทที่ 3 จลนศาสตร์ &amp; โมเมนตัม</a>
    <a href="#ch5">บทที่ 5 ท่อส่งน้ำ &amp; วนลูป →</a>
  </div>
</section>
'''
