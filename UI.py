from tkinter import*
from PIL import Image, ImageTk
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by ...")
        
        #---title---
        #self.icon_title = PhotoImage(file = "images/icon2.png")
        #title = Label(self.root, text = "Inventory Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#dc2700", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)
        title = Label(self.root, text = "Inventory Management System", font = ("times new roman", 40, "bold"), bg = "#dc2700", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70)
root = Tk()
obj = IMS(root)
root.mainloop()