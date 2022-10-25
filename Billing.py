from Library import*

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        self.root.config(bg = "#f1f6f9")
        self.cart_list = []
        self.check_print = 0
        #=====title=====
        self.icon_title = PhotoImage(file = "IMAGES/logo1.png")
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#8843F2", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)

        #===btn_logout===
        btn_logout = Button(self.root, text = "Log Out", font = ("times new roman", 15, "bold"), bg = "#6A67CE", fg="White", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

    #=======Product_Frame==========
        #===Variable===
        
        #===design===
        Product_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg="white")
        Product_Frame.place(x=6,y=110,width=410,height=560)

        pTitle = Label(Product_Frame,text="All Products",font=("Roboto",18,"bold"),bg="#262626",fg="white").pack(side=TOP, fill=X)

        #=========Product Search Frame========
        self.var_search = StringVar() 
        PF_child1 = Frame(Product_Frame, bd = 2, relief = RIDGE, bg="white")
        PF_child1.place(x=2,y=42,width=398,height=90)

        lbl_search = Label(PF_child1, text = "Search Product by Name",font=("Times New Roman",15,"bold"), bg="white",fg="green").place(x=2,y=5) 
        lbl_Pname = Label(PF_child1,text ="Product Name",font=("Times New Roman",15,"bold"), bg="white").place(x=5,y=45) 
        txt_Pname = Entry(PF_child1,textvariable=self.var_search,font=("Times New Roman",15), bg="light yellow").place(x=130,y=47,width=150, height=25) 
        btn_search = Button(PF_child1, text = "Search", command = self.search, font=("Roboto",16), bg="#2196f3", fg="White", cursor="hand2").place(x=285,y=45,width=100,height=27)
        btn_Show_All = Button(PF_child1, text = "Show All", command = self.show, font=("Roboto",16), bg="#083531", fg="White", cursor="hand2").place(x=285,y=10,width=100,height=27)
        
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
        self.Product_table.bind("<ButtonRelease-1>", self.get_data)
        
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
        self.var_cal_input = StringVar()

        cal_Frame = Frame(cal_cart_Frame, bd = 9, relief = RIDGE, bg="white")
        cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input = Entry(cal_Frame, textvariable=self.var_cal_input, font = ('arial', 15, 'bold'), width = 21, bd = 10, relief = GROOVE, state = 'readonly', justify = RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(cal_Frame, text = '7', font = ('arial', 15, 'bold'),command = lambda:self.get_input(7), bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 1, column = 0)
        btn_8 = Button(cal_Frame, text = '8', font = ('arial', 15, 'bold'), command = lambda:self.get_input(8), bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 1, column = 1)
        btn_9 = Button(cal_Frame, text = '9', font = ('arial', 15, 'bold'), command = lambda:self.get_input(9),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 1, column = 2)
        btn_sum = Button(cal_Frame, text = '+', font = ('arial', 15, 'bold'),command = lambda:self.get_input('+'), bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 1, column = 3)
        
        btn_4 = Button(cal_Frame, text = '4', font = ('arial', 15, 'bold'), command = lambda:self.get_input(4),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 2, column = 0)
        btn_5 = Button(cal_Frame, text = '5', font = ('arial', 15, 'bold'), command = lambda:self.get_input(5),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 2, column = 1)
        btn_6 = Button(cal_Frame, text = '6', font = ('arial', 15, 'bold'), command = lambda:self.get_input(6),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 2, column = 2)
        btn_sub = Button(cal_Frame, text = '-', font = ('arial', 15, 'bold'), command = lambda:self.get_input('-'),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 2, column = 3)
        
        btn_1 = Button(cal_Frame, text = '1', font = ('arial', 15, 'bold'), command = lambda:self.get_input(1),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 3, column = 0)
        btn_2 = Button(cal_Frame, text = '2', font = ('arial', 15, 'bold'), command = lambda:self.get_input(2),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 3, column = 1)
        btn_3 = Button(cal_Frame, text = '3', font = ('arial', 15, 'bold'), command = lambda:self.get_input(3),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 3, column = 2)
        btn_mul = Button(cal_Frame, text = '*', font = ('arial', 15, 'bold'), command = lambda:self.get_input('*'),bd = 5, width = 4, pady = 10, cursor = "hand2").grid(row = 3, column = 3)
        
        btn_0 = Button(cal_Frame, text = '0', font = ('arial', 15, 'bold'), command = lambda:self.get_input(0),bd = 5, width = 4, pady = 15, cursor = "hand2").grid(row = 4, column = 0)
        btn_c = Button(cal_Frame, text = 'c', font = ('arial', 15, 'bold'), command = self.clear_cal,bd = 5, width = 4, pady = 15, cursor = "hand2").grid(row = 4, column = 1)
        btn_eq = Button(cal_Frame, text = '=', font = ('arial', 15, 'bold'), command = self.perform_cal,bd = 5, width = 4, pady = 15, cursor = "hand2").grid(row = 4, column = 2)
        btn_div = Button(cal_Frame, text = '/', font = ('arial', 15, 'bold'), command = lambda:self.get_input('/'),bd = 5, width = 4, pady = 15, cursor = "hand2").grid(row = 4, column = 3)
        
        #=======Product Details in Cart======
        cart_Frame=Frame(cal_cart_Frame,bd=2,relief=RIDGE)
        cart_Frame.place(x=280,y=10,width=245,height=342)
        self.cartTitle = Label(cart_Frame,text="Cart \t Total Product:  [0]",font=("Times New Roman",15,"bold"),bg="lightgrey")
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.Cart_table=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.Cart_table.xview)
        scrolly.config(command=self.Cart_table.yview)

        self.Cart_table.heading("pid",text="P_ID")
        self.Cart_table.heading("name",text="Name")
        self.Cart_table.heading("price",text="Price")
        self.Cart_table.heading("qty",text="Qty")
        self.Cart_table["show"]="headings"
        self.Cart_table.column("pid",width=30)
        self.Cart_table.column("name",width=100)
        self.Cart_table.column("price",width=70)
        self.Cart_table.column("qty",width=30)
        self.Cart_table.pack(fill=BOTH,expand=1)
        self.Cart_table.bind("<ButtonRelease-1>", self.get_data_cart)
                
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
        txt_Price= Entry(cart_Menu, textvariable=self.var_price, font=("Time New Roman",15) ,readonlybackground="light yellow",state='readonly').place(x=210,y=35,width=140,height=25)

        lbl_Qty= Label(cart_Menu, text="Quantity", font=("Time New Roman",15) ,bg="White").place(x=370,y=5)
        txt_Qty= Entry(cart_Menu, textvariable=self.var_qty, font=("Time New Roman",15) ,bg="light yellow").place(x=370,y=35,width=140,height=25)

        self.lbl_instock= Label(cart_Menu, text="In Stock", font=("Time New Roman",15) ,bg="White")
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart = Button(cart_Menu, text = "Clear", command=self.clear_cart, font=("Roboto",15), bg="#2196f3", fg="White", cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(cart_Menu, text = "Add to cart", command = self.add_update_cart, font=("Roboto",15), bg="orange", fg="White", cursor="hand2").place(x=340,y=70,width=180,height=30)  

    #======Billing Area======
        billFrame=Frame(self.root,bd=2, relief=RIDGE, bg="white")
        billFrame.place(x=953, y=110, width=410, height=410)
        
        BTitle = Label(billFrame,text="Customer Bill Area",font=("Roboto",15,"bold"),bg="#f44336", fg="white").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side = RIGHT , fill = Y)

        self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill = BOTH, expand = 1)
        scrolly.config(command = self.txt_bill_area.yview)
        
        # =========Billing buttons===========
        billMenuFrame=Frame(self.root,bd=2, relief=RIDGE, bg="white")
        billMenuFrame.place(x=953, y=520, width=410, height=145)

        self.lbl_amnt = Label(billMenuFrame, text = 'Bill Amount\n[0]', font = ('goudy old style', 15, 'bold'), bg='#3f51b5', fg = "white")
        self.lbl_amnt.place(x=2, y=5, width=120, height=70)

        self.lbl_discount = Label(billMenuFrame, text = 'Discount\n[5%]', font = ('goudy old style', 15, 'bold'), bg='#8bc34a', fg = "white")
        self.lbl_discount.place(x=124, y=5, width=120, height=70)

        self.lbl_net_pay = Label(billMenuFrame, text = 'Net Pay\n[0]', font = ('goudy old style', 15, 'bold'), bg='#607d8b', fg = "white")
        self.lbl_net_pay.place(x=246, y=5, width=160, height=70)

        btn_print = Button(billMenuFrame, text = 'Print', cursor = 'hand2',font = ('goudy old style', 15, 'bold'), bg='lightgreen', fg = "white")
        btn_print.place(x=2, y=80, width=120, height=50)

        btn_clear_all = Button(billMenuFrame, text = 'Clear All',command=self.clear_all, cursor = 'hand2',font = ('goudy old style', 15, 'bold'), bg='gray', fg = "white")
        btn_clear_all.place(x=124, y=80, width=120, height=50)

        btn_generate = Button(billMenuFrame, text = 'Generate Bill/Save Bill', command=self.generate_bill, cursor = 'hand2',font = ('goudy old style', 12, 'bold'), bg='#00968B', fg = "white")
        btn_generate.place(x=246, y=80, width=160, height=50)

        # ===================Footer==================
        footer = Label(self.root, text = "IMS-Inventory Management System | Developed by ---\nFor any Technical Issues contact: -------", font = ("times new roman", 8), bg = "#6A67CE", fg = "white").pack(side = BOTTOM, fill = X)

        self.show()
