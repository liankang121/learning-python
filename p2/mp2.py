from multiprocessing import Process
from time import *
import os


def th1(a,d):
    print("这是第一个")
    sleep(2)
    print("第一个为a=%s"%a,d)
    print(os.getppid(), "------", os.getpid())
    print("chifan")


def th2(b):
    print("这是第二个")
    sleep(4)
    print("第二个为b=%s" % b)
    print(os.getppid(), "------", os.getpid())
    print("睡觉")


def th3(c,d):
    print("这是第三个")
    sleep(1)
    print("第三个为a=%s" % c,d)
    print(os.getppid(), "------", os.getpid())
    print("打豆豆")


things = [th1, th2, th3]
jobs = []

for th in things:
    job = Process(target=th)
    jobs.append(job)
    job.start()

for job in jobs:
    job.join()
