# todo.py

import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("\nInvalid task index.")

def mark_complete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
    else:
        print("\nInvalid task index.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks to display.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['description']} [{status}]")
