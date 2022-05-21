#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_char = {'.', '?', ':'}
    mylist = []
    string = ''
    for char in text:
        string += char
        if char in special_char:
            mylist.append(string)
            string = ''
    if string != '':
        mylist.append(string)

    for idx, line in enumerate(mylist):
        print(line.strip())
        if idx != len(mylist) - 1:
            print("")
