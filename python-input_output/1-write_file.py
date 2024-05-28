#!/usr/bin/python3
"""
Function appends a string at the end of a text file and returns the
number of characters added
"""


def write_file(filename="", text=""):
    """Writes on file"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
