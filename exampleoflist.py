import tkinter as tk
import tkinter.messagebox as msg
from base64 import b16decode
from tkinter import *

frame = tk.Tk()

tk.Label(frame, text = 'shopping list', font =('Verdana', 15)).pack(side = "top" , pady = 10)

def add_to_list():
    frame2 = tk.Tk()
    tk.Label(frame2, text = 'would you like to continue', font =('Verdana', 15)).pack(side = "top" , pady = 10)
    B1 = tk.Button(frame2, text = "yes", command = b1)
    B2 = tk.Button(frame2, text = "no",)
    B1.pack()
    B2.pack()
    frame2.mainloop()

def list_addition(canvas1):
   string=  canvas1.get()
   print(string)

def b1():
    slist = []
    frame3 = tk.Tk()
    canvas1 = tk.Canvas(frame3, width=400, height=300)
    canvas1.pack()
    x = tk.Entry(frame3)
    canvas1.create_window(200, 140, window=x)
    label1 = tk.Label(frame3, text=x)
    canvas1.create_window(200, 230, window=label1)
    x = x.get()
    slist = slist.append(x)
    addbutton = tk.Button(frame3, text = "add", command = list_addition)
    addbutton.place(x = 180, y = 200)
    frame3.mainloop()

    

def viewlist ():
    msg.showinfo( "list", )



B = tk.Button(frame, text = "add to list", command = add_to_list)
B2 = tk.Button(frame, text= "remove from list" )
B3 = tk.Button(frame, text = "view list ", command = viewlist)


B.pack()
B2.pack()
B3.pack()
frame.mainloop()