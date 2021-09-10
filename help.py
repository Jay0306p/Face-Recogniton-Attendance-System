from tkinter import*
from tkinter import ttk ## for stylish entry feild
from PIL import Image,ImageTk  ## for images
from tkinter import messagebox
import mysql.connector
import cv2   ## open source computer vision library(ML algo basically used for image or object identification)


class Help:
    def __init__(self,root):    ## for calling the constructor
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="pink")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\helpdesk.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="jay123@gmail.com",font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=600,y=400)   

    







if __name__== "__main__":         ## for calling the main
    root=Tk()                     ##calling root with Toolkit
    obj=Help(root)
    root.mainloop()