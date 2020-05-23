"""
利用多进程网络通讯模型
过程：
创建监听套接字
等待接受客户端请求
客户端链接创建新的进程处理客户端请求
原进程继续等待客户端其他客户端请求
新进程处理完请求后销毁

"""
from socket import *
import os
import  signal


HOST = "0.0.0.0"
PORT = 9000
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()


while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)
        os._exit(0)
    else:
        c.close()
