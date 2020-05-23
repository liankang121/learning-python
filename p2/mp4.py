"""
multiprocessing 类属性练习
"""
from multiprocessing import *
from time import *


def func():
    for i in range(2):
        sleep(2)
        print(ctime())


p = Process(target=func)
#p.daemon = True

print("进程名称", p.name)
p.start()
sleep(1)
print("进程pid", p.pid)
print(p.is_alive())
