from tkinter import *

root = Tk()


# creting a label widget

MyLabel = Label(root, text="Hello World!")


# add the widget into the screen

MyLabel.pack()

root.title("Our Dahlias")

# Adjust size
root.geometry("400x400")
 
# set minimum window size value
root.minsize(400, 400)
 
# set maximum window size value
root.maxsize(400, 400)

root.mainloop()
