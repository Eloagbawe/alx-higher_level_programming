#!/usr/bin/python3
"""Look up module
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    """

    x = obj()
    print(dir(x))
