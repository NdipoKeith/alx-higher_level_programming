#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """invert int operators == and !="""

    def __eq__(self, value):
        """override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior"""
        return self.real == value