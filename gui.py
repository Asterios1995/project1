import tkinter as tk
import tkinter.messagebox as msg
from tkinter.ttk import *

frame = tk.Tk()

def helloCallBack():
   msg.showinfo( "Hello Python", "Hello World")

def goodday():
    msg.showinfo("hello", "good day")

photo = tk.PhotoImage(file = "images\myimage.png")
B = tk.Button(frame, text ="Hello", command = helloCallBack, bd = 5, activeforeground = "blue", bg = "red" )
B2 = tk.Button(frame, image = photo, command = goodday, bd = 5, )


B.pack()
B2.pack()
frame.mainloop()


