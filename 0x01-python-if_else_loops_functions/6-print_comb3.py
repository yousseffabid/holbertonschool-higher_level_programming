#!/usr/bin/python3

for number in range(1, 99):
    if number >= 10:
        string_number = str(number)
        first_digit = string_number[0]
        last_digit = string_number[1]

    if number < 10 or ord(first_digit) < ord(last_digit):
        if number == 89:
            print('{:d}'.format(number))
        else:
            print('{:02}, '.format(number), end='')
