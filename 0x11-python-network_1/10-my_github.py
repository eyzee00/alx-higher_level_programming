#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials
"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    request = get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
