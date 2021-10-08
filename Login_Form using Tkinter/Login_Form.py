import tkinter
from tkinter import*
from tkinter.ttk import *
import tkinter.messagebox
window=tkinter.Tk()
window.geometry('300x150')
window.title('Login Form')

tkinter.Label(window,text='Username').grid(row=0, column=0)
tkinter.Entry(window).grid(row=0, column=1)

tkinter.Label(window,text='Passowrd').grid(row=1, column=0)
tkinter.Entry(window).grid(row=1, column=1)

tkinter.Checkbutton(window,text='Keep me logged in').grid(column=1,row=2)

def CallBack():
    tkinter.messagebox.showinfo("Welcome", "Hellooo !")
tkinter.Button(window,text='Login', command=CallBack).grid(column=1, row=3)

window.mainloop()  