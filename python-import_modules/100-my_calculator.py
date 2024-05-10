#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) - 1 != 3:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if sys.argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = operations[sys.argv[2]](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
