import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("My Spelling Checker")
title_img = PhotoImage(file="icon3.png")
root.iconphoto(False,title_img)
root.geometry("700x400")
root.configure(bg="#dae6f6")

def check_cpelling():
    word = input_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root,text="Correct text is : ",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label(root,text="Spelling Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

input_text = Entry(root,justify="center",width=30,font=('poppins',25),bg="white",bd=2)
input_text.pack(pady=10)
input_text.focus()

btn = Button(root,text="Check",font=("arial",20,"bold"),command=check_cpelling)
btn.pack(pady=10)

spell = Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)

root.mainloop()