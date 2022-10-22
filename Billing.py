from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        self.root.config(bg = "#f1f6f9")
        
        #=====title=====
        self.icon_title = PhotoImage(file = "IMAGES/logo1.png")
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#8843F2", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)

        #===btn_logout===
        btn_logout = Button(self.root, text = "Log Out", font = ("times new roman", 15, "bold"), bg = "#6A67CE", fg="White", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

    #=======Product_Frame==========
        #===Variable===
        self.var_search = StringVar()
        #===design===
        Product_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg="white")
        Product_Frame.place(x=6,y=110,width=410,height=560)

        pTitle = Label(Product_Frame,text="All Products",font=("Roboto",18,"bold"),bg="#262626",fg="white").pack(side=TOP, fill=X)
            
        PF_child1 = Frame(Product_Frame, bd = 2, relief = RIDGE, bg="white")
        PF_child1.place(x=2,y=42,width=398,height=90)

        lbl_search = Label(PF_child1, text = "Search Product by Name",font=("Times New Roman",15,"bold"), bg="white",fg="green").place(x=2,y=5) 
        lbl_Pname = Label(PF_child1,text ="Product Name",font=("Times New Roman",15,"bold"), bg="white").place(x=5,y=45) 
        txt_Pname = Entry(PF_child1,textvariable=self.var_search,font=("Times New Roman",15), bg="light yellow").place(x=130,y=47,width=150, height=25) 
        btn_search = Button(PF_child1, text = "Search", font=("Roboto",16), bg="#2196f3", fg="White", cursor="hand2").place(x=285,y=45,width=100,height=27)
        btn_Show_All = Button(PF_child1, text = "Show All", font=("Roboto",16), bg="#083531", fg="White", cursor="hand2").place(x=285,y=10,width=100,height=27)
        
        #=======Product Details======
        PF_child2=Frame(Product_Frame,bd=2,relief=RIDGE)
        PF_child2.place(x=2,y=140,width=398,height=385)

        scrolly=Scrollbar(PF_child2,orient=VERTICAL)
        scrollx=Scrollbar(PF_child2,orient=HORIZONTAL)

        self.Product_table=ttk.Treeview(PF_child2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)

        self.Product_table.heading("pid",text="P_ID")
        self.Product_table.heading("name",text="Name")
        self.Product_table.heading("price",text="Price")
        self.Product_table.heading("qty",text="Qty")
        self.Product_table.heading("status",text="Status")
        self.Product_table["show"]="headings"
        self.Product_table.column("pid",width=30)
        self.Product_table.column("name",width=130)
        self.Product_table.column("price",width=70)
        self.Product_table.column("qty",width=70)
        self.Product_table.column("status",width=70)
        self.Product_table.pack(fill=BOTH,expand=1)
        #self.Product_table.bind("<ButtonRelease-1>", self.get_data)
        
        lbl_notes = Label(Product_Frame,text="Note:'Enter 0 Quantity to remove product from the cart'",font=("Time New Roman",13), bg="White", fg="red").pack(side=BOTTOM,fill=X)        
        #self.show()

    #======Customer Frame=======
        #===Variables===
        self.var_name = StringVar()
        self.var_contact = StringVar()
        #===design===
        Customer_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg="white")
        Customer_Frame.place(x=420,y=110,width=530,height=75)

        pTitle = Label(Customer_Frame,text="Customer Details",font=("Roboto",15,"bold"),bg="lightgrey").pack(side=TOP, fill=X)
        lbl_Cname = Label(Customer_Frame,text ="Name",font=("Times New Roman",15,"bold"), bg="white").place(x=5,y=35) 
        txt_Cname = Entry(Customer_Frame,textvariable=self.var_name,font=("Times New Roman",15), bg="light yellow").place(x=70,y=36,width=160, height=25) 
        lbl_Contact = Label(Customer_Frame,text ="Contact No",font=("Times New Roman",15,"bold"), bg="white").place(x=245,y=35) 
        txt_contact = Entry(Customer_Frame,textvariable=self.var_contact,font=("Times New Roman",15), bg="light yellow").place(x=360,y=36,width=150, height=25) 

        #====Calculator and Cart=======
        cal_cart_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg="white")
        cal_cart_Frame.place(x=420,y=190,width=530,height=360)
        
        #====Calculator Frame===========
        cal_Frame = Frame(cal_cart_Frame, bd = 2, relief = RIDGE, bg="white")
        cal_Frame.place(x=5,y=10,width=268,height=340)





        
        #=======Product Details in Cart======
        cart_Frame=Frame(cal_cart_Frame,bd=2,relief=RIDGE)
        cart_Frame.place(x=280,y=10,width=245,height=342)
        cartTitle = Label(cart_Frame,text="Cart \t Total Product:  [0]",font=("Times New Roman",15,"bold"),bg="lightgrey").pack(side=TOP, fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.Product_table=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.Product_table.xview)
        scrolly.config(command=self.Product_table.yview)

        self.Product_table.heading("pid",text="P_ID")
        self.Product_table.heading("name",text="Name")
        self.Product_table.heading("price",text="Price")
        self.Product_table.heading("qty",text="Qty")
        self.Product_table.heading("status",text="Status")
        self.Product_table["show"]="headings"
        self.Product_table.column("pid",width=30)
        self.Product_table.column("name",width=100)
        self.Product_table.column("price",width=70)
        self.Product_table.column("qty",width=30)
        self.Product_table.column("status",width=70)
        self.Product_table.pack(fill=BOTH,expand=1)
        #self.Product_table.bind("<ButtonRelease-1>", self.get_data)
                
        #self.show()

        #======Cart_Buttons=======
        #======variables=======
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_instock = StringVar()

        #=====design========
        cart_Menu = Frame(self.root, bd = 4, relief = RIDGE, bg="white")
        cart_Menu.place(x=420,y=555,width=530,height=110)

        lbl_P_name= Label(cart_Menu, text="Product Name", font=("Time New Roman",15) ,bg="White").place(x=5,y=5)
        txt_P_name= Entry(cart_Menu, textvariable=self.var_pname, font=("Time New Roman",15) ,readonlybackground="light yellow",state='readonly').place(x=5,y=35,width=190,height=25)

        lbl_Price= Label(cart_Menu, text="PricePer Qty", font=("Time New Roman",15) ,bg="White").place(x=210,y=5)
        txt_Price= Entry(cart_Menu, textvariable=self.var_pname, font=("Time New Roman",15) ,readonlybackground="light yellow",state='readonly').place(x=210,y=35,width=140,height=25)

        lbl_Qty= Label(cart_Menu, text="Quantity", font=("Time New Roman",15) ,bg="White").place(x=370,y=5)
        txt_Qty= Entry(cart_Menu, textvariable=self.var_pname, font=("Time New Roman",15) ,bg="light yellow").place(x=370,y=35,width=140,height=25)

        self.lbl_instock= Label(cart_Menu, text="In Stock [1000]", font=("Time New Roman",15) ,bg="White")
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart = Button(cart_Menu, text = "Clear", font=("Roboto",15), bg="#2196f3", fg="White", cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(cart_Menu, text = "Add to cart", font=("Roboto",15), bg="orange", fg="White", cursor="hand2").place(x=340,y=70,width=180,height=30)  

    #======Billing Area======
        billFrame=Frame(self.root,bd=4, relief=RIDGE, bg="White")
        billFrame.place(x=953, y=110, width=410, height=410)
        BTitle = Label(Customer_Frame,text="Customer Bill Area",font=("Roboto",15,"bold"),bg="red").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrollx=Scrollbar(billFrame,orient=HORIZONTAL)


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()