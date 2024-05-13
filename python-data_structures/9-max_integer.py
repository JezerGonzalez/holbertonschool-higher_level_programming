#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    bigger_number = my_list[0]
    for index in my_list:
        if index > bigger_number:
            bigger_number = index
    return bigger_number