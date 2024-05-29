#!/usr/bin/python3
import csv, json


def convert_csv_to_json(filename):
    """Converting the csv file to json format"""
    try:
        data = []
        with open(filename, "r", encoding="utf-8") as file:
            csvfile = csv.DictReader(file)
            for row in csvfile:
                data.append(row)
        with open("data.json", "w", encoding="utf-8") as Jfile:
            json.dump(data, Jfile)
        return True
    except Exception:
        return False
