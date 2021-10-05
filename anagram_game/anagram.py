import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = ["harry", "hermione", "ron", 
"potterhead", "snape", "dumbledore", "voldemort"]

words = ["ryrha", "mieroneh", "orn", 
"ttopraedeh", "anspe", "ulrdmedobe", "ldermovot"]

num = random.randrange(0, len(words), 1)

def default():
    global words, answers, num
    lbl.config(text = words[num])

def reset():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)

def check_ans():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Well Done!", "That's Correct!")
        reset()
    else:
        messagebox.showerror("Error", "That's not corret!")
        e1.delete(0, END)

root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Anagrams")
root.configure(background = "#6c4f57")

lbl = Label(
    root,
    text = "Your here",
    font= ("Verdana", 18),
    bg = "#252626",
    fg = "#FFF",
)
lbl.pack(pady = 30, ipady = 10, ipadx = 10)

ans_1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans_1,
)
e1.pack(ipady = 5, ipadx = 5)

btn_check = Button(
    root, 
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#ae8d92",
    fg = "#003458",
    relief = GROOVE,
    command = check_ans,
)
btn_check.pack(pady = 40)

btn_reset = Button(
    root, 
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#ae8d92",
    fg = "#292939",
    relief = GROOVE,
    command = reset,
)
btn_reset.pack()

default()
root.mainloop()
