#!/usr/bin/python3
"""Returns the list of available attribures and methods"""


def lookup(obj):
    """Looks up all attribues and methods usinf the dir function"""

    List = dir(obj)
    return List
