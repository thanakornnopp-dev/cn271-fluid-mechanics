# CN271 Fluid Mechanics: Complete Exam Mastery Handbook (คู่มือเตรียมสอบฉบับสมบูรณ์)
> **Faculty of Engineering, Thammasat University (คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์)**  
> *เรียบเรียงโดย: Commander Chokie & AI Engineering Squad ตามแบบเรียนและเฉลยลายมืออาจารย์ 100%*

---

## 🌟 หมวดที่ 0: ปูพื้นฐานจากศูนย์ (Beginner 101: เข้าใจง่ายสำหรับผู้เริ่มต้น)

### 1. ของไหลและการไหลในท่อคืออะไร? (What is Pipe Flow?)
ในวิชา **Fluid Mechanics (กลศาสตร์ของไหล)** เราสนใจศึกษาว่า เมื่อน้ำหรือของเหลวไหลผ่านท่อปิดที่มีแรงดันเต็มท่อ (Circular Pipes Running Full) จะเกิดอะไรขึ้นบ้าง:
1. **Flow Rate / Discharge (อัตราการไหลเชิงปริมาตร $Q$):** คือปริมาตรน้ำที่ไหลผ่านหน้าตัดท่อในหนึ่งวินาที มีหน่วยเป็นลูกบาศก์เมตรต่อวินาที $[\text{m}^3\text{/s}]$ หรือลิตรต่อวินาที $[\text{L/s}]$ โดยที่ $1\text{ m}^3\text{/s} = 1,000\text{ L/s}$
2. **Mean Velocity (ความเร็วเฉลี่ยของการไหล $v$):**
   $$v = \frac{Q}{A} = \frac{Q}{\frac{\pi}{4} D^2} = \frac{4Q}{\pi D^2} \quad [\text{m/s}]$$
   *ข้อสังเกต:* เมื่อขนาดเส้นผ่านศูนย์กลางท่อ ($D$) เล็กลง ความเร็ว ($v$) จะพุ่งสูงขึ้นอย่างรวดเร็ว (แปรผกผันกับ $D^2$)

---

### 2. รูปแบบการไหล: Laminar vs Turbulent (ประเภทการไหล)
เราแยกประเภทการไหลด้วยตัวเลขไร้มิติที่สำคัญที่สุดในโลกของไหล คือ **Reynolds Number (เลขเรย์โนลด์ส, $Re$):**
$$Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu}$$

*   $\rho$: **Density (ความหนาแน่น)** $[\text{kg/m}^3]$ (น้ำมีค่า $1,000\text{ kg/m}^3$)
*   $v$: **Velocity (ความเร็ว)** $[\text{m/s}]$
*   $D$: **Diameter (เส้นผ่านศูนย์กลางท่อ)** $[\text{m}]$
*   $\mu$: **Dynamic Viscosity (ความหนืดสัมบูรณ์ หรือไดนามิก)** $[\text{N}\cdot\text{s/m}^2 \text{ หรือ } \text{kg/(m}\cdot\text{s)}]$ (น้ำที่อุณหภูมิห้อง $\approx 10^{-3}\text{ N}\cdot\text{s/m}^2$)
*   $\nu = \frac{\mu}{\rho}$: **Kinematic Viscosity (ความหนืดคิเนมาติก)** $[\text{m}^2\text{/s}]$ (น้ำที่อุณหภูมิห้อง $\approx 10^{-6}\text{ m}^2\text{/s}$)

#### เกณฑ์การตัดสินประเภทการไหล:
1.  **Laminar Flow (การไหลแบบราบเรียบ):** $Re \le 2,000$  
    ของไหลจะเคลื่อนที่เป็นชั้น ๆ ขนานกันอย่างเป็นระเบียบ ไม่มีอนุภาคไหลข้ามชั้น
    *   **Friction Factor (สัมประสิทธิ์ความเสียดทาน $f$):** ขึ้นกับ $Re$ เพียงอย่างเดียว ไม่ขึ้นกับความขรุขระท่อ!
        $$f = \frac{64}{Re}$$
