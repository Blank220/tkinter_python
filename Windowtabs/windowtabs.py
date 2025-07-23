from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')
notebook.add(tab3,text='Tab 3')
notebook.pack(expand=True,fill='both')

Label(tab1,text='Bigay nyo sakin saber',width=50,height=25,font=('Arial',20),bg='blue').pack()
Label(tab2,text='Patayin ko si Wise Level 4',width=50,height=25,font=('Arial',20),bg='red').pack()
Label(tab3,text='Tinawagan ko driver ko, Uwi na tayo Pangasinan',width=50,
      height=25,font=('Arial',20),bg='yellow').pack()

window.mainloop()