#!/usr/bin/python3
"""
Returns True if an object is an instance of a class
that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Verifies if object is an instance of a class"""

    if isinstance(obj, a_class):
        return True
    return False
