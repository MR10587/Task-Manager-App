# importing all functions from ui_of_app module
from ui_of_app import *

# Menu
def menu():
    while True:
        # Texts in menu
        print('Welcome to Task Manager')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Mark Task as Completed')
        print('4. Remove Task')
        print('5. Exit')
        # Try/except block to catch non-integer inputs
        try:
            # choice input
            choice = int(input('Choose an option: '))
            # If/elif/else block to handle choices
            if choice == 1:
                task = input('Enter the task: ')
                # Priority input with validation loop
                while True:
                    priority = input('What is importance(low, medium, high): ')
                    if priority in ['low', 'medium', 'high']:
                        break
                    else:
                        print('Please enter low, medium, or high')
                # Call add_task function for inputting 1
                add_task(task, priority)
            elif choice == 2:
                # Call view_tasks function for inputting 2
                view_tasks()
            elif choice == 3:
                # Input index to mark task as completed
                if tasks.tasks == []:
                    print("No tasks available.")
                    continue
                index = int(input('Enter the task number to mark as completed: ')) - 1
                # Call complete_task function for inputting 3
                complete_task(index)
            elif choice == 4:
                # Input index to remove task
                if tasks.tasks == []:
                    print("No tasks available.")
                    continue
                index = int(input('Enter the task number to remove: ')) - 1
                # Call remove_task function for inputting 4
                remove_task(index)
            elif choice == 5:
                # Exit the program for inputting 4
                break
            else:
                # Handle invalid integer inputs
                print('Enter 1, 2, 3, or 4')
        except ValueError:
            print('Enter an integer')
            

# Run the menu function if this file is executed directly
if __name__ == '__main__':
    print(tasks.tasks)
