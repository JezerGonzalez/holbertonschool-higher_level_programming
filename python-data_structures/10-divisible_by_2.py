#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for index in my_list:
        if index % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
