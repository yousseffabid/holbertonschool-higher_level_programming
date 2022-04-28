#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    number_of_args = len(sys.argv) - 1
    if number_of_args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print(f'{a} {operator} {b} = {add(a, b)}')
    elif operator == '-':
        print(f'{a} {operator} {b} = {sub(a, b)}')
    elif operator == '*':
        print(f'{a} {operator} {b} = {mul(a, b)}')
    else:
        print(f'{a} {operator} {b} = {div(a, b)}')

