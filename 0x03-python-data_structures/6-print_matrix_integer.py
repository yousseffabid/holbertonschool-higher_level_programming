#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for index, element in enumerate(row):
                if index != len(row) - 1:
                    print(f'{element:d }', end='')
                else:
                    print(f'{element:d}')
            print('\n')