2.  **Transitional Flow (การไหลช่วงเปลี่ยนผ่าน):** $2,000 < Re < 4,000$  
    การไหลเริ่มปั่นป่วนแต่ยังไม่เต็มที่ ย่านนี้ไม่เสถียร
3.  **Turbulent Flow (การไหลแบบปั่นป่วน):** $Re \ge 4,000$  
    อนุภาคของไหลจะหมุนวน สับสน และมีการผสมกันอย่างรุนแรง ทำให้เกิดแรงต้านทานสูงขึ้นมาก
    *   **Friction Factor ($f$):** ขึ้นกับทั้ง $Re$ และ **Relative Roughness (ความขรุขระสัมพัทธ์ $\varepsilon/D$)** โดยเปิดจาก **Moody Diagram / Glasgow Pipe Friction Chart (ชาร์ตความเสียดทานท่อ)**

---

### 3. ทำไมพลังงานถึงสูญเสีย? (Major Loss vs Minor Loss)
เมื่อของไหลเคลื่อนที่ผ่านท่อ พลังงานรวมจะค่อย ๆ ลดลงเนื่องจากแรงเสียดทานและการรบกวนการไหล:

1.  **Major Loss (การสูญเสียหลักจากแรงเสียดทาน $h_f$):** เกิดขึ้นตลอดความยาวท่อ คำนวณจากสูตร **Darcy-Weisbach (ดาร์ซี-ไวส์บาค):**
    $$h_f = f \frac{L}{D} \frac{v^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5} \quad [\text{m}]$$
2.  **Minor Loss (การสูญเสียรอง $h_m$):** เกิดขึ้นเฉพาะจุดที่มีอุปกรณ์หรือการเปลี่ยนทิศทาง/ขนาด เช่น:
    *   **Sudden Expansion (ท่อขยายตัวกะทันหัน):** $h_m = K_{e} \frac{v_1^2}{2g}$ โดย $K_e = (1 - A_1/A_2)^2$ หรือเปิดชาร์ต
    *   **Sudden Contraction (ท่อหดตัวกะทันหัน):** $h_m = K_{c} \frac{v_2^2}{2g}$ โดยคูณกับความเร็วในท่อเล็กหลังหดตัว
    *   **Pipe Entrance (ทางเข้าท่อจากถัง):** ปากท่อขอบคม $K = 0.5$, ขอบมน $K = 0.04 - 0.2$, ท่อยื่นเข้าไปในถัง $K = 1.0$
    *   **Pipe Exit (ทางออกจากท่อเข้าถัง):** จมใต้ผิวน้ำ $K = 1.0$
    *   **Elbows / Bends (ข้องอ $90^\circ$):** $K = 0.3 - 0.5$

---

### 4. สมการพลังงานรวม (The General Energy Equation)
สมการแม่บทที่ใช้แก้โจทย์ทุกข้อในวิชานี้:
$$\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 + \sum h_L$$

*   $\frac{P}{\gamma}$: **Pressure Head (เฮดความดัน)** $[\text{m}]$ โดย $\gamma = \rho g = 9,810\text{ N/m}^3$ (น้ำ)
*   $\frac{v^2}{2g}$: **Velocity Head (เฮดความเร็ว)** $[\text{m}]$
*   $z$: **Elevation Head (เฮดระดับความสูง)** $[\text{m}]$ เทียบกับ **Datum (ระดับอ้างอิง)**
*   $\sum h_L$: **Total Head Loss (ผลรวมการสูญเสียพลังงาน)** $= \sum h_f + \sum h_m$ $[\text{m}]$

---

## 📘 หมวดที่ 1: เฉลยตัวอย่างบทที่ 5 (Examples 1 - 3 จากชีทอาจารย์)

