#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Get a dictionary representation of the Student.
        args:
            attrs (list): (Optional) The attributes to represent
        """
        if (type(attr) == list and
                all(type(element) == str for element in attr)):
            return {k: getattr(self, k) for k in attr if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
