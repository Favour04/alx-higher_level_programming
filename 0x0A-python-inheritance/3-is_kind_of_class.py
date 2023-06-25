#!/usr/bin/python3
"""
The module contian the
function is_kind_of_class
which validated if obj is
an instance of the class
a_class or inherited
"""


def is_kind_of_class(obj, a_class):
    """
    The function as defined
    in the doc above is wrr
    iten below
    """
    if isinstance(obj, a_class) or type(obj) is a_class:
        return True
    else:
        return False
