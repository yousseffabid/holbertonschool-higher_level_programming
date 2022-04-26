#!/usr/bin/python3


def uppercase(str):
    for character in str:
        if ord(character) <= ord('z') and ord(character) >= ord('a'):
            tmp = chr(ord(character) - 32)
        else:
            tmp = character
        print('{}'.format(tmp), end='')

    print()