### ตัวอย่างที่ 1 (Example 1): ตรวจสอบประเภทการไหลและหาความเร็วสูงสุด
**โจทย์:** น้ำไหลในท่อเส้นผ่านศูนย์กลาง $D = 10\text{ cm}$ ด้วยความเร็ว $v = 0.1\text{ m/s}$ กำหนดค่าความหนืดสัมบูรณ์ $\mu = 10^{-3}\text{ N}\cdot\text{s/m}^2$  
จงหาว่าเป็นการไหลแบบ **Laminar (ราบเรียบ)** หรือ **Turbulent (ปั่นป่วน)**  
และถ้าเป็นการไหลแบบ Turbulent อยากทราบความเร็วสูงสุดที่ทำให้การไหลเป็นแบบ Laminar

**วิธีทำ (ตรงตามอาจารย์):**
1.  **แปลงหน่วย:** $D = 10\text{ cm} = 0.1\text{ m}, \; v = 0.1\text{ m/s}, \; \mu = 10^{-3}\text{ N}\cdot\text{s/m}^2, \; \rho = 1,000\text{ kg/m}^3$
2.  **คำนวณ Reynolds Number (เลขเรย์โนลด์ส):**
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(0.1)(0.1)}{10^{-3}} = 10,000$$
    เนื่องจาก $Re = 10,000 > 2,000 \implies$ **เป็นการไหลแบบ Turbulent (ปั่นป่วน)**
3.  **หาความเร็วสูงสุดของการไหลแบบ Laminar:**  
    กำหนดให้ $Re = 2,000$ (เกณฑ์สูงสุดของ Laminar):
    $$2,000 = \frac{\rho v D}{\mu} = \frac{(1000) v (0.1)}{10^{-3}}$$
    $$v = \frac{2,000 \times 10^{-3}}{100} = 0.02\text{ m/s}$$
*   **สรุปคำตอบ:** $Re = 10,000$ (Turbulent) และ $v_{\text{max, laminar}} = 0.02\text{ m/s}$

---

### ตัวอย่างที่ 2 (Example 2): การหา Pressure Drop (ความดันลดลง $\Delta P$)
**โจทย์:** น้ำไหลในท่อเส้นผ่านศูนย์กลาง $D = 8\text{ cm}$ ด้วยความเร็วเฉลี่ย $v = 0.02\text{ m/s}$  
(ก) จงหาว่าการไหลเป็นแบบ Laminar หรือ Turbulent  
(ข) จงหาค่าความดันที่ลดลง ($\Delta P$) ในระยะทาง $L = 0.5\text{ m}$  
(ค) ถ้าท่อเป็นพลาสติก ($\varepsilon = 0.12\text{ mm}$) จงหาความดันที่ลดลงในระยะทาง $L = 0.1\text{ m}$ เมื่อความเร็วเพิ่มขึ้นเป็น $v = 1\text{ m/s}$

**วิธีทำ (ตรงตามอาจารย์):**
*   **ข้อ (ก):**
    $$Re = \frac{\rho v D}{\mu} = \frac{(1000)(0.02)(0.08)}{10^{-3}} = 1,600 < 2,000 \implies \mathbf{Laminar}$$
*   **ข้อ (ข):** เมื่อท่ออยู่ในแนวราบและขนาดคงที่ $\Delta P = \rho g h_L = f \frac{L}{D} \frac{\rho v^2}{2}$  
    สำหรับ Laminar:
    $$f = \frac{64}{Re} = \frac{64}{1600} = 0.04$$
    $$\Delta P = (0.04) \left(\frac{0.5}{0.08}\right) \frac{(1000)(0.02)^2}{2} = 0.04 \times 6.25 \times 0.2 = \mathbf{0.05\text{ Pa (หรือ N/m}^2)}$$
*   **ข้อ (ค):** เมื่อ $v = 1\text{ m/s}, L = 0.1\text{ m}, \varepsilon = 0.12\text{ mm}$
    $$Re = \frac{(1000)(1)(0.08)}{10^{-3}} = 8 \times 10^4 \quad (\text{Turbulent})$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{80\text{ mm}} = 0.0015$$
    เปิด Moody Diagram ที่ $Re = 8 \times 10^4$ และ $\varepsilon/D = 0.0015$ ได้ค่า $f = 0.024$
    $$\Delta P = (0.024) \left(\frac{0.1}{0.08}\right) \frac{(1000)(1)^2}{2} = 0.024 \times 1.25 \times 500 = \mathbf{15\text{ Pa (หรือ N/m}^2)}$$

