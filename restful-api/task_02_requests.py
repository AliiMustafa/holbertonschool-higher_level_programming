#!/usr/bin/python3
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
def fetch_and_print_posts():
    r = requests.get(url)

    print(f"Status Code: {r.status_code}")
    
    data = r.json()

    for title in data:
        print(title["title"])

def fetch_and_save_posts():
    r = requests.get(url)
    if r.status_code == 200:
        with open("posts.csv", "w", newline='') as file:
            data = r.json()
            fields = ["id", "title", "body"]
            w = csv.DictWriter(file, fieldnames=fields)
            w.writeheader()
            for i in data:
                w.writerow({key: value for key, value in i.items() if key != "userId"})

fetch_and_save_posts()