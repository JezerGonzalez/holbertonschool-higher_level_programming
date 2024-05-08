#!/usr/bin/python3
def uppercase(str):
    for idx in str:
        if 'a' <= idx <= 'z':
            upper = chr(ord(idx) - 32)
        else:
            upper = idx
        print("{}".format(upper), end="")
    print()