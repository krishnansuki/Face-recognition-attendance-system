import cv2
from PIL import Image
import numpy
import pyttsx3
import xlwt
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
wb = xlwt.Workbook()
ws = wb.add_sheet("a test sheet")


engine = pyttsx3.init()

load = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(1)

rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("recognizer/TraningData.yml")

font = cv2.FONT_HERSHEY_SIMPLEX


f = open("datatext.txt","r")
user = {}
for x in f:
        y,z = x.split(" ")
        user[y] = z.replace("\n","")

while(1):
    status,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = load.detectMultiScale(gray,1.3,5)
    eyes = load.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        
        ws.write(1,0,id)
        ws.write(1,1,"present")
        wb.save("new_writting.xls")
        font0 = xlwt.Font()
        font0.name = "Times New Roman"
        font0.colour_index = 2
        font0.bold = True
        style1 = xlwt.XFStyle()
        style1.num_format_str = "D-MMMM-YY"
        style1.font = font0
        from datetime import datetime
        ws.write(0,0,datetime.now(),style1)
        wb.save("new_writting.xls")
        print (id)
                        
        if(conf>75):
            name = "Unknown"
            
        else:
            name = user[str(id)]
            print(name)
            wb.save("new_writting.xls")
            
    

         
        engine.say(name)
        engine.runAndWait()
        
        cv2.putText(image,str(name), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

        
    cv2.imshow('FaceDetect',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
            
        break





engine = pyttsx3.init()

load = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)

rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("recognizer/TraningData.yml")

font = cv2.FONT_HERSHEY_SIMPLEX


f = open("datatext.txt","r")
user = {}
for x  in f:
        y,z = x.split(" ")
        user[y] = z.replace("\n","")

while(1):
    status,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = load.detectMultiScale(gray,1.3,5)
    eyes = load.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        
        ws.write(3,0,id)
        ws.write(3,1,"present")
        wb.save("new_writting.xls")
        font0 = xlwt.Font()
        font0.name = "Times New Roman"
        font0.colour_index = 2
        font0.bold = True
        style1 = xlwt.XFStyle()
        
        style1.font = font0
        
        
        print (id)
                        
        if(conf>75):
            name = "Unknown"
            
        else:
            name = user[str(id)]
            print(name)
            wb.save("new_writting.xls")
    

         
        engine.say(name)
        engine.runAndWait()
        
        cv2.putText(image,str(name), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

        
    cv2.imshow('FaceDetect',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        
            
        break
















    
