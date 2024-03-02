#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    request= get(url)
    commits = request.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
