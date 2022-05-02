#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for index, element in enumerate(row):
                print(f'{element:d}', end='')
                if index != len(matrix) - 1:
                    print(' ', end='')
            print()




