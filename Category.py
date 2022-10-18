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
       #========Variable========
       self.var_cat_id=StringVar()
       self.var_name=StringVar()
       #========title========
       lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
       
       card_frame=Frame(self.root,bd=1,relief=RIDGE)
       card_frame.place(x=25,y=80,width=650,height=400)

       scrolly=Scrollbar(card_frame,orient=VERTICAL)
       scrollx=Scrollbar(card_frame,orient=HORIZONTAL)

       self.categoryTable=ttk.Treeview(card_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.categoryTable.xview)
       scrolly.config(command=self.categoryTable.yview)
       
       self.icon_pro = PhotoImage(file = "IMAGES/icons/Network2_icon.png")
       #self.icon_pro = PhotoImage(file = "IMAGES/side.png")
       self.lbl_processor = Button(card_frame, image = self.icon_pro, bd = 5,  bg="White")
       self.lbl_processor.place(x = 10, y = 20 , height = 150, width = 130)

       #lbl_name=Label(self.root,text="Enter Category",font=("goudy old style",30),bg="white").place(x=50,y=100)
       #txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
       
       #btn_add=Button(self.root,text="ADD",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
       #btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
       #=======Category Details=======
       cat_frame=Frame(self.root,bd=3,relief=RIDGE)
       cat_frame.place(x=700,y=80,width=390,height=300)

       scrolly=Scrollbar(cat_frame,orient=VERTICAL)
       scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

       self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.categoryTable.xview)
       scrolly.config(command=self.categoryTable.yview)

       self.categoryTable.heading("cid",text="C ID")
       self.categoryTable.heading("name",text="Name")
       self.categoryTable["show"]="headings"
       self.categoryTable.column("cid",width=90)
       self.categoryTable.column("name",width=100)
       self.categoryTable.pack(fill=BOTH,expand=1)

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()