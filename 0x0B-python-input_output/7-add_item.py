#!/usr/bin/python3
"""add_item module"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(list):
    """adds all arguments to a Python list, and then save them to a file"""

    filename = "add_item.json"

    if os.path.isfile(filename):
        new_list = load_from_json_file(filename)
        new_list += list[1:]
    else:
        new_list = []
    save_to_json_file(new_list, filename)


if __name__ == '__main__':
    add_item(sys.argv)
