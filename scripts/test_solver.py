"""
Unit tests for CN271 Comprehensive Solver Engine
"""

import unittest
from solver_engine import (
    solve_submarine_model,
    solve_example_1,
    solve_example_2,
    solve_example_3,
    solve_problem_6_velocity,
    solve_problem_7_tank_rising,
    solve_problem_8_sizing,
    solve_problem_9_series_horizontal
)


class TestCN271Comprehensive(unittest.TestCase):

    def test_submarine(self):
        res = solve_submarine_model()
        self.assertAlmostEqual(res["v_m"], 690.67, places=1)
        self.assertAlmostEqual(res["F_p"], 277.99, places=1)

    def test_example_1(self):
        res = solve_example_1()
        self.assertEqual(res["Re"], 10000.0)
        self.assertTrue(res["is_turbulent"])
        self.assertAlmostEqual(res["v_max_laminar"], 0.02, places=4)

    def test_example_2(self):
        res = solve_example_2()
        self.assertEqual(res["Re"], 1600.0)
        self.assertTrue(res["is_laminar"])
        self.assertAlmostEqual(res["f_laminar"], 0.04, places=4)
        self.assertAlmostEqual(res["dp_b"], 0.05, places=4)
        self.assertAlmostEqual(res["dp_c"], 15.0, places=2)

    def test_example_3(self):
        res = solve_example_3()
        self.assertAlmostEqual(res["v1"], 12.73, places=1)
        self.assertAlmostEqual(res["v2"], 3.18, places=1)
        self.assertAlmostEqual(res["v3"], 1.41, places=1)
        self.assertAlmostEqual(res["hL_12"], 9.84, places=1)
        self.assertAlmostEqual(res["hL_23"], 5.47, places=1)

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

    def test_problem_9(self):
        res = solve_problem_9_series_horizontal()
        self.assertAlmostEqual(res["v1"], 0.73, delta=0.02)
        self.assertAlmostEqual(res["v2"], 1.29, delta=0.02)
        self.assertAlmostEqual(res["v3"], 2.91, delta=0.02)
        self.assertAlmostEqual(res["Q"], 3.65e-3, delta=0.1e-3)


if __name__ == "__main__":
    unittest.main()
