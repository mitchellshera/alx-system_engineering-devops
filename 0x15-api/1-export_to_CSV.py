#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports it to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list data
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
