#!/usr/bin/python3
"""Opens, reads and prints the file in my_file_0.txt"""


def read_file(filename=""):
    """Reads and prints the file"""
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
