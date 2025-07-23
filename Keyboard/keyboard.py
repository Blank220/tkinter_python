from tkinter import *

def do_something(event):
    print(f'You pressed {event.keysym}')
    label.config(text=event.keysym)

    if  event.keysym == 'f':
        message.config(text='F for Respect')
    else:
        message.config(text='')
        

window = Tk()

window.config(bg='pink')

key = window.bind("<Key>", do_something)

label = Label(window,font=('Arial',20))
message = Label(window,font=('Arial',20))
label.pack()
message.pack()

window.mainloop()