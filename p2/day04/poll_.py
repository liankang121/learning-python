import select
from socket import *

# 创建套件字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 9000))
sockfd.listen(5)

# 创建io事件与IO文件描述符的地图（字典)
fdmap = {sockfd.fileno(): sockfd}

# 调用poll方法监控IO
p = select.poll()
p.register(sockfd, select.POLLIN | select.POLLERR)

while True:
    # 循环监控IO事件
    events = p.poll()
    print(events)
    for fo, event in events:
        if fo == sockfd.fileno():
            c, addr = fdmap[fo].accept()
            # 将C IO事件添加到IO的监控列表中
            p.register(c, select.POLLIN | select.POLLERR)
            # 将c 事件同步到字典中方便下次查找
            fdmap[c.fileno()] = c

            # 判断事件类型为POLLIN
        elif event & select.POLLIN :
            data = fdmap[fo].recv(1024).decode()
            if not data:
                # 当客户端断开后，注销该io事件
                p.unregister(fo)
                fdmap[fo].close()
                # 从 fdmap中将该事件的文件描述符，与该事件对象删除
                del fdmap[fo]
                continue
            print(data)
            fdmap[fo].send(b"ok")
