#!/usr/bin/python3
"""save_to_json_file module"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    string = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(string)
