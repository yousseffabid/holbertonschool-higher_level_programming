#!/usr/bin/python3
"""write an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write an Object to a text file, using a JSON representation
    args:
        my_obj(object): object to convert to json
        filename(str): the name of the textfile
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
