solution to higher level programming exercises

0. Write a function that reads a text file (UTF8) and prints it to stdout:

        Prototype: def read_file(filename=""):
        You must use the with statement
        You don’t need to manage file permission or file doesn't exist exceptions.
        You are not allowed to import any module

1. Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

        Prototype: def write_file(filename="", text=""):
        You must use the with statement
        You don’t need to manage file permission exceptions.
        Your function should create the file if doesn’t exist.
        Your function should overwrite the content of the file if it already exists

2. Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

        Prototype: def append_write(filename="", text=""):
        If the file doesn’t exist, it should be created
        You must use the with statement
        You don’t need to manage file permission or file doesn't exist exceptions.
        You are not allowed to import any module   

3. Write a function that returns the JSON representation of an object (string):

        Prototype: def to_json_string(my_obj):
        You don’t need to manage exceptions if the object can’t be serialized.

4. Write a function that returns an object (Python data structure) represented by a JSON string:

        Prototype: def from_json_string(my_str):
        You don’t need to manage exceptions if the JSON string doesn’t represent an object.
 
5. Write a function that writes an Object to a text file, using a JSON representation:

        Prototype: def save_to_json_file(my_obj, filename):
        You must use the with statement
        You don’t need to manage exceptions if the object can’t be serialized.
        You don’t need to manage file permission exceptions.

6. Write a function that creates an Object from a “JSON file”:

        Prototype: def load_from_json_file(filename):
        You must use the with statement
        You don’t need to manage exceptions if the JSON string doesn’t represent an object.
        You don’t need to manage file permissions / exceptions.

7. Write a script that adds all arguments to a Python list, and then save them to a file:

        You must use your function save_to_json_file from 5-save_to_json_file.py
        You must use your function load_from_json_file from 6-load_from_json_file.py
        The list must be saved as a JSON representation in a file named add_item.json
        If the file doesn’t exist, it should be created
        You don’t need to manage file permissions / exceptions.