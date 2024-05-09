#!/usr/bin/python3
from sys import argv
if argv == 1:
    print("0 arguments.")
elif argv == 2:
    print("1 argument:")
    print("1 {}".format(argv[1]))
else:
    print("{} arguments:".format(len(argv)- 1))
    for index in range(1, len(argv)):
        print("{}: {}".format(index, argv[index]))
