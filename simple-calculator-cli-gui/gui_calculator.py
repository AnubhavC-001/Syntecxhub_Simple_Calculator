# gui_calculator.py

import tkinter as tk
from calculator_logic import add, subtract, multiply, divide

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(add(a, b))
        elif op == "-":
            result.set(subtract(a, b))
        elif op == "*":
            result.set(multiply(a, b))
        elif op == "/":
            result.set(divide(a, b))

    except:
        result.set("Invalid Input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

# Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")

# Inputs
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Operator
operator = tk.StringVar(value="+")
ops = ["+", "-", "*", "/"]

for op in ops:
    tk.Radiobutton(root, text=op, variable=operator, value=op).pack()

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:", font=("Arial", 12)).pack()
tk.Label(root, textvariable=result, font=("Arial", 16)).pack(pady=10)

# Buttons
tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)

root.mainloop()