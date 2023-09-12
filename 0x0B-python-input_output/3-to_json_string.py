#!/usr/bin/python3
"""this module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of a string object"""
    return json.dumps(my_obj)
