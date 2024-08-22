import os

TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split('|')
                tasks.append({"task": task, "completed": status == "True"})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")


def add_task(tasks, task_description):
    tasks.append({"task": task_description, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{index}. {task['task']} - {status}")


def complete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task_description = input("Enter the task description: ")
            add_task(tasks, task_description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to mark as completed: "))
                complete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_index = int(input("Enter the task number to delete: "))
                delete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
