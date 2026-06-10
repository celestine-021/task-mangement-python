from task_utils import add_task, complete_task, get_pending_tasks, get_progress, list_tasks
from validation import validate_menu_choice, validate_task_title, validate_task_index

def display_menu():
    print("\nTask Management System")
    print("1. Add a task")
    print("2. Mark a task complete")
    print("3. View pending tasks")
    print("4. View all tasks")
    print("5. Track progress")
    print("0. Exit")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if not validate_menu_choice(choice):
            print("Please enter a valid option from 0 to 5.")
            continue

        if choice == "1":
            title = input("Enter the task title: ").strip()
            if not validate_task_title(title):
                print("Task title cannot be empty. Please try again.")
                continue
            add_task(tasks, title)
            print(f"Task added: '{title}'")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available to mark complete.")
                continue
            list_tasks(tasks)
            task_number = input("Enter the number of the task to complete: ").strip()
            index = validate_task_index(task_number, tasks)
            if index is None:
                print("Please enter a valid task number.")
                continue
            complete_task(tasks, index)
            print("Task marked complete.")

        elif choice == "3":
            pending = get_pending_tasks(tasks)
            if len(pending) == 0:
                print("There are no pending tasks.")
            else:
                print("\nPending tasks:")
                for number, task in enumerate(pending, start=1):
                    print(f"{number}. {task['title']}")

        elif choice == "4":
            if len(tasks) == 0:
                print("No tasks have been added yet.")
            else:
                list_tasks(tasks)

        elif choice == "5":
            progress = get_progress(tasks)
            print(f"Progress: {progress:.0f}% complete")

        elif choice == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
