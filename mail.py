#!/usr/bin/python3 
import yagmail
def mailzou(subjectbody):
    file_object = open("/home/logs/package.log")
    try:
         contentsbody = file_object.read()
    finally:
         file_object.close( )
    
    contents = contentsbody
    yag = yagmail.SMTP(user = '#####@###bihu.com', password = '####JDPfyB6ni', host = 'smtp.exmail.qq.com')
    tolist=["995637339@qq.com"]
    yag.send(to =tolist, subject = subjectbody, contents = contentsbody)
if __name__=='__main__':
    mailzou()
#set from=############hu.com
#set smtp=smtp.exmail.qq.com
#set smtp-auth-user=###########bihu.com
#set smtp-auth-password=2#########MFNivxJAx
#set smtp-auth=login

