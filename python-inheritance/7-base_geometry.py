#!/usr/bin/python3
"""Base geometry"""


class BaseGeometry:
    """Start of the class"""

    def area(self):
        """raises an exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
