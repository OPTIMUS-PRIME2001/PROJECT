from Library import*

class categoryClass:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1100x600+220+130")
       self.root.title("Inventory Management System")
       self.root.config(bg="#f1f6f9") 
       self.root.iconbitmap('IMAGES\icons\computer.ico')
       self.root.focus_force()
       #========Variable========
       self.var_cat_id=StringVar()
       self.var_name=StringVar()

       #========title========
       lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)

       w1 = LabelFrame(self.root).place(x=10,y=75,width=760,height=500)
       canvas = Canvas(w1, bg = "white", bd = 1, relief = "ridge", height = 500, width = 760)
       
       yscrollbar = ttk.Scrollbar(w1,orient="vertical",command=canvas.yview)
       yscrollbar.pack(side=RIGHT,fill="y")  

       canvas.configure(yscrollcommand=yscrollbar.set)
       canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
       canvas.place(x=10,y=75)    
      

       btnframe = Frame(canvas)
       canvas.create_window((0,0), window=btnframe, anchor="nw")
       #=======ROW1==========================
       cardFrame1 = Frame(btnframe, width = 720, height = 150, bg = "white")
      #  Row1h=10
       self.icon_pro = Image.open("IMAGES/icons/Processor_icon.png")
       self.icon_pro = self.icon_pro.resize((150, 150), Image.ANTIALIAS)
       self.icon_pro = ImageTk.PhotoImage(self.icon_pro)
       self.lbl_processor = Button(cardFrame1, image = self.icon_pro, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_processor.pack(side = "left")

       self.icon_Mod = Image.open("IMAGES/icons/Motherboard_icon.png")
       self.icon_Mod = self.icon_Mod.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mod = ImageTk.PhotoImage(self.icon_Mod)
       self.lbl_Motherboard = Button(cardFrame1, image = self.icon_Mod, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Motherboard.pack(side = "left", padx = 10)

       self.icon_Lap = Image.open("IMAGES/icons/Laptop_icon.png")
       self.icon_Lap = self.icon_Lap.resize((130, 130), Image.ANTIALIAS)
       self.icon_Lap = ImageTk.PhotoImage(self.icon_Lap)
       self.lbl_Laptops = Button(cardFrame1, image = self.icon_Lap, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Laptops.pack(side = "left")

       self.icon_Mon = Image.open("IMAGES/icons/Monitors_icon.png")
       self.icon_Mon = self.icon_Mon.resize((130, 130), Image.ANTIALIAS)
       self.icon_Mon = ImageTk.PhotoImage(self.icon_Mon)
       self.lbl_Monitors = Button(cardFrame1, image = self.icon_Mon, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Monitors.pack(side = "left", padx = 10)

       self.icon_Desk = Image.open("IMAGES/icons/Desktop_icon.png")
       self.icon_Desk = self.icon_Desk.resize((130, 130), Image.ANTIALIAS)
       self.icon_Desk = ImageTk.PhotoImage(self.icon_Desk)
       self.lbl_Desk = Button(cardFrame1, image = self.icon_Desk, relief="groove", bd = 5,  bg="white", height = 150, width = 130)    
       self.lbl_Desk.pack(side = "left")

       cardFrame1.pack(padx = 5, pady = 5, side="top", fill = X)
       
       #============ROW2================
       cardFrame2 = Frame(btnframe, width = 770, height = 150, bg = "white")
      #  Row2h=170
       self.icon_Store = Image.open("IMAGES/icons/Storage_icon.png")
       self.icon_Store = self.icon_Store.resize((130, 130), Image.ANTIALIAS)
       self.icon_Store = ImageTk.PhotoImage(self.icon_Store)
       self.lbl_Storage = Button(cardFrame2, image = self.icon_Store, relief="groove", bd = 5,  bg="white", height = 150, width = 130)      
       self.lbl_Storage.pack(side = "left")

       self.icon_Pri = Image.open("IMAGES/icons/Printers_icon.png")
       self.icon_Pri = self.icon_Pri.resize((125, 135), Image.ANTIALIAS)
       self.icon_Pri = ImageTk.PhotoImage(self.icon_Pri)
       self.lbl_Printer = Button(cardFrame2, image = self.icon_Pri, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Printer.pack(side = "left", padx = 10)

       self.icon_Net = Image.open("IMAGES/icons/Network_icon.png")
       self.icon_Net = self.icon_Net.resize((130, 130), Image.ANTIALIAS)
       self.icon_Net = ImageTk.PhotoImage(self.icon_Net)
       self.lbl_Network = Button(cardFrame2, image = self.icon_Net, relief="groove", bd = 5,  bg="white", height = 150, width = 130)       
       self.lbl_Network.pack(side = "left")
       
       self.icon_IntC = Image.open("IMAGES/icons/InternalComponents_icon.png")
       self.icon_IntC = self.icon_IntC.resize((130, 130), Image.ANTIALIAS)
       self.icon_IntC = ImageTk.PhotoImage(self.icon_IntC)
       self.lbl_InternalComponent = Button(cardFrame2, image = self.icon_IntC, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_InternalComponent.pack(side = "left", padx = 10)

       self.icon_Per = Image.open("IMAGES/icons/Peripherals_icon.png")
       self.icon_Per = self.icon_Per.resize((120, 120), Image.ANTIALIAS)
       self.icon_Per = ImageTk.PhotoImage(self.icon_Per)
       self.lbl_Peripherals = Button(cardFrame2, image = self.icon_Per, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Peripherals.pack(side = "left")

       cardFrame2.pack(padx = 5, pady = 5, side="top", fill = X)

       #============ROW3===============
       cardFrame3 = Frame(btnframe, width = 770, height = 150, bg = "white")
      #  Row3h = 320
       self.icon_Audio = Image.open("IMAGES/icons/Audio_Accessories_icon.png")
       self.icon_Audio = self.icon_Audio.resize((130, 130), Image.ANTIALIAS)
       self.icon_Audio = ImageTk.PhotoImage(self.icon_Audio)
       self.lbl_Audio_Accessories = Button(cardFrame3, image = self.icon_Audio, relief="groove", bd = 5, bg="white", height = 150, width = 130)
       self.lbl_Audio_Accessories.pack(side = "left")

       self.icon_Vid = Image.open("IMAGES/icons/Video_Accessories_icon.png")
       self.icon_Vid = self.icon_Vid.resize((125, 135), Image.ANTIALIAS)
       self.icon_Vid = ImageTk.PhotoImage(self.icon_Vid)
       self.lbl_Video_Accessories= Button(cardFrame3, image = self.icon_Vid, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Video_Accessories.pack(side = "left", padx = 10)

       self.icon_Cable = Image.open("IMAGES/icons/Cables_icon.png")
       self.icon_Cable = self.icon_Cable.resize((130, 130), Image.ANTIALIAS)
       self.icon_Cable = ImageTk.PhotoImage(self.icon_Cable)
       self.lbl_CableAdapter = Button(cardFrame3, image = self.icon_Cable, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_CableAdapter.pack(side = "left")

       self.icon_MobTab = Image.open("IMAGES/icons/Mobiles_Tablets_icon.png")
       self.icon_MobTab = self.icon_MobTab.resize((130, 130), Image.ANTIALIAS)
       self.icon_MobTab = ImageTk.PhotoImage(self.icon_MobTab)
       self.lbl_MobileTablet = Button(cardFrame3, image = self.icon_MobTab, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_MobileTablet.pack(side = "left", padx = 10)

       self.icon_Gaming = Image.open("IMAGES\icons\Gaming_Accessories_icon.png")
       self.icon_Gaming = self.icon_Gaming.resize((130, 130), Image.ANTIALIAS)
       self.icon_Gaming = ImageTk.PhotoImage(self.icon_Gaming)
       self.lbl_Gaming = Button(cardFrame3, image = self.icon_Gaming, relief="groove", bd = 5,  bg="white", height = 150, width = 130)      
       self.lbl_Gaming.pack(side = "left")

       cardFrame3.pack(padx = 5, pady = 5, side="top", fill = X)

       #============ROW3===============
       cardFrame3 = Frame(btnframe, width = 770, height = 150, bg = "white")
      #  Row3h = 320
       self.icon_Audio = Image.open("IMAGES/icons/Audio_Accessories_icon.png")
       self.icon_Audio = self.icon_Audio.resize((130, 130), Image.ANTIALIAS)
       self.icon_Audio = ImageTk.PhotoImage(self.icon_Audio)
       self.lbl_Audio_Accessories = Button(cardFrame3, image = self.icon_Audio, relief="groove", bd = 5, bg="white", height = 150, width = 130)
       self.lbl_Audio_Accessories.pack(side = "left")

       self.icon_Vid = Image.open("IMAGES/icons/Video_Accessories_icon.png")
       self.icon_Vid = self.icon_Vid.resize((125, 135), Image.ANTIALIAS)
       self.icon_Vid = ImageTk.PhotoImage(self.icon_Vid)
       self.lbl_Video_Accessories= Button(cardFrame3, image = self.icon_Vid, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_Video_Accessories.pack(side = "left", padx = 10)

       self.icon_Cable = Image.open("IMAGES/icons/Cables_icon.png")
       self.icon_Cable = self.icon_Cable.resize((130, 130), Image.ANTIALIAS)
       self.icon_Cable = ImageTk.PhotoImage(self.icon_Cable)
       self.lbl_CableAdapter = Button(cardFrame3, image = self.icon_Cable, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_CableAdapter.pack(side = "left")

       self.icon_MobTab = Image.open("IMAGES/icons/Mobiles_Tablets_icon.png")
       self.icon_MobTab = self.icon_MobTab.resize((130, 130), Image.ANTIALIAS)
       self.icon_MobTab = ImageTk.PhotoImage(self.icon_MobTab)
       self.lbl_MobileTablet = Button(cardFrame3, image = self.icon_MobTab, relief="groove", bd = 5,  bg="white", height = 150, width = 130)
       self.lbl_MobileTablet.pack(side = "left", padx = 10)

       self.icon_Gaming = Image.open("IMAGES\icons\Gaming_Accessories_icon.png")
       self.icon_Gaming = self.icon_Gaming.resize((130, 130), Image.ANTIALIAS)
       self.icon_Gaming = ImageTk.PhotoImage(self.icon_Gaming)
       self.lbl_Gaming = Button(cardFrame3, image = self.icon_Gaming, relief="groove", bd = 5,  bg="white", height = 150, width = 130)      
       self.lbl_Gaming.pack(side = "left")

       cardFrame3.pack(padx = 5, pady = 5, side="top", fill = X)
       #=======Category Details=======
       cat_frame=Frame(self.root,bd=1,relief=RIDGE)
       cat_frame.place(x=780,y=75,width=310,height=515)

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
       self.categoryTable.pack(side = RIGHT, fill=BOTH,expand=1)

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()