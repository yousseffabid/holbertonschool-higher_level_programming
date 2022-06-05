#!/usr/bin/python3
"""Unittest for base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Unittest for base.py
    """

    def test_init(self):

        obj1 = Base()
        obj2 = Base("A")
        obj3 = Base(100)
        obj4 = Base(-1)
        obj5 = Base((1, 2))

        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj2.id, 'A')
        self.assertEqual(obj3.id, 100)
        self.assertEqual(obj4.id, -1)
        self.assertEqual(obj5.id, (1, 2))

    def test_to_json_string(self):
        r = Rectangle(1, 2, 3, 4, 3)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string(None)))
        self.assertEqual("[]", Base.to_json_string([]))
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_from_json_string(self):
        list_input = [{"id": 10, "width": 41, "height": 9}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

        list_input = [
            {"id": 9, "size": 9, "height": 6},
            {"id": 7, "size": 3, "height": 5}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 4, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (10) 1/4 - 3/5", str(r2))


if __name__ == "__main__":
    unittest.main()
