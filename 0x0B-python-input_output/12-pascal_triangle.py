#!/usr/bin/python3
"""returns a list of lists of integers representing"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    Return:
        a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    else:
        my_list = []
        index = -1
        for i in range(n):
            sublist = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    sublist.append(1)
                else:
                    sublist.append(my_list[index][j - 1] + my_list[index][j])
            index += 1
            my_list.append(sublist)
        return my_list
