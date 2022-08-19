#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().encode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
