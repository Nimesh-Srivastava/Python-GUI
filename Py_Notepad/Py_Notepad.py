from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes = [("All files", "*.*"),("Text documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes = [("All files", "*.*"),("Text documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "This is a python based GUI application and is created using Nimesh Srivastava's code")

if __name__=='__main__':
    root = Tk()
    root.title('Untitled - Notepad')
    root.geometry("500x550")

    # Creating a text area
    textArea = Text(root, font="lucida 10")
    textArea.pack(fill=BOTH, expand=True)

    # initial file
    file = None

    # Creating a menu bar
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    # Adding menubar to root
    root.config(menu=menuBar)

    # Adding ScrollBar
    scroll = Scrollbar(textArea, command=textArea.yview)
    scroll.pack(side=RIGHT, fill=Y)
    textArea.config(yscrollcommand=scroll.set)

    root.mainloop()