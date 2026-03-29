"""Mark task done command."""

from utils.validation import validate_task_id, validate_task_file, load_tasks, save_tasks


def mark_done(task_id):
    """Mark a task as complete."""
    tasks_file = validate_task_file()
    if not tasks_file:
        print("No tasks found!")
        return

    tasks = load_tasks()
    validate_task_id(tasks, task_id)

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done: {task['description']}")
            return

    print(f"Task {task_id} not found")
