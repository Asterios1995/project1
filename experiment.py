from tkinter import *

root = Tk()

def run():
    lst1.append(e1.get()) 
    lst2.append(e2.get())

    print(lst1,lst2)
lst1 = [] #this is very important
lst2 = [] 
e1 = Entry(root)
e1.pack(padx=30,pady=10)

e2 = Entry(root)
e2.pack(padx=10,pady=10)

Button(root,text='Append all the text',command=run).pack(pady=10)

root.mainloop()