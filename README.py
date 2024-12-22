# To-Do-List-App-in-Python

def display_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "done": False})
    print(f"Task '{task_name}' added!")

def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
