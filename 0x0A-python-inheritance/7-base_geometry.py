#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """Base Geometry Class"""
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) !=  int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
        else:
            pass
