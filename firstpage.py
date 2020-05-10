#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py Creater.py")
    
def function2():
    
    os.system("py trainer.py")

def function3():

    os.system("py Recog.py")
def function4():
    os.system("py mail.py") 
    

   
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xlsx')

#stting title for the window
root.title("AUTOMATIC FACE RECOGNITION ATTENDANCE SYSTEM")

#creating a text label
Label(root, text="AUTOMATIC FACE RECOGNITION ATTENDANCE SYSTEM",font=("Blackletter",20),fg="white",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Data",font=("times new roman",20),bg="#7F7F7F",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Data",font=("Decorative",20),bg="#3F3F3F",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Attendance",font=('times new roman',20),bg="#7F7F7F",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Mail",font=('Decorative',20),bg="#3F3F3F",fg="white",command=function4).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Exit",font=('times new roman',20),bg="black",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
