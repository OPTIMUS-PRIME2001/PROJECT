from Library import*
class installer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('950x600+250+60')
        self.root.resizable(0, 0)
        self.root.iconbitmap('IMAGES/icons/shield.ico')
        self.root.title('Installer')
        self.root.config(bg='#040405')


        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.root, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        
        self.side_image_label = Label(self.lgn_frame, bg='#040405')
        #self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('IMAGES/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=20)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=130)

        self.var_email = StringVar()
        self.var_ussername = StringVar()
        self.var_password = StringVar()

        # ========================================================================
        # ============================Email====================================
        # ========================================================================
        
        self.email_label = Label(self.lgn_frame, text="Email", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=550, y=170)

        self.email_entry = Entry(self.lgn_frame,textvariable=self.var_email, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("yu gothic ui ", 12, "bold"))
        self.email_entry.place(x=580, y=205, width=270)

        self.email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=550, y=229)
        # ===== Email icon =========
        self.email_icon = Image.open('IMAGES/icons/email_icon.png')
        photo = ImageTk.PhotoImage(self.email_icon)
        self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.email_icon_label.image = photo
        self.email_icon_label.place(x=530, y=202)

        
        # ========================================================================
        # ============================username====================================
        # ========================================================================
        
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame,textvariable=self.var_ussername, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('IMAGES/icons/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('IMAGES/btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='SIGN IN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, textvariable=self.var_password,highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('IMAGES/icons/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='IMAGES/icons/show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='IMAGES/icons/hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#040405"
                                  , borderwidth=0, background="#040405", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="#040405"
                                  , borderwidth=0, background="#040405", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#040405"
                                  , borderwidth=0, background="#040405", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


    
if __name__=="__main__":
    root = Tk()
    obj = installer(root)
    root.mainloop()