---

### ตัวอย่างที่ 3 (Example 3): การหาการสูญเสียพลังงานระหว่างจุด (Energy Loss $h_L$)
**โจทย์:** การไหลของน้ำในท่อเป็นแบบ Incompressible Steady State โดยมีอัตราการไหลคงที่ $Q = 0.1\text{ m}^3/\text{s}$  
จุด 1: $D_1 = 10\text{ cm}, P_1 = 100\text{ kPa}, z_1 = 0\text{ m}$  
จุด 2: $D_2 = 20\text{ cm}, P_2 = 50\text{ kPa}, z_2 = 3\text{ m}$  
จุด 3: $D_3 = 30\text{ cm}, P_3 = 20\text{ kPa}, z_3 = 1\text{ m}$  
จงหาค่าการสูญเสียพลังงานระหว่างจุด 1 ถึง 2 ($h_{L, 1-2}$) และระหว่างจุด 2 ถึง 3 ($h_{L, 2-3}$)

**วิธีทำ (ตรงตามอาจารย์):**
1.  **คำนวณความเร็วในแต่ละท่อน ($v = Q/A$):**
    $$v_1 = \frac{0.1}{\frac{\pi}{4}(0.1)^2} = 12.73\text{ m/s} \implies \frac{v_1^2}{2g} = \frac{(12.73)^2}{2(9.81)} = 8.26\text{ m}$$
    $$v_2 = \frac{0.1}{\frac{\pi}{4}(0.2)^2} = 3.18\text{ m/s} \implies \frac{v_2^2}{2g} = \frac{(3.18)^2}{2(9.81)} = 0.515\text{ m}$$
    $$v_3 = \frac{0.1}{\frac{\pi}{4}(0.3)^2} = 1.41\text{ m/s} \implies \frac{v_3^2}{2g} = \frac{(1.41)^2}{2(9.81)} = 0.101\text{ m}$$
2.  **พลังงานรวมจุดที่ 1 ($H_1$):**
    $$H_1 = \frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{100 \times 10^3}{9,810} + 8.26 + 0 = 10.194 + 8.260 = 18.454\text{ m}$$
3.  **พลังงานรวมจุดที่ 2 ($H_2$):**
    $$H_2 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 = \frac{50 \times 10^3}{9,810} + 0.515 + 3 = 5.097 + 0.515 + 3 = 8.612\text{ m}$$
4.  **พลังงานรวมจุดที่ 3 ($H_3$):**
    $$H_3 = \frac{P_3}{\gamma} + \frac{v_3^2}{2g} + z_3 = \frac{20 \times 10^3}{9,810} + 0.101 + 1 = 2.039 + 0.101 + 1 = 3.140\text{ m}$$
5.  **หาการสูญเสียพลังงาน:**
    $$h_{L, 1-2} = H_1 - H_2 = 18.454 - 8.612 = \mathbf{9.84\text{ m}}$$
    $$h_{L, 2-3} = H_2 - H_3 = 8.612 - 3.140 = \mathbf{5.47\text{ m}}$$

---

## 📝 หมวดที่ 2: ข้อสอบท่อเดี่ยวและถังน้ำ (Problems 6 - 8)

### ข้อที่ 6 (Problem 6): หาความเร็วของการไหล $v$ (วิธีสมมุติค่า Trial & Error)
**โจทย์:** ท่อยาว $L = 700\text{ m}$, การสูญเสียพลังงาน $h_L = 3\text{ m}$, เส้นผ่านศูนย์กลาง $D = 15\text{ cm}$, ความขรุขระ $\varepsilon = 0.12\text{ mm}$ ($\nu = 10^{-6}\text{ m}^2/\text{s}$) จงหาความเร็วของน้ำในท่อ

**วิธีทำ (ตรงตามอาจารย์หน้า 3):**
1.  **ตั้งสมการ:**
    $$h_L = f \frac{L}{D} \frac{v^2}{2g} \implies 3 = f \frac{700}{0.15} \frac{v^2}{2(9.81)}$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{150\text{ mm}} = 0.0008$$
