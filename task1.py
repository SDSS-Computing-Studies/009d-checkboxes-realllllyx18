#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *

state = IntVar()
state.set(1)

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    if decimal > 1:
        decimal_to_binary(decimal//2)
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    binary = binary_to_decimal(decimal)


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    decimal = binary_to_decimal(binary)

def updateCheck():
    e1.delete(0,tk.END)
    e1.insert(0, state.get())


window = tk.Tk()
window.title("tk")

e1 = Entry(window)
e1.insert(0,state.get())

label1 = tk.Label(window, text="Binary/Decimal Converter!")
cb1 = Checkbutton(window, variable = state, command=updateCheck)
cb2 = Checkbutton(window, variable = state, command=updateCheck)
cb3 = Checkbutton(window, variable = state, command=updateCheck)
cb4 = Checkbutton(window, variable = state, command=updateCheck)
cb5 = Checkbutton(window, variable = state, command=updateCheck)
cb6 = Checkbutton(window, variable = state, command=updateCheck)
cb7 = Checkbutton(window, variable = state, command=updateCheck)
cb8 = Checkbutton(window, variable = state, command=updateCheck)
b1 = Button(window, text="Convert to Binary", command=get_binary)
b2 = Button(window, text="Convert to Decimal", command=get_decimal)

label1.pack()
e1.pack()
cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()
cb5.pack()
cb6.pack()
cb7.pack()
cb8.pack()
b1.pack()
b2.pack()

window.mainloop()