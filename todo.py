import os
import json

TASKS_FILE = "tasks.json"
COMPLETED = True
NOT_COMPLETED = False

def load_tasks():
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading tasks: {e}")
    return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": NOT_COMPLETED})
    save_tasks(tasks)
    print(f"=> Task '{description}' added.")

def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"=> Task '{removed_task['description']}' removed.")
    else:
        print("\n--- Invalid task index. ---")

def mark_complete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = COMPLETED
        save_tasks(tasks)
        print(f"=> Task '{tasks[index]['description']}' marked as completed.")
    else:
        print("Invalid task index.")

def list_tasks():
    tasks = load_tasks()
    print("========== LIST OF TASKS ==========")    
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i} - {task['description']} [{status}]")
    print("===================================")
