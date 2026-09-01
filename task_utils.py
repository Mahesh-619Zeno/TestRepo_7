from datetime import datetime


def is_overdue(due_date):
    """Check whether the given due date has passed."""
    if not due_date:
        return False

    try:
        return datetime.fromisoformat(due_date) < datetime.now()
    except ValueError:
        return False


def get_task_age(created_date):
    """Return the number of days since the task was created."""
    created = datetime.fromisoformat(created_date)
    return (datetime.now() - created).days

