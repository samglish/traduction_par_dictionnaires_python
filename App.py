import tkinter as tk
from main import sms_translator
from tkinter import ttk
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()
#
# here are method calls to the window manager class
#
myapp.master.title("SamGlish")
myapp.master.maxsize(500, 500)
myapp.master.minsize(500, 500)
myapp.master.geometry("500x500")
myapp.master.configure(bg="lightblue")
# start the program
Frame=ttk.Frame(myapp, padding=0)
Frame.grid()
ttk.Label(Frame, text="Wadjonautes translator", font=("Arial", 15),background="lightblue",padding=0).grid(column=0, row=0)
ttk.Label(Frame, text="FR to FB",background="lightblue",padding=0).grid(column=0, row=1)

ttk.Entry(Frame,show=True,background="white").grid(column=0, row=8)
ttk.Button(Frame, text = 'Traduire').grid(column=1, row=8)
myapp.mainloop()