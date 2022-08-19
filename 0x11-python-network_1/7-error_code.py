#!/usr/bin/python3
"""
takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.text)
    except requests.exceptions.RequestException:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
