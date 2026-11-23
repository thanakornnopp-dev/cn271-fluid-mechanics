# -*- coding: utf-8 -*-

def get_section_ref():
    return r'''
<section id="ref">
  <header class="top">
    <p class="kick">ตารางค่าคงที่ทางฟิสิกส์ การแปลงหน่วย และคำศัพท์วิศวกรรม</p>
    <h1>ตารางอ้างอิงและคำศัพท์เทคนิค (References &amp; Glossary)</h1>
    <p class="sub">คุณสมบัติของน้ำบริสุทธิ์ · ค่าความขรุขระของท่อพาณิชย์ · สัมประสิทธิ์การสูญเสียรอง · ศัพท์เทคนิคอังกฤษ-ไทย</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">อ้างอิง</span>ตารางค่าคงที่ทางกายภาพและอุปกรณ์</h2>
  <div class="stmt">
    <p>รวบรวมค่าคงที่ทางฟิสิกส์ของน้ำ ค่าความขรุขระผิวท่อตามมาตรฐานสากล สัมประสิทธิ์การสูญเสียพลังงานรอง และตารางคำศัพท์เทคนิคภาษาอังกฤษกำกับภาษาไทย เพื่อใช้ในการคำนวณและการสอบ</p>
  </div>

  <h3 class="grp">1. คุณสมบัติทางกายภาพของน้ำบริสุทธิ์ที่ความดันบรรยากาศ (1 atm)</h3>
  <div class="tw">
    <table>
      <caption>คุณสมบัติของน้ำที่อุณหภูมิต่างๆ (\(0^\circ\text{C} - 100^\circ\text{C}\))</caption>
      <thead>
        <tr>
          <th>อุณหภูมิ (°C)</th>
          <th>ความหนาแน่น \(\rho\) (kg/m³)</th>
          <th>น้ำหนักจำเพาะ \(\gamma\) (N/m³)</th>
          <th>ความหนืดไดนามิก \(\mu\) (\(10^{-3}\) Pa·s)</th>
          <th>ความหนืดคิเนมาติก \(\nu\) (\(10^{-6}\) m²/s)</th>
          <th>ความดันไอ \(P_v\) (kPa)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>0</td><td>999.8</td><td>9,805</td><td>1.787</td><td>1.787</td><td>0.61</td></tr>
        <tr><td>10</td><td>999.7</td><td>9,804</td><td>1.307</td><td>1.307</td><td>1.23</td></tr>
        <tr><td><b>20 (ค่ามาตรฐาน)</b></td><td><b>998.2</b></td><td><b>9,789</b></td><td><b>1.002</b></td><td><b>1.004</b></td><td><b>2.34</b></td></tr>
        <tr><td>25</td><td>997.0</td><td>9,777</td><td>0.890</td><td>0.893</td><td>3.17</td></tr>
        <tr><td>30</td><td>995.7</td><td>9,764</td><td>0.798</td><td>0.801</td><td>4.24</td></tr>
        <tr><td>40</td><td>992.2</td><td>9,730</td><td>0.653</td><td>0.658</td><td>7.38</td></tr>
        <tr><td>100</td><td>958.4</td><td>9,399</td><td>0.282</td><td>0.294</td><td>101.33</td></tr>
      </tbody>
    </table>
  </div>
  <p class="nt">*หมายเหตุ: ในการสอบข้อเขียน หากโจทย์ไม่ระบุอุณหภูมิเฉพาะเจาะจง ให้ใช้ค่ามาตรฐาน: \(\rho = 1,000\text{ kg/m}^3\), \(\gamma = 9,810\text{ N/m}^3\), \(\mu = 10^{-3}\text{ Pa}\cdot\text{s}\), \(\nu = 10^{-6}\text{ m}^2/\text{s}\) และ \(g = 9.81\text{ m/s}^2\)</p>

  <h3 class="grp">2. ค่าความขรุขระสมมูลของท่อพาณิชย์ใหม่ (Equivalent Roughness \(\varepsilon\))</h3>
  <div class="tw">
    <table>
      <caption>ค่าความขรุขระเฉลี่ยสำหรับท่อชนิดต่างๆ จาก Moody (1944)</caption>
      <thead>
        <tr><th>ชนิดของวัสดุท่อ (Pipe Material)</th><th>ความขรุขระ \(\varepsilon\) (mm)</th><th>ความขรุขระ \(\varepsilon\) (ft)</th></tr>
      </thead>
      <tbody>
        <tr><td>แก้ว, พลาสติก, ดึงขึ้นรูป (Drawn Tubing, PVC, Glass)</td><td>0.0015</td><td>0.000005</td></tr>
        <tr><td><b>เหล็กเหนียวพาณิชย์ หรือเหล็กกล้าเชื่อม (Commercial Steel)</b></td><td><b>0.045</b></td><td><b>0.00015</b></td></tr>
        <tr><td>เหล็กหล่อเคลือบแอสฟัลต์ (Asphalted Cast Iron)</td><td>0.12</td><td>0.0004</td></tr>
        <tr><td><b>เหล็กชุบสังกะสี (Galvanized Iron)</b></td><td><b>0.15</b></td><td><b>0.0005</b></td></tr>
        <tr><td>เหล็กหล่อ (Cast Iron)</td><td>0.26</td><td>0.00085</td></tr>
        <tr><td>คอนกรีตผิวเรียบ (Wood Stave / Smooth Concrete)</td><td>0.18 – 0.90</td><td>0.0006 – 0.003</td></tr>
        <tr><td>เหล็กย้ำหมุด (Riveted Steel)</td><td>0.9 – 9.0</td><td>0.003 – 0.03</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp">3. สัมประสิทธิ์การสูญเสียพลังงานรอง (Minor Loss Coefficients \(K_L\))</h3>
  <div class="tw">
    <table>
      <caption>ค่า \(K_L\) สำหรับข้อต่อและวาล์วที่พบบ่อยในข้อสอบ (\(h_m = K_L \frac{v^2}{2g}\))</caption>
      <thead>
        <tr><th>อุปกรณ์ / ลักษณะการสูญเสีย (Fitting / Component)</th><th>สัมประสิทธิ์ \(K_L\)</th><th>หมายเหตุ</th></tr>
      </thead>
      <tbody>
        <tr><td>ทางน้ำเข้าท่อแบบขอบมนโค้งมน (Well-rounded Entrance)</td><td>0.04</td><td>สูญเสียน้อยที่สุด</td></tr>
        <tr><td>ทางน้ำเข้าท่อแบบขอบคมเหลี่ยม (Square-edged Entrance)</td><td>0.50</td><td>โจทย์ข้อสอบส่วนใหญ่ออกค่านี้</td></tr>
        <tr><td>ทางน้ำเข้าท่อแบบท่อยื่นเข้าไปในถัง (Re-entrant Entrance)</td><td>0.80 – 1.00</td><td>มีกระแสวนด้านข้าง</td></tr>
        <tr><td>ทางน้ำออกจากท่อลงสู่ถังใหญ่ (Discharge / Exit to Reservoir)</td><td>1.00</td><td>สูญเสียพลังงานจลน์ทั้งหมด</td></tr>
        <tr><td>ข้องอ 90° ชนิดรัศมีสั้นมาตรฐาน (Standard 90° Elbow)</td><td>0.90</td><td>ข้องอเกลียว</td></tr>
        <tr><td>ข้องอ 90° ชนิดหน้าแปลนขอบโค้งยาว (Long Radius 90° Flanged)</td><td>0.30</td><td>ท่ออุตสาหกรรมขนาดใหญ่</td></tr>
        <tr><td>ข้องอ 45° มาตรฐาน (Standard 45° Elbow)</td><td>0.40</td><td>ข้องอ 45 องศา</td></tr>
        <tr><td>ประตูน้ำเปิดสุด (Gate Valve, Fully Open)</td><td>0.15 – 0.20</td><td>ความดันลดน้อยมาก</td></tr>
        <tr><td>ประตูน้ำเปิด 3/4 (Gate Valve, 3/4 Open)</td><td>1.00</td><td>-</td></tr>
        <tr><td>ประตูน้ำเปิด 1/2 (Gate Valve, 1/2 Open)</td><td>5.60</td><td>-</td></tr>
        <tr><td>ประตูน้ำเปิด 1/4 (Gate Valve, 1/4 Open)</td><td>24.0</td><td>เกิด Throttling รุนแรง</td></tr>
        <tr><td>โกลบวาล์วเปิดสุด (Globe Valve, Fully Open)</td><td>10.0</td><td>ทางน้ำหักเลี้ยวตัว S</td></tr>
        <tr><td>เช็ควาล์วแบบสวิง (Swing Check Valve, Fully Open)</td><td>2.00</td><td>วาล์วกันน้ำย้อน</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp">4. ตารางแปลงหน่วยชลศาสตร์ที่พบบ่อย (Hydraulic Unit Conversions)</h3>
  <div class="tw">
    <table>
      <caption>ตัวคูณการแปลงหน่วยระบบ SI และหน่วยปฏิบัติการวิศวกรรมโยธา</caption>
      <thead>
        <tr><th>ปริมาณ (Quantity)</th><th>หน่วยเริ่มต้น</th><th>หน่วยเป้าหมาย (SI)</th><th>วิธีแปลงหน่วย (คูณด้วย)</th></tr>
      </thead>
      <tbody>
        <tr><td>ปริมาตร (Volume)</td><td>ลิตร (L)</td><td>ลูกบาศก์เมตร (m³)</td><td>\(\times 10^{-3}\) (หาร 1,000)</td></tr>
        <tr><td>ปริมาตร (Volume)</td><td>มิลลิลิตร (mL)</td><td>ลูกบาศก์เมตร (m³)</td><td>\(\times 10^{-6}\) (หาร 1,000,000)</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>ลิตรต่อวินาที (L/s)</td><td>ลูกบาศก์เมตรต่อวินาที (m³/s)</td><td>\(\times 10^{-3}\)</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>ลิตรต่อนาที (L/min)</td><td>ลูกบาศก์เมตรต่อวินาที (m³/s)</td><td>\(\div 60,000\) (\(\times 1.6667 \times 10^{-5}\))</td></tr>
        <tr><td>อัตราการไหล (Flow Rate)</td><td>ลูกบาศก์เมตรต่อชั่วโมง (m³/hr)</td><td>ลูกบาศก์เมตรต่อวินาที (m³/s)</td><td>\(\div 3,600\) (\(\times 2.7778 \times 10^{-4}\))</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>เมตรของน้ำ (m H₂O)</td><td>ปาสคาล (Pa หรือ N/m²)</td><td>\(\times 9,810\) (\(\gamma_{\text{water}}\))</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>มิลลิเมตรปรอท (mmHg)</td><td>ปาสคาล (Pa)</td><td>\(\times 133.322\)</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>บาร์ (bar)</td><td>ปาสคาล (Pa)</td><td>\(\times 10^5\) (\(100,000\text{ Pa}\))</td></tr>
        <tr><td>ความดัน (Pressure)</td><td>กิโลกรัมต่อตารางเซนติเมตร (ksc)</td><td>ปาสคาล (Pa)</td><td>\(\times 98,066.5\) (\(\approx 98.1\text{ kPa}\))</td></tr>
        <tr><td>ความหนืดสัมบูรณ์ (Viscosity)</td><td>พอยส์ (Poise, P)</td><td>ปาสคาล-วินาที (Pa·s)</td><td>\(\times 0.1\)</td></tr>
        <tr><td>ความหนืดสัมบูรณ์ (Viscosity)</td><td>เซนติพอยส์ (Centipoise, cP)</td><td>ปาสคาล-วินาที (Pa·s)</td><td>\(\times 10^{-3}\) (\(1\text{ cP} = 10^{-3}\text{ Pa}\cdot\text{s}\))</td></tr>
        <tr><td>ความหนืดคิเนมาติก</td><td>สโตกส์ (Stokes, St)</td><td>ตารางเมตรต่อวินาที (m²/s)</td><td>\(\times 10^{-4}\)</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp">5. อภิธานศัพท์เทคนิควิศวกรรมชลศาสตร์ (Bilingual Technical Glossary)</h3>
  <div class="tw">
    <table>
      <caption>ศัพท์เทคนิคภาษาอังกฤษกำกับภาษาไทยตามมาตรฐานราชบัณฑิตยสภาและ วสท.</caption>
      <thead>
        <tr><th>คำศัพท์ภาษาอังกฤษ (English Term)</th><th>คำแปลภาษาไทย (Thai Definition)</th><th>บทบาท / ความหมายในกลศาสตร์ของไหล</th></tr>
      </thead>
      <tbody>
        <tr><td><b>Reynolds Number (เลขเรย์โนลด์ส)</b></td><td>พารามิเตอร์ไร้มิติระบุชนิดการไหล</td><td>อัตราส่วนแรงเฉื่อยต่อแรงหนืด (\(Re = \rho v D / \mu\)) ชี้ขาด Laminar หรือ Turbulent</td></tr>
        <tr><td><b>Friction Factor (สัมประสิทธิ์ความเสียดทาน)</b></td><td>ค่าปรับแก้แรงเสียดทานผนังท่อ</td><td>ตัวแปร \(f\) ในสมการ Darcy-Weisbach คำนวณจาก Colebrook หรือ Moody Chart</td></tr>
        <tr><td><b>Relative Roughness (ความขรุขระสัมพัทธ์)</b></td><td>อัตราส่วนความสูงขรุขระต่อเส้นผ่านศูนย์กลาง</td><td>ค่า \(\varepsilon / D\) ใช้เปิดแผนภูมิ Moody เพื่อหาค่าสัมประสิทธิ์แรงเสียดทาน</td></tr>
        <tr><td><b>Dynamic Viscosity (ความหนืดไดนามิก)</b></td><td>ความหนืดสัมบูรณ์</td><td>แรงต้านทานการไหลเชิงโมเลกุล (\(\mu\)) หน่วย SI คือ \(\text{Pa}\cdot\text{s}\) หรือ \(\text{N}\cdot\text{s/m}^2\)</td></tr>
        <tr><td><b>Kinematic Viscosity (ความหนืดคิเนมาติก)</b></td><td>ความหนืดจลนศาสตร์</td><td>อัตราส่วนความหนืดสัมบูรณ์ต่อความหนาแน่น (\(\nu = \mu / \rho\)) หน่วย SI คือ \(\text{m}^2/\text{s}\)</td></tr>
        <tr><td><b>Shear Stress (ความเค้นเฉือน)</b></td><td>แรงเฉือนต่อหนึ่งหน่วยพื้นที่</td><td>แรงเฉือน (\(\tau = \mu \frac{dv}{dy}\)) กระทำขนานกับผิวสัมผัสของของไหล</td></tr>
        <tr><td><b>Velocity Field (สนามความเร็ว)</b></td><td>ฟังก์ชันเวกเตอร์ระบุความเร็วทุกตำแหน่ง</td><td>\(\vec{V}(x,y,z,t) = u\vec{i} + v\vec{j} + w\vec{k}\) ระบุอัตราเร็วและทิศทางของอนุภาค</td></tr>
        <tr><td><b>Convective Acceleration (ความเร่งพา)</b></td><td>ความเร่งจากการเปลี่ยนตำแหน่งในปริภูมิ</td><td>พจน์ \(u\frac{\partial \vec{V}}{\partial x} + v\frac{\partial \vec{V}}{\partial y} + w\frac{\partial \vec{V}}{\partial z}\) เกิดจากการที่อนุภาคไหลไปยังจุดที่ความเร็วต่างกัน</td></tr>
        <tr><td><b>Local Acceleration (ความเร่งเฉพาะที่)</b></td><td>ความเร่งจากการเปลี่ยนแปลงตามเวลา</td><td>พจน์ \(\frac{\partial \vec{V}}{\partial t}\) วัด ณ จุดคงที่เมื่อเวลาเปลี่ยน (เป็นศูนย์ในการไหลคงตัว Steady Flow)</td></tr>
        <tr><td><b>Material Derivative (อนุพันธ์รวมของอนุภาค)</b></td><td>อัตราการเปลี่ยนแปลงที่ตามติดอนุภาคของไหล</td><td>\(\frac{D}{Dt} = (\vec{V}\cdot\nabla) + \frac{\partial}{\partial t}\) ใช้คำนวณความเร่งรวม \(\vec{a} = \frac{D\vec{V}}{Dt}\)</td></tr>
        <tr><td><b>Center of Pressure (จุดศูนย์กลางของแรงกด)</b></td><td>จุดศูนย์กลางแรงดันของเหลว</td><td>จุดที่แรงดันน้ำลัพธ์กระทำบนระนาบ (\(y_{cp} = y_c + I_c / (y_c A)\)) อยู่ต่ำกว่าจุด CG เสมอ</td></tr>
        <tr><td><b>Specific Weight (น้ำหนักจำเพาะ)</b></td><td>น้ำหนักต่อหน่วยปริมาตร</td><td>\(\gamma = \rho g\) สำหรับน้ำบริสุทธิ์มีค่าเท่ากับ \(9,810\text{ N/m}^3\)</td></tr>
        <tr><td><b>Specific Gravity (ความถ่วงจำเพาะ)</b></td><td>อัตราส่วนความหนาแน่นเปรียบเทียบกับน้ำ</td><td>\(SG = \rho / \rho_{\text{water}}\) เป็นปริมาณไร้มิติ</td></tr>
        <tr><td><b>Manometer (มาโนมิเตอร์)</b></td><td>หลอดแก้ววัดความดัน</td><td>เครื่องมือวัดความดันของไหลโดยอาศัยความสูงของลำของเหลว</td></tr>
        <tr><td><b>Buckingham Pi Theorem (ทฤษฎีบทบักกิงแฮมพาย)</b></td><td>ทฤษฎีบทการจัดกลุ่มไร้มิติ</td><td>ระเบียบวิธีจัดรูปตัวแปร \(k\) ตัว ใน \(r\) มิติพื้นฐาน ให้อยู่ในรูปกลุ่มไร้มิติ \(k - r\) กลุ่ม</td></tr>
        <tr><td><b>Similitude (ความคล้ายคลึงของแบบจำลอง)</b></td><td>หลักความคล้ายทางชลศาสตร์</td><td>การสร้างแบบจำลองให้เหมือนของจริงทั้งด้านเรขาคณิต (Geometric), จลนศาสตร์ (Kinematic) และพลศาสตร์ (Dynamic)</td></tr>
        <tr><td><b>Venturi Meter (ท่อเวนจูรี่)</b></td><td>เครื่องมือวัดอัตราการไหลในท่อ</td><td>อาศัยหลักการลดขนาดท่อจนเกิดผลต่างความดันเพื่อคำนวณอัตราการไหลตามสมการเบอร์นูลลี</td></tr>
        <tr><td><b>Net Positive Suction Head (NPSH)</b></td><td>เฮดดูดสุทธิเหนือความดันไอ</td><td>พลังงานแรงดันที่ทางดูดของปั๊มที่สูงกว่าความดันไอ เพื่อป้องกันการระเหิดเป็นฟอง</td></tr>
        <tr><td><b>Cavitation (การเกิดฟองโพรงไอ)</b></td><td>ปรากฏการณ์โพรงไอระเบิด</td><td>การเกิดฟองไอเมื่อความดันลดต่ำกว่า \(P_v\) แล้วฟองยุบตัวระเบิดทำลายผิวใบพัดปั๊ม</td></tr>
      </tbody>
    </table>
  </div>

  <div class="pn" style="margin-top:40px;">
    <a href="#calc">← เครื่องคิดเลขคำนวณสด</a>
    <a href="#sum">กลับสู่หน้าสรุปภาพรวม ↑</a>
  </div>
</section>
'''
