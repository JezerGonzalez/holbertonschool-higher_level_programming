#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    for index in range(0, len(my_list)):
        if idx < 0 or idx > len(my_list):
            return my_list
        elif index == idx:
            new_list[index] = element
            return new_list
