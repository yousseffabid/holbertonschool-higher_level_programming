#!/usr/bin/python3


def remove_char_at(str, n):
    s = str
    if n >= 0:
        s = s[:n] + s[n+1:]
    return s
