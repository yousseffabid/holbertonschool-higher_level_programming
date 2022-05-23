#!/usr/bin/python3
"""create a rectangle
"""


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        """__init__ method
        """
        self.height = height
        self.width = width

    def __str__(self):
        """__str__ method
        print the rectangle on print() or str()
        """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += '#'
            if i is not (self.__height - 1):
                my_str += "\n"
        return my_str

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method
        calculate the rectangle object's area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter method
        calculate the rectangle object's perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
