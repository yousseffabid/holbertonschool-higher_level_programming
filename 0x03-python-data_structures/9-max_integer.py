#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    for element in my_list:
        if max_value < element:
            max_value = element
    return max_value
