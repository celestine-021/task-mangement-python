try:
    from task_utils import add_task, complete_task, get_pending_tasks, get_progress, list_tasks
    from validation import validate_menu_choice, validate_task_title, validate_task_index
except ModuleNotFoundError:
    # Fallback implementations in case the helper modules aren't available
    def add_task(tasks, title, description="", due_date=None, priority=None):
        task = {"title": title.strip(), "description": description.strip() if isinstance(description, str) else description, "due_date": due_date, "priority": priority, "completed": False}
        tasks.append(task)
        return task

    def complete_task(tasks, index):
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            return True
        return False

    def get_pending_tasks(tasks):
        return [task for task in tasks if not task.get("completed", False)]

    def get_progress(tasks):
        total = len(tasks)
        if total == 0:
            return 0.0
        completed = sum(1 for task in tasks if task.get("completed", False))
        return completed / total * 100

    def list_tasks(tasks):
        print("\nAll tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task.get("completed", False) else "Pending"
            print(f"{index}. {task['title']} [{status}]")

    def validate_task_title(title):
        return isinstance(title, str) and len(title.strip()) > 0

    def validate_menu_choice(choice):
        return choice in {"0", "1", "2", "3", "4", "5"}

    def validate_task_index(task_number, tasks):
        if not isinstance(task_number, str) or len(task_number.strip()) == 0:
            return None
        if not task_number.isdigit():
            return None
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            return index
        return None

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
        try:
            choice_raw = input("Choose an option: ")
        except EOFError:
            break
        choice = choice_raw.strip()

        if not validate_menu_choice(choice):
            print("Please enter a valid option from 0 to 5.")
            continue

        if choice == "1":
            try:
                title_raw = input("Enter the task title: ")
            except EOFError:
                break
            title = title_raw.strip()
            if not validate_task_title(title):
                print("Task title cannot be empty. Please try again.")
                continue
            try:
                description = input("Enter the task description: ").strip()
            except EOFError:
                description = ""
            try:
                due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
            except EOFError:
                due_date = None
            try:
                priority = input("Enter priority (1-5): ").strip()
            except EOFError:
                priority = None
            add_task(tasks, title, description, due_date, priority)
            print("Task added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available to mark complete.")
                continue
            list_tasks(tasks)
            try:
                task_number = input("Enter the number of the task to complete: ").strip()
            except EOFError:
                break
            try:
                index = validate_task_index(task_number, tasks)
            except ValueError:
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
