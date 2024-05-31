#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""
import csv, requests


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder."""

    data = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {data.status_code}")
    if data.status_code >= 200 and data.status_code < 300:
        for post in data.json():
            print(post["title"])

def fetch_and_save_posts():
    """Prints a list of dictionaries with id, title and body"""
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    if request.status_code >= 200 and request.status_code < 300:
        data_list = []
        for posts in request.json():
            data_list.append({'id': posts['id'], 'title': posts['title'],
                            'body': posts['body']})

    with open("posts.csv", 'w', encoding="utf-8") as file:
        map = ['id', 'title', 'body']
        writer = csv.DictReader(file, fieldnames=map)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)
