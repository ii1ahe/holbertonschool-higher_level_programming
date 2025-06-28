#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a subclass of the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class
    (directly or indirectly), but not if it's exactly a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
