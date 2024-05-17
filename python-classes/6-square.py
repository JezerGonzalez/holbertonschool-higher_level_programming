#!/usr/bin/python3
"""Empty Class that defines a square"""


class Square():
    """Start of the Class"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for element in position:
            if type(element) is not int and element < 0:
                raise TypeError("position must be a tuple of 2 positive \
integers")
        self.__position = position

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value"""
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for element in value:
            if type(element) is not int and element < 0:
                raise TypeError("position must be a tuple of 2 positive \
integers")
        self.__position = value

    def my_print(self):
        """Prints the square using the '#' character"""
        if self.__size == 0:
            print()
            return
        else:
            for index in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
