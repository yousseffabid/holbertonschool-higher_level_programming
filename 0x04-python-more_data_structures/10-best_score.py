#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        maximum = max(val_list)
        return key_list[val_list.index(maximum)]
    else:
        return None
