#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
"""
from sys import argv
from requests import post, get


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    request = post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = request.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(get("id"), get("name")))
    except ValueError:
        print("Not a valid JSON")
