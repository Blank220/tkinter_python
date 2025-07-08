from tkinter import *

def create_window():
    new_window = Tk()
    new_window.title('Bago')

    old_window.destroy()

old_window = Tk()

Button(old_window,text='Create new window',command=create_window).pack()


old_window.mainloop()