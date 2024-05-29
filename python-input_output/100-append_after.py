#!/usr/bin/python3
"""
Inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends on file"""
    text = ""
    with open(filename) as file:
        for item in file:
            text += item
            if search_string in item:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
