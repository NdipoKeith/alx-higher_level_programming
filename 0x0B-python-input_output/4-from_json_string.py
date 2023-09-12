#!/usr/bin/python3
"""this module defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """returns the Python object representation of a JSON string"""
    return json.loads(my_str)
