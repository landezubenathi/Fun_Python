import tkinter as tk
from flask import Flask, render_template, request

# Function to update the expression in the entry widget
def on_click(button_text):
    current_text = entry_var.get()
    entry_var.set(current_text + button_text)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get())  # Evaluate the mathematical expression
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("340x400")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Define button layout and colors
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

button_colors = {
    'C': 'red',
    '=': 'green',
    '+': 'orange',
    '-': 'orange',
    '*': 'orange',
    '/': 'orange'
}

# Create buttons dynamically with colors
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        color = button_colors.get(char, "lightgray")  # Default color for numbers
        action = lambda x=char: on_click(x) if x not in ('C', '=') else (clear() if x == 'C' else calculate())
        tk.Button(root, text=char, width=5, height=2, font=("Arial", 15), bg=color, fg="black", command=action).grid(row=r, column=c, padx=5, pady=5)

# Run the application
root.mainloop()
