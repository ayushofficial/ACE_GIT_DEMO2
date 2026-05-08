import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.config(bg="#2c3e50")

# Configure grid weights for responsiveness
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

entry = tk.Entry(root, borderwidth=5, font=("Arial", 20), bg="#ecf0f1", fg="#2c3e50", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
entry.bind('<Return>', lambda e: button_equal())

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 16), bg="#27ae60", fg="white", command=button_equal, activebackground="#229954")
    elif text in ['+', '-', '*', '/']:
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 16), bg="#e74c3c", fg="white", command=lambda t=text: button_click(t), activebackground="#c0392b")
    else:
        btn = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 16), bg="#3498db", fg="white", command=lambda t=text: button_click(t), activebackground="#2980b9")
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='Clear', padx=79, pady=20, font=("Arial", 14), bg="#95a5a6", fg="white", command=button_clear, activebackground="#7f8c8d")
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()