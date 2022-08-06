#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute"""
        self.__width = value

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute"""
        self.__height = value

    @property
    def x(self):
        """getter for the height attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the height attribute"""
        self.__x = value

    @property
    def y(self):
        """getter for the height attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the height attribute"""
        self.__y = value
