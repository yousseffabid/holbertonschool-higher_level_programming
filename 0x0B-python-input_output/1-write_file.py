#!/usr/bin/python3
"""writes a string to a text file and return the number of characters"""


def write_file(filename="", text=""):
    """writes a string to a text file and return the number of characters
    args:
        filename(str): the name of the textfile
        text(str): the string to be inserted in the textfile
    return:
        lwngth (int): number of char written into the textfile
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        length = len(text)
        a_file.write(text)
        return length
