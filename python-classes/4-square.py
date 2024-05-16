#!/usr/bin/python3
"""Empty Class that defines a square"""


class Square():
    """Start of the Class"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
