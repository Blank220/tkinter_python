from tkinter import *

def submit():
    print(f'First name: {first_name_entry.get()}')
    print(f'Last name: {last_name_entry.get()}')
    print(f'Email: {email_entry.get()}')


window = Tk()

title_label = Label(window,text='Your Information',font=('Arial',20)).grid(row=0,column=0,columnspan=2)

first_name_label = Label(window,text='First Name: ',width=20,bg='blue').grid(row=1,column=0)
first_name_entry = Entry(window)
first_name_entry.grid(row=1,column=1)

last_name_label = Label(window,text='Last Name: ',bg='yellow').grid(row=2,column=0)
last_name_entry = Entry(window)
last_name_entry.grid(row=2,column=1)

email_label = Label(window,text='Email: ',bg='red').grid(row=3,column=0)
email_entry = Entry(window)
email_entry.grid(row=3,column=1)

submit_button = Button(window,text='Submit',command=submit).grid(row=4,column=0,columnspan=2)

window.mainloop()