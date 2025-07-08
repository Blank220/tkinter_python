from tkinter import *

def post():
    print(entry.get())

window = Tk()

entry = Entry(window)
entry.config(font=('Arial',20),background='Black',foreground='#00FF00')
posts = Button(window,text='Post',command=post)
posts.config(font=('georgia',10),background='blue',foreground='white')

entry.pack()
posts.pack()

window.mainloop()

