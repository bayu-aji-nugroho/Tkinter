import tkinter as tk
from tkinter import ttk

class gui():
    no = 0
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.layout()
        self.widget()
        self.root.mainloop()
        
    def layout(self):
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.frame1 = ttk.Frame(self.root)        
        self.frame2 = ttk.Frame(self.root)
        self.frame1.grid(row=0,column=0)
        self.frame2.grid(row=0,column=1)
        
    def widget(self):
        ttk.Label(self.frame1,text="nama: ").pack(padx=10,side="left")
        ttk.Entry(self.frame1).pack(side="left")
        ttk.Button(self.frame1,text="input",command=self.klik).pack()
        self.label0 = ttk.Label(self.frame2)
        self.label0.pack()
        
    def klik(self):
        self.no += 1
        self.label0.config(text=self.no)
        
        

if __name__ == "__main__":
    ob = gui()