"""
Unit tests for CN271 Problems 1 to 8 Solver Engine
"""

import unittest
from solver_engine import (
    solve_problem_1,
    solve_problem_2,
    solve_problem_3,
    solve_problem_4,
    solve_problem_5,
    solve_problem_6_velocity,
    solve_problem_7_tank_rising,
    solve_problem_8_sizing
)


class TestCN271Problems1To8(unittest.TestCase):

    def test_problem_1(self):
        res = solve_problem_1()
        self.assertEqual(res["Re"], 10000.0)
        self.assertTrue(res["is_turbulent"])
        self.assertAlmostEqual(res["v_max_laminar"], 0.02, places=4)

    def test_problem_2(self):
        res = solve_problem_2()
        self.assertEqual(res["Re"], 1600.0)
        self.assertTrue(res["is_laminar"])
        self.assertAlmostEqual(res["f_laminar"], 0.04, places=4)
        self.assertAlmostEqual(res["dp_b"], 0.05, places=4)
        self.assertAlmostEqual(res["dp_c"], 15.0, places=2)

    def test_problem_3(self):
        res = solve_problem_3()
        self.assertAlmostEqual(res["v1"], 12.73, places=1)
        self.assertAlmostEqual(res["v2"], 3.18, places=1)
        self.assertAlmostEqual(res["v3"], 1.41, places=1)
        self.assertAlmostEqual(res["hL_12"], 9.84, places=1)
        self.assertAlmostEqual(res["hL_23"], 5.47, places=1)

    def test_problem_4(self):
        res = solve_problem_4()
        self.assertAlmostEqual(res["v"], 3.183, places=2)
        self.assertAlmostEqual(res["hm"], 0.52, delta=0.01)
        self.assertTrue(36.0 < res["hf"] < 38.0)

    def test_problem_5(self):
        res = solve_problem_5()
        self.assertAlmostEqual(res["v"], 2.0, places=2)
        self.assertAlmostEqual(res["P1_kPa"], 219.58, delta=0.5)

    def test_problem_6(self):
        res = solve_problem_6_velocity()
        self.assertAlmostEqual(res["v"], 0.77, places=2)
        self.assertEqual(res["f"], 0.021)

    def test_problem_7(self):
        res = solve_problem_7_tank_rising()
        self.assertAlmostEqual(res["v"], 2.51, delta=0.03)
        self.assertEqual(res["f"], 0.0195)

    def test_problem_8(self):
        res = solve_problem_8_sizing()
        self.assertAlmostEqual(res["D"], 0.36, delta=0.01)


if __name__ == "__main__":
    unittest.main()
