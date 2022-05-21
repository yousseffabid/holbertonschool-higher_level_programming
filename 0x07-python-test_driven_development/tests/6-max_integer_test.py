#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertIsNone(max_integer([]))

        self.assertAlmostEqual(max_integer([0.65, 191.0]), 191.0)

        self.assertAlmostEqual(max_integer([-2.3, -134]), -2.3)

        self.assertEqual(max_integer([4, 1.2]), 4)

        self.assertEqual(max_integer([0, 0, 0]), 0)

        self.assertEqual(max_integer([-1, 0, -2]), 0)

        self.assertEqual(max_integer([-1, -2, -3]), -1)

        self.assertEqual(max_integer([1]), 1)

        self.assertEqual(max_integer([-1]), -1)
