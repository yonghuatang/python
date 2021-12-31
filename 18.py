from tkinter import * # Use Tkinter in 2.6
import random
fontsize = 50
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']
def reply(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='ERROR', bg='black', fg=color).pack()
    L.config(fg=color)
def timer():
    L.config(fg=random.choice(colors))
    win.after(250, timer)
def grow():
    global fontsize
    fontsize += 15
    L.config(font=('arial', fontsize, 'italic'))
    win.after(100, grow)
win = Tk()
L = Label(win, text='ERROR' ,
font=('arial', fontsize, 'bold'), fg='red', bg='blue',
relief=RAISED)
L.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='try it', command=(lambda: reply('red'))).pack(side=BOTTOM,fill=X)
Button(win, text='bye', command=timer).pack(side=BOTTOM, fill=X)
Button(win, text='what is this?', command=grow).pack(side=BOTTOM, fill=X)
win.mainloop()


