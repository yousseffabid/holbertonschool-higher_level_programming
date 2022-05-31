#!/usr/bin/python3
"""return an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """return an object (Python data structure) represented by a JSON string
    args:
        my_str(str): json string
    return:
        obj: object from json conversion
    """
    obj = json.loads(my_str)
    return obj
