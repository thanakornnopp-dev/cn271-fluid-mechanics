"""
CN271 Fluid Mechanics - Comprehensive Exam Solver Engine
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


def solve_submarine_model() -> Dict[str, float]:
    """
    Submarine Model Testing:
    Prototype: v_p = 8 m/s, rho_p = 1036 kg/m^3, mu_p = 0.0012 N s/m^2. Scale = 1:100 (D_p/D_m = 100).
    Model: rho_m = 1000 kg/m^3, mu_m = 0.001 N s/m^2. Drag force on model F_m = 200 N.
    Find v_m and prototype drag F_p.
    """
    v_p = 8.0
    scale_ratio = 100.0  # D_p / D_m
    rho_p, mu_p = 1036.0, 0.0012
    rho_m, mu_m = 1000.0, 0.0010
    v_m = v_p * scale_ratio * (rho_p / rho_m) * (mu_m / mu_p)
    
    F_m = 200.0
    F_p = F_m * (rho_p / rho_m) * ((v_p / v_m) ** 2) * (scale_ratio ** 2)
    return {"v_m": v_m, "F_p": F_p}


def solve_example_1() -> Dict[str, Any]:
    """Ex 1: D = 0.1 m, v = 0.1 m/s, mu = 1e-3, rho = 1000."""
    D = 0.1
    v = 0.1
    mu = 1e-3
    rho = 1000.0
    Re = (rho * v * D) / mu  # 10,000
    is_turbulent = Re > 2000.0
    v_max_laminar = (2000.0 * mu) / (rho * D)  # 0.02 m/s
    return {"Re": Re, "is_turbulent": is_turbulent, "v_max_laminar": v_max_laminar}


def solve_example_2() -> Dict[str, Any]:
    """Ex 2: D = 0.08 m, v = 0.02 m/s, mu = 1e-3, rho = 1000."""
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


def solve_example_3() -> Dict[str, Any]:
    """
    Ex 3: Q = 0.1 m^3/s.
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


def solve_problem_9_series_horizontal() -> Dict[str, Any]:
    """
    Problem 9: Three pipes in series horizontal. hL = 25 m.
    Pipe 1: L1=100 m, D1=0.08 m, eps1=0.24 mm
    Pipe 2: L2=200 m, D2=0.06 m, eps2=0.12 mm
    Pipe 3: L3=50 m, D3=0.04 m, eps3=0.20 mm
    """
    f1, f2, f3 = 0.028, 0.0255, 0.031
    bracket = (
        f1 * (100.0 * (0.5625 ** 2) / 0.08)
        + f2 * (200.0 / 0.06)
        + f3 * (50.0 * (2.25 ** 2) / 0.04)
        + 0.24
        + 0.27 * (2.25 ** 2)
    )
    v2 = math.sqrt(2 * G * 25.0 / bracket)  # 1.29 m/s
    v1 = 0.5625 * v2  # 0.73 m/s
    v3 = 2.25 * v2  # 2.91 m/s
    Q = v2 * math.pi * (0.06 ** 2) / 4.0  # 3.65e-3 m^3/s
    Re1 = v1 * 0.08 / NU_WATER
    Re2 = v2 * 0.06 / NU_WATER
    Re3 = v3 * 0.04 / NU_WATER
    return {
        "f1": f1, "f2": f2, "f3": f3,
        "bracket": bracket,
        "v1": v1, "v2": v2, "v3": v3,
        "Q": Q,
        "Re1": Re1, "Re2": Re2, "Re3": Re3
    }
