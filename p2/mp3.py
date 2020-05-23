from multiprocessing import Process
from time import *


def func(sec, name):
    for i in range(2):
        sleep(sec)
        print(name)
        print("i am worker")

def func1(sec, name):
    for i in range(2):
        sleep(sec)
        print(name)
        print("i am worker")


p = Process(target=func, args=(2, "bob"))
p.start()
p.join()

b = Process(target=func1,kwargs={"sec": 3, "name":"bo1b"})
b.start()
b.join()
