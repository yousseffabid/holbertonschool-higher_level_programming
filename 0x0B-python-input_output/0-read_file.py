#!/usr/bin/python3
"""Readding from a textfile"""


def read_file(filename=""):
    """print the content of a textfile to the stdout
    args:
        filename(str): name of hte textfile
    """
    with open(filename, mode="r", encoding='utf-8') as a_file:
        print(a_file.read(), end='')
