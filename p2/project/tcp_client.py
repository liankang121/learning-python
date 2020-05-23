from socket import *

sockfd = socket()
sockfd.connect(("127.0.0.1", 9000))
while True:
    msg = """GET /  HTTP/1.1
    
    """
    sockfd.send(msg.encode())
    re = sockfd.recv(1025)
    print(re.decode())
