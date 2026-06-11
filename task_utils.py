

# Import validation functions
from validation import(
    validate_task_title,
    validate_task_description,
    validate_due_date
)


# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    valid_title, msg1 = validate_task_title(title)
    valid_desc, msg2 = validate_task_description(description)
    valid_date, msg3 = validate_due_date(due_date)

    if not(valid_title and valid_desc and valid_date):
        return False, f"{msg1} | {msg2} | {msg3}"
    
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    return True, "Task added successfully!"
    #print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index")
        return
    tasks[index]["completed"] = True
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