#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numbers in matrix:
        for idx in range(len(numbers)):
            print("{:d}".format(numbers[idx]), end="")
            if idx < len(numbers) - 1:
                print(" ", end="")
        print()
