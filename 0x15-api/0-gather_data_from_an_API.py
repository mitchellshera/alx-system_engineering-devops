#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

def get_employee_todo_progress(user_id):
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()

    # Fetch TODO list data
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task['title'] for task in todos if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get('name'), len(completed_tasks), len(todos)))
    
    for task in completed_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py  <user_id>")
    else:
        user_id = sys.argv[1]
        get_employee_todo_progress(user_id)
