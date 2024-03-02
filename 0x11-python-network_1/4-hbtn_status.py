#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from requests import get


if __name__ == "__main__":
    request = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
