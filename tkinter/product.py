import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import *
a = tk.Tk()
a.geometry("1600x900")
a.config(bg="white")
a.title("FlashCart (Short, snappy, and implies lightning-fast mobile shopping)")

bg = Image.open(r"bgpro.jpg")
bg = ImageTk.PhotoImage(bg.resize((1400,700)))
photo = Label(a, image=bg)
photo.place(x=0,y=0)

img1 = Image.open(r"p1.png")
img1 = ImageTk.PhotoImage(img1.resize((200,200)))
img11 = Label(a, image=img1)
img11.place(x=700,y=400)

img1name = Label(a,text="Nothing 3A",bg="#93d9e3",fg="black", font=("calibri",15,"italic"))
img1name.place(x=750,y=320)

img2 = Image.open(r"p2.jpg")
img2 = ImageTk.PhotoImage(img2.resize((200,200)))
img22 = Label(a, image=img2)
img22.place(x=1000,y=400)

img1name = Label(a,text="Iqoo Z11",bg="#93d9e3",fg="black", font=("calibri",15,"italic"))
img1name.place(x=1050,y=320)

img3 = Image.open(r"p3.jpg")
img3 = ImageTk.PhotoImage(img3.resize((200,200)))
img33 = Label(a, image=img3)
img33.place(x=700,y=100)

img4 = Image.open(r"p4.jpg")
img4 = ImageTk.PhotoImage(img4.resize((200,200)))
img44 = Label(a, image=img4)
img44.place(x=1000,y=100)
a.mainloop()
