import re
from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Title must be string"
    if len(title.strip()) == 0:
        return False, "Title cannot be empty"
    if len(title) < 3:
        return False, "Title too short"
    return True, "Valid"
    
def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Description must be a string"
    if len(description.strip()) == 0:
        return False, "Description can't be empty"
    if len(description) < 5:
        return False, "Description too short"
    
def validate_due_date(due_date):  
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, "Valid"
    except ValueError:
        return False, "Invalid date format. Use YYY-MM-DD"