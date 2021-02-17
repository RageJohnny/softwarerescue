from tkinter import *

root = Tk()
root.title("Calculator")



i = StringVar()
j = StringVar()
r = StringVar()

label1 = Label(root, text="Input Number 1: ").grid(row=0, column=0)
input1 = Entry(root, textvariable=i, width=30).grid(row=0, column=1)
label2 = Label(root, text="Input Number 2: ").grid(row=1, column=0)
input2 = Entry(root, textvariable=j, width=30).grid(row=1, column=1)

labelResult = Label(root, text="Result:").grid(row=3, column=0)
entryResult = Entry(root, textvariable=r, width=30).grid(row=3, column=1)

def addition():
    a = float(i.get())
    b = float(j.get())
    result = a + b
    parsedresult = str(result)
    r.set(parsedresult)


def subtraction():
    c = float(i.get())
    d = float(j.get())
    result = c - d
    parsedresult = str(result)
    r.set(parsedresult)


def multiplication():
    e = float(i.get())
    f = float(j.get())
    result = e * f
    parsedresult = str(result)
    r.set(parsedresult)


def division():
    g = float(i.get())
    h = float(j.get())
    result = g / h
    parsedresult = str(result)
    r.set(parsedresult)

buttonaddition = Button(root, text="+", command=addition, width=5).grid(row=2, column=0)
buttonsubtraction = Button(root, text="-", command=subtraction, width=5).grid(row=2, column=1,ipadx=1)
buttonmultiplication = Button(root, text="*", command=multiplication, width=5).grid(row=2, column=2)
buttondivision = Button(root, text="/", command=division, width=5).grid(row=2, column=3,ipadx=1)


root.mainloop()