# ==============================All functions==================
    
    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            # self.Product_table=ttk.Treeview(PF_child2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select P_id,Pname,price,Qty,Status from PRODUCTS where Status='Active'")
            rows=cur.fetchall()
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def search(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","search input should be required",parent=self.root)
            else:   
                cur.execute("SELECT P_id,Pname,price,Qty,Status FROM PRODUCTS WHERE Pname LIKE '%"+self.var_search.get()+"%' and Status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Product_table.delete(*self.Product_table.get_children())
                    for row in rows:
                        self.Product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self, ev):
        f=self.Product_table.focus()
        content=(self.Product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(1)
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_instock.set(row[3])

    def get_data_cart(self, ev):
        f=self.Cart_table.focus()
        content=(self.Cart_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_instock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', "Please select product from the list", parent = self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror('Error', "Quantity is Required", parent = self.root)
        elif int(self.var_qty.get()) >= int(self.var_instock.get()):
            messagebox.showerror('Error', "Quantiy requested more than in stock availability", parent = self.root)
        else:
            price_cal = self.var_price.get()
            
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(),self.var_instock.get()]
            # ============update cart===============
            present = 'no'
            index_ = -1
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_+=1
            if present=='yes':
                op = messagebox.askyesno('Confirm', "Product already present\nDo you want to Update| Remove from the Cart List", parent = self.root)
                if op ==True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        # P_id,Pname,price,Qty,Stock
                        self.cart_list[index_][3]=self.var_qty.get()  #Qty
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            #row[2] = price per item,    #row[3] = Qty
            self.bill_amnt = self.bill_amnt + (float(row[2])*int(row[3]))
        self.discount = (self.bill_amnt * 5) / 100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text = f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text = f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product:  [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.Cart_table.delete(*self.Cart_table.get_children())
            for row in self.cart_list:
                self.Cart_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Products to cart",parent=self.root)
        else:
            #====BIL Top=====
            self.bill_top()
            #====BIL Middle====
            self.bill_middle()
            #BIL Bottom====
            self.bill_bottom()

            fp = open(f'bill/bill_{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated / Saved in Backend",parent=self.root)
            self.check_print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tXYZ-Inventory
\t Phone No. 98725*****, Kolkata-700052
{str("="*47)}
 Customer Name: {self.var_name.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate:{str(time.strftime("%d-%m-%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_middle(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()   
        try:    
            for row in self.cart_list:
                pid = row[0]
                Name = row[1]
                qty = int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Inactive'
                price = str(float(row[2])*int(row[3]))
                self.txt_bill_area.insert(END,"\n"+Name+"\t\t\t"+row[3]+"\tRs "+price)
                #====Update qty in product table=======
                cur.execute('Update product set qty=?, status=?, where pid=?',(
                    qty,status,pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

            

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs {self.bill_amnt}
 Discount\t\t\t\tRs {self.discount}
 Net Pay\t\t\t\tRs {self.net_pay}
{str("="*47)}
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    
    def clear_cart(self, ev):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_instock.set('')

    def clear_all(self, ev):
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \tTotal Product: [0]")
        self.var_search.set('')
        self.check_print=0
        self.clear_cart()
        self.show()
        self.show_cart()
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print',"Please geberate bill, to print the receipt",parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()