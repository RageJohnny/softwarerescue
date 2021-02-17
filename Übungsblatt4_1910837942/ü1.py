from tkinter import *
from random import randrange
def place():
    button.place(x=randrange(250),y=randrange(250))

root = Tk(className=" Button-Klicker")


root.geometry("300x300")

button = Button(root,text="Drück mich!", bg="red", command=place)
button.config(height=1, width=10)
button.pack()

root.mainloop()

