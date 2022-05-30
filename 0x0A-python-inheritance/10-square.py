#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
