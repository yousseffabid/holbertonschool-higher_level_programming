#!/usr/bin/python3
""" appends a string at the end of a text file
    and return number of char added"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
    and return number of char added

    args:
        filename(str): the name of the file
        text(str): string to append to the file
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
