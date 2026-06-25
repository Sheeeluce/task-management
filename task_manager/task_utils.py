from datetime import datetime

# Import validation functions
from task_manager.validation import(
    validate_task_title,
    validate_task_description,
    validate_due_date
)


# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(task)
        
        return True, "Task added successfully!"
    except ValueError as e:
        return False, str(e)
    #print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 1 or index > len(tasks):
        print("Invalid task index")
        return
    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = []

    for task in tasks:
        if not task["completed"]:
            pending.append(task)
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks))*100
    return progress