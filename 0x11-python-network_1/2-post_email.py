#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")

    request = Request(url, data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
