from tkinter import*
import tkinter
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class SalesClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x600+220+130")
       self.root.title("Inventory Management System")
       self.root.config(bg="white") 
       self.root.focus_force()
       #======================

       

if __name__=="__main__":
    root=Tk()
    obj=SalesClass(root)
    root.mainloop()