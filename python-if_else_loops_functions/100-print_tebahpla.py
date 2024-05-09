#!/usr/bin/python3
for idx in range(122, 96, -1):
    print("{:c}".format(idx if idx % 2 == 0 else idx - 32), end="")