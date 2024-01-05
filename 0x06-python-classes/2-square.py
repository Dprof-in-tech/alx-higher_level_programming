#!/usr/bin/python3
"""defining a class square"""


class Square:
    """class square defined"""
    def __init__(self, size=0):
        """defined the initialization for class square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
