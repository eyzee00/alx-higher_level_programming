#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    request = post(url, data=value)
    print(request.text)
