from tkinter import *
from tkinter import messagebox

root = Tk(className=" Schaltjahr berechnen")

root.geometry("400x50")
y = StringVar()
text = Entry(textvariable=y, width=50).pack()


def onclick():
    m = int(y.get())
    year = m
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        messagebox.showinfo("Schaltjahr", "{} ist ein Schaltjahr!".format(year))

    else:
        messagebox.showinfo("Schaltjahr", "{} ist kein Schaltjahr!".format(year))


button = Button(root, text="berechnen", command=onclick, width=50).pack()

root.mainloop()
