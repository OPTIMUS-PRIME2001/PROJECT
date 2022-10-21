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
        self.root.config(bg="#f1f6f9") 
        self.root.focus_force()
        
        #=======Parent Frame===============
        product_Frame = Frame(self.root, bd=3,relief=RIDGE,bg="#f1f6f9")
        product_Frame.place(x=10,y=10,width=400,height=480)

        #======Variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_contact = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        
        #==title=====
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP, fill=X)
        
        #=======Column1=========
        lbl_Pid = Label(product_Frame,text="Product Id",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=45)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=95)
        lbl_supplier = Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=145)
        lbl_product = Label(product_Frame,text= "Name",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=195)
        lbl_price = Label(product_Frame,text="Price",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=260)
        lbl_Quantity = Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=310)
        lbl_Status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="#f1f6f9").place(x=20,y=360)

        #=======Column2=====
        self.purplebuttonorg = Image.open("IMAGES/icons/Tag_cat.png")
        self.purplebutton1 = ImageTk.PhotoImage((self.purplebuttonorg.resize((150, 35), Image.ANTIALIAS)))
        cmb_pid=Label(product_Frame,image=self.purplebutton1, compound=LEFT,font=("goudy old style",18),bg="#f1f6f9").place(x=150,y=45,width=150)
        
        self.purplebutton2 = ImageTk.PhotoImage((self.purplebuttonorg.resize((200, 35), Image.ANTIALIAS)))
        cmb_cat=Label(product_Frame,image=self.purplebutton2,font=("goudy old style",18),bg="#f1f6f9").place(x=150,y=95,width=200)

        self.purplebutton3 = ImageTk.PhotoImage((self.purplebuttonorg.resize((200, 35), Image.ANTIALIAS)))
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=145,width=200)
        cmb_sup.current(0)
        
        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style",15),bg='lightyellow').place(x=150,y=195,width=200, height=50)
        Label(product_Frame,text="₹", bd=1, relief=FLAT, compound=LEFT,font=("goudy old style",22,"bold"),bg="#f1f6f9").place(x=150,y=255,width=30)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style",15),bg='lightyellow').place(x=180,y=260,width=170)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style",15),bg='lightyellow').place(x=150,y=310,width=130)
        Label(product_Frame,text="Units", bd=1, relief=FLAT, compound=LEFT,font=("goudy old style",18),bg="#f1f6f9").place(x=280,y=305,width=70)
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=360,width=200)
        cmb_status.current(0)

        #=====Button=====

        btn_update=Button(product_Frame,text="Update",command=self.update,font=("Roboto",15,"bold"),bg="#01b1a5",fg="white",cursor="hand2").place(x=120,y=410,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("Roboto",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=240,y=410,width=100,height=40)
    
        #===Searchframe======
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=420,y=10,width=660,height=80)
        
        #===Options=====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10,width=310)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("Roboto",15),bg="#4caf50",fg="white",cursor="hand2").place(x=530,y=10,width=120,height=30)

        #=======Product Details======

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","name","Category","Supplier","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid",text="Product ID")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")

        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()


    #========Functions=========================
    def fetch_cat_sup(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from supplier")
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def add(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "" or self.var_name.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),                                
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_address.get('1.0',END),
                                self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd successfully",parent=self.root)
                    self.show()        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def update(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "" or self.var_name.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? WHERE eid=? ",(
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),                                
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_address.get('1.0',END),
                                self.var_salary.get(),
                                self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated successfully",parent=self.root)
                    self.show()        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self, ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),                                
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),                                
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","search input should be required",parent=self.root)
            else:   
                cur.execute("select * from employee where "+self.var_searchby.get()+"LIKE '%"+self.var_searchtxt.get()+"%")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()