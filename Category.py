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
       card_frame.place(x=20,y=80,width=720,height=400)

       scrolly=Scrollbar(card_frame,orient=VERTICAL)
       scrollx=Scrollbar(card_frame,orient=HORIZONTAL)

       self.categoryTable=ttk.Treeview(card_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.categoryTable.xview)
       scrolly.config(command=self.categoryTable.yview)
       
       #=======ROW1==========================
       self.icon_pro = Image.open("IMAGES/icons/Processor_icon.png")
       self.icon_pro = self.icon_pro.resize((150, 150), Image.ANTIALIAS)
       self.icon_pro = ImageTk.PhotoImage(self.icon_pro)
       self.lbl_processor = Button(card_frame, image = self.icon_pro, relief="groove", bd = 5,  bg="White")
       self.lbl_processor.place(x = 10, y = 20 , height = 150, width = 130)

       self.icon_Mod = Image.open("IMAGES/icons/Motherboard_icon.png")
       self.icon_Mod = self.icon_Mod.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mod = ImageTk.PhotoImage(self.icon_Mod)
       self.lbl_Motherboard = Button(card_frame, image = self.icon_Mod, relief="groove", bd = 5,  bg="White")
       self.lbl_Motherboard.place(x = 150, y = 20 , height = 150, width = 130)

       self.icon_Lap = Image.open("IMAGES/icons/Laptop_icon.png")
       self.icon_Lap = self.icon_Lap.resize((130, 130), Image.ANTIALIAS)
       self.icon_Lap = ImageTk.PhotoImage(self.icon_Lap)
       self.lbl_Laptops = Button(card_frame, image = self.icon_Lap, relief="groove", bd = 5,  bg="White")
       self.lbl_Laptops.place(x = 290, y = 20 , height = 150, width = 130)
       
       self.icon_Mon = Image.open("IMAGES/icons/Monitors_icon.png")
       self.icon_Mon = self.icon_Mon.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mon = ImageTk.PhotoImage(self.icon_Mon)
       self.lbl_Monitors = Button(card_frame, image = self.icon_Mon, relief="groove", bd = 5,  bg="White")
       self.lbl_Monitors.place(x = 430, y = 20 , height = 150, width = 130)

       self.icon_Desk = Image.open("IMAGES/icons/Desktop_icon.png")
       self.icon_Desk = self.icon_Desk.resize((130, 130), Image.ANTIALIAS)
       self.icon_Desk = ImageTk.PhotoImage(self.icon_Desk)
       self.lbl_Desk = Button(card_frame, image = self.icon_Desk, relief="groove", bd = 5,  bg="White")
       self.lbl_Desk.place(x = 570, y = 20 , height = 150, width = 130)

       #============ROW2================
       self.icon_Store = Image.open("IMAGES/icons/Storage_icon.png")
       self.icon_Store = self.icon_Store.resize((130, 130), Image.ANTIALIAS)
       self.icon_Store = ImageTk.PhotoImage(self.icon_Store)
       self.lbl_Storage = Button(card_frame, image = self.icon_Store, relief="groove", bd = 5,  bg="White")
       self.lbl_Storage.place(x = 10, y = 180 , height = 150, width = 130)

       self.icon_Pri = Image.open("IMAGES/icons/Printers_icon.png")
       self.icon_Pri = self.icon_Pri.resize((125, 135), Image.ANTIALIAS)
       self.icon_Pri = ImageTk.PhotoImage(self.icon_Pri)
       self.lbl_Printer = Button(card_frame, image = self.icon_Pri, relief="groove", bd = 5,  bg="White")
       self.lbl_Printer.place(x = 150, y = 180 , height = 150, width = 130)

       self.icon_Net = Image.open("IMAGES/icons/Network_icon.png")
       self.icon_Net = self.icon_Net.resize((130, 130), Image.ANTIALIAS)
       self.icon_Net = ImageTk.PhotoImage(self.icon_Net)
       self.lbl_Network = Button(card_frame, image = self.icon_Net, relief="groove", bd = 5,  bg="White")
       self.lbl_Network.place(x = 290, y = 180 , height = 150, width = 130)
       
       self.icon_IntC = Image.open("IMAGES/icons/InternalComponents_icon.png")
       self.icon_IntC = self.icon_IntC.resize((130, 130), Image.ANTIALIAS)
       self.icon_IntC = ImageTk.PhotoImage(self.icon_IntC)
       self.lbl_InternalComponent = Button(card_frame, image = self.icon_IntC, relief="groove", bd = 5,  bg="White")
       self.lbl_InternalComponent.place(x = 430, y = 180 , height = 150, width = 130)

       self.icon_Per = Image.open("IMAGES/icons/Monitors_icon.png")
       self.icon_Per = self.icon_Per.resize((130, 130), Image.ANTIALIAS)
       self.icon_Per = ImageTk.PhotoImage(self.icon_Per)
       self.lbl_Peripherals = Button(card_frame, image = self.icon_Per, relief="groove", bd = 5,  bg="White")
       self.lbl_Peripherals.place(x = 570, y = 180 , height = 150, width = 130)

       #============ROW3===============
       


       #=======Category Details=======
       cat_frame=Frame(self.root,bd=3,relief=RIDGE)
       cat_frame.place(x=750,y=80,width=390,height=300)

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