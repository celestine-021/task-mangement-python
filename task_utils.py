def add_task(tasks, title):
    """Add a new task to the task list."""
    task = {
        "title": title.strip(),
        "completed": False,
    }
    tasks.append(task)
    return task


def complete_task(tasks, index):
    """Mark the selected task as completed."""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False


def get_pending_tasks(tasks):
    """Return a list of tasks that are not yet completed."""
    return [task for task in tasks if not task.get("completed", False)]


def get_progress(tasks):
    """Return completion progress as a percentage."""
    total = len(tasks)
    if total == 0:
        return 0.0
    completed = sum(1 for task in tasks if task.get("completed", False))
    return completed / total * 100


def list_tasks(tasks):
    """Print all tasks with completion status."""
    print("\nAll tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.get("completed", False) else "Pending"
        print(f"{index}. {task['title']} [{status}]")
