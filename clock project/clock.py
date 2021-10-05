# importing libraries
import tkinter
from tkinter.ttk import*
from tkinter import *
import time
from time import strftime

# initializing window
window=Tk()
window.title('CLOCK')
window.geometry('500x300')
window.configure(background='#000000') 

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(window, font=("ds-digital,80"), background = "#000000", foreground = "#00FF00")
label.place(relx = 0.5, rely = 0.5, anchor = 'center')

time()
window, mainloop()