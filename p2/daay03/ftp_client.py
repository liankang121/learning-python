from threading import *
from socket import *
from time import *

HOST = "127.0.0.1"
PORT = 9001
ADDR = (HOST, PORT)


class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"list list")
        data = self.sockfd.recv(1024)
        if data.decode() == "OK":
            file_list = self.sockfd.recv(4096)
            print(file_list.decode())

    def do_get_file(self, filename):
        msg = "get_file %s" % file_name
        self.sockfd.send(msg.encode())
        re = self.sockfd.recv(1024)
        print(re.decode())
        if re.decode() == "OK":
            self._download(file_name)
        elif re.decode() == "dont exsit":
            print("%s cant be found" % filename)

    def _download(self, file_name):
        f = open(file_name, "wb+")
        while True:
            file_content = self.sockfd.recv(1024)
            if file_content == b"stop":
                break
            print(file_content)
            f.write(file_content)
            f.flush()
        f.close()

    def do_put_file(self, file_name):
        with open(file_name, "r") as f:
            while True:
                data = f.readline()
                if not data:
                    sleep(0.5)
                    self.sockfd.send(b"stop")
                self.sockfd.send(data)

    def is_file_name_exsit(self):
        while True:
            file_name = input("输入文件名")
            if file_name == "quit":
                return ("quit","")
            msg = "put_file %s" % file_name
            self.sockfd.send(msg)
            re = self.sockfd.recv(1024)
            if re.decode() == "exist":
                print("文件已存在")
                continue
            elif re.decode() == "OK":
                return ("OK",file_name)



sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.connect(ADDR)
ftp = FTPClient(sockfd)
while True:
    print("\n=========================")
    print("********** list **********")
    print("******** get file *********")
    print("******** put file *********")
    print("********** quit ***********")
    print("===========================")
    try:
        cmd = input("输入指令:")
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
    else:
        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd.strip() == "get file":
            file_name = input("输入文件：")
            if file_name == "quit":
                continue
            ftp.do_get_file(file_name)
        elif cmd.strip() == "put file":
            re  = ftp.is_file_name_exsit()
            if re == "quit":
                continue
            elif re == "OK":
                ftp.do_put_file()
