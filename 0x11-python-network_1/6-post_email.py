#!/usr/bin/python3
"""
URL and an email address, sends a POST request
to the passed URL with the email as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    pair = {'email': sys.argv[2]}

    response = requests.post(sys.argv[1], data=pair)
    print(response.text)
