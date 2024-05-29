#!/usr/bin/python3
"""
Returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of ints"""
    pascal = []
    if n <= 0:
        return pascal

    prev = []
    for i in range(n + 1):
        current = []
        for j in range(i):
            if j == 0:  # start with 1
                current.append(1)
            elif j == i - 1:  # end with 1
                current.append(1)
            else:  # calculate sum of nums directly above
                current.append(prev[j] + prev[j - 1])
        if i > 0:  # append list to list of lists & reassign previous row
            pascal.append(current)
            prev = current
    return pascal
