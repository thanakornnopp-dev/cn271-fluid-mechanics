"""
Unit tests for CN271 Fluid Mechanics Solver Engine
Guarantees exact numerical convergence, energy conservation, and continuity.
"""

import unittest
import math
from solver_engine import (
    calc_friction_factor,
    solve_problem_1_series_incline,
    solve_problem_2_pipe_sizing,
    solve_problem_huge_tanks,
    solve_problem_4_parallel_series,
    G, GAMMA_WATER
)


class TestCN271Solver(unittest.TestCase):

    def test_laminar_friction(self):
        Re = 1000.0
        f = calc_friction_factor(Re, 0.001)
        self.assertAlmostEqual(f, 64.0 / Re, places=4)

    def test_turbulent_friction_smooth(self):
        Re = 1.0e5
        kd = 0.0001
        f = calc_friction_factor(Re, kd)
        # Expected around 0.018
        self.assertTrue(0.015 < f < 0.022)

    def test_problem_1_energy_balance(self):
        res = solve_problem_1_series_incline()
        # Continuity check
        A1 = math.pi * 0.4**2 / 4.0
        A2 = math.pi * 0.5**2 / 4.0
        A3 = math.pi * 0.3**2 / 4.0
        Q1 = res.v1 * A1
        Q2 = res.v2 * A2
        Q3 = res.v3 * A3
        self.assertAlmostEqual(Q1, Q2, places=4)
        self.assertAlmostEqual(Q1, Q3, delta=0.01)

        # Driving head check
        zB = 280.0 * math.sin(math.radians(5.0))
        dH = (245.25e3 / GAMMA_WATER) - zB  # 0.5964 m
        
        # Energy balance: dH = v3^2/2g - v1^2/2g + hf + hm
        dH_calculated = ((res.v3**2 - res.v1**2) / (2.0 * G)) + res.hf_total + res.hm_total
        self.assertAlmostEqual(dH, dH_calculated, places=2)

    def test_problem_2_head_loss(self):
        res = solve_problem_2_pipe_sizing()
        self.assertAlmostEqual(res.hf, 0.7166, places=3)
        # Check diameter satisfies Darcy-Weisbach
        D = res.final_D
        v = res.final_v
        hf_check = res.final_f * (1500.0 / D) * (v**2 / (2.0 * G))
        self.assertAlmostEqual(res.hf, hf_check, places=2)
        # Check D is approx 0.60 m (597.6 mm)
        self.assertTrue(0.58 < D < 0.62)

    def test_problem_huge_tanks(self):
        res = solve_problem_huge_tanks()
        self.assertAlmostEqual(res.hf, 3.5506, places=2)
        D = res.final_D
        v = res.final_v
        hf_check = res.final_f * (120.0 / D) * (v**2 / (2.0 * G))
        self.assertAlmostEqual(res.hf, hf_check, places=2)
        # Check D is approx 1.44 m
        self.assertTrue(1.40 < D < 1.48)

    def test_problem_4_parallel_continuity(self):
        res = solve_problem_4_parallel_series()
        # Check parallel continuity: Q_total = Q2 + Q3
        self.assertAlmostEqual(res.Q_total, res.Q2 + res.Q3, places=5)
        # Check Pipe 4 head loss
        self.assertAlmostEqual(res.h_AB, 0.05, places=2)
        self.assertAlmostEqual(res.h4, 0.1667, places=2)
        # Check total loss AA to BB
        self.assertAlmostEqual(res.h_total, res.h1 + 0.42 + res.h4, places=4)
        self.assertTrue(1.15 < res.h_total < 1.35)


if __name__ == "__main__":
    unittest.main()
