from tkinter import *

root = Tk()
root.title('Dropdown')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

options = [
    "Monday", 
    "Tuesday",
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday",
    ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myBtn = Button(root, text="Show", command=show)
myBtn.pack()

root.mainloop()