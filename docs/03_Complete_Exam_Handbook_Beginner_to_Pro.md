# CN271 Fluid Mechanics: คลังข้อสอบจริงเจาะลึก ข้อ 1 ถึง ข้อ 8 ฉบับสมบูรณ์
> **Faculty of Engineering, Thammasat University (คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์)**  
> *คู่มือเตรียมสอบวิชาฟลูอิด: สอนละเอียดจากศูนย์ คำศัพท์ภาษาอังกฤษวงเล็บไทย ขั้นตอนตรงตามอาจารย์ 100% ตัวเลขไม่เพี้ยน*

---

## 🌟 ตารางสรุปภาพรวมข้อสอบ ข้อ 1 ถึง ข้อ 8 (Exam Summary Table)

| ข้อที่ | หัวข้อโจทย์ | ข้อมูลที่โจทย์กำหนดให้ | สิ่งที่โจทย์ถาม | คำตอบสุดท้าย | หน่วย |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **1** | ประเภทการไหล & ความเร็วสูงสุด | $D = 10\text{ cm}, v = 0.1\text{ m/s}, \mu = 10^{-3}$ | Laminar หรือ Turbulent, $v_{\text{max, laminar}}$ | $\mathbf{Re = 10,000 \text{ (Turbulent)}}, \; \mathbf{v_{\text{max}} = 0.02}$ | $\text{m/s}$ |
| **2** | ความดันลดลง $\Delta P$ ในท่อราบ | $D = 8\text{ cm}, v = 0.02\text{ m/s}, L = 0.5\text{ m}$ | $\Delta P$ สภาวะ Laminar และ Turbulent | $\mathbf{\Delta P_{\text{laminar}} = 0.05\text{ Pa}}, \; \mathbf{\Delta P_{\text{turbulent}} = 15\text{ Pa}}$ | $\text{Pa}$ |
| **3** | ท่อ 3 ขนาดต่างระดับ | $Q = 0.1\text{ m}^3\text{/s}, D = 10, 20, 30\text{ cm}$ | การสูญเสียพลังงาน $h_{L, 1-2}$ และ $h_{L, 2-3}$ | $\mathbf{h_{L, 1-2} = 9.84\text{ m}}, \; \mathbf{h_{L, 2-3} = 5.47\text{ m}}$ | $\text{m}$ |
| **4** | ท่อยาว $600\text{ m}$ ข้องอ 2 ตัว | $Q = 0.1\text{ m}^3\text{/s}, D = 20\text{ cm}, \varepsilon = 0.4\text{ mm}$ | Major Loss ($h_f$) และ Minor Loss ($h_m$) | $\mathbf{h_f = 36.74\text{ m}}, \; \mathbf{h_m = 0.52\text{ m}} \implies \mathbf{h_L = 37.25\text{ m}}$ | $\text{m}$ |
| **5** | ท่อ $D=0.6\text{ m}$ ขึ้นเนิน $20\text{ m}$ | $v = 2\text{ m/s}, P_2 \ge 10\text{ kPa}, \varepsilon = 3\text{ mm}$ | ความดันน้อยที่สุดที่จุด 1 ($P_{1, \text{min}}$) | $\mathbf{P_1 = 219.58\text{ kPa} \quad (\approx 220\text{ kPa})}$ | $\text{kPa}$ |
| **6** | หาความเร็วในท่อยาว $700\text{ m}$ | $L = 700\text{ m}, h_L = 3\text{ m}, D = 15\text{ cm}$ | Velocity ($v$) ด้วย Trial & Error | $\mathbf{v = 0.77\text{ m/s} \quad (f = 0.021)}$ | $\text{m/s}$ |
| **7** | ถังน้ำลึก $15\text{ m}$ ขึ้นเนิน $10\text{ m}$ | ถังลึก $15\text{ m}, z_2 = 10\text{ m}, D = 15\text{ cm}$ | Velocity ($v$) พุ่งออกสู่อากาศ | $\mathbf{v = 2.51\text{ m/s} \quad (f = 0.0195)}$ *(⭐ ข้อสอบแน่!)* | $\text{m/s}$ |
| **8** | ออกแบบขนาดท่อ $D$ ด้วย $D^5$ | $Q = 0.5\text{ m}^3\text{/s}, h_L = 10\text{ m}, L = 200\text{ m}$ | Diameter ($D$) ด้วย Trial & Error | $\mathbf{D = 0.36\text{ m} \quad (360\text{ mm}, \; f = 0.0155)}$ | $\text{m}$ |

