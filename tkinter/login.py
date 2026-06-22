import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import *
a = tk.Tk()
a.geometry("1600x900")
#a.config(bg="white")
a.title("FlashCart (Short, snappy, and implies lightning-fast mobile shopping)")
bg = Image.open(r"bg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1400,800)))
photo = Label(a, image=bg)
photo.place(x=0,y=0)

title = Label(a,text="FlashCart",bg="#101010",fg="white",font=("Century Gothic",40))
title.place(x=575,y=300)

s="Short, snappy, and implies \nlightning-fast mobile shopping"
slogan = Label(a,text=s,bg="#101010",fg="white",font=("Century Gothic",20))
slogan.place(x=505,y=400)

def nextpage():
    a.destroy()
    import loginpage
explore = Button(a,text="Explore Now -->",bg="#4d4d4d",fg="white",font=("calibri",20),command=nextpage)
explore.place(x=600,y=520)

a.mainloop()
 
