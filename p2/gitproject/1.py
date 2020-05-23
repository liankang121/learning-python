import gevent
from gevent import  monkey
monkey.patch_all()
from socket import *

def handle(c):
    while True:
        data = c.recv(120).decode()
        print(data)
        if not data:
            break
        c.send(b"ok")



sockfd =socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("127.0.0.1",9000))
sockfd.listen(5)
while True:
    c, addr = sockfd.accept()
    print("connect from ",addr)
    g1 = gevent.spawn(handle,c)




