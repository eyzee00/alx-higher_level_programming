#!/usr/bin/python3
"""Module defining lookup function"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
