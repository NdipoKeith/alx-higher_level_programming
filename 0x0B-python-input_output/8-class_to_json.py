#!/usr/bin/python3
"""this module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """returns the dictionary representation of a simple data structure"""
    return obj.__dict__
