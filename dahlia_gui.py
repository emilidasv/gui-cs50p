from tkinter import *
from PIL import ImageTk, Image
import sqlite3
root = Tk()
root.geometry("720x500")
root.title("Our Dahlias")


def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


def sel():
    if str(var.get()) == 1:
        #selection = "You selected the option " + str(var.get()) 
        label.config(text=selection)
        btn2 = Button(root,
             text="Click to open a new window",
             command=openNewWindow)
        label = Label(root,
              text="This is the main window")
    elif str(var.get()) == 2:
        selection = "You selected the option " + str(var.get())
        label.config(text=selection)
    else:
        selection = "You selected the option " + str(var.get())
        label.config(text=selection)



# root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Search by name",
                 variable=var, value=1, command=sel)
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Search by Bloom or plant",
                 variable=var, value=2, command=sel)
R2.pack(anchor=W)
R3 = Radiobutton(root, text="Search in history",
                 variable=var, value=3, command=sel)
R3.pack(anchor=W)

label = Label(root, text = "Select")

label.pack(pady=10)
btn = Button(root,
             text="Click to open a new window",
             command=openNewWindow)
root.mainloop()
