from tkinter import *
import time
import os
class demo:
    def __init__(self, root):
        self.root = root
        frameCnt = 50
        frames = [PhotoImage(file='IMAGES/icons/loader300.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

        def update(ind):

            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label.configure(image=frame)
            self.root.after(40, update, ind)
        label = Label(root)
        label.pack()
        self.root.after(0, update, 0)

if __name__=="__main__":
    root = Tk()
    obj = demo(root)
    root.mainloop()