from Library import*

class LoginPageclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1166x718')
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.root.iconbitmap('IMAGES/icons/Key.ico')
        self.root.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('IMAGES/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.root, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

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
        self.side_image = Image.open('IMAGES/vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('IMAGES/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.var_ussername = StringVar()
        self.var_password = StringVar()

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
        self.login = Button(self.lgn_button_label, command=self.login,text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?", command = self.forget_window,
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405" , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='IMAGES/register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

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

    def login(self):
        con=sqlite3.connect(database='InventoryData.db') 
        cur=con.cursor() 
        try:
            if self.var_ussername.get()=="" or self.var_password.get()=="": 
                messagebox.showerror("Error","All fileds are required",parent=self.root)
            else:
                cur.execute("select name,uname,pass,uType from employee where uname=? AND pass=?",(self.var_ussername.get(),self.var_password.get()))
                user=cur.fetchone( ) 
                if user==None:
                    messagebox.showerror("Error","Invalid user name/password",parent=self.root)
                else:
                    con = sqlite3.connect(database = r'InventoryData.db')
                    cur = con.cursor()
                    cur.execute("Insert into LogBook (Name,uname,pass,utype,time) values(?,?,?,?,?)",(
                                user[0], user[1], user[2], user[3], str(time.strftime("%d-%m-%Y - %I:%M:%S"))
                    ))
                    con.commit()
                    if user[3]=="Admin":
                        self.root.destroy( ) 
                        os.system("python dashboard.py") 
                    else:
                        self.root.destroy() 
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.root)

    def forget_window(self):
        con=sqlite3.connect(database='InventoryData.db' ) 
        cur=con.cursor() 
        try: 
            if self.var_ussername.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.var_ussername.get(),))
                email=cur.fetchone( ) 
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID,try again",parent=self.root)
                else:
                    # ===== forget window===== # 
                    self.var_otp = StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass = StringVar()
                    # call_send_email_function()
                    self.forget_win=Toplevel(self.root) 
                    self.forget_win.title('RESET PASSWORD') 
                    self.forget_win.geometry('400x350+500+100' ) 
                    self.forget_win.focus_force()

                    title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)

                    lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered Email",font=("Andalus",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    
                    lbl_new_pass=Label(self.forget_win,text="Enter New Password ",font=("Andalus",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                    
                    lbl_conf_pass=Label(self.forget_win,text="Enter Confirm Password",font=("Andalus",15)).place(x=20,y=225)
                    txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,text="SUBMIT", font=("times new roman",15,"bold"),bg="lightblue",fg="#00759E",cursor="hand2")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED,font=("times new roman",15,"bold"),bg="lightblue",fg="#00759E",cursor="hand2")
                    self.btn_update.place(x=150,y=300,width=100,height=30)
                   
        except Exception as ex:
            messagebox.showerror("error",f"error due to : {str(ex)}",parent=self.root)


def page():
    root = Tk()
    LoginPageclass(root)
    root.mainloop()


if __name__ == '__main__':
    page()