import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import *
a = tk.Tk()
a.geometry("1600x900")
#a.config(bg="white")

bg = Image.open(r"loginbg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1400,800)))
photo = Label(a, image=bg)
photo.place(x=0,y=0)

title = Label(a,text="Welcome to Login",bg="#f2f3f7",fg="black",font=("calibri",30,"bold"))
title.pack()

us = Label(a,text="Username",bg="#f7f8fa",fg="black",font=("calibri",15,"italic"))
us.place(x=500,y=200)

usd = Entry(a,bg="#f7f8fa",fg="black",font=("calibri",20,"italic"),width=25)
usd.place(x=500,y=250)

pw = Label(a,text="Password",bg="#feffff",fg="black",font=("calibri",15,"italic"))
pw.place(x=500,y=300)

pwd = Entry(a,bg="#f7f8fa",fg="black",font=("calibri",20,"italic"),width=25,show="*")
pwd.place(x=500,y=350)

def nextpage():
    a.destroy()
    import loginpage
login = Button(a,text="Explore Now -->",bg="#4d4d4d",fg="white",font=("calibri",20),width=20,command=nextpage)
login.place(x=532,y=420)
a.mainloop()
