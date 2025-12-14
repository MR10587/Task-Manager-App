# importing list of tasks
import tasks


def add_task(task, priority):
    """Add a task with its priority."""
    tasks.tasks.append({task: priority})
    print(f'✅ Task "{task}" with priority "{priority}" added.')


def view_tasks():
    """Print all tasks with their priorities and emoji badges."""
    if not tasks.tasks:
        print("No tasks available. ✨")
        return
    for idx, task_dict in enumerate(tasks.tasks, start=1):
        for name, priority in task_dict.items():
            if str(priority).lower() in ("high", "h", "1"):
                badge = "🔥"
            elif str(priority).lower() in ("medium", "m", "2"):
                badge = "⚠️"
            else:
                badge = "🟢"
            print(f"{idx}. {name} {badge} ({priority} priority)")


def complete_task(index):
    """Mark a task as completed and remove it from the list."""
    if 0 <= index < len(tasks.tasks):
        print(f'✅ Task {index + 1} marked as completed.')
        tasks.tasks.pop(index)
    else:
        print("Invalid task index")


def remove_task(index):
    """Remove a task by index."""
    if 0 <= index < len(tasks.tasks):
        print(f'🗑️ Task {index + 1} removed.')
        tasks.tasks.pop(index)
    else:
        print("Invalid task index")
