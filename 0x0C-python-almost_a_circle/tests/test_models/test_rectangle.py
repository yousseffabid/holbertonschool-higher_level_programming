#!/usr/bin/python3
"""Unittest for base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_init(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2])
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [2])
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 2, [3])

    def test_area(self):
        r = Rectangle(1, 2)
        a = r.area()
        self.assertEqual(a, 2)

    def test_str(self):
        r = Rectangle(1, 2, 3, 2, 12)
        string = r.__str__()
        self.assertEqual('[Rectangle] (12) 3/2 - 1/2', string)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 2, 12)
        r_dict = {"width": 1, "height": 2, "x": 3, 'y': 2, 'id': 12}
        self.assertEqual(r_dict, r.to_dictionary())

    def test_update(self):
        r = Rectangle(1, 2, 3, 2, 12)
        r.update(9)
        self.assertEqual(r.id, 9)

        r_dict = {"x": 3, 'y': 2, 'id': 12}
        r.update(**r_dict)
        self.assertEqual('[Rectangle] (12) 3/2 - 1/2', str(r))


if __name__ == "__main__":
    unittest.main()
