#!/usr/bin/python3
"""creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file
    args:
        filename(str): the name of the textfile
    return:
        obj(object): object converted from jsonfile
    """
    with open(filename) as a_file:
        obj = json.load(a_file)
        return obj
