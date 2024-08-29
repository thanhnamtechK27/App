from tkinter import * 
from tkinter import font
import tkinter
import cv2, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import numpy as np


class Contact:
    def __init__(self,root):
        self.root = root
        self.root.geometry("600x400+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)

#Bg image
        img3 = Image.open(r"assets/img/bg_contact.png")
        img3 = img3.resize((600,400),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = ttk.Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 600, height = 400)



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
    obj = Contact(root)
    root.mainloop()