#!/usr/bin/python3
"""The Base Class"""


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects