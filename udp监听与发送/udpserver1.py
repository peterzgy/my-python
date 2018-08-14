# -*- coding: utf-8 -*-
import os, datetime, socket
publicip = os.popen("nc ns1.dnspod.net 6666").readlines()[0]
address = ("127.0.0.1", 1234)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is starting")
sock.bind(address)
while True:
        i = datetime.datetime.now()
        today = i.day
        filename = publicip + str(i.year) + str(i.month) + str(i.day) + ".txt"
        print("进入循环")
        while True:
            data, addre = sock.recvfrom(1024)
            print(bytes.decode(data, encoding="utf-8"))
            if data:
                with open(filename, "a") as f:
                    f.write(bytes.decode(data, encoding="utf-8"))
                    if today != i.day:
                        break
            else:
                break
sock.close()
 

