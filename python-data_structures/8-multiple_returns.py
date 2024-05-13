#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence):
        first_letter = sentence[:1]
    else:
        None
    return (length, first_letter)