---

## 📘 เจาะลึกวิธีทำทีละข้อ บรรทัดต่อบรรทัด (Step-by-Step Solutions 1 - 8)

---

### ข้อที่ 1 (ตัวอย่างที่ 1 หน้า 1-2): เช็คประเภทการไหลและหาความเร็วสูงสุดของ Laminar
**โจทย์:** น้ำไหลในท่อขนาดเส้นผ่านศูนย์กลาง $10\text{ cm}$ ด้วยความเร็ว $0.1\text{ m/s}$ กำหนดค่า **Dynamic Viscosity (ความหนืดสัมบูรณ์, $\mu$)** เท่ากับ $10^{-3}\text{ N}\cdot\text{s/m}^2$  
จงหาว่าการไหลเป็นแบบ **Laminar (ราบเรียบ)** หรือ **Turbulent (ปั่นป่วน)**  
ถ้าการไหลเป็นแบบ Turbulent อยากทราบความเร็วที่สูงที่สุดที่ทำให้การไหลเป็นแบบ Laminar

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **แปลงหน่วยให้อยู่ในระบบ SI:**  
    *   เส้นผ่านศูนย์กลางท่อ: $D = 10\text{ cm} = 0.1\text{ m}$
    *   ความเร็วการไหล: $v = 0.1\text{ m/s}$
    *   ความหนืดสัมบูรณ์: $\mu = 10^{-3}\text{ N}\cdot\text{s/m}^2$
    *   ความหนาแน่นน้ำมาตรฐาน: $\rho = 1,000\text{ kg/m}^3$
2.  **คำนวณ Reynolds Number (เลขเรย์โนลด์ส, $Re$):**
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(0.1)(0.1)}{10^{-3}} = \frac{10}{10^{-3}} = \mathbf{10,000}$$
    *เกณฑ์ตัดสิน:* เนื่องจาก $Re = 10,000 > 2,000$ ดังนั้น **เป็นการไหลแบบ Turbulent Flow (การไหลแบบปั่นป่วน)**
3.  **หาความเร็วสูงสุดที่จะยังคงเป็น Laminar Flow (การไหลแบบราบเรียบ):**  
    เกณฑ์สูงสุดของ Laminar คือ $Re = 2,000$ ตั้งสมการย้อนกลับหาความเร็ว $v$:
    $$2,000 = \frac{\rho v D}{\mu} = \frac{(1000) v (0.1)}{10^{-3}} = \frac{100 v}{10^{-3}} = 10^5 v$$
    $$v = \frac{2,000}{10^5} = \mathbf{0.02\text{ m/s}}$$
*   **สรุปคำตอบ:** $Re = 10,000$ (การไหลแบบ Turbulent) และความเร็วสูงสุดของ Laminar คือ $\mathbf{v = 0.02\text{ m/s}}$

---

### ข้อที่ 2 (ตัวอย่างที่ 2 หน้า 1-2): หาความดันลดลง (Pressure Drop, $\Delta P$) ในท่อ
**โจทย์:** น้ำไหลอยู่ในท่อขนาดเส้นผ่านศูนย์กลางเท่ากับ $8\text{ cm}$ ด้วยความเร็วเฉลี่ยเท่ากับ $0.02\text{ m/s}$  
(ก) จงหาว่า การไหลเป็นแบบ Laminar หรือ Turbulent  
(ข) จงหาค่าความดันที่ลดลงในระยะทาง $0.5\text{ m}$  
(ค) ถ้าท่อเป็นพลาสติก (ค่าสัมประสิทธิ์ความขรุขระ $\varepsilon = 0.12\text{ mm}$) จงหาความดันที่ลดลงในระยะทาง $0.1\text{ m}$ และความเร็วเพิ่มขึ้นเป็น $1\text{ m/s}$

**วิธีทำอย่างละเอียด (Step-by-Step):**
*   **ข้อ (ก) ตรวจสอบ Reynolds Number:**
    $$D = 8\text{ cm} = 0.08\text{ m}, \quad v = 0.02\text{ m/s}$$
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(0.02)(0.08)}{10^{-3}} = \mathbf{1,600}$$
    เนื่องจาก $Re = 1,600 < 2,000 \implies$ **การไหลเป็นแบบ Laminar Flow (การไหลแบบราบเรียบ)**
