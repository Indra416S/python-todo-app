todos = []

def show_todos():
    if not todos:
        print("\n⚠️ No tasks yet.\n")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")
    print()

def add_todo():
    task = input("Enter a new task: ")
    todos.append(task)
    print("✅ Task added!\n")

def remove_todo():
    show_todos()
    if not todos:
        return
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(todos):
            removed = todos.pop(index - 1)
            print(f"❌ Removed: {removed}\n")
        else:
            print("⚠️ Invalid number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

while True:
    print("====== To-Do List App ======")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        remove_todo()
    elif choice == "4":
        print("✅ Exiting app... Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.\n")
