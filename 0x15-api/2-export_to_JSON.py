#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to both JSON and CSV formats."""

import csv
import json
import requests
import sys

def fetch_employee_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data
    user_response = requests.get(url + f"users/{user_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        return None, None
    
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODO list data
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    return user_data, username, todos

def export_to_csv(user_id, username, todos):
    csv_filename = f"{user_id}.csv"
    
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todos:
            csv_writer.writerow([user_id, username, task.get("completed"), task.get("title")])

    print(f"CSV data exported to {csv_filename}.")

def export_to_json(user_id, username, todos):
    json_data = {user_id: []}
    
    for task in todos:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        json_data[user_id].append(task_data)

    json_filename = f"{user_id}.json"
    
    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"JSON data exported to {json_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <user_id>")
    else:
        user_id = sys.argv[1]
        user_data, username, todos = fetch_employee_data(user_id)

        if user_data and todos:
            export_to_csv(user_id, username, todos)
            export_to_json(user_id, username, todos)
