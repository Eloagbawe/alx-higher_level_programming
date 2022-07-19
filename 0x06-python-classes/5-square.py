#!/usr/bin/python3

"""
This module defines a Square class

"""


class Square:

    """Square class

        Attributes:
        attr1(size): size of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area: returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """my_print: prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format("#"), end="")
                print("")
