#!/usr/bin/python3
"""Unittest for square.py
"""

import unittest
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [2])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_area(self):
        s = Square(1, 2)
        a = s.area()
        self.assertEqual(a, 1)

    def test_str(self):
        s = Square(2, 2, 2, 12)
        string = s.__str__()
        self.assertEqual('[Square] (12) 2/2 - 2', string)

    def test_to_dictionary(self):
        s = Square(2, 2, 2, 12)
        s_dict = {'id': 12, "size": 2, "x": 2, 'y': 2}
        self.assertEqual(s_dict, s.to_dictionary())

    def test_update(self):
        s = Square(2, 2, 2, 12)
        s.update(9)
        self.assertEqual(s.id, 9)

        s_dict = {"x": 3, 'y': 2, 'id': 12}
        s.update(**s_dict)
        self.assertEqual('[Square] (12) 3/2 - 2', str(s))


if __name__ == "__main__":
    unittest.main()
