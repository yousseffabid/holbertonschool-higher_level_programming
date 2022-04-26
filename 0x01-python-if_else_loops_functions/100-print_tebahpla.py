#!/usr/bin/python3


alternate = 1

for asscii in range(122, 96, -1):
    if alternate % 2 == 0:
        new_asccii = asscii - 32
    else:
        new_asccii = asscii

    print('{}'.format(chr(new_asccii)), end='')
    alternate += 1
