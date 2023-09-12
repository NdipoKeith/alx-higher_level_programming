#!/usr/bin/python3
"""this module defines a file-appending function."""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
