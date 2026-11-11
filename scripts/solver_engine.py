"""
CN271 Fluid Mechanics - Complete Problems 1 to 8 Solver Engine
Faculty of Engineering, Thammasat University
"""

import math
from typing import Dict, Any

G = 9.81
RHO_WATER = 1000.0
GAMMA_WATER = 9810.0
NU_WATER = 1.0e-6


def calc_friction_factor(Re: float, relative_roughness: float, max_iter: int = 50, tol: float = 1e-8) -> float:
    """Computes Darcy friction factor using Colebrook-White."""
    if Re <= 2000.0:
        return 64.0 / max(Re, 1e-5)
    f = 0.25 / (math.log10(relative_roughness / 3.7 + 5.74 / (Re ** 0.9))) ** 2
    for _ in range(max_iter):
        rhs = -2.0 * math.log10(relative_roughness / 3.7 + 2.51 / (Re * math.sqrt(f)))
        f_next = (1.0 / rhs) ** 2
        if abs(f_next - f) < tol:
            return f_next
        f = f_next
    return f


def solve_problem_1() -> Dict[str, Any]:
    """Problem 1 (Ex 1): D = 0.1 m, v = 0.1 m/s, mu = 1e-3, rho = 1000."""
    D = 0.1
    v = 0.1
    mu = 1e-3
    rho = 1000.0
    Re = (rho * v * D) / mu  # 10,000
    is_turbulent = Re > 2000.0
    v_max_laminar = (2000.0 * mu) / (rho * D)  # 0.02 m/s
    return {"Re": Re, "is_turbulent": is_turbulent, "v_max_laminar": v_max_laminar}


def solve_problem_2() -> Dict[str, Any]:
    """Problem 2 (Ex 2): D = 0.08 m, v = 0.02 m/s, mu = 1e-3, rho = 1000."""
    D = 0.08
    v = 0.02
    mu = 1e-3
    rho = 1000.0
    Re = (rho * v * D) / mu  # 1,600
    is_laminar = Re <= 2000.0
    f_laminar = 64.0 / Re  # 0.04
    L_b = 0.5
    dp_b = f_laminar * (L_b / D) * (rho * (v ** 2) / 2.0)  # 0.05 Pa
    
    # Part c: plastic pipe eps = 0.12 mm, L = 0.1 m, v = 1 m/s
    v_c = 1.0
    L_c = 0.1
    eps = 0.12e-3
    Re_c = (rho * v_c * D) / mu  # 80,000
    kd_c = eps / D  # 0.0015
    f_c = 0.024  # from Moody
    dp_c = f_c * (L_c / D) * (rho * (v_c ** 2) / 2.0)  # 15 Pa
    return {
        "Re": Re, "is_laminar": is_laminar, "f_laminar": f_laminar, "dp_b": dp_b,
        "Re_c": Re_c, "kd_c": kd_c, "f_c": f_c, "dp_c": dp_c
    }


def solve_problem_3() -> Dict[str, Any]:
    """
    Problem 3 (Ex 3): Q = 0.1 m^3/s.
    Point 1: D1 = 0.1 m, P1 = 100 kPa, z1 = 0 m
    Point 2: D2 = 0.2 m, P2 = 50 kPa, z2 = 3 m
    Point 3: D3 = 0.3 m, P3 = 20 kPa, z3 = 1 m
    """
    Q = 0.1
    v1 = Q / (math.pi * (0.1 ** 2) / 4.0)  # 12.73 m/s
    v2 = Q / (math.pi * (0.2 ** 2) / 4.0)  # 3.18 m/s
    v3 = Q / (math.pi * (0.3 ** 2) / 4.0)  # 1.41 m/s
    
    H1 = (100.0e3 / GAMMA_WATER) + (v1 ** 2 / (2 * G)) + 0.0
    H2 = (50.0e3 / GAMMA_WATER) + (v2 ** 2 / (2 * G)) + 3.0
    H3 = (20.0e3 / GAMMA_WATER) + (v3 ** 2 / (2 * G)) + 1.0
    
    hL_12 = H1 - H2  # 9.84 m
    hL_23 = H2 - H3  # 5.47 m
    return {
        "v1": v1, "v2": v2, "v3": v3,
        "H1": H1, "H2": H2, "H3": H3,
        "hL_12": hL_12, "hL_23": hL_23
    }


