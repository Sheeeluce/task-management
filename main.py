# Import functions from task_manager.task_utils package
from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


# Define the main function
def main():

    tasks = []
    
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date(YYYY-MM-DD): ")

            success, message = add_task(title, description, due_date)
            if success:
                print(message)
            else:
                print("No task added")

        elif choice == "2":
            try:
                index = int(input("Enter task index: "))
                mark_task_as_complete(index, tasks)
            except ValueError:
                print("Invalid index")

        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if not pending:
                print("No pending tasks")
            else:
                for task in pending:
                    print(task)

        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.2f}%")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
