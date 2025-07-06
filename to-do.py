import sys

tasks = []

def list_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python to-do.py [add/list] [task]")
    else:
        command = sys.argv[1]

        if command == "list":
            list_tasks()
        elif command == "add":
            if len(sys.argv) < 3:
                print("Please provide a task to add.")
            else:
                task = " ".join(sys.argv[2:])
                add_task(task)
        else:
            print("Unknown command. Use 'add' or 'list'.")
