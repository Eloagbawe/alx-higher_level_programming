#!/usr/bin/python3

"""
This module defines a Square class

"""


class Square:

    """Square class

        Attributes:
        attr1(size): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @property
    def position(self):
        """gets the position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple and (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area: returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """my_print: prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for k in range(self.__size):
                    print("{}".format("#"), end="")
                print("")
