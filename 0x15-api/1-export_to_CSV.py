#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports it to CSV format."""

import json
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

    # Prepare and export data to JSON
    json_data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(json_data, jsonfile)
