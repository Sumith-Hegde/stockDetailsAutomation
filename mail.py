import smtplib
import sys
sender="email of sender"
reciever=["email of reciever"]
msg="there is some fluctuations in your stocks "+ sys.argv[1]
try:
    x=smtplib.SMTP('smtp.gmail.com',587)
    x.starttls()
    x.login(sender,"password of sender email")
    x.sendmail(sender,reciever,msg)
    print("sent")
except:
    print("not sent")
