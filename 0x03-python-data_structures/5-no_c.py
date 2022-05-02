#!/usr/bin/python3
def no_c(my_string):
    no_c = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            no_c += char
    if no_c:
        return no_c
    else:
        return my_string
