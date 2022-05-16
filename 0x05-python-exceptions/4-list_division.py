#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    i = 0
    while i < list_length:
        try:
            c = my_list_1[i] / my_list_2[i]
            result[i] = c
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            i += 1
    return result
