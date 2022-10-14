from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x500+220+130")
       self.root.title("Inventory Management System")
       self.root.config(bg="white") 
       self.root.focus_force()
       #========title========
       lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
       lbl_name=Label(self.root,text="Enter Category",font=("goudy old style",30),bg="white").pack(side=TOP,fill=X,padx=10,pady=10)
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()