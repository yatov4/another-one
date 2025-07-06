tasks = []

def list_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    list_tasks()
