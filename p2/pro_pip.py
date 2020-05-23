from multiprocessing import  Pipe,Process
#双向管道
fb1,fb2 = Pipe(duplex=True)
"""
如果duplex是flase，则是单项管道
fb1 只能调用recv fb2只能调用send
"""

def APP1():
    print("请APP2授权")
    print("发送")
    fb1.send("授权嘛")
    data = fb1.recv()
    if data:
        print(data)

def APP2():
    data = fb2.recv()
    print(data)
    fb2.send("授权成功")

p1 = Process(target=APP1)
p2 = Process(target=APP2)
p1.start()
p2.start()
p1.join()
p2.join()
