#!/usr/bin/python3
"""
This module fetches posts from JSONPlaceholder.
It can print post titles or save post data into a CSV file.
"""

import requests
import json
import csv


def fetch_and_print_posts():
    """Fetch posts and print status + titles"""
    posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {posts.status_code}")

    if posts.status_code == 200:
        data = posts.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save selected fields (id, title, body) to posts.csv"""
    posts = requests.get("https://jsonplaceholder.typicode.com/posts")

    if posts.status_code == 200:
        data = posts.json()

        # Structure the data to only include id, title, and body
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        # Write to CSV file
        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)
