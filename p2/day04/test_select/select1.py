from select import select
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 9000))
sockfd.listen(4)

rlist = [sockfd]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    for r in rs:
        if r is sockfd:
            c, addr = r.accept()
            rlist.append(c)
        else:
            data = r.recv(1024)
            print(data.decode())
            if not data:
                rlist.remove(r)
                continue
            wlist.append(r)

    for w in ws:
        w.send(b"hello")
        wlist.remove(w)
