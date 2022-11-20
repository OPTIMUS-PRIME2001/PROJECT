import LoginPage
from Library import*

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        self.root.config(bg = "#f1f6f9")
        self.root.iconbitmap('IMAGES/icons/computer.ico')
        
        #=====title=====
        self.icon_title = PhotoImage(file = "IMAGES/logo1.png")
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#8843F2", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)

        #===btn_logout===
        btn_logout = Button(self.root, text = "Log Out",command=self.logout, font = ("times new roman", 15, "bold"), bg = "#6A67CE", fg="White", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

        #=====Welcome=====
        self.welcomebg = ImageTk.PhotoImage(Image.open("IMAGES/bgcolor1.png").resize((790, 200), Image.ANTIALIAS))
        self.welcomepic = ImageTk.PhotoImage(Image.open("IMAGES/welcome2.png").resize((245, 245), Image.ANTIALIAS))
        lbl_welc = Frame(self.root,bd=3,relief=FLAT,bg = "#f1f6f9")
        lbl_welc.place(x = 229, y = 70, width = 800, height = 200)

        self_bg = Label(lbl_welc, image=self.welcomebg, font = ("times new roman", 15), bg = "#f1f6f9", fg = "white")
        self_bg.place(x = 0, y = 0, width = 800, height = 200)
        #self.welpic = Label(lbl_welc, image = self.welcomepic,bg='grey',compound=CENTER)
        #self.welpic.place(x = 570, y = 0, height = 200, width = 200)
        self.canvas = Canvas(lbl_welc, width=200, height=180, bd=2, highlightthickness=2)
        self.image_id = self.canvas.create_image(50,50, image=self.welcomepic)

        self.note1 = Label(lbl_welc, text="Welcome Back Username!\n We're glad You're here", compound=LEFT, font = ("Roboto", 25, "bold"), bg = "#c9ceef" , fg = "#6F38C5")
        self.note1.place(x = 15, y = 55, width = 520, height = 100 )
        #self.note2 = Label(lbl_welc, text="The fastest way to help your Customer", compound=LEFT, font = ("Roboto", 25, "bold"), bg = "#c9ceef" , fg = "#6F38C5")
        #self.note2.place(x = 15, y = 55, width = 520, height = 100 )
        #====Clock=====
        self.btn_bg1 = ImageTk.PhotoImage(Image.open("IMAGES/button_bg.png").resize((265, 190), Image.ANTIALIAS))
        Label(self.root,image=self.btn_bg1).place(x = 1040, y = 80, width = 257, height = 185)
        self.lbl_clock = Frame(self.root,bd=0,relief=FLAT,bg = "White",padx=10,pady=30)
        self.lbl_clock.place(x = 1050, y = 90, width = 239, height = 160)
        
        self.Time_label = Label( self.lbl_clock, text = "00 : 00 : 00", font = ("Technology", 30), bg = "White", fg = "#00D2FF")  
        self.meridiem_label = Label( self.lbl_clock, text = "AM", font = ("Technology", 32),  bg = "White", fg = "#00D2FF" )  
        Label( self.lbl_clock, text = "Hours     Minutes    Seconds",compound=LEFT, font = ("Arial",10 ),  bg = "White", fg = "#a9a9a9").place(x=0,y=64,width=185)  
        self.day_label = Label( self.lbl_clock, text = "WEDNESDAY", compound=RIGHT,font = ("Agency FB", 23),  bg = "White", fg = "#00D2FF" )  
        self.Date_label = Label( self.lbl_clock, text = "DD-MM-YYYY", font = ("Technology", 23),  bg = "White", fg = "#00D2FF" )  
        
        # using the grid() method to set the position of the above  
        # labels in a grid form on the window screen  
        
        self.Time_label.place(x=0,y=28, width=170) 
        self.meridiem_label.place(x=175,y=28)
        self.day_label.place(x=5,y=80,width=310)  
        self.Date_label.place(x=0,y=0)
        self.update_time()
        #===Left Menu===
        self.MenuLogo = Image.open("IMAGES/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd = 2, relief = RIDGE, bg = "white")
        LeftMenu.place(x = 0, y = 71, width = 200, height = 590)

        lbl_menuLogo = Label(LeftMenu, image = self.MenuLogo)
        lbl_menuLogo.pack(side = TOP, fill = X)
        
        self.dash = ImageTk.PhotoImage(Image.open("IMAGES/icons/Dashboard_icon.png").resize((40, 40), Image.ANTIALIAS))
        self.employee_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/employee_icon.png").resize((50, 50), Image.ANTIALIAS))
        self.supplier_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/supplier_icon.png").resize((40, 40), Image.ANTIALIAS))
        self.category_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/category_icon.png").resize((40, 40), Image.ANTIALIAS))
        self.product_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/product_icon.png").resize((50, 50), Image.ANTIALIAS))
        self.sales_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/sales.png").resize((50, 50), Image.ANTIALIAS))
        self.exit_icon = ImageTk.PhotoImage(Image.open("IMAGES/icons/exit.png").resize((55, 55), Image.ANTIALIAS))

        lbl_menu = Label(LeftMenu, text = "Dashboard", image = self.dash, compound = LEFT, padx = 5,bg="White", font = ("times new roman", 22, "bold") ).pack(side = TOP, fill = X)
        
        btn_employee = Button(LeftMenu, text = "Employee",command = self.employee, image = self.employee_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_supplier = Button(LeftMenu, text = "Supplier", command = self.supplier, image = self.supplier_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_category = Button(LeftMenu, text = "Category", command = self.category, image = self.category_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_product = Button(LeftMenu, text = "Product", command = self.product, image = self.product_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_sales = Button(LeftMenu, text = "Sales", command = self.sales, image = self.sales_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_exit = Button(LeftMenu, text = "Exit", command = self.root.destroy, image = self.exit_icon, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)

        #====content====
        self.btn_bg = ImageTk.PhotoImage(Image.open("IMAGES/button_bg.png").resize((265, 150), Image.ANTIALIAS))
        r1y=280
        self.icon1 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card1_truck.png").resize((70, 70), Image.ANTIALIAS))
        dash_card1=Frame(self.root,bd=0,relief=FLAT,bg = "#f1f6f9")
        dash_card1.place(x = 230, y = r1y, height = 150, width = 260)
        Label(dash_card1,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon1 = Label(dash_card1, image = self.icon1, compound=CENTER, bg = "white", fg="#01b1a5")
        self.lbl_count1 = Label(dash_card1, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_reorder = Label(dash_card1, text = "Products to Reorder",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon1.place(x = 7, y = 10, height = 70, width = 243)
        self.lbl_count1.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_reorder.place(x = 7, y = 110, height = 25, width = 243)

        
        self.icon2 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card2_currentstock.png").resize((50, 50), Image.ANTIALIAS))
        dash_card2=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card2.place(x = 500, y = r1y, height = 150, width = 260)
        Label(dash_card2,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon2 = Label(dash_card2, image = self.icon2,compound=CENTER, bg = "White")
        self.lbl_count2 = Label(dash_card2, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_current = Label(dash_card2, text = "Current Stock (units)",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon2.place(x = 7, y = 5, height = 65, width = 243)
        self.lbl_count2.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_current.place(x = 7, y = 110, height = 25, width = 243)

        self.icon3 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card3_zerostock.png").resize((55, 55), Image.ANTIALIAS))
        dash_card3=Frame(self.root, bd=0, relief=FLAT, bg = "#f1f6f9")
        dash_card3.place(x = 770, y = r1y, height = 150, width = 260)
        Label(dash_card3,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon3 = Label(dash_card3, image = self.icon3, compound=CENTER,bg = "White")
        self.lbl_count3 = Label(dash_card3, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_zerostock = Label(dash_card3, text = "Zero Stock Products",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon3.place(x = 7, y = 10, height = 65, width = 243)
        self.lbl_count3.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_zerostock.place(x = 7, y = 110, height = 25, width = 243)

        self.icon4 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card4_products.png").resize((65, 65), Image.ANTIALIAS))
        dash_card4=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card4.place(x = 1040, y = r1y, height = 150, width = 260)
        Label(dash_card4,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon4 = Label(dash_card4, image = self.icon4,compound=CENTER, bg = "White")
        self.lbl_count4 = Label(dash_card4, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_products = Label(dash_card4, text = "Products",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon4.place(x = 7, y = 10, height = 65, width = 243)
        self.lbl_count4.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_products.place(x = 7, y = 110, height = 25, width = 243)

        r2y=440
        self.icon5 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card5_value.png").resize((60, 60), Image.ANTIALIAS))
        dash_card5=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card5.place(x = 230, y = r2y, height = 150, width = 260)
        Label(dash_card5,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon5 = Label(dash_card5, image = self.icon5,compound=CENTER, bg = "White")
        self.lbl_count5 = Label(dash_card5, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_value = Label(dash_card5, text = "Stock Current Value(₹)",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon5.place(x = 7, y = 10, height = 65, width = 243)
        self.lbl_count5.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_value.place(x = 7, y = 110, height = 25, width = 243)

        self.icon6 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card6_employee.png").resize((100, 100), Image.ANTIALIAS))
        dash_card6=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card6.place(x = 500, y = r2y, height = 150, width = 260)
        Label(dash_card6,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon6 = Label(dash_card6, image = self.icon6, compound=CENTER,bg = "White")
        self.lbl_count6 = Label(dash_card6, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_employee = Label(dash_card6, text = "Employees",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon6.place(x = 7, y = 10, height = 65, width = 243)
        self.lbl_count6.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_employee.place(x = 7, y = 110, height = 25, width = 243)

        self.icon7 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card7_supplier.png").resize((55, 55), Image.ANTIALIAS))
        dash_card7=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card7.place(x = 770, y = r2y, height = 150, width = 260)
        Label(dash_card7,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon7 = Label(dash_card7, image = self.icon7, compound=CENTER, bg = "White")
        self.lbl_count7 = Label(dash_card7, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_supplier = Label(dash_card7, text = "Suppliers",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon7.place(x = 7, y = 5, height = 65, width = 243)
        self.lbl_count7.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_supplier.place(x = 7, y = 110, height = 25, width = 243)

        self.icon8 = ImageTk.PhotoImage(Image.open("IMAGES/icons/card8_sales.png").resize((100, 60), Image.ANTIALIAS))
        dash_card8=Frame(self.root,bd=0, relief=FLAT,bg = "#f1f6f9")
        dash_card8.place(x = 1040, y = r2y, height = 150, width = 260)
        Label(dash_card8,image=self.btn_bg).pack(fill=BOTH)
        self.lbl_icon8 = Label(dash_card8, image = self.icon8, compound=CENTER, bg = "White")
        self.lbl_count8 = Label(dash_card8, text = "0", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 30, "bold"))
        self.lbl_sales = Label(dash_card8, text = "Total Sales (₹)",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon8.place(x = 7, y = 5, height = 70, width = 243)
        self.lbl_count8.place(x = 7, y = 65, height = 35, width = 243)
        self.lbl_sales.place(x = 7, y = 110, height = 25, width = 243)
        #====footer====
        lbl_footer = Label(self.root, text = "Developed by Group 5 Members : Saptarshi Chatterjee, Saptarshi Majhi, Pratik Gayen, Somak Poddar, Priyanshu Sharma \nFor any Technical Issues contact: -------", font = ("times new roman", 12), bg = "#6A67CE", fg = "white").pack(side = BOTTOM, fill = X)
    
        self.update_content()
    #==============================================================================================================================
    
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win) 

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
    
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win) 
    
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_time(self):  
        # using the strftime() method to represent current time in string  
        hour = str(time.strftime("%H"))  
        Time = str(time.strftime("%I : %M : %S"))   
        Date = str(time.strftime("%d-%m-%Y"))
        Day = str(time.strftime("%A"))
        # if the hour range between 12 to 24 and minute is greater  
        # than or equal to 0 then set the value of the meridiem_label label to PM  
        if int(hour) >= 12 and int(hour) < 24 and int (str(time.strftime("%M"))) >= 0:  
            self.meridiem_label = "PM"  
        # else set the value of the meridiem_label to AM  
        else:  
            self.meridiem_label = "AM"  
  
        # configuring the text of the date,hour, minute, and second labels   
        self.Time_label.config(text = f" {str(Time)} ")
        self.Date_label.config(text = f" {str(Date)} ")
        self.day_label.config(text = f" {str(Day)} ")
        self.note1.config(text = f"Welcome Back {LoginPage.var_UserName}!\n We're glad You're here")
        # using the after() to call the display_time() after 200 milliseconds  
        self.Time_label.after(200, self.update_time)  
    
    def update_content(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM PRODUCTS")
            product=cur.fetchall()
            reorder = 0
            cur_stock = 0
            zero_stock = 0
            stock_value = 0.0
            for p in product:
                cur_stock += int(p[5])
                if int(p[5]) == 0:
                    zero_stock += 1
                if int(p[5]) < 5:
                    reorder += 1
                stock_value = stock_value + float(p[4])*int(p[5])
            self.lbl_count1.config(text=f'{str(reorder)}')
            self.lbl_count2.config(text=f'{str(cur_stock)}')
            self.lbl_count3.config(text=f'{str(zero_stock)}')
            self.lbl_count4.config(text=f'{str(len(product))}')
            self.lbl_count5.config(text=f'{str(stock_value)}')

            cur.execute("SELECT * FROM employee")
            employee=cur.fetchall()
            self.lbl_count6.config(text=f'{str(len(employee))}')

            cur.execute("SELECT * FROM supplier")
            supplier=cur.fetchall()
            self.lbl_count7.config(text=f'{str(len(supplier))}')

            cur.execute("SELECT Net_Pay FROM Bills")
            bills=cur.fetchall()
            Sales_value = 0
            for net in bills: Sales_value += net[0] 
            self.lbl_count8.config(text=f'{str(Sales_value)}')
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python LoginPage.py")
  
# main function
if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()