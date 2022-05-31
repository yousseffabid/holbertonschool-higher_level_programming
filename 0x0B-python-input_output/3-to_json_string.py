#!/usr/bin/python3
"""return the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object (string)
    args:
        my_obj(object string): the object to convert to json representation
    return:
        json_rep: json representation
    """
    json_rep = json.dumps(my_obj)
    return json_rep
