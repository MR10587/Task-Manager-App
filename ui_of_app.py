# importing list of tasks
import tasks

# Function to add a task with its priority
def add_task(task, priority):
    # Append task as a dictionary to the tasks list
    tasks.tasks.append({task: priority})
    print(f'Task "{task}" with priority "{priority}" added.')
    
# Function to view all tasks with their priorities
def view_tasks():
    # Iterate through tasks and print them with their priorities
    if tasks.tasks == []:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks.tasks, start=1):
        for task, priority in task.items():
            print(f"{idx}. {task}({priority} priority)")
            
# Function to mark a task as completed
def complete_task(index):
    # Remove task from the tasks list based on index
    if 0 <= index < len(tasks.tasks):
        print(f'Task {index + 1} marked as completed.')
        tasks.tasks.pop(index)
    else:
        print("Invalid task index")

# Function to delete task
def remove_task(index):
    # Remove task from the tasks list based on index
    if 0 <= index < len(tasks.tasks):
        print(f'Task {index + 1} removed.')
        tasks.tasks.pop(index)
    else:
        print("Invalid task index")
