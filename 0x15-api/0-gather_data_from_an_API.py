#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys
import requests

def get_employee_todo_progress(employee_id):
    # Define the API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for Employee ID {employee_id}")
        return

    # Fetch TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    if todo_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list data for Employee ID {employee_id}")
        return

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Display TODO list progress
    employee_name = user_data['name']
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter Employee ID: "))
    get_employee_todo_progress(employee_id)
