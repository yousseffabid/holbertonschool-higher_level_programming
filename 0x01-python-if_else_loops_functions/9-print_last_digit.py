#!/usr/bin/python3


def print_last_digit(number):
    string_number = str(number)
    last_character = string_number[-1]
    print('{:d}'.format(int(last_character)), end='')

    return int(last_character)
