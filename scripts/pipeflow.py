"""วย 271 บทที่ 5 การไหลในท่อ: ตัวคำนวณที่ใช้ตรวจเลขทุกข้อในเว็บ

ทุกตัวเลขที่ขึ้นในเว็บต้องตรงกับไฟล์นี้ (ดู test_pipeflow.py)
f หาจาก Colebrook-White ซึ่งใกล้เคียงค่าที่อ่านจากชาร์ต Glasgow/Moody
(ในห้องสอบอ่านชาร์ตได้ละเอียดแค่ ~3 หลัก จึงคลาดเคลื่อนได้เล็กน้อย)
"""
from __future__ import annotations

import math
from dataclasses import dataclass

G = 9.81
GAMMA = 9810.0  # N/m^3 (น้ำ)
NU = 1.0e-6  # m^2/s (น้ำ)


def area(d: float) -> float:
    return math.pi * d * d / 4.0


def friction_factor(re: float, rel_rough: float) -> float:
    """Darcy f: laminar 64/Re, otherwise Colebrook-White (iterate)."""
    if re < 2000.0:
        return 64.0 / re
    f = 0.02
    for _ in range(300):
        f_new = (-2.0 * math.log10(rel_rough / 3.7 + 2.51 / (re * math.sqrt(f)))) ** -2
        if abs(f_new - f) < 1e-12:
            return f_new
        f = f_new
    return f


def reynolds(v: float, d: float, nu: float = NU) -> float:
    return v * d / nu


def hf(f: float, length: float, d: float, v: float) -> float:
    return f * length / d * v * v / (2 * G)


def v_from_head(h: float, d: float, length: float, eps: float, k_sum: float = 0.0,
                exit_head: float = 0.0, nu: float = NU):
    """Type 2: หา v จาก h = (exit_head + k_sum + f L/D) v^2/2g  (วนหา f)"""
    f = 0.02
    v = 0.0
    for _ in range(300):
        v = math.sqrt(2 * G * h / (exit_head + k_sum + f * length / d))
        f_new = friction_factor(reynolds(v, d, nu), eps / d)
        if abs(f_new - f) < 1e-12:
            f = f_new
            break
        f = f_new
    return v, f


def d_from_q(q: float, h: float, length: float, eps: float, nu: float = NU):
    """Type 3: หา D จาก Q และ hf (ไม่มี minor loss)  D = (8 f L Q^2 / (pi^2 g h))^(1/5)"""
    f = 0.02
    d = 0.5
    for _ in range(300):
        d = (8 * f * length * q * q / (math.pi ** 2 * G * h)) ** 0.2
        v = q / area(d)
        f_new = friction_factor(reynolds(v, d, nu), eps / d)
        if abs(f_new - f) < 1e-12:
            f = f_new
            break
        f = f_new
    return d, f


# ---------------------------------------------------------------- Q1-Q8
def q1():
    d, v, mu, rho = 0.1, 0.1, 1e-3, 1000.0
    re = rho * v * d / mu
    v_lam = 2000 * mu / (rho * d)
    return {"Re": re, "turbulent": re > 4000, "v_lam_max": v_lam}


def q2():
    rho, mu, d = 1000.0, 1e-3, 0.08
    re_a = rho * 0.02 * d / mu
    f_a = 64 / re_a
    dp_b = f_a * 0.5 / d * rho * 0.02 ** 2 / 2
    re_c = rho * 1.0 * d / mu
    f_c = friction_factor(re_c, 0.12e-3 / d)
    dp_c = f_c * 0.1 / d * rho * 1.0 ** 2 / 2
    return {"Re_a": re_a, "f_a": f_a, "dp_b": dp_b, "Re_c": re_c, "f_c": f_c, "dp_c": dp_c}


def q3():
    q = 0.1
    v = [q / area(d) for d in (0.1, 0.2, 0.3)]
    head = lambda p, vv, z: p / GAMMA + vv * vv / (2 * G) + z
    h = [head(100e3, v[0], 0), head(50e3, v[1], 3), head(20e3, v[2], 1)]
    return {"v": v, "H": h, "hL12": h[0] - h[1], "hL23": h[1] - h[2]}


