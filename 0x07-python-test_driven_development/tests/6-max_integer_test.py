#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer([0, 0, 0]), 0)

        self.assertEqual(max_integer([-1, 0, -2]), 0)

        self.assertEqual(max_integer([-1, -2, -3]), -1)

        self.assertEqual(max_integer([1]), 1)

        self.assertEqual(max_integer([-1]), -1)


if __name__ == '__main__':
    unittest.main()
