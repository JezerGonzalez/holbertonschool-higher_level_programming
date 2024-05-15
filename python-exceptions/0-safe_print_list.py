#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(0, x):
            print("{:d}".format(my_list[index]), end="" if index < x - 1 else "\n")
    except IndexError:
        print()
        return index
    return index + 1
