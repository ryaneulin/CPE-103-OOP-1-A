
# GUI Conversion of the Calculator:
import tkinter as tk
import math

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def op(func):
    try:
        value = float(entry.get())
        if func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        elif func == 'sqrt':
            result == math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x430+10+10")
root.config(bg = "lightblue")

#Display Current Output
entry = tk.Entry(root, width = 20, font = ("Arial", 18), borderwidth = 20, relief = "ridge", justify="right", bg = "lightblue", fg = "black")
entry.grid(row = 0, column = 0, columnspan =4, padx = 10, pady = 10)

button_frame = tk.Frame(root, bg = "lightgray")
button_frame.grid(row = 1, column = 0, columnspan = 4)

# Buttons
buttons = [
    ("sin", lambda: op('sin')),
    ("cos", lambda: op('cos')),
    ("tan", lambda: op('tan')),
    ("√", lambda: op('sqrt')),
    ("7", lambda: press('7')),
    ("8", lambda: press('8')),
    ("9", lambda: press('9')),
    ("C", clear),
    ("4", lambda: press('4')),
    ("5", lambda: press('5')),
    ("6", lambda: press('6')),
    ("*", lambda: press('*')),
    ("1", lambda: press('1')),
    ("2", lambda: press('2')),
    ("3", lambda: press('3')),
    ("/", lambda: press('/')),
    ("0", lambda: press('0')),
    ("=", evaluate),
    ("+", lambda: press('+')),
    ("-", lambda: press('-')),
]

row = 1
col = 0
button_bg = "lightgray"
button_fg = "black"
for (text, cmd) in buttons:
    tk.Button(root, text = text, width = 5, height = 2, font = ("Arial", 14), command = cmd, bg = button_bg, fg = button_fg). grid(row = row, column = col, padx = 2, pady = 2 )
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()