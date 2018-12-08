# unpack.py
import time
from tkinter import Tk, Label
root = Tk()

my_text = Label(root, text='Hello, world!')
my_text.pack()
my_text.pack_forget()

root.mainloop()