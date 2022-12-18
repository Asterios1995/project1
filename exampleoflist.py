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
    # leads user to the adding frame
slist = []
def b1():
     #empty list where items will be stored
    def list_addition():
        slist.append(x.get()) #function we call upon for the add button that appends what we enter into the list 
        print(slist)
        return slist  
    frame3 = tk.Tk()
    canvas1 = tk.Canvas(frame3, width=400, height=300)
    canvas1.pack()
    x = tk.Entry(frame3) #entry frame
    canvas1.create_window(200, 140, window=x)
    label1 = tk.Label(frame3, text=x)
    canvas1.create_window(200, 230, window=label1)
    addbutton = tk.Button(frame3, text = "add", command = list_addition) #what creates the button we will use to add to the list
    addbutton.place(x = 180, y = 200)
    frame3.mainloop()
    return slist

    

def viewlist ():
    msg.showinfo( "list", )



B = tk.Button(frame, text = "add to list", command = add_to_list)
B2 = tk.Button(frame, text= "remove from list" )
B3 = tk.Button(frame, text = "view list ", command = viewlist)


B.pack()
B2.pack()
B3.pack()
frame.mainloop()