#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports it to CSV format."""

import csv
import requests
import sys

def get_employee_todo_progress(user_id):
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list data
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Display TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get('name'), len(completed_tasks), len(todos)))
    
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

    # Export to CSV
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in completed_tasks:
            csv_writer.writerow([user_id, username, task.get("completed"), task.get("title")])
    
    print(f"CSV data exported to {csv_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
    else:
        user_id = sys.argv[1]
        get_employee_todo_progress(user_id)
