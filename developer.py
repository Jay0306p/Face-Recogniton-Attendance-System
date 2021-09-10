from tkinter import*
from tkinter import ttk ## for stylish entry feild
from PIL import Image,ImageTk  ## for images
from tkinter import messagebox
import mysql.connector
import cv2   ## open source computer vision library(ML algo basically used for image or object identification)


class Developer:
    def __init__(self,root):    ## for calling the constructor
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="pink")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\developer.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")  ## we want to put frame over the background(so used bg_img),and border=2
        main_frame.place(x=1000,y=0,width=500,height=600)  ## x=10 y=55 bcz we have to put the frame below the title and height of title is 45

        # image in mainframe
        img_top1=Image.open(r"college_images\jay.jpg")
        img_top1=img_top1.resize((200,300),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=300)

        ## DEveloper info
        dev_label=Label(main_frame,text="Hello My Name Is JAY",font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=0,y=5)   

        dev_label=Label(main_frame,text="I am a Full Stack Developer",font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=0,y=40)   

        img2=Image.open(r"college_images\developer.jfif")
        img2=img2.resize((500,300),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=300)





if __name__== "__main__":         ## for calling the main
    root=Tk()                     ##calling root with Toolkit
    obj=Developer(root)
    root.mainloop()