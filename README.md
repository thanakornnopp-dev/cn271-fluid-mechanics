# 🌊 CN271 Fluid Mechanics: Pipe Flow Exam Preparation & Solutions
> **Thammasat University — Faculty of Engineering**  
> Civil & Mechanical Engineering Core Curriculum  
> Author: Thanaporn Nopparat & AI Engineering Squad (Commander Chokie)

[![Live Web Portal](https://img.shields.io/badge/🌐_Live_Web_Portal-Click_Here_to_Open-blue?style=for-the-badge&logo=google-chrome)](https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/)
[![Quality Gate](https://img.shields.io/badge/Inspector_QC-PASSED_(6%2F6_Tests)-emerald?style=for-the-badge)](https://github.com/thanakornnopp-dev/cn271-fluid-mechanics)

---

### 🌐 ลิงก์เข้าใช้งานหน้าเว็บสรุปสูตร & เครื่องคิดเลขจำลอง (Live Interactive Website):
👉 **[https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/](https://thanakornnopp-dev.github.io/cn271-fluid-mechanics/)**  
*(หน้าเว็บพร้อมใช้งานทันที มีสูตร LaTeX ครบถ้วน, คู่มืออ่านชาร์ต Glasgow, เฉลยข้อสอบ 4 ข้อแบบละเอียด และเครื่องคิดเลขจำลองการไหลวนลูป Trial & Error อัตโนมัติ)*

---

## 📌 Repository Overview (ภาพรวมคลังเอกสารและโค้ด)

คลังนี้จัดทำขึ้นเป็นพิเศษเพื่อเตรียมตัวสอบวิชา **CN271 Fluid Mechanics (กลศาสตร์ของไหล)** ในหัวข้อ **Flow in Closed Conduits / Pipe Networks (การไหลในท่อและโครงข่ายท่อ)** โดยรวบรวม:
1. **สูตร First Principles และ Step-by-Step Algorithms** ครบทุกรูปแบบโจทย์ (หา $h_f$, หา $Q/v$, หาขนาดท่อ $D$, ท่ออนุกรมเอียง, ท่อขนาน)
2. **เฉลยข้อสอบจริงฉบับเต็มบรรทัดต่อบรรทัด** ตามวิธีเขียนและรูปแบบที่อาจารย์ผู้สอนต้องการในห้องสอบ
3. **Python Solver & Verification Engine** สำหรับคำนวณและตรวจสอบตัวเลขด้วยสมการ Colebrook-White และ Darcy-Weisbach 100%
4. **Unit Test Suite** ตรวจสอบสมดุลพลังงานและความต่อเนื่อง (Conservation of Mass & Energy)

---

## 🗂 โครงสร้างไฟล์ใน Repository (Directory Structure)

```
cn271-fluid-mechanics/
├── index.html                               # หน้าเว็บหลัก Live Portal (GitHub Pages)
├── README.md                                # หน้าหลักพร้อมลิงก์เว็บและคำอธิบาย
├── docs/
│   ├── 01_CN271_Exam_Mastery_Guide.md       # สรุปทฤษฎี สเต็ปการทำ และจุดดักคะแนนข้อสอบ
│   ├── 02_Instructor_Exam_Solutions_Step_by_Step.md # เฉลยข้อสอบลายมืออาจารย์ฉบับสมบูรณ์
│   └── interactive_portal.html              # ไฟล์ต้นฉบับเว็บพอร์ทัล
├── scripts/
│   ├── solver_engine.py                     # เอนจินคำนวณและวนลูป Trial & Error อัตโนมัติ
│   └── test_solver.py                       # สคริปต์ Unit Test ยืนยันความถูกต้องของตัวเลข
└── solve_all.py                             # สคริปต์รันคำนวณสรุปโจทย์ทั้งหมด
```

---

## 🚀 วิธีการรันสคริปต์คำนวณ (How to Run)

### 1. รันเอนจินคำนวณโจทย์ข้อสอบทั้งหมด:
```bash
python3 scripts/solver_engine.py
```

### 2. รันการทดสอบ Unit Test (Verification Gates):
```bash
python3 -m unittest discover -s scripts
```

---

## 📊 ตารางสรุปผลลัพธ์ข้อสอบ (Summary of Exam Results)

| ข้อสอบ | หัวข้อโจทย์ | ข้อมูลตั้งต้น | คำตอบสุดท้าย | หน่วย |
| :---: | :--- | :--- | :--- | :---: |
| **1** | ท่ออนุกรม 3 ท่อน วางเอียง $\theta = 5^\circ$ พร้อม Expansion & Contraction | $\Delta P = 245.25\text{ kPa}, \nu = 10^{-6}$ | $v_1 = 0.713, v_2 = 0.456, v_3 = 1.269$ | $\text{m/s}$ |
| **2** | ท่อขนาดสม่ำเสมอปล่อยสู่อากาศ สูงขึ้น $10\text{ m}$ ($L=1500\text{ m}$) | $Q = 0.14\text{ m}^3\text{/s}, P_1 = 105.13\text{ kPa}$ | $D = 0.60\text{ m} \quad (598\text{ mm})$ | $\text{m}$ |
| **3** | ถังขนาดใหญ่ 2 ถัง เชื่อมด้วยท่อเอียง $12^\circ$ ($L=120\text{ m}$) | $Q = 12\text{ m}^3\text{/s}, h_f = 3.55\text{ m}$ | $D = 1.44\text{ m} \quad (1439\text{ mm})$ | $\text{m}$ |
| **4** | โครงข่ายท่ออนุกรม-ขนาน 4 ท่อน (15 คะแนน) | $h_3 = 0.42\text{ m}, P_A = 910, P_B = 811.41\text{ kPa}$ | $h_{AA \to BB} = 1.24\text{ m}$ | $\text{m}$ |
