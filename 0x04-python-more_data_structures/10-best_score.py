#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        elements = []
        for key, element in a_dictionary.items():
            elements.append(element)
        maximum = reduce(max, elements)
        return maximum
    else:
        return None
