#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]

    request = get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
