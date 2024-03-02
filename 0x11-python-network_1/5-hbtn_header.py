#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
from sys import argv
from requests import get, request


if __name__ == "__main__":
    url = argv[1]

    request = get(url)
    print(request.headers.get("X-Request-Id"))
