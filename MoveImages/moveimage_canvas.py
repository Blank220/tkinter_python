from tkinter import *

def move_up(event):
    canvas.move(car_image,0,-10)

def move_left(event):
    canvas.move(car_image,-10,0)

def move_down(event):
    canvas.move(car_image,0,10)

def move_right(event):
    canvas.move(car_image,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Left>",move_left)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

car = PhotoImage(file=r"C:\Users\User\Downloads\car-removebg-preview.png")
car_image = canvas.create_image(0,0,image=car,anchor=NW)

window.mainloop()