2.  **Trial 1:** สมมุติ $f = 0.020$
    $$3 = \frac{0.020 \times 700 \times v^2}{0.15 \times 2(9.81)} \implies v = 0.79\text{ m/s}$$
    $$Re = \frac{0.79 \times 0.15}{10^{-6}} = 1.2 \times 10^5 \implies \text{เปิด Moody ได้ } f = 0.021 \quad (\text{ไม่เท่ากับ 0.020 } \to \text{No})$$
3.  **Trial 2:** ใช้ $f = 0.021$
    $$v = 0.77\text{ m/s} \implies Re = \frac{0.77 \times 0.15}{10^{-6}} = 1.16 \times 10^5 \approx 1.2 \times 10^5 \implies \text{เปิด Moody ได้ } f = 0.021 \quad (\text{ตรงเดิม } \to \text{OK!})$$
*   **สรุปคำตอบ:** $\mathbf{v = 0.77\text{ m/s}}$

---

### ข้อที่ 7 (Problem 7): ถังน้ำไหลขึ้นเนินพุ่งออกสู่อากาศ (ข้อที่อาจารย์เน้น "ข้อสอบแน่!")
**โจทย์:** ท่อยาว $L = 100\text{ m}$, เส้นผ่านศูนย์กลาง $D = 15\text{ cm}$, ทำจาก Asphalted Cast Iron ($\varepsilon = 0.12\text{ mm}$)  
น้ำไหลจากถังเก็บน้ำที่มีผิวน้ำสูงกว่าทางเข้าท่อ $15\text{ m}$ แนวท่อเดินขึ้นเนินไปสูง $10\text{ m}$ แล้วพุ่งออกสู่อากาศ  
สัมประสิทธิ์การสูญเสียรอง: ทางเข้าท่อ $K_{\text{entrance}} = 1.0$, ข้องอ 2 ตัว $K_{\text{elbow}} = 0.3$ แต่ละตัว จงหาความเร็วของน้ำ

**วิธีทำ (ตรงตามอาจารย์หน้า 6):**
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
    $$v = \sqrt{\frac{5 \times 2(9.81)}{15.93}} = 2.48\text{ m/s}$$
    $$Re = \frac{2.48 \times 0.15}{10^{-6}} = 3.7 \times 10^5 \implies \text{เปิด Moody ได้ } f = 0.0195$$
4.  **Trial 2:** ใช้ $f = 0.0195$
    $$\text{Bracket} = 2.6 + (0.0195) \left(\frac{100}{0.15}\right) = 2.6 + 13.0 = 15.60$$
    $$v = \sqrt{\frac{5 \times 2(9.81)}{15.60}} = \mathbf{2.51\text{ m/s}}$$
    $$Re = \frac{2.51 \times 0.15}{10^{-6}} = 3.77 \times 10^5 \approx 3.8 \times 10^5 \implies \text{เปิด Moody ได้ } f = 0.0195 \quad (\text{ลู่เข้าสมบูรณ์!})$$
*   **สรุปคำตอบ:** $\mathbf{v = 2.51\text{ m/s}}$

---

### ข้อที่ 8 (Problem 8): หาขนาดเส้นผ่านศูนย์กลางท่อ $D$ (ด้วยการจัดรูป $D^5$)
**โจทย์:** น้ำไหลด้วยอัตราการไหล $Q = 0.5\text{ m}^3/\text{s}$, ความขรุขระ $\varepsilon = 0.12\text{ mm}$, ความยาวท่อ $L = 200\text{ m}$, การสูญเสียพลังงาน $h_L = 10\text{ m}$ จงหาขนาดเส้นผ่านศูนย์กลาง $D$

**วิธีทำ (ตรงตามอาจารย์หน้า 7):**
1.  **จัดรูปสมการความเร็ว:**
    $$Q = v A = v \frac{\pi D^2}{4} = 0.5 \implies v = \frac{4(0.5)}{\pi D^2} = \frac{2}{\pi D^2}$$
    $$v^2 = \left[ \frac{2}{\pi D^2} \right]^2 = \frac{4}{\pi^2 D^4}$$
