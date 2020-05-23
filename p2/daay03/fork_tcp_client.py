from socket import *

HOST = "127.0.0.1"
PORT = 9000
ADDR = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM)
s.connect(ADDR)
while True:
    try:
        data = input(">>")
        s.send(data.encode())
        data2 = s.recv(1024)
    except KeyboardInterrupt:
        print("输入错误")
        break
    if not data2:
        break
    print(data2.decode())

