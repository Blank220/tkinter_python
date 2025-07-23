from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='System',message='Hacker!')
    messagebox.showwarning(title='System',message='Bayross!')
    messagebox.showerror(title='System',message='No Internet!')

    if messagebox.askokcancel(title='Ask ok cancel',message='U want?'):
        print('U want')
    else:
        print('Dont want')

    if messagebox.askretrycancel(title='Ask ok cancel',message='U want?'):
        print('U retry')
    else:
        print('Dont retry')

    if messagebox.askyesno(title='Yes or no',message='Do u want to u know?'):
        print('Me too')
    else:
        print('Lame')

    answer = messagebox.askquestion(title='Ask qs',message='Do u like me?')
    if answer == 'yes':
        print('Tommorrow at 10am')
    else:
        print('Alangan sabihin mong kasarap')

    answer2 = messagebox.askyesnocancel(title='what',message='Cu mogs?')
    if answer2 == True:
        print('LLPAN na ;0')
    elif answer2 == False:
        print('bp edit')
    else:
        print('Play safe')

    
    

    

window = Tk()

button = Button(window,text='click me',command=click)
button.pack()


window.mainloop()