# -*- coding: utf-8 -*-
import os, datetime
# rec-txt-name = time.strftime("%Y%m%d") + ".txt"

publicip = os.popen("nc ns1.dnspod.net 6666").readlines()[0]
if __name__=="__main__":
        import socket  
        print("Server is starting")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.bind(('127.0.0.1', 1234))
        sock.listen(5)
        print("Server is listenting port 60001, with max connection 5")
        while True:
                i = datetime.datetime.now()
                today = i.day
                filename = publicip + str(i.year) + str(i.month) + str(i.day) + ".txt"
                connection,address = sock.accept()  
                try:  
                        connection.settimeout(50)
                        while True:
                                buf = connection.recv(1024)
                                if buf:
                                    with open(filename, "a") as f:
                                        f.write(bytes.decode(buf, encoding="utf-8"))
                                        if today != i.day:
                                            break
                                else:
                                    break
                except socket.timeout:
                                print('time out')
                                print("closing one connection")
                                connection.close()
 

