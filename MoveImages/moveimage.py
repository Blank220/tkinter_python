from tkinter import *
from PIL import Image, ImageTk

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

window = Tk()
window.geometry("500x500")
window.configure(bg='white')

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Left>",move_left)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)


original_image = Image.open(r"C:\Users\User\Downloads\car-removebg-preview.png")
resized_image = original_image.resize((250, 250))
car = ImageTk.PhotoImage(resized_image)

label = Label(window, image=car, bg='white')
label.place(x=0, y=0)

window.mainloop()
