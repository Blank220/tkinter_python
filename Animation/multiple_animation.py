from tkinter import *
import time
from ball import *
from PIL import Image, ImageTk



window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

original_map = Image.open(r"C:\Users\User\Downloads\map_ml.png")
resized_map = original_map.resize((WIDTH,HEIGHT))
background = ImageTk.PhotoImage(resized_map)

map = canvas.create_image(0,0, image=background,anchor=NW)


volleyball = Ball(canvas,0,0,100,1,1,"blue")
tennisball = Ball(canvas,10,10,50,3,5,"yellow")
basketball = Ball(canvas,50,50,200,5,7,"orange")

while True:
    volleyball.move()
    tennisball.move()
    basketball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()