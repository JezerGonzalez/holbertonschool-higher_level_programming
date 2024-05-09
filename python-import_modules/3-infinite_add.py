#!/usr/bin/python3
from sys import argv
result = 0
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        result += int(argv)
        print("{}".format(result))
        