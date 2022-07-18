#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as error:
        print("{}{}".format("Exception: ", error), file=sys.stderr)
        return None
