def validate_task_title(title):
    """Return True when the task title is a non-empty string."""
    return isinstance(title, str) and len(title.strip()) > 0


def validate_menu_choice(choice):
    """Return True when the menu choice is a valid numeric option."""
    return choice in {"0", "1", "2", "3", "4", "5"}


def validate_task_index(task_number, tasks):
    """Convert a task number to a zero-based index if valid."""
    if not isinstance(task_number, str) or len(task_number.strip()) == 0:
        return None
    if not task_number.isdigit():
        return None
    index = int(task_number) - 1
    if 0 <= index < len(tasks):
        return index
    return None
