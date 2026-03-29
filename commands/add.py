"""Add task command."""

from utils.validation import validate_description, save_tasks
from utils.paths import get_tasks_file


def add_task(description):
    """Add a new task."""
    description = validate_description(description)

    tasks = []
    tasks_file = get_tasks_file()
    if tasks_file.exists():
        import json
        tasks = json.loads(tasks_file.read_text())

    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "done": False})

    save_tasks(tasks)
    print(f"Added task {task_id}: {description}")
