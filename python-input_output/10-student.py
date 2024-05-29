#!/usr/bin/python3
"""Class that defines a student"""


class Student:
    """Start of the class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if not type(attrs) is list:
            return self.__dict__
        if all(type(item) is str for item in attrs):
            dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dict[key] = value
            return dict
