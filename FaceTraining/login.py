from tkinter import * 
from tkinter import font
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from register import Register
from Class import *


class Login_Windows:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500+0+0")
        self.root.title("Login System")
        self.root.option_add("*tearOff", False)

        # Tải ảnh nền
        img3 = Image.open(r"assets/img/loginwd.jpg")
        img3 = img3.resize((800, 500), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Đặt ảnh nền
        bg_img = ttk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=800, height=500)

        # Khung chính
        main_frame = Frame(bg_img, bg="#03153B")
        main_frame.place(x=440, y=0, width=445, height=500)

        # Tải ảnh người dùng
        img4 = Image.open(r"assets/img/User.png")
        img4 = img4.resize((80, 80), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img4 = Label(self.root, image=self.photoimg4, bg="#03153B")
        lbl_img4.place(x=580, y=20, width=75, height=75)
        
        # Nhãn đăng nhập
        login = Label(main_frame, text="Đăng nhập", font=("Google Sans", 20, "bold"), fg="white", bg="#03153B")
        login.place(x=100, y=70, width=150, height=100)

        # Nhãn và trường nhập tên đăng nhập
        username = Label(main_frame, text="Tên đăng nhập ", font=("Google Sans", 9, "bold"), fg="#4F6998", bg="#03153B")
        username.place(x=55, y=180, width=120, height=20)

        self.txtUser = ttk.Entry(main_frame, font=("Google Sans", 11, "bold"), width=17)
        self.txtUser.place(x=70, y=200, width=250, height=35)

        # Nhãn và trường nhập mật khẩu
        password = Label(main_frame, text="Mật khẩu ", font=("Google Sans", 9, "bold"), fg="#4F6998", bg="#03153B")
        password.place(x=40, y=250, width=120, height=20)

        self.txtPwd = ttk.Entry(main_frame, font=("Google Sans", 11, "bold"), width=17)
        self.txtPwd.place(x=70, y=270, width=250, height=35)

        # Tải ảnh biểu tượng người dùng
        img5 = Image.open(r"assets/img/uslg.png")
        img5 = img5.resize((33, 33), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        uslg_img = Label(main_frame, image=self.photoimg5, bg="#03153B")
        uslg_img.place(x=33, y=200, width=33, height=33)

        # Tải ảnh biểu tượng mật khẩu
        img6 = Image.open(r"assets/img/pwd.png")
        img6 = img6.resize((25, 30), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        pwd_img = Label(main_frame, image=self.photoimg6, bg="#03153B")
        pwd_img.place(x=33, y=270, width=33, height=33)

        # Nút đăng nhập
        loginbtn = ttk.Button(main_frame, command=self.login, text="Đăng nhập")
        loginbtn.place(x=45, y=350, width=125, height=33)

        # Nút đăng ký
        regbtn = ttk.Button(main_frame, command=self.register, text="Đăng ký")
        regbtn.place(x=200, y=350, width=125, height=33)

        # Nút quên mật khẩu
        fgpwdbtn = Button(main_frame, text="Quên mật khẩu", borderwidth=0, font=("Google Sans", 9, "italic"), fg="#4F6998", bg="#03153B", activeforeground="#52A1EC", activebackground="#03153B")
        fgpwdbtn.place(x=55, y=400, width=260, height=33)


    def login(self):
        if self.txtUser.get() == "" or self.txtPwd.get() == "":
            messagebox.showerror("Error", "Không được để trống Tên đăng nhập hoặc Mật khẩu!")    
        else:
            try:
                conn = mysql.connector.connect(user='root', password='250301', host='localhost', database='face_recognition')
                print('Connect successfully')  
                cursor = conn.cursor()
                cursor.execute("select * from user_data where user = %s and pwd = %s", (
                    self.txtUser.get(),
                    self.txtPwd.get()
                ))
                rows = cursor.fetchone()
                if rows is None:
                    messagebox.showerror("Error", "Tên đăng nhập hoặc mật khẩu không đúng!")               
                else:
                    self.new_window = Toplevel(self.root)
                    self.obj = Face_Recognition_System(self.new_window)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
    def register(self):
        self.new_window = Toplevel(self.root)
        self.obj = Register(self.new_window)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x500+0+0")  # Đảm bảo kích thước cửa sổ giống như trong lớp Login_Windows
    root.title("Login System")

    # Tạo đối tượng Style cho ttk
    style = ttk.Style(root)

    # Sử dụng chủ đề mặc định của ttk
    style.theme_use('default')

    # Khởi tạo đối tượng Login_Windows
    obj = Login_Windows(root)
    root.mainloop()
