#!/usr/bin/python3
"""Shapes, Interfaces and Duck Typing"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract Class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Class that checks the cricle shape"""

    def __init__(self, radius):
        if type(radius) in [int, float]:
            self.radius = abs(radius)

    def area(self):
        return (pi * (self.radius ** 2))

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    """class that checks the rectangle shape"""

    def __init__(self, width=0, height=0):
        if type(width) in [int, float]:
            self.width = width
        if type(height) in [int, float]:
            self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    """Prints the information of the shape"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
