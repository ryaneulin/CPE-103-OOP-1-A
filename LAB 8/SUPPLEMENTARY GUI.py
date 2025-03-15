#TUI Implementation
# Simple TUI Calculator

#GUI Conversion of the Calculator:
import tkinter as tk

# Functions for calculation
def add():
    result_value = (float(entry1.get()) + float(entry2.get()))
    result.set(result_value)
    store_history(f"{entry1.get()} + {entry2.get()} = {result_value}")
def subtract():
    result_value = (float(entry1.get()) - float(entry2.get()))
    result.set(result_value)
    store_history(f"{entry1.get()} - {entry2.get()} = {result_value}")
def multiply():
    result_value = (float(entry1.get()) * float(entry2.get()))
    result.set(result_value)
    store_history(f"{entry1.get()} * {entry2.get()} = {result_value}")
def divide():
    try:
        result_value = (float(entry1.get()) / float(entry2.get()))
        result.set(result_value)
        store_history(f"{entry1.get()} / {entry2.get()} = {result_value}")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")
    history_list.delete(0, 'end')

history = []
def store_history(entry):
    history.append(entry)
    update_history()

def update_history():
    history_list.delete(0,'end')
    for item in history:
        history_list.insert('end', item)


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300+10+10")

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:").grid(row=2, column=1)
entry1 = tk.Entry(root)
entry1.grid(row=2, column=2)

tk.Label(root, text="Enter second number:").grid(row=3, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=3, column=2)


# Buttons for operations
tk.Button(root, text="DEL", command = delete).grid(row=2, column=4)
tk.Button(root, text="CLR", command = clear).grid(row=2, column=5)
tk.Button(root, text="Add", command=add).grid(row=3, column=4)
tk.Button(root, text="Subtract", command=subtract).grid(row=3, column=5)
tk.Button(root, text="Multiply", command=multiply).grid(row=4, column=4)
tk.Button(root, text="Divide", command=divide).grid(row=4, column=5)

# Label to show result
tk.Label(root, text="Result:").grid(row=4, column=1)
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=2)


#History
tk.Label(root, text="History").grid(row=5, column=1)
history_list = tk.Listbox(root, width=50, height=10)
history_list.grid(row=6, column=1, columnspan=5)
 
# Start the main loop
root.mainloop()
