# -*- coding: utf-8 -*-
"""Unit tests สำหรับตรวจสอบความถูกต้องของตัวเลขในทุกบทของหลักสูตร CN271"""
import unittest
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from master_solver import FluidSolver


class TestFullCourse(unittest.TestCase):
    def test_ch1_shear_stress(self):
        tau = FluidSolver.shear_stress(mu=0.29, v=3.2, h=0.008)
        self.assertAlmostEqual(tau, 116.0, places=3)

    def test_ch2_manometer_p9(self):
        # Ex 9: SG1 = 1.0, SG2 = 0.8
        p_b = 0.0
        p_a = p_b - (1.0 * 9810.0 * 0.2)
        p_c = p_b + (1.0 * 9810.0 * 0.2)
        p_d = p_c
        p_e = p_d + (0.8 * 9810.0 * 0.7)
        self.assertAlmostEqual(p_a, -1962.0, places=1)
        self.assertAlmostEqual(p_b, 0.0, places=1)
        self.assertAlmostEqual(p_c, 1962.0, places=1)
        self.assertAlmostEqual(p_d, 1962.0, places=1)
        self.assertAlmostEqual(p_e, 7455.6, places=1)

    def test_ch2_plane_gate_p22(self):
        res = FluidSolver.center_of_pressure_rect(h_top=0.0, height=6.0, width=5.0, theta_deg=90.0)
        self.assertAlmostEqual(res["f_r"], 882900.0, delta=10.0)
        self.assertAlmostEqual(res["y_cp"], 4.0, places=3)

    def test_ch2_tilted_gate_p26(self):
        # Gate CD: b=1.8, L=2.0, slope 4:3:5 => sin=0.8, cos=0.6, water 2m above C
        # y_C = 2.0 / 0.8 = 2.5m, y_cg = 3.5m, h_cg = 2.8m
        # A = 3.6m2 => F_R = 9810 * 2.8 * 3.6 = 98884.8 N
        # I_xc = 1.8 * 2^3 / 12 = 1.2 m4 => y_cp = 3.5 + 1.2/(3.5*3.6) = 3.5952m
        # d_F = 3.5952 - 2.5 = 1.0952m, d_W = 1.0 * 0.6 = 0.6m
        # W = 98884.8 * 1.0952 / 0.6 = 180498 N ~ 180.5 kN
        f_r = 9810.0 * 2.8 * 3.6
        y_cp = 3.5 + 1.2 / (3.5 * 3.6)
        d_f = y_cp - 2.5
        d_w = 1.0 * 0.6
        w = (f_r * d_f) / d_w
        self.assertAlmostEqual(w / 1000.0, 180.5, delta=0.5)

    def test_ch2_curved_gate_p29(self):
        # R = 6m, b = 2m
        f_h = 9810.0 * 3.0 * (6.0 * 2.0)
        vol = (math.pi * (6.0 ** 2) / 4.0) * 2.0
        f_v = 9810.0 * vol
        f_r = math.sqrt(f_h**2 + f_v**2)
        theta_deg = math.degrees(math.atan(f_v / f_h))
        self.assertAlmostEqual(f_h / 1000.0, 353.16, places=1)
        self.assertAlmostEqual(f_v / 1000.0, 554.74, places=1)
        self.assertAlmostEqual(f_r / 1000.0, 657.6, delta=0.5)
        self.assertAlmostEqual(theta_deg, 57.52, places=1)

    def test_ch3_jet_vane_p5(self):
        # (a) Fixed: v=24, A=0.01, rho=1000 => Fx = 2 * rho * A * v^2 = 11.52 kN
        fixed = FluidSolver.jet_on_curved_vane(v=24.0, area=0.010, u=0.0)
        self.assertAlmostEqual(fixed["f_x"] / 1000.0, 11.52, places=2)
        # (b) Moving: u=6 => vr = 18 => Fx = 2 * rho * A * vr^2 = 6.48 kN
        moving = FluidSolver.jet_on_curved_vane(v=24.0, area=0.010, u=6.0)
        self.assertAlmostEqual(moving["f_x"] / 1000.0, 6.48, places=2)

    def test_ch3_siphon_p9(self):
        # dz = 3m => v3 = sqrt(2 * 9.81 * 3) = 7.672 m/s
        # P2/gamma = -5m => P2 = - (0.84 * 9810) * 5 = -41.2 kPa
        v3 = math.sqrt(2.0 * 9.81 * 3.0)
        p2 = -(0.84 * 9810.0) * 5.0
        self.assertAlmostEqual(v3, 7.672, places=2)
        self.assertAlmostEqual(p2 / 1000.0, -41.2, delta=0.1)

    def test_ch4_similitude(self):
        # River model: scale 1:80, vm = 18 => vp = 18 * sqrt(80) = 161.0 m/s
        river = FluidSolver.froude_scale(scale_ratio=1.0 / 80.0, v_m=18.0)
        self.assertAlmostEqual(river["v_p"], 161.00, delta=0.1)
        # Pipe model: scale 1:10, vp = 0.2 => vm = 2.0 m/s
        pipe = FluidSolver.reynolds_scale(scale_ratio=1.0 / 10.0, v_p=0.2)
        self.assertAlmostEqual(pipe["v_m"], 2.0, places=2)

    def test_meter_cavitation_p14(self):
        # Q=0.015, D=0.2 => v = 0.4775 m/s, v^2/(2g) = 0.01162 m
        # hL = 20 * 0.01162 = 0.232 m
        # Patm = 101 kPa, Pv = 5950 Pa, NPSHR = 4.6 m
        # Z1_max = (101000 - 5950)/9810 - 4.6 - 0.232 = 4.857 m
        v = (4.0 * 0.015) / (math.pi * (0.2**2))
        hl = 20.0 * (v**2) / (2.0 * 9.81)
        z1_max = (101000.0 - 5950.0) / 9810.0 - 4.6 - hl
        self.assertAlmostEqual(z1_max, 4.86, delta=0.05)


if __name__ == "__main__":
    unittest.main()
