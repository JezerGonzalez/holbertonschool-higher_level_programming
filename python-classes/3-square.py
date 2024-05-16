#!/usr/bin/python3
"""Empty Class that defines a square"""


class Square():
    """Start of the Class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
