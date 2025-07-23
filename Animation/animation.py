from tkinter import *
from PIL import Image, ImageTk
import time

WIDTH = 500
HEIGHT = 500
velocity_x = 4
velocity_y = 7


window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

original_map = Image.open(r"C:\Users\User\Downloads\map_ml.png")
resized_map = original_map.resize((500, 500))
background = ImageTk.PhotoImage(resized_map)

map = canvas.create_image(0,0, image=background,anchor=NW)

original_image = Image.open(r"C:\Users\User\Downloads\Python\python_prac\gui\tkinter_lol\Animation\kyle.png")
resized_image = original_image.resize((100, 100))
photo = ImageTk.PhotoImage(resized_image)

kyle = canvas.create_image(0, 0, image=photo, anchor=NW)

image_width, image_height = resized_image.size


while True:
    coordinates = canvas.coords(kyle)
    print(coordinates)
    if (coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        velocity_x = -velocity_x
    if (coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        velocity_y = -velocity_y
    canvas.move(kyle,velocity_x,velocity_y)
    window.update()
    time.sleep(0.01)


window.mainloop()
