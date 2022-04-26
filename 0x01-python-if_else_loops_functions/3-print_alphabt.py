#!/usr/bin/python3

for asscii in range(97, 123):
    if ord('q') != asscii and ord('e') != asscii:
        letter = chr(asscii)
        print(f'{letter}', end='')
