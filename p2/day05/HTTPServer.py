from socket import *
from select import *


class HTTPServer:
    def __init__(self, host="0.0.0.0", port=8000, dir=None):
        """
        初始化HTTPserver类
        :param host:
        :param port:
        :param dir:
        """
        self.host = host
        self.port = port
        self.dir = dir
        self.addr = (host, port)
        self.create_socket()
        self.bind()

    def create_socket(self):
        """
        创建套接字
        :return:
        """
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        """
        监听套接字端口
        :return:
        """
        self.sockfd.bind(self.addr)

    def get_html(self, c, filename):
        if filename == "/":
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + filename
        try:
            f = open(filename)
        except Exception:
            msg = "HTTP/1.1 404 Not Found\r\n "
            msg += "Content-Type: text/html\r\n"
            msg += "\r\n"
            msg += "<H1>SORRY"
        else:
            msg = "HTTP/1.1 200 OK\r\n "
            msg += "Content-Type: text/html\r\n"
            msg += "\r\n"
            msg += f.read()
        finally:
            c.send(msg.encode())

    def get_data(self, c):
        msg = "HTTP/1.1 404 Not Found\r\n "
        msg += "Content-Type: text/html\r\n"
        msg += "\r\n"
        msg += "<H1>SORRY"
        c.send(msg.encode())

    def do_requset(self, c):
        re = c.recv(4096)
        re_list_b = re.splitlines()
        print(re_list_b)
        re_str = re_list_b[0].decode().split(" ")[1]
        if re_str == "/" or re_str[-5:] == ".html":
            self.get_html(c, re_str)
        else:
            self.get_data(c)

    def server_forever(self):
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        self.sockfd.listen(5)
        while True:
            rs, ws, xs = select(rlist, wlist, xlist)
            for r in rs:
                if r is self.sockfd:
                    c, c_addr = self.sockfd.accept()
                    print("connect from ", c_addr)
                    rlist.append(c)
                else:
                    self.do_requset(r)


if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 9000
    DIR = "/home/tarena/static"
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.server_forever()
