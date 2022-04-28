#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print(f'{a} + {b} = {add(10, 5)}')
    print(f'{a} - {b} = {sub(10, 5)}')
    print(f'{a} * {b} = {mul(10, 5)}')
    print(f'{a} / {b} = {div(10, 5)}')
