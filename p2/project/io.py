from socket import *
from time import *

f = open("log.txt", "a+")

sockfd = socket()
sockfd.bind(("0.0.0.0", 9000))
sockfd.listen(5)

# sockfd.setblocking(False)
sockfd.settimeout(3)

while True:
    try:
        print("waiting for connectiong .. ")
        c, addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        sleep(3)
        f.write("%s: %s\n"%(ctime(),e))
        f.flush()
    else:
        data = c.recv(1024)
        print(data.decode())

