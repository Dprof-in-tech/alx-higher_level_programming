#!/usr/bin/python3
"""defining a class rectangle"""


class Rectangle:
    """class rectangle defined"""
    def __init__(self, size=0, height=0):
        """defined the initialization for class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self, value):
        return self.__width

    @property
    def height(self, value):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
