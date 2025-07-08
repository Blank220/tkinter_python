from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text File", ".txt"),
                                               ("HTML File", ".html"),
                                               ("All files", ".*")])
    file_text = str(text.get(1.0,END))
    file_text = input('Enter some text: ')
    file.write(file_text)
    file.close()

window = Tk()

button = Button(window,text='save',command=save_file)
button.pack()
text = Text(window)
text.pack()

window.mainloop()