"""ทดสอบว่าตัวเลขที่ใช้ในเว็บตรงกับการคำนวณ Colebrook-White

รัน:  python3 -m unittest discover -s scripts
"""
import re
import unittest
from pathlib import Path

import pipeflow as p

ROOT = Path(__file__).resolve().parent.parent


class Main(unittest.TestCase):
    def test_q1(self):
        r = p.q1()
        self.assertEqual(r["Re"], 10000)
        self.assertAlmostEqual(r["v_lam_max"], 0.02)

    def test_q2(self):
        r = p.q2()
        self.assertEqual(r["Re_a"], 1600)
        self.assertAlmostEqual(r["dp_b"], 0.05)
        self.assertAlmostEqual(r["dp_c"], 15.0, delta=0.5)

    def test_q3(self):
        r = p.q3()
        self.assertAlmostEqual(r["hL12"], 9.84, places=2)
        self.assertAlmostEqual(r["hL23"], 5.47, places=2)

    def test_q4(self):
        r = p.q4()
        self.assertAlmostEqual(r["hf"], 36.7, delta=0.1)
        self.assertAlmostEqual(r["hm"], 0.52, places=2)

    def test_q5(self):
        self.assertAlmostEqual(p.q5()["P1_kPa"], 219.6, delta=0.1)

    def test_q6(self):
        self.assertAlmostEqual(p.q6()["v"], 0.77, places=2)

    def test_q7(self):
        self.assertAlmostEqual(p.q7()["v"], 2.51, places=2)

    def test_q8(self):
        self.assertAlmostEqual(p.q8()["D"], 0.365, places=3)


class Exam(unittest.TestCase):
    def test_a(self):
        r = p.exam_a()
        self.assertAlmostEqual(r["v"][0], 0.713, places=3)
        self.assertAlmostEqual(r["v"][1], 0.457, places=3)
        self.assertAlmostEqual(r["v"][2], 1.268, places=3)

    def test_b(self):
        r = p.exam_b()
        self.assertAlmostEqual(r["h_ab"], 0.05, places=2)
        self.assertAlmostEqual(r["total"], 1.24, places=2)


class Extra(unittest.TestCase):
    def test_q9_matches_board(self):
        r = p.q9()
        # กระดานอาจารย์: v1=0.73, v2=1.29, v3=2.90, Q=3.67e-3 (อ่าน f จากชาร์ต)
        self.assertAlmostEqual(r["v"][0], 0.73, delta=0.01)
        self.assertAlmostEqual(r["v"][1], 1.29, delta=0.01)
        self.assertAlmostEqual(r["v"][2], 2.90, delta=0.02)
        self.assertAlmostEqual(r["Q"], 3.67e-3, delta=0.05e-3)

    def test_q10(self):
        self.assertAlmostEqual(p.q10()["Qtot"], 0.0237, places=4)

    def test_q12(self):
        self.assertAlmostEqual(p.q12()["Q"], 0.541, places=3)

    def test_q13(self):
        r = p.q13()
        self.assertAlmostEqual(r["D4"], 0.388, places=3)
        self.assertAlmostEqual(r["h4"], 4.17, places=2)


class FrictionFactor(unittest.TestCase):
    def test_laminar(self):
        self.assertAlmostEqual(p.friction_factor(1600, 0.001), 0.04)

    def test_matches_moody_reading(self):
        # ค่าที่อ่านจากชาร์ตในไฟล์ของอาจารย์ (Q6/Q7/Q8)
        self.assertAlmostEqual(p.friction_factor(1.2e5, 0.0008), 0.021, delta=0.001)
        self.assertAlmostEqual(p.friction_factor(3.7e5, 0.0008), 0.0195, delta=0.0006)
        self.assertAlmostEqual(p.friction_factor(1.77e6, 0.00033), 0.0155, delta=0.0006)


class SiteMatchesSolver(unittest.TestCase):
    """คำตอบสุดท้ายที่พิมพ์ในหน้าเว็บ (index.html) ต้องเป็นค่าเดียวกับตัวคำนวณ"""

    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_answers_present(self):
        for needle in ("0.77", "2.51", "0.36", "219.6", "9.84", "5.47", "36.7",
                       "0.713", "1.24", "3.64", "0.0149", "0.0237", "0.54", "0.388"):
            self.assertIn(needle, self.text, needle)

    def test_all_pages_present(self):
        for pid in ("sum", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "ea", "eb",
                    "q9", "q10", "q11", "q12", "q13", "calc", "ref"):
            self.assertIn('<section id="%s">' % pid, self.text, pid)

    def test_each_problem_has_exam_and_detail(self):
        for pid in ("q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "ea", "eb",
                    "q9", "q10", "q11", "q12", "q13"):
            part = self.text.split('<section id="%s">' % pid, 1)[1].split("</section>", 1)[0]
            self.assertIn('class="exam"', part, pid)
            self.assertIn('class="detail"', part, pid)

    def test_no_katex_breaking_unicode(self):
        # จุดกลาง (·) ใน \text{...} ทำให้ KaTeX ขึ้นตัวแดง \cdotp
        self.assertEqual(re.findall(r"\\text\{[^}]*\u00b7[^}]*\}", self.text), [])

    def test_removed_unverified_problems(self):
        self.assertNotIn("105.13", self.text)
        self.assertNotIn("1,500", self.text)


if __name__ == "__main__":
    unittest.main()
