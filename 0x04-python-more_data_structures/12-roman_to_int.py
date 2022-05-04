#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    else:
        number = 0
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}

        for i in range(len(roman_string)):
            if i + 1 != len(roman_string) and my_dict[roman_string[i]] <\
                    my_dict[roman_string[i + 1]]:
                number -= my_dict[roman_string[i]]
            else:
                number += my_dict[roman_string[i]]
        return number
