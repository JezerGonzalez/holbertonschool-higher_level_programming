#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for idx in range(len(my_list)):
        if my_list[idx] == search:
            new[idx] = replace
        else:
            new[idx] = my_list[idx]
    return new