*   **ข้อ (ข) หาความดันลดลง $\Delta P$ ที่ระยะทาง $L = 0.5\text{ m}$:**  
    ท่ออยู่ในแนวราบและขนาดคงที่ ($z_1 = z_2, v_1 = v_2$):
    $$\frac{\Delta P}{\gamma} = h_f = f \frac{L}{D} \frac{v^2}{2g} \implies \Delta P = f \frac{L}{D} \frac{\rho v^2}{2}$$
    สำหรับ Laminar Flow:
    $$f = \frac{64}{Re} = \frac{64}{1600} = \mathbf{0.04}$$
    $$\Delta P = (0.04) \left(\frac{0.5}{0.08}\right) \frac{(1000)(0.02)^2}{2} = (0.04)(6.25)\frac{(1000)(0.0004)}{2} = \mathbf{0.05\text{ Pa (หรือ N/m}^2)}$$
*   **ข้อ (ค) กรณีท่อพลาสติก $\varepsilon = 0.12\text{ mm}, L = 0.1\text{ m}, v = 1\text{ m/s}$:**  
    คำนวณ $Re$ ใหม่:
    $$Re = \frac{(1000)(1)(0.08)}{10^{-3}} = \mathbf{8 \times 10^4} \quad (\text{Turbulent Flow})$$
    คำนวณ **Relative Roughness (ความขรุขระสัมพัทธ์, $\varepsilon/D$):**
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{80\text{ mm}} = \mathbf{0.0015}$$
    เปิดชาร์ตท่อ (Moody Diagram) ที่ $Re = 8 \times 10^4$ และ $\varepsilon/D = 0.0015$ อ่านได้ค่า $f = \mathbf{0.024}$
    $$\Delta P = f \frac{L}{D} \frac{\rho v^2}{2} = (0.024) \left(\frac{0.1}{0.08}\right) \frac{(1000)(1)^2}{2} = (0.024)(1.25)(500) = \mathbf{15\text{ Pa}}$$

---

### ข้อที่ 3 (ตัวอย่างที่ 3 หน้า 1, 3, 4): ท่อเปลี่ยน 3 ขนาดต่างระดับ หาการสูญเสียพลังงาน $h_L$
**โจทย์:** การไหลของน้ำในท่อเป็นแบบ Incompressible Steady State (การไหลแบบบีบอัดไม่ได้และสม่ำเสมอตามเวลา) โดยอัตราการไหลคงที่เท่ากับ $0.1\text{ m}^3/\text{s}$  
*   จุด 1: $D_1 = 10\text{ cm}, P_1 = 100\text{ kPa}, z_1 = 0\text{ m}$
*   จุด 2: $D_2 = 20\text{ cm}, P_2 = 50\text{ kPa}, z_2 = 3\text{ m}$
*   จุด 3: $D_3 = 30\text{ cm}, P_3 = 20\text{ kPa}, z_3 = 1\text{ m}$  
จงหาค่าการสูญเสียพลังงานระหว่างจุด 1 ถึง 2 ($h_{L, 1-2}$) และระหว่างจุด 2 ถึง 3 ($h_{L, 2-3}$)

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **คำนวณความเร็ว $v = Q/A$ และ Velocity Head ($\frac{v^2}{2g}$):**
    *   หน้าตัด 1: $A_1 = \frac{\pi}{4}(0.1)^2 = 0.007854\text{ m}^2 \implies v_1 = \frac{0.1}{0.007854} = \mathbf{12.73\text{ m/s}}$  
        $$\frac{v_1^2}{2g} = \frac{(12.73)^2}{2(9.81)} = \mathbf{8.260\text{ m}}$$
    *   หน้าตัด 2: $A_2 = \frac{\pi}{4}(0.2)^2 = 0.031416\text{ m}^2 \implies v_2 = \frac{0.1}{0.031416} = \mathbf{3.18\text{ m/s}}$  
        $$\frac{v_2^2}{2g} = \frac{(3.18)^2}{2(9.81)} = \mathbf{0.515\text{ m}}$$
    *   หน้าตัด 3: $A_3 = \frac{\pi}{4}(0.3)^2 = 0.070686\text{ m}^2 \implies v_3 = \frac{0.1}{0.070686} = \mathbf{1.41\text{ m/s}}$  
        $$\frac{v_3^2}{2g} = \frac{(1.41)^2}{2(9.81)} = \mathbf{0.101\text{ m}}$$