2.  **แทนค่าลงในสมการ Darcy-Weisbach:**
    $$h_L = 10 = f \frac{L}{D} \frac{v^2}{2g} = f \frac{200}{D} \frac{1}{2g} \left[ \frac{4}{\pi^2 D^4} \right] = f \frac{200 \times 4}{D^5 \cdot 2g \cdot \pi^2}$$
    $$\mathbf{D^5 = \frac{f \times 200 \times 4}{10 \times 2(9.81) \times \pi^2} = \frac{800 f}{1936.43}} \quad (\star)$$
3.  **Trial 1:** สมมุติ $f = 0.030$
    $$D^5 = \frac{0.030 \times 800}{1936.43} = 0.01239 \implies D = (0.01239)^{0.2} = 0.416\text{ m} \approx 0.42\text{ m}$$
    $$v = \frac{2}{\pi (0.42)^2} = 3.61\text{ m/s} \implies Re = \frac{3.61 \times 0.42}{10^{-6}} = 1.5 \times 10^6$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{420\text{ mm}} = 0.00029 \implies \text{Moody } f = 0.015$$
4.  **Trial 2:** ใช้ $f = 0.015$
    $$D^5 = \frac{0.015 \times 800}{1936.43} = 0.006197 \implies D = (0.006197)^{0.2} = 0.362\text{ m} \approx 0.36\text{ m}$$
    $$v = \frac{2}{\pi (0.36)^2} = 4.91\text{ m/s} \implies Re = \frac{4.91 \times 0.36}{10^{-6}} = 1.77 \times 10^6$$
    $$\frac{\varepsilon}{D} = \frac{0.12\text{ mm}}{360\text{ mm}} = 0.00033 \implies \text{Moody } f = 0.0155$$
5.  **Trial 3:** ใช้ $f = 0.0155 \implies D = 0.364\text{ m} \approx 0.36\text{ m}$ (คงที่!)
*   **สรุปคำตอบ:** $\mathbf{D = 0.36\text{ m} = 360\text{ mm}}$

---

## 📝 หมวดที่ 3: ข้อสอบท่ออนุกรม & โครงข่ายท่อขนาน (Problems 9, Incline, Parallel)

### ข้อที่ 9 (Problem 9): ท่ออนุกรม 3 ท่อน วางในแนวราบ พร้อม Sudden Contraction
**โจทย์:** ท่อส่งน้ำ 3 ท่อต่อกันในแนวราบ การสูญเสียพลังงานจาก A ไป B คือ $h_L = 25\text{ m}$  
*   ท่อ 1: $L_1 = 100\text{ m}, D_1 = 8\text{ cm} = 0.08\text{ m}, \varepsilon_1 = 0.24\text{ mm}$
*   ท่อ 2: $L_2 = 200\text{ m}, D_2 = 6\text{ cm} = 0.06\text{ m}, \varepsilon_2 = 0.12\text{ mm}$
*   ท่อ 3: $L_3 = 50\text{ m}, D_3 = 4\text{ cm} = 0.04\text{ m}, \varepsilon_3 = 0.20\text{ mm}$  
จงหาอัตราการไหลในท่อ ($Q$)

**วิธีทำ (ตรงตามอาจารย์หน้า 8):**
1.  **สัมประสิทธิ์การสูญเสียรอง (Minor Loss Coefficients):**
    *   รอยต่อท่อ 1 ไป 2 (Sudden Contraction): $A_2 / A_1 = (6/8)^2 = 0.5625 \implies K_{c1} = 0.24$
    *   รอยต่อท่อ 2 ไป 3 (Sudden Contraction): $A_3 / A_2 = (4/6)^2 = 0.444 \implies K_{c2} = 0.27$
2.  **ใช้สมการความต่อเนื่องดึงในรูปความเร็ว $v_2$:**
    $$v_1 = v_2 \left(\frac{6}{8}\right)^2 = 0.5625 v_2, \qquad v_3 = v_2 \left(\frac{6}{4}\right)^2 = 2.25 v_2$$
