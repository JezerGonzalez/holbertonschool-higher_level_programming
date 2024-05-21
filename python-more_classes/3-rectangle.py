#!/usr/bin/python3
"""Method that prints out a rectangle"""


class Rectangle:
    """Start of the rectangle class"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Gets the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates and sets the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates and sets the height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Que se me pegue el culo"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for idex in range(self.__height):
            string += "#" * self.__width + "\n"
        return string
