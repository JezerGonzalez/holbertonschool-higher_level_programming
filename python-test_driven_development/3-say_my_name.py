#!/usr/bin/python3
"""Documentation"""


def say_my_name(first_name, last_name=""):
    """Documentation"""

    first = "first_name must be a string"
    last = "last_name must be a string"

    if type(first_name) is not str:
        raise TypeError(first)
    if type(last_name) is not str:
        raise TypeError(last)
    if last_name is "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