2.  **คำนวณพลังงานรวมที่จุด 1 ($H_1$):**
    $$H_1 = \frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{100 \times 10^3}{9,810} + 8.260 + 0 = 10.194 + 8.260 = \mathbf{18.454\text{ m}}$$
3.  **คำนวณพลังงานรวมที่จุด 2 ($H_2$):**
    $$H_2 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 = \frac{50 \times 10^3}{9,810} + 0.515 + 3 = 5.097 + 0.515 + 3 = \mathbf{8.612\text{ m}}$$
4.  **คำนวณพลังงานรวมที่จุด 3 ($H_3$):**
    $$H_3 = \frac{P_3}{\gamma} + \frac{v_3^2}{2g} + z_3 = \frac{20 \times 10^3}{9,810} + 0.101 + 1 = 2.039 + 0.101 + 1 = \mathbf{3.140\text{ m}}$$
5.  **หาการสูญเสียพลังงานระหว่างจุด:**
    $$h_{L, 1-2} = H_1 - H_2 = 18.454 - 8.612 = \mathbf{9.84\text{ m}}$$
    $$h_{L, 2-3} = H_2 - H_3 = 8.612 - 3.140 = \mathbf{5.47\text{ m}}$$

---

### ข้อที่ 4 (หน้า 4): ท่อยาว $600\text{ m}$ ข้องอ 2 ตัว หา Major Loss และ Minor Loss
**โจทย์:** น้ำไหลในท่อด้วยอัตราการไหลเท่ากับ $0.1\text{ m}^3/\text{s}$ ที่มีเส้นผ่านศูนย์กลางคงที่ $20\text{ cm}$ ความยาวจากจุด 1 ไปจุด 2 เท่ากับ $600\text{ m}$ ค่าสัมประสิทธิ์ความขรุขระ $\varepsilon = 0.4\text{ mm}$ ความหนืดสัมบูรณ์ $\mu = 10^{-3}\text{ N}\cdot\text{s/m}^2$  
แนวท่อมีข้องอ 2 ตัว แต่ละตัวมีสัมประสิทธิ์การสูญเสียรอง $K_L = 0.5$ และจุด 2 อยู่สูงกว่าจุด 1 อยู่ $2\text{ m}$  
จงหาการสูญเสียพลังงานหลัก (Major loss, $h_f$) และการสูญเสียพลังงานรอง (Minor loss, $h_m$) จากจุด 1 ไปจุด 2

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **แปลงหน่วยและหาความเร็ว $v$:**
    $$D = 0.2\text{ m}, \quad A = \frac{\pi}{4}(0.2)^2 = 0.031416\text{ m}^2$$
    $$v = \frac{Q}{A} = \frac{0.1}{0.031416} = \mathbf{3.183\text{ m/s}}$$
    $$\frac{v^2}{2g} = \frac{(3.183)^2}{2(9.81)} = \mathbf{0.5165\text{ m}}$$
2.  **คำนวณ Reynolds Number และ Relative Roughness:**
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(3.183)(0.2)}{10^{-3}} = \mathbf{6.37 \times 10^5}$$
    $$\frac{\varepsilon}{D} = \frac{0.4\text{ mm}}{200\text{ mm}} = \mathbf{0.0020}$$
3.  **เปิดชาร์ตท่อหาค่า Friction Factor ($f$):**  
    ที่ $Re = 6.37 \times 10^5$ และ $\varepsilon/D = 0.0020 \implies f = \mathbf{0.0238 \approx 0.024}$
4.  **คำนวณการสูญเสียหลัก (Major Loss, $h_f$):**
    $$h_f = f \frac{L}{D} \frac{v^2}{2g} = (0.0238) \left(\frac{600}{0.2}\right) (0.5165) = (0.0238)(3000)(0.5165) = \mathbf{36.88\text{ m}} \quad (\text{หรือ } 37.19\text{ m ถ้าใช้ } f=0.024)$$
5.  **คำนวณการสูญเสียรอง (Minor Loss, $h_m$):**  
    มีข้องอ 2 ตัว $\sum K_L = 0.5 + 0.5 = 1.0$:
    $$h_m = \left(\sum K_L\right) \frac{v^2}{2g} = (1.0)(0.5165) = \mathbf{0.52\text{ m}}$$
