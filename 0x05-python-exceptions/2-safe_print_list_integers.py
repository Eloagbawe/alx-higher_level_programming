#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 1
    index = 0
    length = 0

    for y in my_list:
        length += 1
    while counter <= x:
        try:
            if (index == (length - 1)) and (x <= length):
                break
            print("{:d}".format(my_list[index]), end="")
            counter += 1
        except (TypeError, ValueError):
            pass
        finally:
            index += 1
    print("")
    return counter - 1
