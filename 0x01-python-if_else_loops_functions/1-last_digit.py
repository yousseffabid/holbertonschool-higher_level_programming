#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

string_number = str(number)
last_character = string_number[-1]
last_digit = int(last_character)
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    str = 'Last digit of {:d} is {:d} and is greater than 5'
    print(str.format(number, last_digit))
elif last_digit == 0:
    str = 'Last digit of {:d} is {:d} and is 0'
    print(str.format(number, last_digit))
else:
    str = 'Last digit of {:d} is {:d} and is less than 6 and not 0'
    print(str.format(number, last_digit))