def solve_problem_4() -> Dict[str, Any]:
    """
    Problem 4: Q = 0.1 m^3/s, D = 0.2 m, L = 600 m, eps = 0.4 mm, mu = 1e-3.
    Two elbows K_L = 0.5 each.
    """
    Q = 0.1
    D = 0.2
    L = 600.0
    eps = 0.4e-3
    v = Q / (math.pi * (D ** 2) / 4.0)  # 3.183 m/s
    v_head = (v ** 2) / (2.0 * G)  # 0.5165 m
    Re = v * D / NU_WATER  # 6.37e5
    kd = eps / D  # 0.0020
    f = calc_friction_factor(Re, kd)  # ~0.0237
    hf = f * (L / D) * v_head  # 36.74 m
    hm = (0.5 + 0.5) * v_head  # 0.52 m
    hL = hf + hm  # 37.25 m
    return {"v": v, "v_head": v_head, "Re": Re, "kd": kd, "f": f, "hf": hf, "hm": hm, "hL": hL}


def solve_problem_5() -> Dict[str, Any]:
    """
    Problem 5: D = 0.6 m, v = 2.0 m/s, P2 >= 10 kPa, L = 120 m, eps = 3 mm, dz = 20 m.
    Two elbows K_L = 0.3 each. Find min P1.
    """
    D = 0.6
    v = 2.0
    v_head = (v ** 2) / (2.0 * G)  # 0.2039 m
    L = 120.0
    eps = 3.0e-3
    dz = 20.0
    P2 = 10.0e3
    Re = v * D / NU_WATER  # 1.20e6
    kd = eps / D  # 0.0050
    f = calc_friction_factor(Re, kd)  # ~0.0304
    hf = f * (L / D) * v_head  # 1.24 m
    hm = (0.3 + 0.3) * v_head  # 0.12 m
    hL = hf + hm  # 1.36 m
    P1_head = (P2 / GAMMA_WATER) + dz + hL  # 22.38 m
    P1 = P1_head * GAMMA_WATER  # 219.58 kPa
    return {"v": v, "Re": Re, "kd": kd, "f": f, "hf": hf, "hm": hm, "hL": hL, "P1_head": P1_head, "P1_kPa": P1 / 1000.0}


def solve_problem_6_velocity() -> Dict[str, Any]:
    """Problem 6: L = 700 m, hL = 3 m, D = 0.15 m, eps = 0.12 mm."""
    L = 700.0
    hL = 3.0
    D = 0.15
    eps = 0.12e-3
    kd = eps / D  # 0.0008
    f = 0.021
    v = math.sqrt((2 * G * hL * D) / (f * L))
    Re = v * D / NU_WATER
    return {"f": f, "v": v, "Re": Re, "kd": kd}


def solve_problem_7_tank_rising() -> Dict[str, Any]:
    """
    Problem 7 (Exam Star!):
    Tank depth = 15 m. Pipe rises by 10 m to open air discharge.
    L = 100 m, D = 0.15 m, eps = 0.12 mm (kd = 0.0008).
    Minor loss: entrance K = 1.0, two elbows K = 0.3 each (sum K = 1.6).
    5 = [2.6 + f * (100/0.15)] * v^2 / 2g
    """
    L, D, eps = 100.0, 0.15, 0.12e-3
    kd = eps / D
    f = 0.0195
    bracket = 2.6 + f * (L / D)
    v = math.sqrt(2 * G * 5.0 / bracket)
    Re = v * D / NU_WATER
    Q = v * (math.pi * D**2 / 4.0)
    return {"f": f, "bracket": bracket, "v": v, "Re": Re, "Q": Q}


def solve_problem_8_sizing() -> Dict[str, Any]:
    """
    Problem 8: Q = 0.5 m^3/s, eps = 0.12 mm, L = 200 m, hL = 10 m.
    v = 2 / (pi * D^2) -> v^2 = 4 / (pi^2 * D^4)
    hL = 10 = f * (200 / D) * (4 / (2g * pi^2 * D^4)) = f * 800 / (D^5 * 2g * pi^2)
    D^5 = (f * 200 * 4) / (10 * 2g * pi^2)
    """
    Q, eps, L, hL = 0.5, 0.12e-3, 200.0, 10.0
    f = 0.0155
    D = ((f * L * 4.0) / (hL * 2.0 * G * (math.pi ** 2))) ** 0.2
    v = Q / (math.pi * (D ** 2) / 4.0)
    Re = v * D / NU_WATER
    kd = eps / D
    return {"f": f, "D": D, "v": v, "Re": Re, "kd": kd}
