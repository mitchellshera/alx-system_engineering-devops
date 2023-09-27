#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_todo_list_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t for t in todos if t.get("completed")]
    total_tasks = len(todos)
    completed_tasks = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_tasks, total_tasks))
    
    for task in completed:
        print("\t{}".format(task["title"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    try:
        int(employee_id)  # Ensure the input is an integer
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_todo_list_progress(employee_id)
