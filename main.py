from todo import add_task, remove_task, mark_complete, list_tasks

def display_menu():
    print("\n\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Complete")
    print("4. List Tasks")
    print("5. Exit")
    print("=========================")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        print()
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to remove: "))
            remove_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as complete: "))
            mark_complete(index)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            print("Exiting the program... Goodbye!\n")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
