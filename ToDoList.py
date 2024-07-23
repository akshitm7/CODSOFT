class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f"Added task: {task}")
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            print(f"Task {index + 1} marked as done.")
        else:
            print("Invalid task number.")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{i}. {task['task']} - {status}")
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Mark task as done")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_done(index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()
