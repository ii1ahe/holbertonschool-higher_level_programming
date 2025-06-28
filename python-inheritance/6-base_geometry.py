#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry serves as a base class for geometric shapes.
    """

    def area(self):
        """
        Raises an Exception to indicate area() is not implemented.
        """
        raise Exception("area() is not implemented")
