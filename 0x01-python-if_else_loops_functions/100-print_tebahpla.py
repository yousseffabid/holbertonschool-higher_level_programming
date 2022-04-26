#!/usr/bin/python3


for asscii in range(90, 64, -1):
    if asscii % 2 == 0:
        asscii += 32
    print(f'{chr(asscii)}', end='')
