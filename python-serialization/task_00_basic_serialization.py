#!/usr/bin/python3
"""Documentation"""
import json


def serialize_and_save_to_file(data, filename):
    """dump data into a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """load data from a file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
