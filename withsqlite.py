import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
root = tk.Tk()
root.geometry("720x500")
root.title("using db sqlite3")

# create or connect to database

conn = sqlite3.connect('dahlia2.db')
# create cursor
curs = conn.cursor()
# curs.execute("""CREATE TABLE flowers (
#      bloomtype,
#      bloomsize
# )
# """)


curs.execute("select * from flowers")
# comit changes
conn.commit()

# close conentcion
conn.close()

root.mainloop()
