#!/usr/bin/python3
"""Unittest for base.py
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_save_to_file(self):
        @classmethod
        def tearDown(self):
            """Delete any created files."""
            try:
                os.remove("Rectangle.json")
            except IOError:
                pass
            try:
                os.remove("Square.json")
            except IOError:
                pass
            try:
                os.remove("Base.json")
            except IOError:
                pass

        r = Rectangle(3, 5, 1, 4, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as a_file:
            json_str = a_file.read()
        correct_str = '[{"id": 10, "width": 3, "height": 5, "x": 1, "y": 4}]'
        self.assertEqual(json_str, correct_str)

        r1 = Rectangle(1, 2, 4, 9, 5)
        r2 = Rectangle(2, 7, 1, 4, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as a_file:
            json_str = a_file.read()
        str1 = '[{"id": 5, "width": 1, "height": 2, "x": 4, "y": 9}, '
        str2 = '{"id": 3, "width": 2, "height": 7, "x": 1, "y": 4}]'
        self.assertEqual(json_str, str1 + str2)

        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as a_file:
            json_str = a_file.read()
        correct_str = '[{"id": 8, "size": 10, "x": 7, "y": 2}]'
        self.assertEqual(json_str, correct_str)

        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as a_file:
            json_str = a_file.read()
        str1 = '[{"id": 8, "size": 10, "x": 7, "y": 2}, '
        str2 = '{"id": 3, "size": 8, "x": 1, "y": 2}]'
        self.assertEqual(json_str, str1 + str2)

    def test_load_from_file(self):
        r1 = Rectangle(11, 7, 2, 5, 1)
        r2 = Rectangle(2, 4, 5, 1, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_save_to_csv(self):
        r1 = Rectangle(11, 7, 2, 5, 1)
        r2 = Rectangle(2, 4, 5, 1, 2)
        Rectangle.save_to_file_csv([r1, r2])
        correct_str = "id,width,height,x,y\n1,11,7,2,5\n2,2,4,5,1\n"
        with open("Rectangle.csv", "r") as a_file:
            self.assertEqual(correct_str, a_file.read())

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        correct_str = "id,size,x,y\n3,5,1,3\n3,9,5,2\n"
        with open("Square.csv", "r") as a_file:
            self.assertEqual(correct_str, a_file.read())

    def load_from_file_csv(self):
        r1 = Rectangle(11, 7, 2, 5, 1)
        r2 = Rectangle(2, 4, 5, 1, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_objs = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_objs[0]))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_objs = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_objs[1]))


if __name__ == "__main__":
    unittest.main()
