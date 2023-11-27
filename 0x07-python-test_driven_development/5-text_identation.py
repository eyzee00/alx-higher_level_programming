#!/usr/bin/pyhton3
"""Module defining text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text, end="")