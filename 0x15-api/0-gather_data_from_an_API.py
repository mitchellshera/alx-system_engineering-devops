#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

def get_employee_todo_progress(user_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetch TODO list data
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todo_data if task['completed']]
        total_tasks = len(todo_data)

        # Display employee's progress
        print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        print(f"EMPLOYEE_NAME: {user_data['name']}")
        print(f"NUMBER_OF_DONE_TASKS: {len(completed_tasks)}")
        print(f"TOTAL_NUMBER_OF_TASKS: {total_tasks}")

        for task_title in completed_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
    else:
        user_id = int(sys.argv[1])
        get_employee_todo_progress(user_id)
