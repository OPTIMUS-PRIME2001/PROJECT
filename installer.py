from Library import*
class installer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('950x600+250+60')
        self.root.resizable(0, 0)

        self.root.title('Installer')
        self.root.config(bg='#040405')


if __name__=="__main__":
    root = Tk()
    obj = installer(root)
    root.mainloop()