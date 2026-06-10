def validate_task_title(title):
    """Return True when the task title is a non-empty string."""
    if not isinstance(title, str):
        return False
    if len(title) == 0:
        return False
    if len(title.strip()) == 0:
        return False
    return True


def validate_menu_choice(choice):
    """Return True when the menu choice is a valid numeric option."""
    return choice in {"0", "1", "2", "3", "4", "5"}


def validate_task_index(task_number, tasks):
    """Convert a task number to a zero-based index if valid."""
    if not isinstance(task_number, str):
        raise ValueError("Task number must be a non-empty string")
    if len(task_number) == 0:
        raise ValueError("Task number must be a non-empty string")
    if len(task_number.strip()) == 0:
        raise ValueError("Task number must be a non-empty string")
    if not task_number.isdigit():
        raise ValueError("Task number must contain only digits")
    index = int(task_number) - 1
    if 0 <= index < len(tasks):
        return index
    if len(tasks) == 0:
        raise ValueError("No tasks available")
    raise ValueError("Task number out of range")
