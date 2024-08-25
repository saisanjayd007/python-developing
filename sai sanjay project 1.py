import json

# Load tasks from a json file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save tasks to a json file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generate a new task ID
def get_new_id(tasks):
    return str(max(map(int, tasks.keys()), default=0) + 1)
def create_task(tasks):
    task_id = get_new_id(tasks)
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = "Pending"
    tasks[task_id] = {"title": title, "description": description, "status": status}
    print("Task created successfully!")
def update_task(tasks):
    task_id = input("Enter task ID to update: ")
    if task_id in tasks:
        title = input("Enter new title (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")
        status = input("Enter new status (Pending, In Progress, Completed) or leave blank to keep current: ")
        
        if title:
            tasks[task_id]["title"] = title
        if description:
            tasks[task_id]["description"] = description
        if status in ["Pending", "In Progress", "Completed"]:
            tasks[task_id]["status"] = status
        
        print("Task updated successfully!")
    else:
        print("Task ID not found.")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, details in tasks.items():
            print(f"ID: {task_id}")
            print(f"Title: {details['title']}")
            print(f"Description: {details['description']}")
            print(f"Status: {details['status']}")
            print("-" * 20)
def main():
    tasks = load_tasks()
    
    while True:
        print("To-Do List Application")
        print("1. Create Task")
        print("2. Update Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            create_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting and saving tasks...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__": main()
