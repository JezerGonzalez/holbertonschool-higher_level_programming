#!/usr/bin/python3
"""Rectangle class that inherits from base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Start of the subclass"""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
