# CN271 Fluid Mechanics: Pipe Flow Exam Mastery Guide
**Faculty of Engineering, Thammasat University**  
*Compiled by Commander Chokie & The Autonomous Engineering Squad*

---

## 1. First Principles & Fundamental Equations (สมการหลักและรากฐานทางฟิสิกส์)

### 1.1 The General Energy Equation (สมการพลังงานรวม)
สมการพลังงานระหว่างจุดที่ 1 (ต้นทาง) และจุดที่ 2 (ปลายทาง):
$$\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 + h_p = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 + h_t + \sum h_L$$

*   $\frac{P}{\gamma}$: **Pressure Head** (เฮดความดัน) $[\text{m}]$ โดย $\gamma = \rho g = 9,810\text{ N/m}^3$ (สำหรับน้ำ)
*   $\frac{v^2}{2g}$: **Velocity Head** (เฮดความเร็ว) $[\text{m}]$
*   $z$: **Elevation Head** (เฮดระดับความสูงเทียบกับ Datum) $[\text{m}]$
*   $h_p$: Head ที่ปั๊มเพิ่มให้ระบบ $[\text{m}]$
*   $h_t$: Head ที่เทอร์ไบน์ดึงออกจากระบบ $[\text{m}]$
*   $\sum h_L$: Total Head Loss (การสูญเสียพลังงานรวม) $= \sum h_f + \sum h_m$ $[\text{m}]$

---

### 1.2 Darcy-Weisbach Equation (สมการการสูญเสียหลักเนื่องจากแรงเสียดทาน)
$$h_f = f \frac{L}{D} \frac{v^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5}$$

*   $f$: Darcy Friction Factor (สัมประสิทธิ์ความเสียดทานแบบ Darcy) $[ - ]$
*   $L$: ความยาวท่อ $[\text{m}]$
*   $D$: เส้นผ่านศูนย์กลางท่อ $[\text{m}]$
*   $v$: ความเร็วเฉลี่ยในท่อ $= \frac{Q}{A} = \frac{4Q}{\pi D^2}$ $[\text{m/s}]$
*   $Q$: อัตราการไหล $[\text{m}^3\text{/s}]$

> **[IMPORTANT] ระวังความต่างของสูตรอังกฤษ vs อเมริกัน (Glasgow Chart):**  
> ชาร์ตของ Glasgow College of Nautical Studies ที่อาจารย์แจกในห้องสอบระบุสูตรบนชาร์ตชัดเจนว่า:  
> $$f = \frac{h}{\frac{L}{d} \frac{u^2}{2g}} \quad \text{และเส้นลามินาร์คือ } f = \frac{64}{Re}$$  
> นี่คือ **Darcy Friction Factor ($f$)** ธรรมดา ไม่ใช่ Fanning ($f_F = f/4$) ไม่ต้องเอา 4 ไปคูณหรือหารเพิ่ม!

---

### 1.3 Reynolds Number & Flow Regimes
$$Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu}$$

*   $\nu = 10^{-6}\text{ m}^2/\text{s}$ สำหรับน้ำที่อุณหภูมิห้อง
*   **Laminar Flow ($Re \le 2000$):**  
    $$f = \frac{64}{Re}$$ (ขึ้นกับ $Re$ เท่านั้น ไม่ขึ้นกับความขรุขระ $\varepsilon$)
