"""
select
IO多路复用
"""

from select import select
from socket import *

rlist = []
wlist = []
xlist = []

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 9000))
sockfd.listen(4)
rlist.append(sockfd)

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            c, addr = sockfd.accept()
            print("connect from %s %s" % (addr[0], addr[1]))
            rlist.append(c)

        else:
            re = r.recv(1024)

            if not re:
                rs.remove(r)
                continue
            print(re.decode())
            wlist.append(r)
    for w in ws:
        w.send(b"ok")
        wlist.remove(w)

    for x in xs:
        pass
