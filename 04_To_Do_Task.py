#Mini to do app using JSON-Java Script Object Notation.

# File for storing tasks 
Task_File = 'my_tasks.json'

#Ensure the tasks file exists
import os
import json

if not os.path.exists(Task_File): #So, this condition means: "If the file does NOT exist, then do the following...".
    with open(Task_File, 'w') as file: 
        json.dump([], file) #The reason for dumping [] is usually to initialize the file with an empty list of tasks

#Step-1: Load tasks from JSON
def load_tasks():
    with open(Task_File,'r') as file:
        return json.load(file)
    
#Step-2: Save tasks to JSON 
def save_tasks(tasks):
    with open(Task_File,'w') as file:
        json.dump(tasks,file,indent=2) #Converts the Python object tasks into JSON format and writes it into the file. indent=2 makes the JSON nicely formatted with indentation (2 spaces).

#Step-3: Add a task
def add_task():
    task_name = input("Enter the task name :").strip()       
    tasks = load_tasks()
    tasks.append({"Task":task_name, "Status": "Incomplete"}) #Adds a new dictionary (task) to the list.
    save_tasks(tasks)
    print(f'Task "{task_name}" added successfully!')

#Step-4: View all tasks 
def view_tasks():
    tasks = load_tasks() #Calls your earlier load_tasks() function.
    if tasks :
        print("\n---To Do List---")
        for idx, task in enumerate(tasks,start=1): #Loops through each task in the list. start=1 means numbering will begin at 1 (instead of 0).
            print(f"{idx}.{task['Task']} - {task['Status']}")
    else:
        print("No tasks found.")        

#Learnings 
# enumerate() is a built-in Python function that lets you loop over a sequence (like a list, tuple, or string) and get both: The index (position) of the item and The value (item itself).

#Step-5: Update Task Status
def update_status():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update:")) - 1
        if 0 <= task_index < len(tasks): #Checks if the number entered is valid (within the range of available tasks).
            new_status = input("Enter the new status (Complete/Incomplete):").strip().capitalize()
            tasks[task_index]['Status'] = new_status #Updates the "Status" key of the selected task with the new value.
            save_tasks(tasks)
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

#Learnings 
# Subtracts 1 because Python lists are 0-based index but your tasks are displayed starting at 1. Example: if user chooses task 2, internally it becomes index 1.        

#Step-6: Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete:")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'Task "{deleted_task["Task"]}" delete successfully!')
        else :
            print("Invalid task number")
    except ValueError:
        print("Invalid input.Please enter a valid task number .")              

#Step-7: Display Menu
def display_menu():
    print("/n---Mini To Do Menu---")
    print("1.Add a new task")
    print("2.View all tasks") 
    print("3.Update task status")
    print("4.Delete a task")
    print("5.Exit")

#Step-8: Main program loops
while True:
    display_menu()
    choice = input("Enter your choice (1-5):").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_status()
    elif choice == '4':
        delete_task()                                   
    elif choice == '5':
        print("Exititng the To Do List app. Goodbye!")
        break
    else:
        print("Invalid choice.Please enter a valid number (1-5).")    
