from tkinter import *

root = Tk()
root.title("Simple Calculator")

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    state.delete(0, END)
    state.insert(0, "Everything is cleared!!!")

def button_add():
    global num1
    global math
    math = "add"
    num1 = e.get()
    e.delete(0, END)

def button_sub():
    global num1
    global math
    math = "sub"
    num1 = e.get()
    e.delete(0, END)

def button_mul():
    global num1
    global math
    math = "mul"
    num1 = e.get()
    e.delete(0, END)

def button_div():
    global num1
    global math
    math = "div"
    num1 = e.get()
    e.delete(0, END)

def button_equal():
    global strng
    num2 = e.get()
    e.delete(0, END)
    if math == "add":
        num3 = int(num1) + int(num2)
        strng = str(num1) + " + " + str(num2) + " = " + str(num3)
    elif math == "sub":
        num3 = int(num1) - int(num2)
        strng = str(num1) + " - " + str(num2) + " = " + str(num3)
    elif math == "mul":
        num3 = int(num1) * int(num2)
        strng = str(num1) + " * " + str(num2) + " = " + str(num3)
    elif math == "div":
        num3 = int(num1) / int(num2)
        strng = str(num1) + " / " + str(num2) + " = " + str(num3)
    e.insert(0, num3)
    state.delete(0, END)
    state.insert(0, strng)
    
operation = Label(root, text="Operation")
operation.grid(row=1, column=0, columnspan=1)

e = Entry(root, width=50, borderwidth=5)
e.insert(0, "0")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

state = Entry(root, width=30)
state.insert(0, "Operation will appear here")
state.grid(row=1, column=1, columnspan=2, pady=5, padx=5)

#define buttons
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=19.1, pady=10, command=button_add)
button_equals = Button(root, text="=", padx=74, pady=10, command=button_equal)
button_clr = Button(root, text="CLEAR", padx=60.1, pady=10, command=button_clear)

button_sub = Button(root, text="-", padx=22, pady=10, command=button_sub)
button_mul = Button(root, text="*", padx=22, pady=10, command=button_mul)
button_div = Button(root, text="/", padx=22, pady=10, command=button_div)

#put buttons on screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)

button_clr.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equals.grid(row=6, column=1, columnspan=2)
button_sub.grid(row=7, column=0)
button_mul.grid(row=7, column=1)
button_div.grid(row=7, column=2)

root.mainloop()