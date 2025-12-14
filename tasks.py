import json


tasks = []


def save_tasks(filename='tasks.json'):
    """Save tasks to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(tasks, f)
        print("Tasks saved.")
    except Exception as e:
        print(f"Save Error: {e}")


def load_tasks(filename='tasks.json'):
    """Load tasks from a JSON file."""
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
        print("No saved tasks found, starting fresh.")
    except Exception as e:
        print(f"Load Error: {e}")
        