import tkinter as tk
from tkinter import messagebox


# Function to update the display
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + value)


# Function to evaluate the expression
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to clear the display
def clear_display():
    display.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#F0F0F0")

# Display area
display = tk.Entry(root, font=("Helvetica", 18), bd=10, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, font=("Helvetica", 14), bg="#4CAF50", fg="white",
                        height=2, width=5, command=evaluate)
    else:
        btn = tk.Button(root, text=button, font=("Helvetica", 14), bg="#E0E0E0", fg="black",
                        height=2, width=5, command=lambda b=button: update_display(b))

    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1

    if col > 3:
        col = 0
        row += 1

# Clear button
btn_clear = tk.Button(root, text="C", font=("Helvetica", 14), bg="#f44336", fg="white", height=2, width=5,
                      command=clear_display)
btn_clear.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