def q4():
    q, d, length, eps = 0.1, 0.2, 600.0, 0.4e-3
    v = q / area(d)
    re = reynolds(v, d)
    f = friction_factor(re, eps / d)
    return {"v": v, "Re": re, "f": f, "hf": hf(f, length, d, v),
            "hf_chart": hf(0.024, length, d, v), "hm": 1.0 * v * v / (2 * G)}


def q5():
    d, v, length, eps = 0.6, 2.0, 120.0, 3e-3
    re = reynolds(v, d)
    f = friction_factor(re, eps / d)
    h_major = hf(f, length, d, v)
    h_minor = 0.6 * v * v / (2 * G)
    head1 = 10e3 / GAMMA + 20 + h_major + h_minor
    return {"Re": re, "f": f, "hf": h_major, "hm": h_minor, "P1_kPa": head1 * GAMMA / 1e3}


def q6():
    v, f = v_from_head(3.0, 0.15, 700.0, 0.12e-3)
    return {"v": v, "f": f}


def q7():
    v, f = v_from_head(15 - 10, 0.15, 100.0, 0.12e-3, k_sum=1.0 + 0.3 + 0.3, exit_head=1.0)
    return {"v": v, "f": f, "Re": reynolds(v, 0.15)}


def q8():
    d, f = d_from_q(0.5, 10.0, 200.0, 0.12e-3)
    return {"D": d, "f": f, "v": 0.5 / area(d)}


# ------------------------------------------------- ข้อสอบ 15 คะแนน (A, B)
def exam_a():
    """3 ท่ออนุกรมวางเอียง 5 องศา, PA-PB = 245.25 kPa; K12=0.15 (ขยาย), K23=0.35 (หด) จากชาร์ต"""
    d = [0.4, 0.5, 0.3]
    length = [80.0, 120.0, 80.0]
    eps = [0.08e-3, 0.15e-3, 0.12e-3]
    z_b = sum(length) * math.sin(math.radians(5))
    head = 245.25e3 / GAMMA - z_b
    v1 = 1.0
    f = [0.02] * 3
    v = [v1, 0, 0]
    for _ in range(300):
        v = [v1, v1 * (d[0] / d[1]) ** 2, v1 * (d[0] / d[2]) ** 2]
        f = [friction_factor(reynolds(v[i], d[i]), eps[i] / d[i]) for i in range(3)]
        total = ((v[2] ** 2 - v[0] ** 2) + sum(f[i] * length[i] / d[i] * v[i] ** 2 for i in range(3))
                 + 0.15 * v[0] ** 2 + 0.35 * v[2] ** 2) / (2 * G)
        v1 *= math.sqrt(head / total)
    return {"zB": z_b, "H": head, "v": v, "f": f, "Q": v[0] * area(d[0])}


def _v_for_head(h, d, length, eps):
    return v_from_head(h, d, length, eps)


def exam_b():
    """ท่อ 4 เส้น: 2 กับ 3 ขนาน; ท่อ 4 ผ่านจุด A-B ยาว 300 จาก 1000 m"""
    h_ab = (910e3 - 811.41e3) / GAMMA - 10.0  # = 0.05 m
    h4 = h_ab * 1000.0 / 300.0
    v3, f3 = _v_for_head(0.42, 0.6, 800.0, 0.48e-3)
    v2, f2 = _v_for_head(0.42, 0.8, 800.0, 0.32e-3)
    q = v3 * area(0.6) + v2 * area(0.8)
    v1 = q / area(0.9)
    f1 = friction_factor(reynolds(v1, 0.9), 0.9e-3 / 0.9)
    h1 = hf(f1, 900.0, 0.9, v1)
    return {"h_ab": h_ab, "h4": h4, "v2": v2, "f2": f2, "v3": v3, "f3": f3, "Q": q,
            "v1": v1, "f1": f1, "h1": h1, "total": h1 + 0.42 + h4}


