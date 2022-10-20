from tkinter import*
import tkinter
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class ProductClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white") 
        self.root.focus_force()
        
        #=======Parent Frame===============
        product_Frame = Frame(self.root, bd=3,relief=RIDGE,bg="White")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #======Variables==========
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_contact=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        #==title=====
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP, fill=X)
        
        #=======Column1=========
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",18),bg="White").place(x=30,y=60)
        lbl_supplier = Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="White").place(x=30,y=110)
        lbl_product = Label(product_Frame,text= "Name",font=("goudy old style",18),bg="White").place(x=30,y=160)
        lbl_price = Label(product_Frame,text="Price",font=("goudy old style",18),bg="White").place(x=30,y=210)
        lbl_Quantity = Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="White").place(x=30,y=260)
        lbl_Status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="White").place(x=30,y=310)

        #=======Column2=====
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=60,width=200)
        cmb_sup.current(0)

        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)


if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()