*   **สรุปคำตอบ:** Major Loss $\mathbf{h_f \approx 36.88 - 37.19\text{ m}}$, Minor Loss $\mathbf{h_m = 0.52\text{ m}}$ (การสูญเสียรวม $h_L \approx 37.40\text{ m}$)

---

### ข้อที่ 5 (หน้า 4): ท่อ $D = 0.6\text{ m}$ ขึ้นเนิน $20\text{ m}$ หาความดันน้อยที่สุดที่จุด 1
**โจทย์:** น้ำไหลในท่อที่มีเส้นผ่านศูนย์กลาง $0.6\text{ m}$ ไหลด้วยความเร็ว $2\text{ m/s}$ ถ้าความดันที่จุด 2 จะต้องมากกว่า $10\text{ kPa}$ จงหาค่าความดันที่น้อยที่สุดที่จุด 1 ให้คิดการสูญเสียพลังงานทั้งหมดในการไหล  
จุด 1 และจุด 2 ห่างกัน $L = 120\text{ m}$, สัมประสิทธิ์การสูญเสียรองข้องอ $90^\circ$ เท่ากับ $0.3$ (มีข้องอ 2 ตัว), ความสูงเนิน $z_2 - z_1 = 20\text{ m}$, ความขรุขระ $\varepsilon = 3\text{ mm}$

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **ข้อมูลและเฮดความเร็ว:**
    $$D = 0.6\text{ m}, \quad v = 2.0\text{ m/s}$$
    $$\frac{v^2}{2g} = \frac{(2.0)^2}{2(9.81)} = \mathbf{0.2039\text{ m}}$$
    *ข้อสังเกต:* ท่อมีขนาดคงที่ตลอดแนว $D_1 = D_2 = 0.6\text{ m} \implies v_1 = v_2 = 2.0\text{ m/s}$ ดังนั้น Velocity head ตัดกันได้ในสมการพลังงาน!
2.  **คำนวณ Reynolds Number และ Relative Roughness:**
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(2.0)(0.6)}{10^{-3}} = \mathbf{1.20 \times 10^6}$$
    $$\frac{\varepsilon}{D} = \frac{3\text{ mm}}{600\text{ mm}} = \mathbf{0.0050}$$
3.  **หา Friction Factor ($f$):**  
    ที่ $Re = 1.2 \times 10^6$ และ $\varepsilon/D = 0.0050$ (อยู่ในช่วง Fully Rough Turbulent Zone):
    $$f \approx \mathbf{0.0304 \approx 0.030}$$
4.  **คำนวณการสูญเสียพลังงานรวม ($\sum h_L$):**
    *   Major Loss: $h_f = f \frac{L}{D} \frac{v^2}{2g} = (0.0304) \left(\frac{120}{0.6}\right) (0.2039) = (0.0304)(200)(0.2039) = \mathbf{1.24\text{ m}}$
    *   Minor Loss: มีข้องอ 2 ตัว $\sum K = 0.3 + 0.3 = 0.6 \implies h_m = (0.6)(0.2039) = \mathbf{0.12\text{ m}}$
    *   $\sum h_L = h_f + h_m = 1.24 + 0.12 = \mathbf{1.36\text{ m}}$
5.  **ตั้งสมการพลังงานจากจุด 1 ไปยังจุด 2:**
    $$\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 + \sum h_L$$
    $$\frac{P_1}{\gamma} = \frac{P_2}{\gamma} + (z_2 - z_1) + \sum h_L$$
    แทนค่า $P_2 = 10\text{ kPa} = 10 \times 10^3\text{ Pa}$ และ $z_2 - z_1 = 20\text{ m}$:
    $$\frac{P_1}{\gamma} = \frac{10 \times 10^3}{9,810} + 20 + 1.36 = 1.019 + 20 + 1.36 = \mathbf{22.38\text{ m}}$$
    $$P_1 = 22.38 \times 9,810 = 219,548\text{ Pa} = \mathbf{219.58\text{ kPa} \quad (\approx 220\text{ kPa})}$$
*   **สรุปคำตอบ:** ค่าความดันที่น้อยที่สุดที่จุด 1 คือ $\mathbf{P_1 = 219.58\text{ kPa}}$

---

