
from datetime import datetime


def get_employee_details(name, joining_date):
    """Return basic employee details with experience in days."""
    joined = datetime.fromisoformat(joining_date)
    experience_days = (datetime.now() - joined).days

    return {
        "name": name,
        "joining_date": joining_date,
        "experience_days": experience_days,
    }


def is_recent_joiner(joining_date, days=90):
    """Check whether an employee joined within the given number of days."""
    joined = datetime.fromisoformat(joining_date)
    return (datetime.now() - joined).days <= days