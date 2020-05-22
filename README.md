# AUTOMATIC FACE RECOGNITION WITH VOICE OUTPUT#

The Aim of this project is to detect and recognize the faces and mark the attendance for the person and mail the attendance sheet to the respective person 

It has four modules: 

1)    Create Data
2)   Train Data
3)   Recognizer
4)   Mail

###You can create the data of the person by using  Creater.py program 
         *It brings the ID and NAME of the person and it stores the data in the datatext.txt file
         *After saving the data it capture the image of the person in GRAY SCALE and it store the images in the Data folder. For that you want to create the folder with the name of data

###You can train the data with trainer.py program
          * By running this program it train all the images it captured

###You can Recognize the name and the ID of the user for  Attendance you want to run Recog.py program
          *By running this program it mark the attendance for that person in the xl sheet with date
          *After Detecting the face it says your Name and ID with voice output.

###You can mail the program to the respective person(staff/Head Of the Department) by using mail.py program
          *You want to include the sender's and reciver's mail id in this program and the sender's password also 

###Before running the program install the following packages

1.  Python
2.  Opencv
3.  Tkinter
4.  Numpy
5.  Pillow
6.  xlwt
7.  pyttsx3

NOTE: (You can run all these program at the same time with the help of firstpage.py program)

youtube link : https://youtu.be/rnMSo5kx4RA
