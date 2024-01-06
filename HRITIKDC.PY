import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        # Task list with due dates
        self.tasks = []

        # Entry widget for adding tasks
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Entry widget for adding due date
        self.date_entry = tk.Entry(self.master, width=20)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.date_entry.insert(0, "YYYY-MM-DD")

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.view_button = tk.Button(self.master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=1, column=0, padx=10, pady=10)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        due_date_str = self.date_entry.get()

        if task and due_date_str:
            try:
                # Convert the due date string to a datetime object
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                self.tasks.append({"Task": task, "Due Date": due_date})
                messagebox.showinfo("Task Added", f'Task "{task}" added successfully with due date {due_date}.')
                self.task_entry.delete(0, tk.END)  # Clear the task entry field
                self.date_entry.delete(0, tk.END)  # Clear the date entry field
                self.date_entry.insert(0, "YYYY-MM-DD")  # Reset the default text
            except ValueError:
                messagebox.showwarning("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        else:
            messagebox.showwarning("Input Error", "Please enter both a task and a due date.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks available.")
        else:
            tasks_window = tk.Toplevel(self.master)
            tasks_window.title("Tasks")
            task_listbox = tk.Listbox(tasks_window)
            task_listbox.pack(padx=10, pady=10)

            for task in self.tasks:
                task_listbox.insert(tk.END, f'{task["Task"]} - Due Date: {task["Due Date"]}')

    def remove_task(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks available.")
        else:
            remove_window = tk.Toplevel(self.master)
            remove_window.title("Remove Task")
            remove_label = tk.Label(remove_window, text="Select a task to remove:")
            remove_label.pack(padx=10, pady=10)

            task_listbox = tk.Listbox(remove_window)
            task_listbox.pack(padx=10, pady=10)

            for task in self.tasks:
                task_listbox.insert(tk.END, f'{task["Task"]} - Due Date: {task["Due Date"]}')

            remove_button = tk.Button(
                remove_window, text="Remove", command=lambda: self.process_remove(task_listbox.get(tk.ACTIVE))
            )
            remove_button.pack(pady=10)

    def process_remove(self, selected_task):
        if selected_task:
            # Parse the selected task to get the task name
            task_name = selected_task.split(' - ')[0]
            
            # Remove the task from the list
            for task in self.tasks:
                if task["Task"] == task_name:
                    self.tasks.remove(task)
                    messagebox.showinfo("Task Removed", f'Task "{task_name}" removed successfully.')
    
def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
