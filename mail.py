#!/usr/bin/python3 
import yagmail
def mailzou(subjectbody):
    file_object = open("./aa.html")
    try:
         contentsbody = file_object.read()
    finally:
         file_object.close( )
    
    contents = contentsbody
    yag = yagmail.SMTP(user = 'zouguoyin@shbihu.com', password = 'qaoAndWJDPfyB6ni', host = 'smtp.exmail.qq.com')
    tolist=["995637339@qq.com"]
    yag.send(to =tolist, subject = subjectbody, contents = contentsbody)
if __name__=='__main__':
    mailzou()
#set from=zouguoyin@shbihu.com
#set smtp=smtp.exmail.qq.com
#set smtp-auth-user=zouguoyin@shbihu.com
#set smtp-auth-password=2k3NrnJMFNivxJAx
#set smtp-auth=login

