#!/usr/bin/python3
"""
This module defines the BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """
    BaseGeometry class for geometric operations.
    """

    def area(self):
        """
        Raises an Exception to indicate area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
