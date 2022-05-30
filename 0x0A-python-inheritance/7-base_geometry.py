#!/usr/bin/python3
"""BaseGeomerty class"""


class BaseGeometry:
    """BaseGeomerty class"""
    def area(self):
        """raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is strictly positive integer grater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
