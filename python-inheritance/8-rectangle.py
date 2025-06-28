#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates width and height as positive integers.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated width and height.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
