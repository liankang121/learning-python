"""
线程/进程并发模型
env：python3.6
构建ftp服务器实现查看，上传，下载功能
"""
from socket import *
from threading import Thread
import sys, os
from time import *

# 全局变量：
HOST = "0.0.0.0"
PORT = 9001
ADDR = (HOST, PORT)
FILE = "/home/tarena/p2/day02/"


class FTPServer(Thread):
    """
    实现服务器文件查看、上传、下载功能
    """

    def __init__(self, sockfd):
        self.sockfd = sockfd
        super().__init__()

    def __get_path_file_name(self):
        str_file = ""
        files = os.listdir(FILE)
        for file in files:
            str_file = str_file + file + "\n"
        return str_file

    def _do_list(self):
        self.sockfd.send(b"OK")
        sleep(0.1)
        str_file = self.__get_path_file_name()
        print(str_file)
        self.sockfd.send(str_file.encode())

    def _do_get_file(self, filename):
        if filename not in self.__get_path_file_name():
            self.sockfd.send(b"dont exsit")
        else:
            self.sockfd.send(b"OK")
            sleep(0.1)
            with open(FILE + filename, "rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        sleep(0.5)
                        self.sockfd.send(b"stop")
                        break
                    self.sockfd.send(data)

    def run(self):
        while True:
            data = self.sockfd.recv(1024)
            if not data :
                break
            print(data.decode())
            protocal = data.decode().split(" ")
            print(protocal)
            if protocal[0] == "list":
                print("list")
                self._do_list()
            elif protocal[0] == "get_file":
                print(protocal[0])
                self._do_get_file(protocal[1])
            elif protocal[]


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        try:
            c, addr = s.accept()
            print("connect from %s %s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(e)
            continue

        client = FTPServer(c)
        client.daemon = True
        client.start()


if __name__ == '__main__':
    main()