### ข้อที่ 6 (หน้า 3, 4): หาความเร็วของการไหล $v$ (วิธี Trial & Error สมมุติค่า)
**โจทย์:** ท่อยาว $L = 700\text{ m}$, การสูญเสียพลังงาน $h_L = 3\text{ m}$, เส้นผ่านศูนย์กลาง $D = 15\text{ cm}$, ความขรุขระ $\varepsilon = 0.12\text{ mm}$ ($\nu = 10^{-6}\text{ m}^2/\text{s}$) จงหาความเร็วของน้ำในท่อ

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **ตั้งสมการ Darcy-Weisbach:**
    $$h_L = f \frac{L}{D} \frac{v^2}{2g} \implies 3 = f \frac{700}{0.15} \frac{v^2}{2(9.81)}$$
    $$v = \sqrt{\frac{3 \times 0.15 \times 2(9.81)}{700 f}} = \sqrt{\frac{0.012613}{f}}$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{150\text{ mm}} = 0.0008$$
2.  **Trial 1 (สมมุติรอบแรก):** สมมุติ $f = 0.020$
    $$v = \sqrt{\frac{0.012613}{0.020}} = \mathbf{0.79\text{ m/s}}$$
    คำนวณ $Re = \frac{0.79 \times 0.15}{10^{-6}} = 1.185 \times 10^5 \approx 1.2 \times 10^5$
    เปิด Moody ที่ $Re = 1.2 \times 10^5, \varepsilon/D = 0.0008 \implies f_{\text{Moody}} = \mathbf{0.021} \neq 0.020 \quad (\text{ยังไม่ตรง } \to \text{No})$
3.  **Trial 2 (สมมุติรอบสอง):** ใช้ $f = 0.021$
    $$v = \sqrt{\frac{0.012613}{0.021}} = \mathbf{0.77\text{ m/s}}$$
    คำนวณ $Re = \frac{0.77 \times 0.15}{10^{-6}} = 1.155 \times 10^5 \approx 1.2 \times 10^5$
    เปิด Moody ที่ $Re = 1.2 \times 10^5, \varepsilon/D = 0.0008 \implies f_{\text{Moody}} = \mathbf{0.021} \quad (\text{ตรงเดิม } \to \mathbf{OK!})$
*   **สรุปคำตอบ:** ความเร็วของน้ำในท่อคือ $\mathbf{v = 0.77\text{ m/s}}$

---

### ข้อที่ 7 (หน้า 5-6): ถังน้ำลึก $15\text{ m}$ ขึ้นเนิน $10\text{ m}$ (อาจารย์เขียนเน้น "ข้อสอบแน่!")
**โจทย์:** ท่อยาว $L = 100\text{ m}$, เส้นผ่านศูนย์กลาง $D = 15\text{ cm}$, ทำจาก Asphalted Cast Iron ($\varepsilon = 0.12\text{ mm}$)  
น้ำไหลจากถังเก็บน้ำที่มีผิวน้ำสูงกว่าทางเข้าท่อ $15\text{ m}$ แนวท่อเดินขึ้นเนินไปสูง $10\text{ m}$ แล้วพุ่งออกสู่อากาศ  
สัมประสิทธิ์การสูญเสียรอง: ทางเข้าท่อ $K_{\text{ent}} = 1.0$, ข้องอ 2 ตัว $K_{\text{elbow}} = 0.3$ แต่ละตัว จงหาความเร็วของน้ำ

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **ตั้งสมการพลังงานจากผิวน้ำ (จุด 1) ไปยังปลายทางออก (จุด 2):**
    *   จุด 1 (ผิวน้ำถังใหญ่): $P_1 = 0, v_1 = 0, z_1 = 15\text{ m}$
    *   จุด 2 (ปลายท่อพุ่งออกสู่อากาศ): $P_2 = 0, v_2 = v, z_2 = 10\text{ m}$
    $$15 + 0 + 0 = 0 + \frac{v^2}{2g} + 10 + f \left(\frac{100}{0.15}\right) \frac{v^2}{2g} + [1.0 + 0.3 + 0.3] \frac{v^2}{2g}$$
    $$15 - 10 = 5 = \left[ 1 + 1.6 + f \frac{100}{0.15} \right] \frac{v^2}{2g}$$
    $$\mathbf{5 = \left[ 2.6 + f \left(\frac{100}{0.15}\right) \right] \frac{v^2}{2g}} \quad (\star)$$
