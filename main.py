class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}\n
    Title: {self.title}\n
    Description: {self.description}\n
    Priority: {self.priority}\n
    Status: {self.status}\n"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # to keep track of the next task ID

    def add_task(self, title, description, priority, status):
        task = Task(self.next_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title: task.title = title
            if description: task.description = description
            if priority: task.priority = priority
            if status: task.status = status
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        return self.tasks

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]
def display_menu():
    print("Task Manager Menu:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Filter Tasks by Priority")
    print("6. Exit")

def get_user_input(prompt):
    return input(prompt)

def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            title = get_user_input("Enter title: ")
            description = get_user_input("Enter description: ")
            priority = get_user_input("Enter priority (High/Medium/Low): ")
            status = get_user_input("Enter status (Pending/In Progress/Completed): ")
            manager.add_task(title, description, priority, status)
            print("Task added successfully.")

        elif choice == '2':
            task_id = int(get_user_input("Enter task ID to edit: "))
            title = get_user_input("Enter new title (or leave blank to keep unchanged): ")
            description = get_user_input("Enter new description (or leave blank to keep unchanged): ")
            priority = get_user_input("Enter new priority (High/Medium/Low) (or leave blank to keep unchanged): ")
            status = get_user_input("Enter new status (Pending/In Progress/Completed) (or leave blank to keep unchanged): ")
            if manager.edit_task(task_id, title, description, priority, status):
                print("Task edited successfully.")
            else:
                print("Task not found.")

        elif choice == '3':
            task_id = int(get_user_input("Enter task ID to delete: "))
            if manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif choice == '4':
            tasks = manager.view_all_tasks()
            for task in tasks:
                print(task)

        elif choice == '5':
            priority = get_user_input("Enter priority to filter by (High/Medium/Low): ")
            tasks = manager.filter_tasks_by_priority(priority)
            for task in tasks:
                print(task)

        elif choice == '6':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
