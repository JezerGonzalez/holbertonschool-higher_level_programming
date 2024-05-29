#!/usr/bin/python3
"""Documentation"""
import pickle


class CustomObject:
    """Start of class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes"""
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is student {self.is_student}")

    def serialize(self, filename):
        """Dump data into a file"""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Load data from a file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
