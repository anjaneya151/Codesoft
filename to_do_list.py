# to_do_list.py

todo_list = []

def show_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

def remove_task(task_num):
    if 0 < task_num <= len(todo_list):
        removed = todo_list.pop(task_num - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: add, remove, show, exit")
    choice = input("Enter your choice: ").lower()

    if choice == "add":
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == "remove":
        show_tasks()
        task_num = int(input("Enter task number to remove: "))
        remove_task(task_num)
    elif choice == "show":
        show_tasks()
    elif choice == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")
