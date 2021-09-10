from tkinter import*
from tkinter import ttk ## for stylish entry feild
from PIL import Image,ImageTk  ## for images
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2   ## open source computer vision library(ML algo basically used for image or object identification)
import os
import  numpy as np

class Face_Recognition:
    def __init__(self,root):    ## for calling the constructor
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ## 1st image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        ## 2nd image
        img_bottom=Image.open(r"college_images\scan.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)   ## ANTIALIAS is used to reduce the quality/size of the image
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        ## Button    
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="green",fg="white")
        b1_1.place(x=370,y=620,width=200,height=40)

    ##============= attendance ============
    def mark_attendance(self,i,r,n,d):
        with open("jay.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            ## for attendaNCE not repeated
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")      ## for date
                dtString=now.strftime("%H:%M:%S")   ## for time
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    # =========== face recognition==============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):    ## we need these arguments to draw the boundary..
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #  converting img to grayscale
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]  # creating empty coordinate bcz we want to draw a rectangle in face.

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)   ## their is an inbuilt function rectangle in cv2
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    ##                          (where to place the rect),(font),(font thickness),(color),(rect thickness)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)  # id ,roll,name ,dept
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()   ## localBinaryPatternHistogramFace recognition
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)   ## 0 is for ur own lappy/pc camera for other 1 is used

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__== "__main__":         ## for calling the main
    root=Tk()                     ##calling root with Toolkit
    obj=Face_Recognition(root)
    root.mainloop()

#========= run the file after starting the xampp server=====