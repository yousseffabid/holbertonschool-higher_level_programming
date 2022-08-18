#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
arg=$1; if [ $(curl -s -L -w '%{http_code}' "$arg" -o /dev/null) -eq 200 ]; then curl -sL "$arg"; fi
