#!/usr/bin/python3
'''Returns information about TODO list progress by employee ID.'''
import requests
from sys import argv

if __name__ == '__main__':
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    
    todos_response = requests.get(todos_url)
    users_response = requests.get(users_url)
    
    if todos_response.status_code != 200 or users_response.status_code != 200:
        print('Failed to retrieve data from the API.')
        exit(1)
    
    todos_data = todos_response.json()
    users_data = users_response.json()

    employee_id = int(argv[1])
    user = next((u for u in users_data if u['id'] == employee_id), None)
    
    if user is None:
        print(f'Employee with ID {employee_id} not found.')
        exit(1)
    
    tasks = [task for task in todos_data if task['userId'] == employee_id]
    completed_tasks = [task for task in tasks if task['completed']]
    
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
