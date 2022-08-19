#!/usr/bin/python3
import sys
from urllib.request import urlopen
from urllib import request, parse

if __name__ == "__main__":
    pair = {"email": sys.argv[2]}
    data = parse.urlencode(pair).encode("ascii")

    req = request.Request(sys.argv[1], data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
