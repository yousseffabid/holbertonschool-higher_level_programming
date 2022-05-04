#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    else:
        number = 0
        flag = 0
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string) - 1, -1, -1):
            if roman_string[i] != "I":
                flag = 1
                number += my_dict[roman_string[i]]
            elif flag == 1:
                number += -1
            else:
                number += 1
        return number
