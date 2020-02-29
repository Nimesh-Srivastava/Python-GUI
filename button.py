from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="The button is clicked")
    myLabel.pack()

myButton = Button(root, text="click", padx=10, pady=5, command=myClick, fg="yellow", bg="black")
myButton.pack()

root.mainloop()