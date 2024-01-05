#!/usr/bin/python3
"""defining a class square"""


class Square:
    """class square defined"""
    def __init__(self, size=0):
        """defined the initialization for class square"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve self"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set size"""
        if not isInstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
         """return area of a square"""
         return self.__size * self.__size
