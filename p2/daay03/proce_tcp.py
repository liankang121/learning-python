import socket
import multiprocessing
import signal
import  os

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok121")
    c.close()


HOST = "0.0.0.0"
PORT = 9000
ADDR = (HOST, PORT)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(6)
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    p = multiprocessing.Process(target=handle, args=(c,))
    p.daemon = True
    p.start()


s.close()
