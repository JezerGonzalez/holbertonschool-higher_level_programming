#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_letter = sentence[:1] if len(sentence) > 0 else None
    return (length, first_letter)
