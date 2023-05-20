import tkinter as tk
from tkinter import messagebox

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo(title, message)

    root.deiconify()
    root.destroy()