#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = int(str(number)[-1])
    print("{}".format(lastdigit), end="")
    return lastdigit
