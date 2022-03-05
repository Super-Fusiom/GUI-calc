import tkinter as tk
from tkinter import *

def hello(greeting):
    print(greeting)

root = tk.Tk()
root.title("OOOOOH")

Hellobtn = tk.Button(root, text="Hello", command=lambda:hello("Hello"))
Byebtn = tk.Button(root, text="Bye", command=lambda:hello("Bye"))
Hellobtn.pack()
Byebtn.pack()

root.mainloop()
