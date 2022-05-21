#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    row = '#' * size
    for i in range(size):
        print(row)
