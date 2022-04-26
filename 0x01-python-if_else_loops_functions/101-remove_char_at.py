#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = ''
    str_len = len(str)
    for character in str:
        if n >= str_len or n <= -str_len:
            return str
        if character != str[n]:
            new_str += character
    return new_str
