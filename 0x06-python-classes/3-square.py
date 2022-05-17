#!/usr/bin/python3
"""Square Class
This is a square
"""


class Square:
    """Square Class
    Square with size
    """
    def __init__(self, size=0):
        """__init__
        initializing square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of the Square
        """
        return self.__size * self.__size
