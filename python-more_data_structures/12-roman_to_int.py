#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    previous = 0
    for char in reversed(roman_string):
        if char in romans:
            number = romans[char]
            if number < previous:
                result -= number
            else:
                result += number
            previous = number
    return result
