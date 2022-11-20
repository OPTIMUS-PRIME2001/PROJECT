from Library import*

class categoryClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1140x600+220+130")
       self.root.title("Inventory Management System")
       self.root.config(bg="#f1f6f9") 
       self.root.iconbitmap('IMAGES\icons\computer.ico')
       self.root.focus_force()
       #========Variable========
       self.var_cat_id=StringVar()
       self.var_name=StringVar()

       #========title========
       lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)

       w = 760
       h = 520
       canvas = Canvas(self.root, bg = "white", bd = 1, relief = "ridge", height = h, width = w, scrollregion=(0,0,600,600))
       canvas.config(width=w,height=h)
       canvas.place(x=10,y=75, height = h, width = w)     
      
       self.btn_val=StringVar()
       #=======ROW1==========================
       cardFrame1 = Frame(canvas, width = 720, height = 150, bg = "white")
      #  Row1h=10
       self.icon_pro = Image.open("IMAGES/icons/Processor_icon.png")
       self.icon_pro = self.icon_pro.resize((150, 150), Image.ANTIALIAS)
       self.icon_pro = ImageTk.PhotoImage(self.icon_pro)
       self.lbl_processor = Button(cardFrame1, image = self.icon_pro,command=self.btn1, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_processor.pack(side = "left")

       self.icon_Mod = Image.open("IMAGES/icons/Motherboard_icon.png")
       self.icon_Mod = self.icon_Mod.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mod = ImageTk.PhotoImage(self.icon_Mod)
       self.lbl_Motherboard = Button(cardFrame1, image = self.icon_Mod,command=self.btn2, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Motherboard.pack(side = "left", padx = 10)

       self.icon_Lap = Image.open("IMAGES/icons/Laptop_icon.png")
       self.icon_Lap = self.icon_Lap.resize((130, 130), Image.ANTIALIAS)
       self.icon_Lap = ImageTk.PhotoImage(self.icon_Lap)
       self.lbl_Laptops = Button(cardFrame1, image = self.icon_Lap,command=self.btn3, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Laptops.pack(side = "left")

       self.icon_Mon = Image.open("IMAGES/icons/Monitors_icon.png")
       self.icon_Mon = self.icon_Mon.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mon = ImageTk.PhotoImage(self.icon_Mon)
       self.lbl_Monitors = Button(cardFrame1, image = self.icon_Mon,command=self.btn4, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Monitors.pack(side = "left", padx = 10)

       self.icon_Desk = Image.open("IMAGES/icons/Desktop_icon.png")
       self.icon_Desk = self.icon_Desk.resize((130, 130), Image.ANTIALIAS)
       self.icon_Desk = ImageTk.PhotoImage(self.icon_Desk)
       self.lbl_Desk = Button(cardFrame1, image = self.icon_Desk,command=self.btn5, relief="groove", bd = 5,  bg="white", height = 150, width = 130)    
       self.lbl_Desk.pack(side = "left")

       cardFrame1.pack(padx = 5, pady = 5, side="top", fill = X)
       
       #============ROW2================
       cardFrame2 = Frame(canvas, width = 770, height = 150, bg = "white")
      #  Row2h=170
       self.icon_Store = Image.open("IMAGES/icons/Storage_icon.png")
       self.icon_Store = self.icon_Store.resize((130, 130), Image.ANTIALIAS)
       self.icon_Store = ImageTk.PhotoImage(self.icon_Store)
       self.lbl_Storage = Button(cardFrame2, image = self.icon_Store,command=self.btn6, relief="groove", bd = 5,  bg="white", height = 150, width = 130)      
       self.lbl_Storage.pack(side = "left")

       self.icon_Pri = Image.open("IMAGES/icons/Printers_icon.png")
       self.icon_Pri = self.icon_Pri.resize((125, 135), Image.ANTIALIAS)
       self.icon_Pri = ImageTk.PhotoImage(self.icon_Pri)
       self.lbl_Printer = Button(cardFrame2, image = self.icon_Pri,command=self.btn7, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Printer.pack(side = "left", padx = 10)

       self.icon_Net = Image.open("IMAGES/icons/Network_icon.png")
       self.icon_Net = self.icon_Net.resize((130, 130), Image.ANTIALIAS)
       self.icon_Net = ImageTk.PhotoImage(self.icon_Net)
       self.lbl_Network = Button(cardFrame2, image = self.icon_Net,command=self.btn8, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Network.pack(side = "left")
       
       self.icon_IntC = Image.open("IMAGES/icons/InternalComponents_icon.png")
       self.icon_IntC = self.icon_IntC.resize((130, 130), Image.ANTIALIAS)
       self.icon_IntC = ImageTk.PhotoImage(self.icon_IntC)
       self.lbl_InternalComponent = Button(cardFrame2, image = self.icon_IntC,command=self.btn9, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_InternalComponent.pack(side = "left", padx = 10)

       self.icon_Per = Image.open("IMAGES/icons/Peripherals_icon.png")
       self.icon_Per = self.icon_Per.resize((120, 120), Image.ANTIALIAS)
       self.icon_Per = ImageTk.PhotoImage(self.icon_Per)
       self.lbl_Peripherals = Button(cardFrame2, image = self.icon_Per,command=self.btn10, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Peripherals.pack(side = "left")

       cardFrame2.pack(padx = 5, pady = 5, side="top", fill = X)

       #============ROW3===============
       cardFrame3 = Frame(canvas, width = 770, height = 150, bg = "white")
      #  Row3h = 320
       self.icon_Audio = Image.open("IMAGES/icons/Audio_Accessories_icon.png")
       self.icon_Audio = self.icon_Audio.resize((130, 130), Image.ANTIALIAS)
       self.icon_Audio = ImageTk.PhotoImage(self.icon_Audio)
       self.lbl_Audio_Accessories = Button(cardFrame3, image = self.icon_Audio,command=self.btn11, relief="groove", bd = 5, bg="white", height = 150, width = 130)
       self.lbl_Audio_Accessories.pack(side = "left")

       self.icon_Vid = Image.open("IMAGES/icons/Video_Accessories_icon.png")
       self.icon_Vid = self.icon_Vid.resize((125, 135), Image.ANTIALIAS)
       self.icon_Vid = ImageTk.PhotoImage(self.icon_Vid)
       self.lbl_Video_Accessories= Button(cardFrame3, image = self.icon_Vid,command=self.btn12, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Video_Accessories.pack(side = "left", padx = 10)

       self.icon_Cable = Image.open("IMAGES/icons/Cables_icon.png")
       self.icon_Cable = self.icon_Cable.resize((130, 130), Image.ANTIALIAS)
       self.icon_Cable = ImageTk.PhotoImage(self.icon_Cable)
       self.lbl_CableAdapter = Button(cardFrame3, image = self.icon_Cable,command=self.btn13, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_CableAdapter.pack(side = "left")

       self.icon_MobTab = Image.open("IMAGES/icons/Mobiles_Tablets_icon.png")
       self.icon_MobTab = self.icon_MobTab.resize((130, 130), Image.ANTIALIAS)
       self.icon_MobTab = ImageTk.PhotoImage(self.icon_MobTab)
       self.lbl_MobileTablet = Button(cardFrame3, image = self.icon_MobTab,command=self.btn14, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_MobileTablet.pack(side = "left", padx = 10)

       self.icon_Gaming = Image.open("IMAGES\icons\Gaming_Accessories_icon.png")
       self.icon_Gaming = self.icon_Gaming.resize((130, 130), Image.ANTIALIAS)
       self.icon_Gaming = ImageTk.PhotoImage(self.icon_Gaming)
       self.lbl_Gaming = Button(cardFrame3, image = self.icon_Gaming,command=self.btn15, relief="groove", bd = 5,  bg="white", height = 150, width = 130)      
       self.lbl_Gaming.pack(side = "left")

       cardFrame3.pack(padx = 5, pady = 5, side="top", fill = X)
       #=======Category Details=======
       cat_frame=Frame(self.root,bd=1,relief=RIDGE)
       cat_frame.place(x=780,y=75,width=330,height=515)

       scrolly=Scrollbar(cat_frame,orient=VERTICAL)
       scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

       self.categoryTable=ttk.Treeview(cat_frame,columns=("Pname","Qty","price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.categoryTable.xview)
       scrolly.config(command=self.categoryTable.yview)

       self.categoryTable.heading("Pname",text="Product")
       self.categoryTable.heading("Qty",text="Qty")
       self.categoryTable.heading("price",text="Qty")
       self.categoryTable["show"]="headings"
       self.categoryTable.column("Pname",width=90)
       self.categoryTable.column("Qty",width=50)
       self.categoryTable.column("price",width=50)
       self.categoryTable.pack(side = RIGHT, fill=BOTH,expand=1)

       #=========FUNCTIONS============
    def show(self):
        con = sqlite3.connect(database = r'InventoryData.db')
        cur = con.cursor()
        try:
            cur.execute("select Pname,Qty,price from PRODUCTS where cid LIKE '%"+self.btn_val.get()+"%'")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def btn1(self):
        self.btn_val.set("1")
        self.show()

    def btn2(self):
        self.btn_val.set("2")
        self.show()

    def btn3(self):
        self.btn_val.set("3")
        self.show()

    def btn4(self):
        self.btn_val.set("4")
        self.show()
       
    def btn5(self):
        self.btn_val.set("5")
        self.show()

    def btn6(self):
        self.btn_val.set("6")
        self.show()

    def btn7(self):
        self.btn_val.set("7")
        self.show()

    def btn8(self):
        self.btn_val.set("8")
        self.show()
       
    def btn9(self):
        self.btn_val.set("9")
        self.show()
       
    def btn10(self):
        self.btn_val.set("10")
        self.show()
       
    def btn11(self):
        self.btn_val.set("11")
        self.show()
       
    def btn12(self):
        self.btn_val.set("12")
        self.show()

    def btn13(self):
        self.btn_val.set("13")
        self.show()

    def btn14(self):
        self.btn_val.set("14")
        self.show()

    def btn15(self):
        self.btn_val.set("15")
        self.show()
        

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()