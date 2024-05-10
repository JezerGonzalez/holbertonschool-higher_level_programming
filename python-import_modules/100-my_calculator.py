#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    
    a = int(argv[1])
    b = int(argv[3])
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) - 1 != 3:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operations[argv[2]](a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