# --------------------------------------------------------- เสริม Q9-Q13
def q9(k12=0.2, k23=0.28):
    d = [0.08, 0.06, 0.04]
    length = [100.0, 200.0, 50.0]
    eps = [0.24e-3, 0.12e-3, 0.20e-3]
    v2 = 1.0
    v, f = [0, 0, 0], [0.02] * 3
    for _ in range(300):
        v = [v2 * area(d[1]) / area(d[0]), v2, v2 * area(d[1]) / area(d[2])]
        f = [friction_factor(reynolds(v[i], d[i]), eps[i] / d[i]) for i in range(3)]
        total = (sum(f[i] * length[i] / d[i] * v[i] ** 2 for i in range(3))
                 + k12 * v[1] ** 2 + k23 * v[2] ** 2) / (2 * G)
        v2 *= math.sqrt(25.0 / total)
    return {"v": v, "f": f, "Q": v[0] * area(d[0])}


def q10():
    d = [0.08, 0.06, 0.04]
    length = [100.0, 200.0, 50.0]
    eps = [0.24e-3, 0.12e-3, 0.20e-3]
    out = [v_from_head(15.0, d[i], length[i], eps[i]) for i in range(3)]
    q = [out[i][0] * area(d[i]) for i in range(3)]
    return {"v": [o[0] for o in out], "f": [o[1] for o in out], "Q": q, "Qtot": sum(q)}


def q12(include_expansion=True):
    l1, d1, e1, l2, d2, e2 = 60.0, 0.4, 0.6e-3, 40.0, 0.8, 0.64e-3
    k_exp = (1 - (d1 / d2) ** 2) ** 2 if include_expansion else 0.0
    v1 = 3.0
    for _ in range(500):
        v2 = v1 * (d1 / d2) ** 2
        f1 = friction_factor(reynolds(v1, d1), e1 / d1)
        f2 = friction_factor(reynolds(v2, d2), e2 / d2)
        total = (v2 ** 2 + f1 * l1 / d1 * v1 ** 2 + f2 * l2 / d2 * v2 ** 2 + (0.8 + k_exp) * v1 ** 2) / (2 * G)
        v1 *= math.sqrt((34.5 - 60 * math.sin(math.radians(30))) / total)
    return {"v1": v1, "v2": v2, "f1": f1, "f2": f2, "Q": v1 * area(d1), "K_exp": k_exp}


def q13():
    v2, d2 = 0.2, 0.4
    f2 = friction_factor(reynolds(v2, d2), 0.0015)
    h2 = hf(f2, 1000.0, d2, v2)
    v3, f3 = v_from_head(h2, 0.8, 1000.0, 0.002 * 0.8)
    q2, q3 = v2 * area(d2), v3 * area(0.8)
    q = q2 + q3
    v1 = q / area(0.6)
    f1 = friction_factor(reynolds(v1, 0.6), 0.002)
    h1 = hf(f1, 1000.0, 0.6, v1)
    h4 = 5.0 - h1 - h2
    d4, f4 = d_from_q(q, h4, 1000.0, 0.1e-3)
    return {"f2": f2, "h2": h2, "v3": v3, "f3": f3, "Q2": q2, "Q3": q3, "Q": q,
            "v1": v1, "f1": f1, "h1": h1, "h4": h4, "D4": d4, "f4": f4}


def fully_rough_table():
    """ค่า f ที่ Re สูงมาก (เริ่มสมมุติรอบแรกของ Type 2/3)"""
    return {rr: friction_factor(1e9, rr) for rr in
            (0.0002, 0.0003, 0.0004, 0.0005, 0.0008, 0.001, 0.0015, 0.002, 0.003, 0.005, 0.01)}


if __name__ == "__main__":
    import pprint
    for name in ("q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "exam_a", "exam_b",
                 "q9", "q10", "q12", "q13"):
        print("==", name)
        pprint.pprint(globals()[name]())
    print("== fully rough f")
    pprint.pprint(fully_rough_table())
