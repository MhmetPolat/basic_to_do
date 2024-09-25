tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks():
    if not tasks:
        print("Task list empty.")
    else:
        print("Task:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)    
        print(f"Task deleted: {removed_task}")
    else:
        print("Invalid number!")

while True:
    print("\n 1. Add Task")
    print("2. List Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Make your choice: ")

    if choice == "1":
        task = input("The task you want to add: ")
        add_task(task)

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        list_tasks()                   
        task_number = int(input("Enter the task number you want to delete: "))
        delete_task(task_number)

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice, please try again!")
