#!/usr/bin/python3
"""Define a Python class-to-JSON function."""


def class_to_json(obj):
    """Define a Python class-to-JSON function."""
    return obj.__dict__
