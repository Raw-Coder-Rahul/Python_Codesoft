import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# Functions for task operations
def input_error():
    if enter_task_field.get() == "":
        messagebox.showerror("Input Error", "Enter a task.")
        return False
    return True

def clear_task_number_field():
    task_number_field.delete(0.0, tk.END)

def clear_task_field():
    enter_task_field.delete(0, tk.END)
    due_date_field.delete(0, tk.END)
    priority_field.delete(0, tk.END)

def insert_task():
    global counter
    if not input_error():
        return
    task = enter_task_field.get()
    due_date = due_date_field.get()
    priority = priority_field.get()
    task_details = f"{task} | Due: {due_date} | Priority: {priority}\n"
    tasks_list.append(task_details)
    TextArea.insert(tk.END, f"[ {counter} ] {task_details}")
    counter += 1
    clear_task_field()

def delete_task():
    global counter
    if not tasks_list:
        messagebox.showerror("No task", "No task to delete.")
        return
    task_no = task_number_field.get(1.0, tk.END).strip()
    if not task_no.isdigit():
        messagebox.showerror("Input Error", "Enter a valid task number.")
        return
    task_no = int(task_no)
    if task_no < 1 or task_no > len(tasks_list):
        messagebox.showerror("Input Error", "Invalid task number.")
        return
    tasks_list.pop(task_no - 1)
    counter -= 1
    clear_task_number_field()
    TextArea.delete(1.0, tk.END)
    for i, task in enumerate(tasks_list, 1):
        TextArea.insert(tk.END, f"[ {i} ] {task}")

def exit_app():
    window.destroy()

# Create a GUI window
window = tk.Tk()
window.title("To-Do List")
window.geometry("1200x800")

# Background image
bg_img = tk.PhotoImage(file="Flexible-work-arrangements.png")
bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

tasks_list = []
counter = 1

# Name label and entry
name_label = tk.Label(window, text="Name", bg="light green", font=("Helvetica", 14))
name_label.place(x=30, y=30)
name_entry = tk.Entry(window, font=("Helvetica", 14))
name_entry.place(x=100, y=30, width=300)

# Enter task label and entry field
enter_task_label = tk.Label(window, text="Enter Your Task", bg="light green", font=("Helvetica", 14))
enter_task_label.place(x=30, y=70)
enter_task_field = tk.Entry(window, font=("Helvetica", 14))
enter_task_field.place(x=200, y=70, width=300)

# Due date label and entry field
due_date_label = tk.Label(window, text="Due Date (YYYY-MM-DD)", bg="light green", font=("Helvetica", 14))
due_date_label.place(x=30, y=110)
due_date_field = tk.Entry(window, font=("Helvetica", 14))
due_date_field.place(x=250, y=110, width=150)

# Priority label and entry field
priority_label = tk.Label(window, text="Priority (High/Medium/Low)", bg="light green", font=("Helvetica", 14))
priority_label.place(x=30, y=150)
priority_field = tk.Entry(window, font=("Helvetica", 14))
priority_field.place(x=250, y=150, width=150)

# Text area for displaying tasks
TextArea = tk.Text(window, height=15, width=50, font=("Helvetica", 14))
TextArea.place(x=30, y=190)

# Task number label and text field for deleting task
task_number_label = tk.Label(window, text="Delete Task Number", bg="light green", font=("Helvetica", 14))
task_number_label.place(x=30, y=450)
task_number_field = tk.Text(window, height=1, width=2, font=("Helvetica", 14))
task_number_field.place(x=230, y=450)

# Buttons
submit_button = tk.Button(window, text="Add Task", fg="White", bg="Blue", font=("Helvetica", 14), command=insert_task)
submit_button.place(x=30, y=500, width=100)
delete_button = tk.Button(window, text="Delete", fg="White", bg="Red", font=("Helvetica", 14), command=delete_task)
delete_button.place(x=150, y=500, width=100)
exit_button = tk.Button(window, text="Exit", fg="White", bg="Black", font=("Helvetica", 14), command=exit_app)
exit_button.place(x=270, y=500, width=100)

# Run the GUI
window.mainloop()
