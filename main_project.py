from tkinter import * 
from tkinter import messagebox
from tkcalendar import *

def login():
    username = e1.get()
    password = e2.get()

    if(username == "" and password == "") :
        messagebox.showinfo("", "Tidak Boleh Kosong")

    elif(username == "user" and password == "123"):
        messagebox.showinfo("","Login Berhasil")
        root.destroy()
    #    mainprogram()

    else :
        messagebox.showinfo("","Username dan Password Salah")

root = Tk()
root.title("Log In")
root.geometry("300x200")
global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Log In", command=login ,height = 3, width = 13).place(x=10, y=100)
root.mainloop()