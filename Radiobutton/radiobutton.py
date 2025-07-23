from tkinter import *

window = Tk()

x = IntVar()

food = ['sisig','shawarma','tapa']

def order():
    if x.get() == 0:
        print('Sisig Mamser')
    elif x.get() == 1:
        print('Shawarma Mamser')
    elif x.get() == 2:
        print('Tapa Mamser')
    else:
        print('Order mamser')


sisig = PhotoImage(file='facebook.png')
shawarma = PhotoImage(file='facebook.png')
tapa = PhotoImage(file='facebook.png')
foodimages = [sisig,shawarma,tapa]


for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],variable=x,value=index,padx=25,
                              font=('georgia',50),image=foodimages[index],compound='left',
                              indicatoron=0,width=575,command=order)
    radiobutton.config()
    radiobutton.pack(anchor='w')
    



window.mainloop()