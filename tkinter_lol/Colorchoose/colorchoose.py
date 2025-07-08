from tkinter import *
from tkinter import colorchooser

def color():
    color = colorchooser.askcolor()
    window.config(bg=color[1])


window = Tk()
window.geometry('500x500')

button = Button(text='click this',command=color)
button.pack()

window.mainloop()