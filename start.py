#import tkinter for GUI 
import tkinter as tk
from tkinter import *
#Start of GUI app
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
#Creating buttons
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Wooomy\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
#Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                               command=self.master.destroy)
        self.quit.pack(side="bottom")
#When button is pressed
    def say_hi(self):
        print("Wooomy")

root = tk.Tk()
app = Application(master=root)
app.mainloop()


