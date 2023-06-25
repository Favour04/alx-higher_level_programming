#!/usr/bin/python3
"""
this module contains
inherits_from which
validate if it is
a sub_class
"""


def inherits_from(obj, a_class):
    """
    The defination of
    this function co-
    mes bellow
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
