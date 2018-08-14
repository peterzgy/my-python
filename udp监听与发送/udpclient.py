# coding = utf-8
if __name__ == "__main__":
        import socket, time
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address=('45.33.32.73', 1234)
        flag = "1"
        while True: 
                time.sleep(1)
                sock.sendto(bytes(flag, "utf-8"), address)
                if int(flag) == 1:
                        flag = "2"
                else:
                        flag = "1"
                
        sock.close()  
