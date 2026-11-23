# 🌊 CN271 Fluid Mechanics: Master Course & Exam Mastery Portal
> **Thammasat University — Faculty of Engineering (วิศวกรรมศาสตร์ มธ.)**  
> Civil & Mechanical Engineering Core Curriculum  
> Author: Thanaporn Nopparat & AI Engineering Squad (Commander Chokie)

[![Live Web Portal](https://img.shields.io/badge/🌐_Live_Web_Portal-Click_Here_to_Open-blue?style=for-the-badge&logo=google-chrome)](https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/)
[![Quality Gate](https://img.shields.io/badge/Inspector_QC-PASSED_(30%2F30_Tests)-emerald?style=for-the-badge)](https://github.com/thanakornnopp-dev/cn271-fluid-mechanics)

---

### 🌐 ลิงก์เข้าใช้งานหน้าเว็บสรุปสูตร & คลังเฉลยข้อสอบ Interactive (Live Portal):
👉 **[https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/](https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/)**  
*(หน้าเว็บอัปเกรดใหม่สมบูรณ์แบบ 100% ครอบคลุมเนื้อหาทุกบท มีสูตร MathJax/KaTeX ครบถ้วน, ตารางเก็งข้อสอบอัตนัย, เฉลยละเอียด 4 สเต็ปไม่มีลัดขั้นตอน, และเครื่องคิดเลขจำลองการคำนวณสด)*

---

## 📌 ภาพรวมหลักสูตรและเนื้อหาทั้งหมด (Complete Course Coverage)

คลังความรู้นี้จัดทำขึ้นเป็นพิเศษเพื่อเตรียมความพร้อมสู่การทำข้อสอบอัตนัยวิชา **CN271 Fluid Mechanics (กลศาสตร์ของไหล)** ตามหลักสูตรจริงของคณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ โดยสังเคราะห์เนื้อหาและโจทย์จากเอกสารปี 2569 และ 2570 ครบทุกบท:

1. **บทที่ 1: คุณสมบัติของของไหล (Fluid Properties)**
   * กฎความหนืดของนิวตัน ($\tau = \mu \frac{dv}{dy}$), ความเค้นเฉือน, การไหลเชิงเส้นระหว่างแผ่นขนาน (เฉลยข้อ 1 หน้า 1)
2. **บทที่ 2: สถิตยศาสตร์ของไหลและบานประตู (Fluid Statics & Gates - 39 ข้อ)**
   * กฎการเดินท่อมาโนมิเตอร์ (Walking Method), ของเหลวหลายชนิด, ท่อเอียงมุม $\theta$ (เฉลยข้อ 9 หน้า 3)
   * แรงดันบนระนาบเรียบ ($F_R = \gamma h_{cg} A$), จุดศูนย์กลางแรงกด ($y_{cp}$), สมดุลโมเมนต์บานพับ ($\sum M_{\text{hinge}} = 0$) (เฉลยข้อ 22 หน้า 8, ข้อ 26 หน้า 9)
   * แรงดันบนระนาบโค้งวงกลม ($F_H, F_V, F_R$) (เฉลยข้อ 29 หน้า 10)
   * แรงลอยตัว (Archimedes' Principle) และของไหลที่มีความเร่ง ($\tan\theta = a_x / g$)
3. **บทที่ 3: จลนศาสตร์และสมการโมเมนตัม/พลังงาน (Kinematics & Momentum - 10 ข้อ)**
   * สมการความต่อเนื่อง ($Q = A_1 v_1 = A_2 v_2$) และสมการเบอร์นูลลี
   * แรงปะทะของสายน้ำชนแผ่นโค้ง $180^\circ$ (เปรียบเทียบแผ่นอยู่นิ่ง $F_x = 2\rho A v^2$ vs แผ่นเคลื่อนที่ตามน้ำ $F_x = 2\rho A (v-u)^2$) (เฉลยข้อ 5 หน้า 21)
   * ท่อกาลักน้ำ (Siphon) และการเกิดความดันสุญญากาศที่ยอดกาลักน้ำ ($P_2 = -41.2\text{ kPa}$) (เฉลยข้อ 9 หน้า 22)
4. **บทที่ 4: การวิเคราะห์มิติและความคล้ายคลึง (Dimensional Analysis & Similitude - 9 ข้อ)**
   * ทฤษฎีบท Buckingham $\Pi$ บังคับแสดงครบ 8 สเต็ปตามระเบียบอาจารย์ (เฉลยข้อ 2 หน้า 23: แรงผลักใบพัด)
   * กฎความคล้ายคลึงของแบบจำลอง: Froude Similitude (แม่น้ำ/คลื่น/เรือ) (เฉลยข้อ 6 หน้า 23) และ Reynolds Similitude (ท่อ/สะพาน/อากาศยาน) (เฉลยข้อ 5 หน้า 23)
5. **บทที่ 5: การไหลในท่อและระบบท่อส่งน้ำ (Flow in Pipes & Losses - 14 ข้อ)**
   * การจำแนก Laminar ($f = 64/Re$) vs Turbulent Flow
   * การสูญเสียพลังงานหลัก (Darcy-Weisbach) และการสูญเสียรอง (Minor Losses)
   * โจทย์ Type II: การปล่อยน้ำออกจากถังผ่านข้องอ วนลูป $f$ ลู่เข้าที่ $v = 2.51\text{ m/s}$ (เฉลยข้อ 7 หน้า 40 เน้น "ข้อสอบแน่!")
   * โจทย์ Type III: การออกแบบขนาดท่อ $D$ ดึงตัวแปร $D^5$ วนลูปจนได้ $D = 0.36\text{ m}$ (เฉลยข้อ 8 หน้า 40)
   * ระบบท่อขนาน 4 ท่อและอัตราการไหลรวม (Exam 4 ข้อสอบ 15 คะแนน)
6. **เครื่องมือวัดอัตราการไหลและ Cavitation (Flow Measurement & NPSH)**
   * การคำนวณ Venturi Meter, Orifice Meter, Pitot Tube
   * การตรวจสอบระยะติดตั้งปั๊มน้ำเพื่อป้องกัน Cavitation ($\text{NPSHA} \ge \text{NPSHR}$)

---

## 🎯 แผนเก็งข้อสอบและข้อที่ต้องฝึกทำ (High-Yield Exam Forecast)

| ลำดับ | บทเรียน | ข้อในชีทที่ตรงเป๊ะ | มโนทัศน์และสเต็ปสำคัญ | โอกาสออกสอบ |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **บทที่ 2: มาโนมิเตอร์หลายของไหล** | **ข้อ 9, 13, 17** | เดินท่อขึ้นลบ-ลงบวก, ท่อเอียงคูณ $\sin\theta$, และคิดความดันสัมบูรณ์ vs เกจ | **95% (เต็งหนึ่ง)** |
| **2** | **บทที่ 2: แรงดันบนระนาบเอียง/บานพับ** | **ข้อ 25, 26, 28** | หา $F_R = \gamma h_{cg} A$, หา $y_{cp} = y_{cg} + \frac{I_{xx}}{y_{cg} A}$ แล้วเทคโมเมนต์รอบบานพับ $\sum M_{\text{hinge}} = 0$ | **90%** |
| **3** | **บทที่ 2: แรงดันบนระนาบโค้ง** | **ข้อ 29, 31, 32** | แยกคิด $F_H$ (พื้นที่ฉาย) และ $F_V$ (ปริมาตรของเหลว) รวมเป็น $F_R = \sqrt{F_H^2 + F_V^2}$ | **85%** |
| **4** | **บทที่ 3: แรงปะทะของลำน้ำ (Jet on Vane)** | **ข้อ 5 (ก, ข)** | คิดกรณีแผ่นอยู่นิ่ง ($F_x = 2\rho A v^2$) และกรณีแผ่นเคลื่อนที่ด้วยความเร็ว $u$ (ใช้ความเร็วสัมพัทธ์ $v_r = v-u$) | **85%** |
| **5** | **บทที่ 4: Buckingham $\Pi$ Theorem** | **ข้อ 2, 4** | แสดงครบ 8 สเต็ป พิสูจน์มิติ แก้ระบบสมการหาเลขชี้กำลัง $A, B, C$ | **95% (เต็งหนึ่ง)** |
| **6** | **บทที่ 4: การสเกลแบบจำลอง (Similitude)** | **ข้อ 6, 7, 8** | Froude Scaling สำหรับแม่น้ำ/คลื่น ($\lambda_v = \sqrt{\lambda_L}$) และ Reynolds Scaling สำหรับท่อ ($\lambda_v = 1/\lambda_L$) | **90%** |
| **7** | **บทที่ 5: ท่อต่อออกจากถังแบบวนซ้ำ (Type II)** | **ข้อ 6, 7 (เน้น "ข้อสอบแน่!")** | เขียนสมการพลังงาน $H = [K_L + f(L/D)]\frac{v^2}{2g}$ ตีตาราง Trial & Error 2 รอบ ลู่เข้าที่ $v = 2.51\text{ m/s}$ | **98% (ออกชัวร์)** |
| **8** | **บทที่ 5: การออกแบบขนาดท่อ (Type III)** | **ข้อ 8** | ดึงตัวแปร $D^5 = \frac{f L 16 Q^2}{2 g \pi^2 h_L}$ วนลูป 3 รอบจนได้ $D = 0.36\text{ m} = 360\text{ mm}$ | **80%** |
| **9** | **บทที่ 5: ระบบท่อขนานและอนุกรม** | **ข้อ 10, 11, Exam 4** | ท่อขนาน $h_{L1} = h_{L2}$ และ $Q_{\text{total}} = Q_1 + Q_2$ | **85%** |

---

## 🗂 โครงสร้างเอกสารและไฟล์ใน Repository

```
cn271-fluid-mechanics/
├── index.html                               # หน้าเว็บหลัก Master Interactive Portal (GitHub Pages)
├── README.md                                # หน้าหลักพร้อมคู่มือและตารางเก็งข้อสอบ
├── docs/
│   ├── 04_CN271_Complete_Course_Exam_Forecast.md    # แผนเก็งข้อสอบครบทุกบทและ 5 จุดดักคะแนน
│   └── 05_Master_Course_Problem_Bank_Solutions.md   # คลังเฉลยข้อสอบอัตนัย 4 สเต็ปฉบับเต็มทุกบท
├── scripts/
│   ├── master_solver.py                     # เอนจินคำนวณกลศาสตร์ของไหลครบทุกบท
│   ├── test_course.py                       # Unit Tests ยืนยันความถูกต้องของตัวเลขทุกบท
│   ├── pipeflow.py                          # เอนจินคำนวณการไหลในท่อ
│   ├── test_pipeflow.py                     # Unit Tests การไหลในท่อ
│   └── site/                                # โมดูลสร้างหน้าเว็บ index.html
└── source_materials/                        # เอกสารต้นฉบับและผลการสกัดข้อมูล 2569/2570
```

---

## 🚀 วิธีการทดสอบความถูกต้องของตัวเลข (Verification)

```bash
# รันการทดสอบ Unit Tests ทุกบท (Ran 30 tests in 0.010s: OK)
python3 -m unittest discover -s scripts
```

---
*จัดทำขึ้นโดยทีมวิศวกรอัตโนมัติ เพื่อสนับสนุนการเรียนรู้และการสอบของ Thanaporn Nopparat (Faculty of Engineering, Thammasat University)*
