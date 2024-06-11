import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("login")
root.resizable(False,False)
root.geometry("210x100")
nama = tk.StringVar()
umur = tk.StringVar()
password = tk.StringVar()

def klik():
    print(nama.get(),umur.get(),password.get())

ttk.Label(root,text="nama: ").grid(row=0,column=0)
ttk.Entry(root,textvariable=nama).grid(row=0,column=1)
ttk.Label(root,text="umur: ").grid(row=1,column=0)
ttk.Entry(root,textvariable=umur).grid(row=1,column=1)
ttk.Label(root,text="password: ").grid(row=2,column=0)
ttk.Entry(root,textvariable=password).grid(row=2,column=1)
ttk.Button(root,text="input data",command=klik).grid(row=3,column=1)

root.mainloop()