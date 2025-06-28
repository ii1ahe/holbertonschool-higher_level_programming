#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square with size validated as a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
