import tkinter as tk
from tkinter import Scrollbar

window = tk.Tk()
window.resizable(width=False, height=True)
window.title('Split file')
def print_input(*args):
    for entry in entries:
        print(entry.get())

entries = [Entry(tk) for _ in range(2)]
for entry in entries:
    entry.pack()

btn = Button(tk, text="Print", command=print_input)