2.  **Relative Roughness:**
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{150\text{ mm}} = 0.0008$$
3.  **Trial 1:** สมมุติ $f = 0.020$
    $$\text{Bracket} = 2.6 + (0.020) \left(\frac{100}{0.15}\right) = 2.6 + 13.33 = 15.93$$
    $$v = \sqrt{\frac{5 \times 2(9.81)}{15.93}} = \mathbf{2.48\text{ m/s}}$$
    $$Re = \frac{2.48 \times 0.15}{10^{-6}} = 3.7 \times 10^5 \implies \text{เปิด Moody ได้ } f = \mathbf{0.0195}$$
4.  **Trial 2:** ใช้ $f = 0.0195$
    $$\text{Bracket} = 2.6 + (0.0195) \left(\frac{100}{0.15}\right) = 2.6 + 13.0 = 15.60$$
    $$v = \sqrt{\frac{5 \times 2(9.81)}{15.60}} = \mathbf{2.51\text{ m/s}}$$
    $$Re = \frac{2.51 \times 0.15}{10^{-6}} = 3.77 \times 10^5 \approx 3.8 \times 10^5 \implies \text{เปิด Moody ได้ } f = \mathbf{0.0195} \quad (\text{ลู่เข้าตรงเดิม!})$$
*   **สรุปคำตอบ:** ความเร็วของน้ำพุ่งออกจากท่อคือ $\mathbf{v = 2.51\text{ m/s}}$

---

### ข้อที่ 8 (หน้า 5, 7): หาขนาดเส้นผ่านศูนย์กลางท่อ $D$ ด้วยการจัดรูป $D^5$
**โจทย์:** น้ำไหลด้วยอัตราการไหล $Q = 0.5\text{ m}^3/\text{s}$, ความขรุขระ $\varepsilon = 0.12\text{ mm}$, ความยาวท่อ $L = 200\text{ m}$, การสูญเสียพลังงาน $h_L = 10\text{ m}$ จงหาขนาดเส้นผ่านศูนย์กลาง $D$

**วิธีทำอย่างละเอียด (Step-by-Step):**
1.  **จัดรูปสมการความเร็ว:**
    $$Q = v A = v \frac{\pi D^2}{4} = 0.5 \implies v = \frac{4(0.5)}{\pi D^2} = \frac{2}{\pi D^2}$$
    $$v^2 = \left[ \frac{2}{\pi D^2} \right]^2 = \frac{4}{\pi^2 D^4}$$
2.  **แทนค่าลงในสมการ Darcy-Weisbach:**
    $$h_L = 10 = f \frac{L}{D} \frac{v^2}{2g} = f \frac{200}{D} \frac{1}{2g} \left[ \frac{4}{\pi^2 D^4} \right] = f \frac{200 \times 4}{D^5 \cdot 2g \cdot \pi^2}$$
    $$\mathbf{D^5 = \frac{f \times 200 \times 4}{10 \times 2(9.81) \times \pi^2} = \frac{800 f}{1936.43}} \quad (\star)$$
3.  **Trial 1:** สมมุติ $f = 0.030$
    $$D^5 = \frac{0.030 \times 800}{1936.43} = 0.01239 \implies D = (0.01239)^{0.2} = 0.416\text{ m} \approx \mathbf{0.42\text{ m}}$$
    $$v = \frac{2}{\pi (0.42)^2} = 3.61\text{ m/s} \implies Re = \frac{3.61 \times 0.42}{10^{-6}} = 1.5 \times 10^6$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{420\text{ mm}} = 0.00029 \implies \text{Moody } f = \mathbf{0.015}$$
4.  **Trial 2:** ใช้ $f = 0.015$
    $$D^5 = \frac{0.015 \times 800}{1936.43} = 0.006197 \implies D = (0.006197)^{0.2} = 0.362\text{ m} \approx \mathbf{0.36\text{ m}}$$
    $$v = \frac{2}{\pi (0.36)^2} = 4.91\text{ m/s} \implies Re = \frac{4.91 \times 0.36}{10^{-6}} = 1.77 \times 10^6$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{360\text{ mm}} = 0.00033 \implies \text{Moody } f = \mathbf{0.0155}$$
5.  **Trial 3:** ใช้ $f = 0.0155$
    $$D^5 = \frac{0.0155 \times 800}{1936.43} = 0.006403 \implies D = (0.006403)^{0.2} = 0.364\text{ m} \approx \mathbf{0.36\text{ m}} \quad (\text{ลู่เข้าคงที่!})$$
*   **สรุปคำตอบ:** ขนาดเส้นผ่านศูนย์กลางท่อที่ต้องการคือ $\mathbf{D = 0.36\text{ m} = 360\text{ mm}}$
