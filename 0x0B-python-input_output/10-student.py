#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            for y in self.__dict__:
                if x == y:
                    new_dict.update({y : self.__dict__[y]})
        return new_dict
