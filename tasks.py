import json


tasks = []


# function to save tasks
def save_tasks(filename='tasks.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(tasks, f)
            print("Tasks saved")
    except Exception as e:
        print(f"Save Error: {e}")


# function to load tasks
def load_tasks(filename='tasks.json'):
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
        print("Tasks loaded")
    except FileNotFoundError:
        tasks = []
        print("No saved tasks found, starting fresh.")
    except Exception as e:
        print(f"Load Error: {e}")
