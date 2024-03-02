#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]

    request = Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode("ascii"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
