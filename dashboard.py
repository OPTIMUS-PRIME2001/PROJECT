from tkinter import*
from PIL import Image, ImageTk
from Category import categoryClass
from Employee import employeeClass
from supplier import supplierClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        self.root.config(bg = "#f1f6f9")
        
        #=====title=====
        self.icon_title = PhotoImage(file = "IMAGES/logo1.png")
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#dc2700", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)

        #===btn_logout===
        btn_logout = Button(self.root, text = "Log Out", font = ("times new roman", 15, "bold"), bg = "yellow", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

        #=====clock=====
        self.lbl_clock = Label(self.root, text = "Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg = "#3bc8a7", fg = "white")
        self.lbl_clock.place(x = 0, y = 70, relwidth = 1, height = 30)

        #===Left Menu===
        self.MenuLogo = Image.open("IMAGES/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd = 2, relief = RIDGE, bg = "white")
        LeftMenu.place(x = 0, y = 102, width = 200, height = 565)

        lbl_menuLogo = Label(LeftMenu, image = self.MenuLogo)
        lbl_menuLogo.pack(side = TOP, fill = X)

        self.icon_side = PhotoImage(file = "IMAGES/side.png")
        lbl_menu = Label(LeftMenu, text = "Menu", font = ("times new roman", 20), bg = "#01b1a5").pack(side = TOP, fill = X)
        
        btn_employee = Button(LeftMenu, text = "Employee",command = self.employee, image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_supplier = Button(LeftMenu, text = "Supplier", command = self.supplier, image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_category = Button(LeftMenu, text = "Category", command=self.category, image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_product = Button(LeftMenu, text = "Product", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_sales = Button(LeftMenu, text = "Sales", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_exit = Button(LeftMenu, text = "Exit", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)

        #====content====
        
        dash_card1=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card1.place(x = 230, y = 120, height = 150, width = 260)
        self.lbl_icon1 = Label(dash_card1, image = "", bg = "White")
        self.lbl_count1 = Label(dash_card1, text = "9", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_reorder = Label(dash_card1, text = "Products to Reorder",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon1.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count1.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_reorder.place(x = 0, y = 110, height = 25, width = 250)

        dash_card2=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card2.place(x = 500, y = 120, height = 150, width = 260)
        self.lbl_icon2 = Label(dash_card2, image = "", bg = "White")
        self.lbl_count2 = Label(dash_card2, text = "1494", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_current = Label(dash_card2, text = "Current Stock (units)",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon2.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count2.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_current.place(x = 0, y = 110, height = 25, width = 250)

        dash_card3=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card3.place(x = 770, y = 120, height = 150, width = 260)
        self.lbl_icon3 = Label(dash_card3, image = "", bg = "White")
        self.lbl_count3 = Label(dash_card3, text = "7", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_zerostock = Label(dash_card3, text = "Zero Stock Products",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon3.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count3.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_zerostock.place(x = 0, y = 110, height = 25, width = 250)

        dash_card4=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card4.place(x = 1040, y = 120, height = 150, width = 260)
        self.lbl_icon4 = Label(dash_card4, image = "", bg = "White")
        self.lbl_count4 = Label(dash_card4, text = "102", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_products = Label(dash_card4, text = "Products",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon4.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count4.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_products.place(x = 0, y = 110, height = 25, width = 250)

        dash_card5=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card5.place(x = 230, y = 280, height = 150, width = 260)
        self.lbl_icon5 = Label(dash_card5, image = "", bg = "White")
        self.lbl_count5 = Label(dash_card5, text = "45,626.00", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_value = Label(dash_card5, text = "Stock Current Value(₹)",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon5.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count5.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_value.place(x = 0, y = 110, height = 25, width = 250)

        dash_card6=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card6.place(x = 500, y = 280, height = 150, width = 260)
        self.lbl_icon6 = Label(dash_card6, image = "", bg = "White")
        self.lbl_count6 = Label(dash_card6, text = "15", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_employee = Label(dash_card6, text = "Employees",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon6.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count6.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_employee.place(x = 0, y = 110, height = 25, width = 250)

        dash_card7=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card7.place(x = 770, y = 280, height = 150, width = 260)
        self.lbl_icon7 = Label(dash_card7, image = "", bg = "White")
        self.lbl_count7 = Label(dash_card7, text = "27", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_supplier = Label(dash_card7, text = "Suppliers",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon7.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count7.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_supplier.place(x = 0, y = 110, height = 25, width = 250)

        dash_card8=Frame(self.root,bd=3,relief=RIDGE,bg = "White")
        dash_card8.place(x = 1040, y = 280, height = 150, width = 260)
        self.lbl_icon8 = Label(dash_card8, image = "", bg = "White")
        self.lbl_count8 = Label(dash_card8, text = "45,626", bg = "White", compound=CENTER,fg = "black", font = ("Roboto", 32, "bold"))
        self.lbl_sales = Label(dash_card8, text = "Total Sales",compound=CENTER, bg = "White", fg = "#01b1a5", font = ("Roboto", 15, "bold"))
        self.lbl_icon8.place(x = 50, y = 0, height = 50, width = 50)
        self.lbl_count8.place(x = 0, y = 65, height = 35, width = 250)
        self.lbl_sales.place(x = 0, y = 110, height = 25, width = 250)
        #====footer====
        lbl_footer = Label(self.root, text = "IMS-Inventory Management System | Developed by ---\nFor any Technical Issues contact: -------", font = ("times new roman", 12), bg = "#1795ff", fg = "white").pack(side = BOTTOM, fill = X)
    
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
if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()


