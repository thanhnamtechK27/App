import os
from tkinter import * 
from tkinter import font
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from contact import Contact
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x750+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)
        

        #Bg image
        img3 = Image.open(r"assets/img/bg_img.png")
        img3 = img3.resize((1195,765),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 765)

        main_frame = Frame(bg_img, bg = "#03153B")
        main_frame.place(x = 75, y = 190, width = 1040, height = 470)
        
        #student buttom
        img4 = Image.open(r"assets/img/student.png")
        img4 = img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bt1 = Label(main_frame, image = self.photoimg4, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt1.place(x = 18, y = 10, width = 180, height = 180)

        b1_1 = ttk.Button(main_frame, text = "Thông tin Sinh viên",command = self.student_details , style="ToggleButton", cursor= "hand2")
        b1_1.place(x = 18, y = 160, width = 180, height = 40)



        #Detect face buttom
        img5 = Image.open(r"assets/img/FaceDetect.png")
        img5 = img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bt2 = Label(main_frame, image = self.photoimg5, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt2.place(x = 293, y = 10, width = 180, height = 180)

        b1_2 = ttk.Button(main_frame, text = "Nhận diện khuôn mặt", command = self.face_data, style="ToggleButton", cursor= "hand2")
        b1_2.place(x = 293, y = 160, width = 180, height = 40)



        #Attendance face buttom
        img6 = Image.open(r"assets/img/attendance.png")
        img6 = img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bt3 = Label(main_frame, image = self.photoimg6, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt3.place(x = 568, y = 10, width = 180, height = 180)

        b1_3 = ttk.Button(main_frame, text = "Thông tin điểm danh", command = self.attendance_data, style="ToggleButton", cursor= "hand2")
        b1_3.place(x = 568, y = 160, width = 180, height = 40)


#Help buttom
        img7 = Image.open(r"assets/img/help.png")
        img7 = img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        bt4 = Label(main_frame, image = self.photoimg7, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt4.place(x = 843, y = 10, width = 180, height = 180)

        b1_4 = ttk.Button(main_frame, command = self.help_data, text = "Hướng dẫn sử dụng", style="ToggleButton", cursor= "hand2")
        b1_4.place(x = 843, y = 160, width = 180, height = 40)

#Training buttom
        img8 = Image.open(r"assets/img/training.png")
        img8 = img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        bt4 = Label(main_frame, image = self.photoimg8, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt4.place(x = 18, y = 260, width = 180, height = 180)

        b2_1 = ttk.Button(main_frame, text = "Training",command = self.train_data, style="ToggleButton", cursor= "hand2")
        b2_1.place(x = 18, y = 410, width = 180, height = 40)
#Photo buttom
        img9 = Image.open(r"assets/img/photo.png")
        img9 = img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        bt4 = Label(main_frame, image = self.photoimg9, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt4.place(x = 293, y = 260, width = 180, height = 180)

        b2_2 = ttk.Button(main_frame, text = "Ảnh", style="ToggleButton", cursor= "hand2", command = self.open_img)
        b2_2.place(x = 293, y = 410, width = 180, height = 40)

#Contact buttom
        img10 = Image.open(r"assets/img/Contact.png")
        img10 = img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        bt4 = Label(main_frame, image = self.photoimg10, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt4.place(x = 568, y = 260, width = 180, height = 180)

        b2_3 = ttk.Button(main_frame, command = self.contact_data, text = "Liên hệ", style="ToggleButton", cursor= "hand2")
        b2_3.place(x = 568, y = 410, width = 180, height = 40)

#Exit buttom
        img11 = Image.open(r"assets/img/Exit.png")
        img11 = img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        bt4 = Label(main_frame, image = self.photoimg11, cursor= "hand2",fg = "#4F6998", bg = "#03153B")
        bt4.place(x = 843, y = 260, width = 180, height = 180)

        b2_4 = ttk.Button(main_frame, command = self.iExit, text = "Thoát", style="ToggleButton", cursor= "hand2")
        b2_4.place(x = 843, y = 410, width = 180, height = 40)



#================...========================
    def open_img(self):
        os.startfile("data")

    def iExit(self):
            self.iExit = tkinter.messagebox.askyesno("Thông báo", "Bạn có muốn thoát khỏi hệ thống!", parent = self.root)
            if self.iExit > 0:
                    self.root.destroy()
            else:
                    return

    def student_details(self):
        self.new_windows = Toplevel(self.root)
        self.app = Student(self.new_windows)
    
    def train_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Train(self.new_windows)




    def face_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Face_Recognition(self.new_windows)

    def attendance_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Attendance(self.new_windows)

    def contact_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Contact(self.new_windows)

    def help_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Help(self.new_windows)


    




if __name__ == "__main__":
        root =Tk()
        root.option_add("*tearOff", False)

        # Make the app responsive
        root.columnconfigure(index=0, weight=1)
        root.columnconfigure(index=1, weight=1)
        root.columnconfigure(index=2, weight=1)
        root.rowconfigure(index=0, weight=1)
        root.rowconfigure(index=1, weight=1)
        root.rowconfigure(index=2, weight=1)

        # Create a style
        style = ttk.Style(root)



# Import the tcl file
        root.tk.call("source", "Azure-ttk-theme/azure-dark.tcl")

# Set the theme with the theme_use method
        style.theme_use("azure-dark")
        obj = Face_Recognition_System(root)
        root.mainloop()