from tkinter import *

def order():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print('Orders: ')
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,background='gray',font=('georgia',20),width=12,selectmode=MULTIPLE)
listbox.insert(1, 'Tapsilog')
listbox.insert(2, 'Hotsilog')
listbox.insert(3, 'Tocilog')
listbox.insert(4, 'Pares')
listbox.insert(5, 'Steak')

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text='Order',command=order)
submitbutton.pack(anchor='e')

addbutton = Button(window,text='add',command=add)
addbutton.pack()

delbutton = Button(window,text='del',command=delete)
delbutton.pack()

listbox.pack()

window.mainloop()