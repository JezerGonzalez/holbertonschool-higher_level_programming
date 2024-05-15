#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for index in range(0, x):
            print("{:d}".format(my_list[index]), end="")
            number += 1
    except IndexError:
        print()
        return number
    print()
    return number
