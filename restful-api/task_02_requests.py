#!/usr/bin/python3
"""
Module task_02_requests
Consuming and processing data from an API using Python

Fetches posts from the JSONPlaceholder API, prints their titles, and saves
selected post fields to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from the API and print the response status and titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts from the API and save selected fields to ``posts.csv``.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        formatted = []

        for post in posts:
            formatted.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
            )

        name = "posts.csv"
        field = ["id", "title", "body"]

        with open(name, mode="w", encoding="utf-8", newline="") as file:
            dictwriter = csv.DictWriter(file, fieldnames=field)
            dictwriter.writeheader()
            dictwriter.writerows(formatted)
