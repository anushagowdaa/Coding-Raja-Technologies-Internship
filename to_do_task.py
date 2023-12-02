import json
import os
import datetime

# Task object
class Task:
    def __init__(self, id, name, priority, due_date, completed):
        self.id = id
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Priority: {self.priority}, Due Date: {self.due_date}, Completed: {self.completed}"

# Function to create a new task
def create_task(name, priority, due_date):
    new_task = Task(len(tasks) + 1, name, priority, due_date, False)
    tasks.append(new_task)
    return new_task

# Function to delete a task
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id != id]

# Function to update a task's properties
def update_task(id, name=None, priority=None, due_date=None, completed=None):
    for task in tasks:
        if task.id == id:
            if name:
                task.name = name
            if priority:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            if completed is not None:
                task.completed = completed
            return task

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a file
def load_tasks():
    global tasks
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = [Task(**task) for task in json.load(f)]

# Function to print tasks
def print_tasks():
    for task in tasks:
        print(task)

# Load tasks from the file
load_tasks()

# Example usage
create_task("Buy Groceries", "high", datetime.date(2022, 5, 10))
create_task("Submit Assignment", "medium", datetime.date(2022, 5, 12))

update_task(1, name="Buy Fruits", priority="medium", due_date=datetime.date(2022, 5, 11))
delete_task(2)

# Save tasks to the file
save_tasks(tasks)

# Print tasks
print_tasks()