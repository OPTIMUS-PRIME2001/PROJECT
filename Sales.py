from tkinter import*
import tkinter
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class salesClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x600+220+130")
       self.root.title("Inventory Management System")
       self.root.config(bg="white") 
       self.root.focus_force()
       
       #title====================
       lbl_title=Label(self.root,text="View Customer Bills",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
       
       lbl_invoice = Label(self.root, text = "Invoice No.", font = ("times new roman", 15), bg = "white").place(x = 50, y = 100)

if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()