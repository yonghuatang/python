from tkinter import *

main_window = Tk()  # case-sensitive!

button = Button(main_window)
button.pack()

def update_l1(value):
    selection = "Value 1 = " + str(slider1.get())
    L1.config(text=selection)

def update_l2(value):
    selection = "Value 2 = " + str(slider2.get())
    L2.config(text=selection)

def update_l3(value):
    selection = "Value 3 = " + str(slider3.get())
    L3.config(text=selection)

L1 = Label(main_window, text="My first tkinter")
L1.pack()

slider1 = Scale(main_window, from_=100, to=0, command=update_l1)
slider1.pack()

L2 = Label(main_window, text="My first tkinter")
L2.pack()

slider2 = Scale(main_window, from_=100, to=0, command=update_l2)
slider2.pack()

L3 = Label(main_window, text="My first tkinter")
L3.pack()

slider3 = Scale(main_window, from_=100, to=0, command=update_l3)
slider3.pack()

main_window.mainloop()  # display the window