3.  **ตั้งสมการพลังงาน:**
    $$25 = \left[ f_1 \frac{100 \times 0.5625^2}{0.08} + f_2 \frac{200}{0.06} + f_3 \frac{50 \times 2.25^2}{0.04} + 0.24 + 0.27(2.25^2) \right] \frac{v_2^2}{2g}$$
    $$25 = \left[ 395.5 f_1 + 3333.3 f_2 + 6328.1 f_3 + 1.607 \right] \frac{v_2^2}{2g}$$
4.  **Relative Roughness:**
    *   ท่อ 1: $(\varepsilon/D)_1 = \frac{0.24}{80} = 0.003 \implies f_{1,\text{guess}} = 0.027$
    *   ท่อ 2: $(\varepsilon/D)_2 = \frac{0.12}{60} = 0.002 \implies f_{2,\text{guess}} = 0.025$
    *   ท่อ 3: $(\varepsilon/D)_3 = \frac{0.20}{40} = 0.005 \implies f_{3,\text{guess}} = 0.030$
5.  **Trial 1:** แทนค่าเดาแรก $\implies \text{Bracket} = 285.5$
    $$v_2 = 1.31\text{ m/s}, \quad v_1 = 0.74\text{ m/s}, \quad v_3 = 2.95\text{ m/s}$$
    เปิด Moody: $f_1 = 0.028, f_2 = 0.0255, f_3 = 0.031$
6.  **Trial 2:** แทนค่าใหม่ $\implies \text{Bracket} = 293.9$
    $$v_2 = 1.29\text{ m/s}, \quad v_1 = 0.73\text{ m/s}, \quad v_3 = 2.91\text{ m/s}$$
    ตรวจสอบ $Re \implies$ ได้ $f$ เดิมตรงเป๊ะ!
    $$Q = v_2 \frac{\pi}{4}(0.06)^2 = 1.29 \times 0.002827 = \mathbf{3.65 \times 10^{-3}\text{ m}^3/\text{s} = 3.65\text{ L/s}}$$

---

### ข้อสอบใหญ่ 1 (หน้า 9): ท่อ 3 ท่อนต่ออนุกรม วางเอียง $\theta = 5^\circ$
*   $P_A - P_B = 245.25\text{ kPa}, \theta = 5^\circ$
*   $z_B = 280 \sin 5^\circ = 24.40\text{ m}$
*   $\Delta H = 25.00 - 24.40 = 0.60\text{ m}$
*   $0.60 = [3.427 + 200 f_1 + 98.3 f_2 + 845 f_3] \frac{v_1^2}{2g}$
*   **คำตอบ:** $\mathbf{v_1 = 0.71\text{ m/s}, \; v_2 = 0.46\text{ m/s}, \; v_3 = 1.27\text{ m/s}}$

---

### ข้อสอบใหญ่ 2 (หน้า 10): โครงข่ายท่ออนุกรมผสมขนาน 4 ท่อน (15 คะแนน)
*   ท่อ 4 ระหว่าง A และ B: $\frac{910 - 811.41}{9.81} = 10 + h_{AB} \implies h_{AB} = 0.05\text{ m} \implies h_4 = 0.05 \times \frac{1000}{300} = 0.17\text{ m}$
*   ท่อขนาน: $h_2 = h_3 = 0.42\text{ m} \implies Q_3 = 0.16\text{ m}^3/\text{s}, Q_2 = 0.35\text{ m}^3/\text{s} \implies Q_{\text{tot}} = 0.51\text{ m}^3/\text{s}$
*   ท่อ 1: $Q_1 = 0.51\text{ m}^3/\text{s} \implies v_1 = 0.80\text{ m/s} \implies h_1 = 0.66\text{ m}$
*   รวม Head Loss: $h_{AA \to BB} = h_1 + h_2 + h_4 = 0.66 + 0.42 + 0.17 = \mathbf{1.24\text{ m}}$
