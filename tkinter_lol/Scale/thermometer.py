from tkinter import *

window = Tk()

def submit():
    temp = scale.get()
    print(f'The temperature is {temp} degrees C')
    if temp >= 38:
        print('Sick hot')
    elif temp <= 30:
        print('Sick cold')
    else:
        print('not sick')


scale = Scale(window,from_=100,to=0,length=600,orient='vertical',
              font=('georgia',20),tickinterval=10,troughcolor='red',fg='blue',bg='black')

scale.set(50)
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()