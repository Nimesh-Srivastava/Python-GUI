from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry("400x400")

def check():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off", command=check)
c.pack()
c.deselect()

myLabel = Label(root, text=var.get()).pack()

root.mainloop()