*   **Transitional Flow ($2000 < Re < 4000$):** ย่านไม่เสถียร
*   **Turbulent Flow ($Re \ge 4000$):**  
    คำนวณจากสมการ Colebrook-White:
    $$\frac{1}{\sqrt{f}} = -2 \log_{10} \left( \frac{\varepsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
    หรืออ่านจาก **Moody Diagram / Glasgow Pipe Friction Chart**

---

### 1.4 Minor Losses (การสูญเสียรอง)
$$h_m = K \frac{v^2}{2g}$$

1.  **Sudden Expansion (ท่อขยายตัวกะทันหัน):**  
    $$h_{m} = K_e \frac{v_1^2}{2g} = \frac{(v_1 - v_2)^2}{2g} = \left( 1 - \frac{A_1}{A_2} \right)^2 \frac{v_1^2}{2g}$$  
    *ข้อควรจำ:* อาจารย์มักให้เปิดชาร์ต Sudden Expansion เทียบกับอัตราส่วนพื้นที่ $A_1 / A_2$ โดย $K$ คูณกับ $\frac{v_1^2}{2g}$ (ความเร็วท่อเล็กก่อนขยาย)
2.  **Sudden Contraction (ท่อหดตัวกะทันหัน):**  
    $$h_{m} = K_c \frac{v_2^2}{2g}$$  
    *ข้อควรจำ:* อ่านค่า $K_c$ จากชาร์ตเทียบกับ $A_2 / A_1$ หรือ $A_3 / A_2$ โดย $K_c$ จะคูณกับ $\frac{v_{\text{downstream}}^2}{2g}$ (ความเร็วในท่อเล็กหลังหดตัว)
3.  **Pipe Entrance (ทางเข้าท่อจากถัง):**  
    *   Sharp-edged (ขอบคม): $K = 0.5$
    *   Rounded (ขอบมน): $K = 0.04 - 0.2$
4.  **Pipe Exit (ทางออกจากท่อเข้าถัง):**  
    *   Submerged discharge (ไหลจมลงถัง): $K = 1.0$

---

## 2. Master Step-by-Step Problem Solving Framework (สเต็ปการทำโจทย์ 3 รูปแบบหลัก)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ประเภทโจทย์การไหลในท่อ                           │
└───────┬──────────────────────────┬──────────────────────────┬──────────┘
        │                          │                          │
┌───────▼──────────────┐   ┌───────▼──────────────┐   ┌───────▼──────────┐
│       Type 1         │   │       Type 2         │   │      Type 3      │
│  หา Head Loss (hf)   │   │ หา Velocity/Flow (Q) │   │ หาขนาดท่อ (D)    │
│  (รู้ D, L, Q, eps)  │   │  (รู้ hf, D, L, eps) │   │ (รู้ hf, Q, L, eps)│
└──────────────────────┘   └──────────────────────┘   └──────────────────┘
```

### Type 1: หา Head Loss หรือความดันลด $\Delta P$ (คำนวณตรงไปตรงมา)
1.  คำนวณความเร็ว $v = \frac{4Q}{\pi D^2}$
2.  หา $Re = \frac{v D}{\nu}$ และ Relative Roughness $\frac{\varepsilon}{D}$
3.  เปิดชาร์ตหาค่า $f$
4.  แทนค่า $h_f = f \frac{L}{D} \frac{v^2}{2g}$ และ $h_m = \sum K \frac{v^2}{2g}$
5.  แทนในสมการพลังงานหา $P_1 - P_2$

---

### Type 2: หาอัตราการไหล $Q$ หรือความเร็ว $v$ (วิธีสมมุติค่า / Trial & Error)
โจทย์มักจะบอกความดันลด $\Delta P$ หรือผลต่างระดับน้ำมาให้ แต่ไม่รู้ความเร็ว $v$ ทำให้หา $Re$ ไม่ได้:

*   **Step 1:** จัดรูปสมการพลังงาน ให้ติดตัวแปร $v$ ในเทอมของ $f$:
    $$h_f = \left[ C_{\text{minor}} + f \frac{L}{D} \right] \frac{v^2}{2g} \implies v = \sqrt{\frac{2g h_f}{C + f \frac{L}{D}}}$$
*   **Step 2 (สมมุติค่ารอบที่ 1):**  
    ดูค่า $\frac{\varepsilon}{D}$ บนชาร์ต แล้วลากไปทางขวาสุดที่โซน **Fully Turbulent Flow** (โซนเส้นนอนราบที่ค่า $f$ ไม่ขึ้นกับ $Re$) อ่านค่า $f_{\text{guess 1}}$ หรือเริ่มที่ $f \approx 0.02$
*   **Step 3:** นำ $f_{\text{guess 1}}$ ไปแทนค่าหา $v_1$
*   **Step 4:** นำ $v_1$ ไปคำนวณ $Re_1 = \frac{v_1 D}{\nu}$
*   **Step 5:** เปิดชาร์ตด้วย $Re_1$ และ $\frac{\varepsilon}{D}$ ได้ค่า $f_{\text{new}}$
*   **Step 6:** เปรียบเทียบ $f_{\text{new}}$ กับ $f_{\text{guess}}$:
    *   ถ้าเท่ากันหรือใกล้เคียงมาก ($< 1-2\%$) $\implies$ **STOP! คำตอบลู่เข้าแล้ว**
    *   ถ้ายังไม่เท่า $\implies$ ใช้ $f_{\text{new}}$ เป็นค่าเดาใหม่ในรอบถัดไป (ปกติทำเพียง 2-3 รอบก็ตรงเป๊ะ)

---

### Type 3: หาขนาดเส้นผ่านศูนย์กลางท่อ $D$ (วิธีสมมุติค่าหาขนาดท่อ)
โจทย์รู้ $Q, h_f, L, \varepsilon$ ต้องการหา $D$:

*   **Step 1:** จัดรูป Darcy-Weisbach ให้อยู่ในรูป $D$:
    $$h_f = \frac{8 f L Q^2}{\pi^2 g D^5} \implies D = \left( \frac{8 f L Q^2}{\pi^2 g h_f} \right)^{1/5}$$
*   **Step 2:** สมมุติค่า $f_{\text{guess}} = 0.020$
*   **Step 3:** คำนวณหา $D$
*   **Step 4:** คำนวณความเร็ว $v = \frac{4Q}{\pi D^2}$ แล้วหา $Re = \frac{v D}{\nu}$ และ $\frac{\varepsilon}{D}$
*   **Step 5:** เปิดชาร์ตได้ $f_{\text{new}}$ แล้วนำกลับไปคำนวณ $D$ รอบใหม่จนกว่าค่า $D$ จะคงที่ (มักได้คำตอบใน 2 รอบ)

---

## 3. Systematic Piping Systems (ระบบท่อแบบต่าง ๆ ในข้อสอบอาจารย์)

### 3.1 Pipes in Series with Inclination (ท่อต่ออนุกรมวางเอียง)
เมื่อท่อ $1, 2, 3$ ขนาดต่างกันต่ออนุกรมกัน และวางทำมุมเอียง $\theta$:

1.  **กำหนดระนาบอ้างอิง (Datum):**  
    กำหนดให้จุดเริ่มต้น $A$ เป็น Datum ($z_A = 0$)  
    จุดปลาย $B$ จะอยู่ที่ระดับ:
    $$z_B = L_{\text{total}} \sin \theta = (L_1 + L_2 + L_3) \sin \theta$$
2.  **ใช้สมการความต่อเนื่องแปลงความเร็วให้อยู่ในเทอมของ $v_1$ ตัวเดียว (Eliminate unknowns):**
    $$Q_1 = Q_2 = Q_3 \implies v_1 A_1 = v_2 A_2 = v_3 A_3$$
    $$v_2 = v_1 \left( \frac{D_1}{D_2} \right)^2, \quad v_3 = v_1 \left( \frac{D_1}{D_3} \right)^2$$
3.  **แทนค่าทั้งหมดลงในสมการพลังงาน:**
    $$\frac{P_A - P_B}{\gamma} - z_B = \left[ \left(\frac{v_3}{v_1}\right)^2 - 1 + f_1 \frac{L_1}{D_1} + f_2 \frac{L_2}{D_2}\left(\frac{v_2}{v_1}\right)^2 + f_3 \frac{L_3}{D_3}\left(\frac{v_3}{v_1}\right)^2 + K_{\text{exp}} + K_{\text{cont}}\left(\frac{v_3}{v_1}\right)^2 \right] \frac{v_1^2}{2g}$$
4.  **ทำ Trial & Error หา $v_1$!**

---

### 3.2 Pipes in Parallel (ท่อต่อขนาน)
เมื่อท่อแตกกิ่งออกเป็น 2 ท่อ (เช่น ท่อ 2 และท่อ 3) แล้วกลับมารวมกัน:

1.  **กฎเหล็กข้อที่ 1 (Head loss เท่ากันเสมอ):**
    $$h_{L2} = h_{L3}$$
    *เหตุผลทางฟิสิกส์:* ความดันที่จุดแยก (Junction 1) และจุดรวม (Junction 2) มีค่าคู่เดียวกัน ดังนั้นพลังงานที่สูญเสียไปตามเส้นทางที่ 2 และเส้นทางที่ 3 ต้องเท่ากันเป๊ะ!
2.  **กฎเหล็กข้อที่ 2 (อัตราการไหลรวมเท่ากับผลบวก):**
    $$Q_{\text{total}} = Q_1 = Q_2 + Q_3 = Q_4$$
3.  **การหา Total Head Loss จากต้นทางถึงปลายทาง:**
    $$h_{AA \to BB} = h_1 + h_2 + h_4 = h_1 + h_3 + h_4$$
    *(ห้ามเอา $h_2 + h_3$ เด็ดขาด! ให้เลือกเส้นทางใดเส้นทางหนึ่ง)*

---

## 4. Socrates Intuition & Exam Traps (มุมมองเชิงลึกและจุดดักคะแนนของอาจารย์)

> [!WARNING] **5 จุดตายที่นักศึกษาเสียคะแนนบ่อยที่สุดในห้องสอบ CN271:**
> 1. **ลืมแปลงหน่วยมิลลิเมตรเป็นเมตรในค่าความขรุขระ $\varepsilon$:**  
>    เช่น $\varepsilon = 0.08\text{ mm} \implies 0.08 \times 10^{-3}\text{ m}$ เมื่อหารด้วย $D = 0.4\text{ m}$ จะได้ $k/D = \frac{0.08}{400} = 0.0002$ ถ้าลืมคูณ $10^{-3}$ ตัวเลขจะผิดทันที 1,000 เท่า!
> 2. **ลืมแปลง kPa เป็น Pa ($\times 10^3$):**  
>    ความดัน $245.25\text{ kPa}$ ต้องคูณ $10^3$ ก่อนหารด้วย $\gamma = 9,810\text{ N/m}^3$ ถึงจะได้เฮดเป็นเมตร ($25.00\text{ m}$)
> 3. **สับสนตัวคูณความเร็วของ Minor Loss:**  
>    *   Sudden Expansion: $K_{\text{exp}}$ คูณกับ $\frac{v_1^2}{2g}$ (ความเร็วก่อนขยาย)
>    *   Sudden Contraction: $K_{\text{cont}}$ คูณกับ $\frac{v_3^2}{2g}$ (ความเร็วในท่อเล็กหลังหดตัว)
> 4. **การบวกลบระดับความสูงของระนาบเอียง ($z_B$):**  
>    ถ้าของไหลไหลขึ้นเนิน ความสูงปลายทาง $z_B > z_A$ ค่า $z_B$ จะอยู่ฝั่งขวาของสมการพลังงาน เมื่อย้ายข้างมาทางซ้ายจะต้องเป็น **ลบ** เสมอ!
> 5. **การคิดท่อขนานผิด:**  
>    เอา $h_2 + h_3$ มารวมกัน ซึ่งผิดหลักฟิสิกส์อย่างสิ้นเชิง จำไว้ว่าของไหล 1 ก้อนเลือกเดินทางใดทางหนึ่งเท่านั้น ดังนั้น Head Loss รวมของระบบขนานคือ $h_2$ (หรือ $h_3$) ตัวใดตัวหนึ่งเท่านั้น!
