

from socket import *

def handel(c):
    while True:
        data = c.recv(1024).decode()
        print(data)
        if not data:
            break
        c.send(b"ok")

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",9000))
sockfd.listen(5)

while True:
    c,addr = sockfd.accept()
    print("connected from ", addr)
    handel(c)
