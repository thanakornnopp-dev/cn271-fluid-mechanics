"""
CN271 Fluid Mechanics - Pipe Flow Solver Engine
Faculty of Engineering, Thammasat University

Includes rigorous solvers for:
1. Colebrook-White friction factor calculation.
2. Problem 1: Three inclined pipes in series with sudden expansion & contraction.
3. Problem 2: Pipe sizing (diameter determination) with elevation difference and open outlet.
4. Problem 3: Two large reservoirs connected by inclined pipe without minor loss.
5. Problem 4: Series-parallel pipe network with known head loss on one parallel branch.
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any

# Standard physical constants
G = 9.81  # Gravitational acceleration (m/s^2)
RHO_WATER = 1000.0  # Density of water at standard conditions (kg/m^3)
GAMMA_WATER = RHO_WATER * G  # Specific weight of water (N/m^3 = 9810 N/m^3)
NU_WATER = 1.0e-6  # Kinematic viscosity of water (m^2/s)


def calc_friction_factor(Re: float, relative_roughness: float, max_iter: int = 50, tol: float = 1e-8) -> float:
    """
    Computes Darcy friction factor 'f' using Colebrook-White equation.
    For laminar flow (Re <= 2000): f = 64 / Re.
    For turbulent flow: 1 / sqrt(f) = -2 * log10( (k/D)/3.7 + 2.51 / (Re * sqrt(f)) )
    """
    if Re <= 2000.0:
        return 64.0 / max(Re, 1e-5)
    
    # Swamee-Jain explicit approximation as initial guess
    f = 0.25 / (math.log10(relative_roughness / 3.7 + 5.74 / (Re ** 0.9))) ** 2
    
    for _ in range(max_iter):
        rhs = -2.0 * math.log10(relative_roughness / 3.7 + 2.51 / (Re * math.sqrt(f)))
        f_next = (1.0 / rhs) ** 2
        if abs(f_next - f) < tol:
            return f_next
        f = f_next
    return f


@dataclass
class PipeSeriesResult:
    iterations: List[Dict[str, Any]]
    v1: float
    v2: float
    v3: float
    Q: float
    Re1: float
    Re2: float
    Re3: float
    f1: float
    f2: float
    f3: float
    hf_total: float
    hm_total: float


def solve_problem_1_series_incline() -> PipeSeriesResult:
    """
    Problem 1 (Exam):
    Three pipes connected in series at incline angle theta = 5 deg.
    PA - PB = 245.25 kPa. Kinematic viscosity nu = 1e-6 m^2/s.
    Pipe 1: D=0.4 m, L=80 m, eps=0.08 mm -> k/D = 0.0002
    Pipe 2: D=0.5 m, L=120 m, eps=0.15 mm -> k/D = 0.0003
    Pipe 3: D=0.3 m, L=80 m, eps=0.12 mm -> k/D = 0.0004
    Sudden expansion (1->2): A1/A2 = (0.4/0.5)^2 = 0.64 -> K_12 = 0.15
    Sudden contraction (2->3): A3/A2 = (0.3/0.5)^2 = 0.36 -> K_23 = 0.35
    """
    L1, D1, eps1 = 80.0, 0.4, 0.08e-3
    L2, D2, eps2 = 120.0, 0.5, 0.15e-3
    L3, D3, eps3 = 80.0, 0.3, 0.12e-3
    theta_deg = 5.0
    L_total = L1 + L2 + L3
    z_B = L_total * math.sin(math.radians(theta_deg))  # 24.40 m
    
    delta_P = 245.25e3  # Pa
    head_P = delta_P / GAMMA_WATER  # 25.00 m
    net_driving_head = head_P - z_B  # 0.60 m
    
    c2 = (D1 / D2) ** 2  # 0.64
    c3 = 1.78  # Teacher approximation (D1/D3)^2 = 1.7778 -> 1.78
    
    K12 = 0.15
    K23 = 0.35
    
    kd1 = eps1 / D1
    kd2 = eps2 / D2
    kd3 = eps3 / D3
    
    # Fully turbulent initial guesses from Glasgow chart
    f1, f2, f3 = 0.014, 0.015, 0.016
    
    iters = []
    v1 = 0.0
    for it in range(1, 10):
        # Bracket coeff multiplying v1^2 / (2g)
        # [ (1.78^2 - 1) + f1*(80/0.4) + f2*(120/0.5)*(0.64^2) + f3*(80/0.3)*(1.78^2) + 0.15 + 0.35*(1.78^2) ]
        f_bracket = (
            (c3 ** 2 - 1.0)
            + f1 * (L1 / D1)
            + f2 * (L2 / D2) * (c2 ** 2)
            + f3 * (L3 / D3) * (c3 ** 2)
            + K12
            + K23 * (c3 ** 2)
        )
        
        v1 = math.sqrt(2.0 * G * net_driving_head / f_bracket)
        v2 = c2 * v1
        v3 = c3 * v1
        
        Re1 = v1 * D1 / NU_WATER
        Re2 = v2 * D2 / NU_WATER
        Re3 = v3 * D3 / NU_WATER
        
        f1_new = calc_friction_factor(Re1, kd1)
        f2_new = calc_friction_factor(Re2, kd2)
        f3_new = calc_friction_factor(Re3, kd3)
        
        iters.append({
            "iter": it,
            "f1_in": f1, "f2_in": f2, "f3_in": f3,
            "v1": v1, "v2": v2, "v3": v3,
            "Re1": Re1, "Re2": Re2, "Re3": Re3,
            "f1_out": f1_new, "f2_out": f2_new, "f3_out": f3_new
        })
        
        if max(abs(f1_new - f1), abs(f2_new - f2), abs(f3_new - f3)) < 1e-4:
            f1, f2, f3 = f1_new, f2_new, f3_new
            break
        f1, f2, f3 = f1_new, f2_new, f3_new
        
    Q = v1 * (math.pi * D1**2 / 4.0)
    hf1 = f1 * (L1 / D1) * (v1**2 / (2 * G))
    hf2 = f2 * (L2 / D2) * (v2**2 / (2 * G))
    hf3 = f3 * (L3 / D3) * (v3**2 / (2 * G))
    hm1 = K12 * (v1**2 / (2 * G))
    hm2 = K23 * (v3**2 / (2 * G))
    
    return PipeSeriesResult(
        iterations=iters,
        v1=v1, v2=v2, v3=v3, Q=Q,
        Re1=Re1, Re2=Re2, Re3=Re3,
        f1=f1, f2=f2, f3=f3,
        hf_total=hf1 + hf2 + hf3,
        hm_total=hm1 + hm2
    )


@dataclass
class PipeSizingResult:
    iterations: List[Dict[str, Any]]
    final_D: float
    final_v: float
    final_Re: float
    final_f: float
    hf: float


def solve_problem_2_pipe_sizing() -> PipeSizingResult:
    """
    Problem 2: Constant diameter pipe sizing.
    Outlet point 2 is 10 m higher than point 1 (Z2 - Z1 = 10 m).
    Length L = 1500 m. Discharge Q = 0.14 m^3/s. Roughness eps = 0.9 mm.
    Pressure at point 1 is P1 = 105.13 kPa. Outlet discharges to atmosphere (P2 = 0).
    Find pipe diameter D.
    """
    L = 1500.0
    Q = 0.14
    eps = 0.9e-3
    P1 = 105.13e3
    dz = 10.0
    
    # Energy Eq: P1/gamma + v1^2/2g + z1 = P2/gamma + v2^2/2g + z2 + hf
    # Since D is constant, v1 = v2 -> velocity heads cancel.
    # P2 = 0 (gauge, open discharge).
    # hf = P1/gamma - dz = 105130/9810 - 10 = 0.7166 m
    hf = (P1 / GAMMA_WATER) - dz
    
    # From Darcy-Weisbach: hf = (8 f L Q^2) / (pi^2 g D^5)
    # D = [ (8 f L Q^2) / (pi^2 g hf) ]^(1/5)
    f_guess = 0.020  # standard trial starting value
    iters = []
    final_D = 0.0
    final_v = 0.0
    final_Re = 0.0
    
    for it in range(1, 15):
        D = ((8.0 * f_guess * L * (Q ** 2)) / (math.pi ** 2 * G * hf)) ** 0.2
        v = Q / (math.pi * (D ** 2) / 4.0)
        Re = v * D / NU_WATER
        kd = eps / D
        f_new = calc_friction_factor(Re, kd)
        
        iters.append({
            "iter": it,
            "f_in": f_guess,
            "D": D,
            "D_mm": D * 1000.0,
            "v": v,
            "Re": Re,
            "kd": kd,
            "f_out": f_new
        })
        
        final_D = D
        final_v = v
        final_Re = Re
        
        if abs(f_new - f_guess) < 1e-5:
            f_guess = f_new
            break
        f_guess = f_new
        
    return PipeSizingResult(
        iterations=iters,
        final_D=final_D,
        final_v=final_v,
        final_Re=final_Re,
        final_f=f_guess,
        hf=hf
    )


def solve_problem_huge_tanks() -> PipeSizingResult:
    """
    Problem: Two huge tanks connected by inclined pipe.
    Left tank: depth to inlet = 45 m.
    Right tank: depth to outlet = 16.5 m.
    Pipe length L = 120 m, inclined upward at 12 deg.
    Q = 12 m^3/s, eps = 0.48 mm, rho = 1000, mu = 1e-3 (nu = 1e-6). Minor losses ignored.
    """
    L = 120.0
    theta_deg = 12.0
    Q = 12.0
    eps = 0.48e-3
    
    # Elevation difference between two water surfaces:
    # z_inlet = 0 (datum) -> z1 = 45.0 m
    # z_outlet = L * sin(12 deg) = 120 * sin(12 deg) = 24.95 m
    # z2 = z_outlet + 16.5 = 24.95 + 16.5 = 41.45 m
    # Driving head hf = z1 - z2 = 45.0 - 41.45 = 3.55 m
    z_outlet = L * math.sin(math.radians(theta_deg))
    hf = 45.0 - (z_outlet + 16.5)
    
    f_guess = 0.020
    iters = []
    final_D = 0.0
    final_v = 0.0
    final_Re = 0.0
    
    for it in range(1, 15):
        D = ((8.0 * f_guess * L * (Q ** 2)) / (math.pi ** 2 * G * hf)) ** 0.2
        v = Q / (math.pi * (D ** 2) / 4.0)
        Re = v * D / NU_WATER
        kd = eps / D
        f_new = calc_friction_factor(Re, kd)
        
        iters.append({
            "iter": it,
            "f_in": f_guess,
            "D": D,
            "D_mm": D * 1000.0,
            "v": v,
            "Re": Re,
            "kd": kd,
            "f_out": f_new
        })
        
        final_D = D
        final_v = v
        final_Re = Re
        
        if abs(f_new - f_guess) < 1e-5:
            f_guess = f_new
            break
        f_guess = f_new
        
    return PipeSizingResult(
        iterations=iters,
        final_D=final_D,
        final_v=final_v,
        final_Re=final_Re,
        final_f=f_guess,
        hf=hf
    )


@dataclass
class ParallelNetworkResult:
    h_AB: float
    h4: float
    v3: float
    Q3: float
    f3: float
    v2: float
    Q2: float
    f2: float
    Q_total: float
    v1: float
    Re1: float
    f1: float
    h1: float
    h_total: float


def solve_problem_4_parallel_series() -> ParallelNetworkResult:
    """
    Problem 4 (Exam - 15 points):
    Four pipes connected in series-parallel: Pipe 1 -> (Pipe 2 // Pipe 3) -> Pipe 4.
    Point A is 10 m lower than Point B on Pipe 4. Length AB = 300 m.
    PA = 910 kPa, PB = 811.41 kPa.
    Given h3 = 0.42 m. Minor loss ignored.
    Pipe 1: D=0.9 m, L=900 m, eps=0.90 mm -> k/D = 0.001
    Pipe 2: D=0.8 m, L=800 m, eps=0.32 mm -> k/D = 0.0004
    Pipe 3: D=0.6 m, L=800 m, eps=0.48 mm -> k/D = 0.0008
    Pipe 4: L=1000 m, eps=0.96 mm
    Find total major losses from AA to BB (h_AA_BB).
    """
    # 1. Pipe 4 between A and B
    # PA/gamma + vA^2/2g + zA = PB/gamma + vB^2/2g + zB + h_AB
    # Since pipe 4 is constant diameter, vA = vB -> (PA - PB)/gamma = (zB - zA) + h_AB
    # (910 - 811.41)*1000 / 9810 = 10.05 m = 10 + h_AB -> h_AB = 0.05 m
    h_AB = ((910.0e3 - 811.41e3) / GAMMA_WATER) - 10.0
    h4 = h_AB * (1000.0 / 300.0)
    
    # 2. Parallel branch 3: h3 = 0.42 m, D3=0.6, L3=800, eps3=0.48mm
    kd3 = 0.48e-3 / 0.6  # 0.0008
    f3 = 0.019  # guess from chart
    v3 = 0.0
    for _ in range(10):
        v3 = math.sqrt(2.0 * G * 0.42 / (f3 * (800.0 / 0.6)))
        Re3 = v3 * 0.6 / NU_WATER
        f3_new = calc_friction_factor(Re3, kd3)
        if abs(f3_new - f3) < 1e-6:
            break
        f3 = f3_new
    Q3 = v3 * (math.pi * 0.6**2 / 4.0)
    
    # 3. Parallel branch 2: in parallel, h2 = h3 = 0.42 m
    kd2 = 0.32e-3 / 0.8  # 0.0004
    f2 = 0.016  # guess from chart
    v2 = 0.0
    for _ in range(10):
        v2 = math.sqrt(2.0 * G * 0.42 / (f2 * (800.0 / 0.8)))
        Re2 = v2 * 0.8 / NU_WATER
        f2_new = calc_friction_factor(Re2, kd2)
        if abs(f2_new - f2) < 1e-6:
            break
        f2 = f2_new
    Q2 = v2 * (math.pi * 0.8**2 / 4.0)
    
    # 4. Total discharge Q = Q2 + Q3 = Q1
    Q_total = Q2 + Q3
    
    # 5. Pipe 1: D=0.9, L=900, eps=0.90mm
    kd1 = 0.90e-3 / 0.9  # 0.001
    v1 = Q_total / (math.pi * 0.9**2 / 4.0)
    Re1 = v1 * 0.9 / NU_WATER
    f1 = calc_friction_factor(Re1, kd1)
    h1 = f1 * (900.0 / 0.9) * (v1**2 / (2.0 * G))
    
    # Total major loss AA to BB
    h_total = h1 + 0.42 + h4
    
    return ParallelNetworkResult(
        h_AB=h_AB,
        h4=h4,
        v3=v3, Q3=Q3, f3=f3,
        v2=v2, Q2=Q2, f2=f2,
        Q_total=Q_total,
        v1=v1, Re1=Re1, f1=f1, h1=h1,
        h_total=h_total
    )


if __name__ == "__main__":
    print("=================================================================")
    print("   CN271 FLUID MECHANICS EXAM SOLVER & VERIFICATION ENGINE")
    print("=================================================================\n")
    
    res1 = solve_problem_1_series_incline()
    print("[Problem 1: Inclined Series Pipes]")
    print(f"  v1 = {res1.v1:.4f} m/s, v2 = {res1.v2:.4f} m/s, v3 = {res1.v3:.4f} m/s")
    print(f"  Q  = {res1.Q:.4f} m^3/s ({res1.Q*1000:.2f} L/s)")
    print(f"  f1 = {res1.f1:.4f}, f2 = {res1.f2:.4f}, f3 = {res1.f3:.4f}")
    print(f"  Total friction loss hf = {res1.hf_total:.4f} m, minor loss hm = {res1.hm_total:.4f} m\n")
    
    res2 = solve_problem_2_pipe_sizing()
    print("[Problem 2: Pipe Sizing (Atmospheric Exit)]")
    print(f"  Driving Head hf = {res2.hf:.4f} m")
    print(f"  Calculated Diameter D = {res2.final_D:.4f} m ({res2.final_D*1000:.1f} mm)")
    print(f"  Flow velocity v = {res2.final_v:.4f} m/s, Re = {res2.final_Re:.2e}, f = {res2.final_f:.4f}\n")
    
    res_tanks = solve_problem_huge_tanks()
    print("[Problem: Two Huge Reservoirs]")
    print(f"  Head loss hf = {res_tanks.hf:.4f} m")
    print(f"  Calculated Diameter D = {res_tanks.final_D:.4f} m ({res_tanks.final_D*1000:.1f} mm)")
    print(f"  Flow velocity v = {res_tanks.final_v:.4f} m/s, f = {res_tanks.final_f:.4f}\n")
    
    res4 = solve_problem_4_parallel_series()
    print("[Problem 4: Parallel & Series Pipe Network (AA to BB)]")
    print(f"  Pipe 4: h_AB = {res4.h_AB:.4f} m -> h4 = {res4.h4:.4f} m")
    print(f"  Pipe 3: v3 = {res4.v3:.4f} m/s, Q3 = {res4.Q3:.4f} m^3/s, f3 = {res4.f3:.4f}")
    print(f"  Pipe 2: v2 = {res4.v2:.4f} m/s, Q2 = {res4.Q2:.4f} m^3/s, f2 = {res4.f2:.4f}")
    print(f"  Total Discharge Q1 = Q_total = {res4.Q_total:.4f} m^3/s")
    print(f"  Pipe 1: v1 = {res4.v1:.4f} m/s, f1 = {res4.f1:.4f}, h1 = {res4.h1:.4f} m")
    print(f"  >>> TOTAL MAJOR LOSS (AA to BB) = h1 + h2 + h4 = {res4.h_total:.4f} m <<<\n")
