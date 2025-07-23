from tkinter import *

def do_something(event):
    print(f'Mouse Coordinates at {str(event.x)},{str(event.y)}')

window = Tk()

#window.bind("<Button-3>",do_something) #1 is left, #2 is the scroll, #3 is right
#window.bind("<ButtonRelease>",do_something) #1 is left, #2 is the scroll, #3 is right
#window.bind("<Enter>",do_something) #mouse enter the window
#window.bind("<Leave>",do_something) #mouse leaves
window.bind("<Motion>",do_something) #mouse moves

window.mainloop()