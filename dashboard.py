from tkinter import*
from PIL import Image, ImageTk
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        self.root.config(bg = "white")
        
        #=====title=====
        self.icon_title = PhotoImage(file = "IMAGES/logo1.png")
        title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#dc2700", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)

        #===btn_logout===
        btn_logout = Button(self.root, text = "Log Out", font = ("times new roman", 15, "bold"), bg = "yellow", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

        #=====clock=====
        self.lbl_clock = Label(self.root, text = "Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg = "#1795ff", fg = "white")
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
        lbl_menu = Label(LeftMenu, text = "Menu", font = ("times new roman", 20), bg = "#00ba1f").pack(side = TOP, fill = X)
        
        btn_employee = Button(LeftMenu, text = "Employee", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_supplier = Button(LeftMenu, text = "Supplier", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_category = Button(LeftMenu, text = "Category", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_product = Button(LeftMenu, text = "Product", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_sales = Button(LeftMenu, text = "Sales", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)
        btn_exit = Button(LeftMenu, text = "Exit", image = self.icon_side, compound = LEFT, padx = 5, anchor = "w", font = ("times new roman", 20, "bold"), bg = "white", bd = 3, cursor = "hand2").pack(side = TOP, fill = X)

        #====content====
        self.lbl_employee = Label(self.root, text = "Total Employees\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#9100F5", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_employee.place(x = 300, y = 120, height = 150, width = 300)

        self.lbl_supplier = Label(self.root, text = "Total Suppliers\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#FF8000", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x = 650, y = 120, height = 150, width = 300)

        self.lbl_category = Label(self.root, text = "Total Categories\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#4900FF", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_category.place(x = 1000, y = 120, height = 150, width = 300)

        self.lbl_product = Label(self.root, text = "Total Products\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#006F05", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_product.place(x = 300, y = 300, height = 150, width = 300)

        self.lbl_sales = Label(self.root, text = "Total Sales\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#6F0000", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_sales.place(x = 650, y = 300, height = 150, width = 300)
        #====footer====
        lbl_footer = Label(self.root, text = "IMS-Inventory Management System | Developed by ---\nFor any Technical Issues contact: -------", font = ("times new roman", 12), bg = "#1795ff", fg = "white").pack(side = BOTTOM, fill = X)
        
root = Tk()
obj = IMS(root)
root.mainloop()


