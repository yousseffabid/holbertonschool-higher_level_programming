#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """define a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize instance"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """calculate area"""

        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""

        if self.__width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character #"""

        if self.__width == 0 or self.height == 0:
            return ''
        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """return a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print msg after deleting an instance"""

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
