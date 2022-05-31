#!/usr/bin/python3

def pascal_triangle(n):
    """eturns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    else:
        my_list = []
        for i in range(n):
            number = 11**i
            sub_list = [int(char) for char in str(number)]
            my_list.append(sub_list)
        return my_list
