# coding = utf-8
if __name__=="__main__":
        import socket  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.connect(('127.0.0.1', 1234))
        import time  
        flag = "1"
        while True: 
                time.sleep(3)  
                print("send to server with value: " + flag)
                sock.send(bytes(flag+"test", "utf-8"))
                #print(sock.recv(1024))
                # change to another type of value each time
                if int(flag) == 1:
                        flag = "2"
                else:
                        flag = "1"
                
        sock.close()  
