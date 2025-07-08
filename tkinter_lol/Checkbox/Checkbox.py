from tkinter import *

def display():
    if(x.get()==1)&(y.get()==0):
        print('I am done in Purcom')
    elif(x.get()==0)&(y.get()==1):
        print('I am done in OOP')
    elif(x.get()==1)&(y.get()==1):
        print('I am done with BOTH!')
    else:
        print('Not done with anything')

window = Tk()

x = IntVar()
y= IntVar()

checkbox = Checkbutton(window,text ='Project Purcom',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.config(font=('georgia',20))
checkbox.config(fg='#00FF00')
checkbox.config(bg="Black")
checkbox.config(activeforeground='#00FF00')
checkbox.config(activebackground="black")
checkbox.config(padx=10,pady=1,width=100,height=5)
checkbox.config(anchor='w')
checkbox.pack()

checkbox2 = Checkbutton(window,text ='Project OOP',variable=y,onvalue=1,offvalue=0,command=display)
checkbox2.config(font=('georgia',20))
checkbox2.config(fg='#00FF00')
checkbox2.config(bg="Black")
checkbox2.config(activeforeground='#00FF00')
checkbox2.config(activebackground="black")
checkbox2.config(padx=10,pady=1,width=100,height=5)
checkbox2.config(anchor='w')
checkbox2.pack()

window.mainloop()