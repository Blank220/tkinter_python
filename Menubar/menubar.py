from tkinter import *

def open_file():
    print('File Opened')

def save_file():
    print('File saved')

def cut():
    print('Cut Text')

def copy():
    print('Copy Text')

def paste():
    print('paste Text')

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0,font=('georgia',20))
menubar.add_cascade(label='File',menu=file_menu,font=('Ink Free',10))
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=quit)

edit_menu = Menu(menubar,tearoff=0,font=('georgia',20))
menubar.add_cascade(label='Edit',menu=edit_menu,)

edit_menu.add_command(label='Cut',command=cut)
edit_menu.add_command(label='Copy',command=copy)
edit_menu.add_separator()
edit_menu.add_command(label='Paste',command=paste)


window.mainloop()