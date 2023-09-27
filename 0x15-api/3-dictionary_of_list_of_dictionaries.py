#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to both JSON and CSV formats."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    def fetch_all_employee_data():
        url = "https://jsonplaceholder.typicode.com/users"

        try:
            # Fetch all user data
            user_response = requests.get(url)
            user_data = user_response.json()

            all_employee_data = {}

            for user in user_data:
                user_id = user["id"]
                username = user["username"]

                # Fetch TODO list data for each user
                todos_response = requests.get(url + f"/{user_id}/todos")
                todos = todos_response.json()

                # Prepare data for the user
                user_tasks = []
                for task in todos:
                    user_tasks.append({
                        "username": username,
                        "task": task["title"],
                        "completed": task["completed"]
                    })

                all_employee_data[user_id] = user_tasks

            return all_employee_data

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def export_to_json(all_employee_data):
        json_data = all_employee_data
        json_filename = "todo_all_employees.json"

        with open(json_filename, "w") as jsonfile:
            json.dump(json_data, jsonfile, indent=4)

        print(f"JSON data exported to {json_filename}.")

    all_employee_data = fetch_all_employee_data()

    if all_employee_data:
        export_to_json(all_employee_data)
