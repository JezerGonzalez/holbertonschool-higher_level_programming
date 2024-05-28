#!/usr/bin/python3
"""Appends a string at the end of a text file and returns the number of characters added"""


def append_write(filename="", text=""):
    """Apends and returns number of characters"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
