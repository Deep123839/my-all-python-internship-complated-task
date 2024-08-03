#-------------------------------------------------------------------------------
import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def update_task(index, new_description):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['description'] = new_description
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Task not found.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Task not found.")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Task not found.")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "✔️" if task['completed'] else "❌"
        print(f"{i + 1}. {task['description']} [{status}]")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            new_description = input("Enter new task description: ")
            update_task(index, new_description)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == '4':
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(index)
        elif choice == '5':
            list_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
