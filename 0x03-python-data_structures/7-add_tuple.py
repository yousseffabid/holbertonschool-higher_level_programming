#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[0:2]
    b = tuple_b[0:2]
    if len(a) < 2:
        if not len(a):
            a = (0, 0)
        else:
            a = (a[0], 0)
    if len(b) < 2:
        if not len(b):
            b = (0, 0)
        else:
            b = (b[0], 0)

    result = [sum(pair) for pair in zip(a, b)]

    tuple_result = tuple(result)
    return tuple_result
