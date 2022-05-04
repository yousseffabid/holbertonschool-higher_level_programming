#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dict = {key: element*2 for key, element in a_dictionary.items()}
        return new_dict
    return a_dictionary
