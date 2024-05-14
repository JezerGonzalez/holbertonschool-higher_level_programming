#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name = []
    highscore = 0
    for key, value in a_dictionary.items():
        if value > highscore:
            highscore = value
            name = key
    return name
