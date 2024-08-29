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


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x750+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)
        

        self.labvar = StringVar()

        #Bg image
        img3 = Image.open(r"assets/img/bg_help.png")
        img3 = img3.resize((1195,765),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 765)


#main frame
        main_frame = Frame(bg_img, bg = "#03153B")
        main_frame.place(x = 50, y = 130, width = 1100, height = 600)

        img4 = Image.open(r"assets/img/student_help.png")
        img4 = img4.resize((70,70),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        icon1 = Label(main_frame, image = self.photoimg4, bg = "#03153B")
        icon1.place(x = 0,y = 40, width = 70, height = 70)
        self.text = """THÔNG TIN SINH VIÊN
Truy cập vào chức năng này để nhập các thông tin của sinh viên \n(thông tin môn học, thông tin cá nhân, tìm kiếm thông tin…). \nLưu ý: không được bỏ trống bất kỳ thông tin nào. Sau khi nhập đầy đủ hãy nhấn:
   - “Lưu”: để lưu trữ thông tin vừa nhập.
   - “Cập nhật”: để cập nhật lại thông tin mới.
   - “Xoá”: để xoá thông tin vừa nhập.
   - “Nhập lại”: để làm trống các ô thông tin vừa nhập.
   - “Chụp ảnh”: để chụp ảnh khuôn mặt chính diện (Nếu chưa có ảnh trước đó)"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =70, y = 0, width = 470, height =150)

        img5 = Image.open(r"assets/img/train_help.png")
        img5 = img5.resize((70,70),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        icon1 = Label(main_frame, image = self.photoimg5, bg = "#03153B")
        icon1.place(x = 0,y = 200, width = 70, height = 70)
        self.text = """TRAINING
Truy cập chức năng này, nhấn vào biểu tượng khuôn mặt để hệ thống \nthu thập các thông tin trước đó.
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =70, y = 200, width = 420, height =70)

        img6 = Image.open(r"assets/img/face_recog_help.png")
        img6 = img6.resize((70,70),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        icon1 = Label(main_frame, image = self.photoimg6, bg = "#03153B")
        icon1.place(x = 0,y = 350, width = 70, height = 70)
        self.text = """NHẬN DIỆN KHUÔN MẶT
Truy cập chức năng này, nhấn vào biểu tượng khuôn mặt, sau đó sẽ nhận diện \nvà hiển thị các thông tin(chữ xanh) của sinh viên đối với các hình ảnh(video) \nkhuôn mặt của sinh viên đó. Nếu sinh viên chưa có dữ liệu trong hệ thống \nsẽ hiện các dòng chữ đỏ (Unknow).
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =70, y = 330, width = 460, height =130)

        img7 = Image.open(r"assets/img/photo_help.png")
        img7 = img7.resize((70,70),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        icon1 = Label(main_frame, image = self.photoimg7, bg = "#03153B")
        icon1.place(x = 0,y = 500, width = 70, height = 70)
        self.text = """ẢNH
Truy cập chức năng này để xem tất cả các ảnh đã được chụp.
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =60, y = 515, width =380, height =50)


        img8 = Image.open(r"assets/img/atten_help.png")
        img8 = img8.resize((70,70),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        icon1 = Label(main_frame, image = self.photoimg8, bg = "#03153B")
        icon1.place(x = 570,y = 40, width = 70, height = 70)
        self.text = """THÔNG TIN ĐIỂM DANH
Truy cập chức năng này để quản lý thông tin điểm danh sinh viên. \nỞ đây bạn có thể sửa các thông tin của sinh viên, trạng thái điểm danh. Nhấn:
    - “Nhập CSV”: chọn một file CSV mà bạn cần mở, \n\tcác dữ liệu trong file sẽ hiện ở bảng “Thông tin điểm danh”.
    - “Cập nhập”: để cập nhật thông tin vừa sửa.
    - “Xuất CSV”: điền tên tạo một file CSV mới chứa thông tin vừa cập nhật \n\thoặc chọn một file đã có sẵn mà bạn muốn thay đổi thông tin.
    - “Nhập lại”: để làm trống các ô thông tin vừa nhập.
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =640, y = 0, width =450, height =165)

        img9 = Image.open(r"assets/img/contact_help.png")
        img9 = img9.resize((70,70),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        icon1 = Label(main_frame, image = self.photoimg9, bg = "#03153B")
        icon1.place(x = 570,y = 200, width = 70, height = 70)
        self.text = """LIÊN HỆ
Truy cập chức năng này nếu bạn gặp sự cố khi sử dụng hệ thống.
Chúng tôi sẽ sẵn sàng hổ trợ bạn mọi lúc.
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =640, y = 200, width =400, height =70)

        img10 = Image.open(r"assets/img/exit_help.png")
        img10 = img10.resize((70,70),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        icon1 = Label(main_frame, image = self.photoimg10, bg = "#03153B")
        icon1.place(x = 570,y = 350, width = 70, height = 70)
        self.text = """THOÁT
Truy cập trức năng này để thoát khỏi chương trình.
"""
        help_text = Label(main_frame, text = self.text, justify=LEFT, bg = "#03153B")
        help_text.place(x =640, y = 350, width =320, height =70)


        img11 = Image.open(r"assets/img/thank.png")
        img11 = img11.resize((70,70),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        icon1 = Label(main_frame, image = self.photoimg11, bg = "#03153B")
        icon1.place(x = 570,y = 500, width = 70, height = 70)
        help_text = Label(main_frame, text = "CẢM ƠN BẠN ĐÃ TIN TƯỞNG VÀ SỬ DỤNG HỆ THỐNG CỦA CHÚNG TÔI!" , bg = "#03153B")
        help_text.place(x =640, y = 500, width =400, height =70)
  
        scroll_x = ttk.Scrollbar(main_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)      

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)  

        


        

        



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
        obj = Help(root)
        root.mainloop()