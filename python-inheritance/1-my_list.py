#!/usr/bin/python3
"""A class that inherits from List"""


class MyList(list):
    """New Class"""

    def print_sorted(self):
        """A Method that prints the inherited attributes"""

        print(f"{sorted(self)}")
