import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#enter your mail id here#   
fromaddr = "enter your amil id"
#enter the respective person's mail id#
toaddr = "enter the respective person's mail id"
msg = MIMEMultipart()    
msg['From'] = fromaddr   
msg['To'] = toaddr 
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
#set the xl sheet path here#
filename = "D:\wa\Face-Recognition-with-Voice-Output-master\Face-Recognition-with-Voice-Output-master\\new_writting.xls"
attachment = open("D:\wa\Face-Recognition-with-Voice-Output-master\Face-Recognition-with-Voice-Output-master\\new_writting.xls", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read())  
encoders.encode_base64(p)    
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()
#enter your mail id's password#
s.login(fromaddr, "enter your mail id's password") 
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text) 
s.quit() 
