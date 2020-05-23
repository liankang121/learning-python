import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 9000))
s.listen(4)

# 创建IO事件对象与io事件描述符字典，方便查找IO对象
fdmap = {s.fileno(): s}

ep = select.epoll()
ep.register(s, select.EPOLLIN | select.POLLERR)

while True:
    events = ep.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connected from %s" % addr[0])
            ep.register(c, select.EPOLLIN | select.POLLERR)
            fdmap[c.fileno()] = c
        elif event & select.EPOLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)
                fdmap[fd.fileno()].close()
                del fdmap[fd]
                continue

            print(data)
            fdmap[fd].send(b"ok")
